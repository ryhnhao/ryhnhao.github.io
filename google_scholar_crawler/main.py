#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch Google Scholar citation data with a rolling 10-success fallback."""

import json
import os
import time
from datetime import datetime
from pathlib import Path

from scholarly import ProxyGenerator, scholarly
from scholarly._proxy_generator import MaxTriesExceededException

RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

OUT_JSON = RESULTS_DIR / "gs_data.json"
OUT_BADGE = RESULTS_DIR / "gs_data_shieldsio.json"
HISTORY_JSON = RESULTS_DIR / "gs_history.json"
HISTORY_LIMIT = 10

# Keep the crawler responsive when Scholar blocks automated requests.
scholarly.set_timeout(30)
scholarly.set_retries(2)


def sleep_backoff(attempt: int, base: int = 2, cap: int = 10):
    time.sleep(min(cap, base**attempt))


def configure_proxy(mode: str, http_p: str = None, https_p: str = None) -> bool:
    """Configure environment, free or direct access."""
    pg = ProxyGenerator()
    try:
        if mode == "env":
            if not (http_p or https_p):
                return False
            ok = pg.SingleProxy(http=http_p, https=https_p)
            if ok:
                scholarly.use_proxy(pg)
                print("[info] 使用环境代理: env")
            return bool(ok)

        if mode == "free":
            try:
                ok = pg.FreeProxies(timeout=5, https=True)
            except TypeError:
                ok = pg.FreeProxies(timeout=5)
            if ok:
                scholarly.use_proxy(pg)
                print("[info] 使用免费代理: FreeProxies(新池)")
            return bool(ok)

        if mode == "none":
            scholarly.use_proxy(None)
            print("[info] 使用直连: none")
            return True

        print(f"[warn] 未知代理模式: {mode}")
        return False
    except Exception as exc:
        print(f"[warn] 代理模式 {mode} 失败: {exc}")
        return False


def robust_search_author(
    gs_id: str, modes=("env", "free", "none"), max_attempts_per_mode: int = 2
):
    """Try several proxy modes, with limited retries."""
    http_p = os.getenv("HTTP_PROXY") or os.getenv("http_proxy")
    https_p = os.getenv("HTTPS_PROXY") or os.getenv("https_proxy")
    last_err = None

    for mode in modes:
        ok = configure_proxy(mode, http_p, https_p)
        print(f"[info] 尝试代理模式: {mode}, ok={ok}")
        if not ok:
            continue

        for i in range(max_attempts_per_mode):
            try:
                return scholarly.search_author_id(gs_id)
            except MaxTriesExceededException as exc:
                print(
                    f"[warn] search_author_id MaxTriesExceeded "
                    f"(mode={mode}, attempt={i + 1}): {exc}"
                )
                last_err = exc
            except Exception as exc:
                print(f"[warn] search_author_id 失败 (mode={mode}, attempt={i + 1}): {exc}")
                last_err = exc
            if i + 1 < max_attempts_per_mode:
                sleep_backoff(i)

    if last_err is not None:
        raise last_err
    raise RuntimeError("无法配置可用代理或 search_author_id 持续失败")


def robust_fill(author: dict, sections, max_attempts: int = 2) -> dict:
    """Fill a section without retrying indefinitely."""
    last_err = None
    for i in range(max_attempts):
        try:
            scholarly.fill(author, sections=sections)
            return author
        except MaxTriesExceededException as exc:
            print(f"[warn] fill MaxTriesExceeded (attempt={i + 1}, sections={sections}): {exc}")
            last_err = exc
        except Exception as exc:
            print(f"[warn] fill 失败 (attempt={i + 1}, sections={sections}): {exc}")
            last_err = exc
        if i + 1 < max_attempts:
            sleep_backoff(i)

    if last_err is not None:
        raise last_err
    raise RuntimeError("fill 失败")


def valid_count(value):
    """Accept non-negative integer counts; reject bool, null and placeholders."""
    if type(value) is int and value >= 0:
        return value
    if isinstance(value, str) and value.strip().isdecimal():
        return int(value.strip())
    return None


def read_existing_data() -> dict:
    try:
        data = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, OSError, ValueError):
        return {}


def load_history() -> list[int]:
    """Read the last 10 REAL successful counts from a persistent JSON file."""
    try:
        data = json.loads(HISTORY_JSON.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, ValueError):
        return []

    if not isinstance(data, list):
        return []
    counts = [n for value in data if (n := valid_count(value)) is not None]
    return counts[-HISTORY_LIMIT:]


def write_outputs(author: dict | None):
    """Real count when fetched; otherwise maximum of last 10 successful counts."""
    history = load_history()
    old_data = read_existing_data()
    count = valid_count(author.get("citedby")) if isinstance(author, dict) else None

    now = datetime.now().isoformat(timespec="seconds")
    if count is not None:
        data = dict(author)
        data["citedby"] = count
        data["updated"] = now

        pubs = data.get("publications", [])
        if isinstance(pubs, list):
            data["publications"] = {
                pub.get("author_pub_id", f"idx-{i}"): pub
                for i, pub in enumerate(pubs)
                if isinstance(pub, dict)
            }

        # Only genuine new successful fetches enter the history.
        history = (history + [count])[-HISTORY_LIMIT:]
        print(f"✅ 抓取成功，使用 Google Scholar 真实引用数: {count}")
    else:
        # For an older installation without gs_history.json, seed from an
        # existing real gs_data.json count. Do NOT seed from the old hardcoded
        # shields badge (592), as it may not be a genuine Scholar value.
        if not history:
            old_count = valid_count(old_data.get("citedby"))
            if old_count is not None:
                history = [old_count]

        if not history:
            # A failed run must never destroy remote data or create fake counts.
            raise RuntimeError(
                "抓取失败且没有有效历史引用数，停止发布（旧数据分支不会被覆盖）"
            )

        count = max(history[-HISTORY_LIMIT:])
        data = dict(old_data)
        data["citedby"] = count
        data["updated"] = now
        print(f"⚠️ 抓取失败，采用最近 {len(history)} 次成功抓取的最大值: {count}")

    badge = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(count),
    }
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_BADGE.write_text(json.dumps(badge, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    HISTORY_JSON.write_text(json.dumps(history[-HISTORY_LIMIT:], indent=2) + "\n", encoding="utf-8")
    print(f"✅ 保存完成: gs_data.json / gs_data_shieldsio.json / gs_history.json (citations={count})")


def main():
    print("正在查找作者信息...")
    gs_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not gs_id:
        print("[error] 缺少 GOOGLE_SCHOLAR_ID")
        write_outputs(None)
        return

    try:
        author = robust_search_author(gs_id)

        try:
            robust_fill(author, sections=["basics", "indices", "counts"])
        except Exception as exc:
            # If a real citation count was already fetched, keep it; otherwise
            # fall back to history below.
            print(f"[warn] basics/indices/counts 填充失败: {exc}")
            if not isinstance(author, dict) or valid_count(author.get("citedby")) is None:
                raise

        # Publications are optional; their failure must not discard citedby.
        try:
            robust_fill(author, sections=["publications"])
        except Exception as exc:
            print(f"[warn] publications 填充失败，仍使用已获取的引用数: {exc}")

        write_outputs(author)
    except Exception as exc:
        print(f"[warn] Google Scholar 抓取失败: {exc}")
        write_outputs(None)


if __name__ == "__main__":
    main()
