#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import time
from datetime import datetime
from pathlib import Path

from scholarly import scholarly, ProxyGenerator
from scholarly._proxy_generator import MaxTriesExceededException

print("正在查找作者信息...")

# ======================
# 常量/路径
# ======================
RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = RESULTS_DIR / "gs_data.json"
OUT_BADGE = RESULTS_DIR / "gs_data_shieldsio.json"

# ======================
# scholarly 全局配置（更宽松）
# ======================
scholarly.set_timeout(60)   # 默认10，容易卡超时
scholarly.set_retries(6)    # 默认2，偏低，容易触发 MaxTriesExceeded

def sleep_backoff(attempt: int, base: int = 2, cap: int = 20):
    """指数退避：1,2,4,8,... 秒，封顶 cap 秒"""
    t = min(cap, base ** attempt)
    time.sleep(t)

def configure_proxy(mode: str, http_p: str = None, https_p: str = None) -> bool:
    """
    根据 mode 配置代理：
      - "env": 使用环境代理（HTTP_PROXY/HTTPS_PROXY）
      - "free": 申请一组新的免费代理池
      - "none": 不使用代理
    成功返回 True，失败 False
    """
    pg = ProxyGenerator()
    try:
        if mode == "env":
            if http_p or https_p:
                ok = pg.SingleProxy(http=http_p, https=https_p)
                if ok:
                    scholarly.use_proxy(pg)
                    print(f"[info] 使用环境代理: env")
                    return True
            return False
        elif mode == "free":
            try:
                ok = pg.FreeProxies(timeout=5, https=True)
            except TypeError:
                ok = pg.FreeProxies(timeout=5)
            if ok:
                scholarly.use_proxy(pg)
                print(f"[info] 使用免费代理: FreeProxies(新池)")
                return True
            return False
        elif mode == "none":
            scholarly.use_proxy(None)
            print(f"[info] 使用直连: none")
            return True
        else:
            print(f"[warn] 未知代理模式: {mode}")
            return False
    except Exception as e:
        print(f"[warn] 代理模式 {mode} 失败: {e}")
        return False

def robust_search_author(gs_id: str,
                         modes=("env", "free", "none"),
                         max_attempts_per_mode: int = 3):
    """对 search_author_id 做分模式、多次重试 + 退避"""
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
                author = scholarly.search_author_id(gs_id)
                return author
            except MaxTriesExceededException as e:
                print(f"[warn] search_author_id MaxTriesExceeded (mode={mode}, attempt={i+1}): {e}")
                last_err = e
            except Exception as e:
                print(f"[warn] search_author_id 失败 (mode={mode}, attempt={i+1}): {e}")
                last_err = e
            sleep_backoff(i)
    if last_err:
        raise last_err
    raise RuntimeError("无法配置可用代理或 search_author_id 持续失败")

def robust_fill(author: dict, sections, max_attempts: int = 4) -> dict:
    """对 scholarly.fill 做多次重试 + 退避，专治限流"""
    last_err = None
    for i in range(max_attempts):
        try:
            scholarly.fill(author, sections=sections)
            return author
        except MaxTriesExceededException as e:
            print(f"[warn] fill MaxTriesExceeded (attempt={i+1}, sections={sections}): {e}")
            last_err = e
        except Exception as e:
            print(f"[warn] fill 失败 (attempt={i+1}, sections={sections}): {e}")
            last_err = e
        sleep_backoff(i)
    if last_err:
        raise last_err

def write_outputs(author: dict | None):
    """根据抓取结果写输出：成功则写全量；失败则尽量保留旧数据"""
    if author:
        author["updated"] = datetime.now().isoformat(timespec="seconds")
        pubs = author.get("publications", [])
        if isinstance(pubs, list):
            author["publications"] = {
                v.get("author_pub_id", f"idx-{i}"): v for i, v in enumerate(pubs)
            }

        OUT_JSON.write_text(
            json.dumps(author, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        shields = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{author.get('citedby', 0)}",
        }
        OUT_BADGE.write_text(
            json.dumps(shields, ensure_ascii=False),
            encoding="utf-8"
        )
        print("✅ 数据抓取并保存完成")
    else:
        # 失败：优先保留旧数据，仅更新时间戳；没有旧数据才写占位
        if OUT_JSON.exists():
            print("⚠️ 抓取失败：保留上次成功数据，仅更新时间戳")
            try:
                data = json.loads(OUT_JSON.read_text(encoding="utf-8"))
                data["updated"] = datetime.now().isoformat(timespec="seconds")
                OUT_JSON.write_text(
                    json.dumps(data, ensure_ascii=False, indent=2),
                    encoding="utf-8"
                )
            except Exception:
                # 旧数据损坏就写占位
                OUT_JSON.write_text(
                    json.dumps({"updated": datetime.now().isoformat(timespec="seconds")}, ensure_ascii=False, indent=2),
                    encoding="utf-8"
                )
        else:
            OUT_JSON.write_text(
                json.dumps({"updated": datetime.now().isoformat(timespec="seconds")}, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

        if not OUT_BADGE.exists():
            OUT_BADGE.write_text(
                json.dumps({"schemaVersion": 1, "label": "citations", "message": "403"}, ensure_ascii=False),
                encoding="utf-8"
            )
        print("⚠️ 抓取失败，已写入占位/或保留旧文件")

def main():
    gs_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not gs_id:
        print("[error] 缺少 GOOGLE_SCHOLAR_ID")
        write_outputs(None)
        return

    try:
        # 1) 搜索作者（分代理+多次重试）
        author = robust_search_author(gs_id)

        # 2) 先取轻量字段，成功率更高
        robust_fill(author, sections=["basics", "indices", "counts"])

        # 3) publications 较重，单独再尝试；失败也不影响前面数据落盘
        try:
            robust_fill(author, sections=["publications"])
        except Exception as e:
            print(f"[warn] publications 填充失败，将保存已获得的数据: {e}")

        # 4) 写盘
        write_outputs(author)

    except Exception as e:
        print(f"[warn] 最终失败: {e}")
        write_outputs(None)

if __name__ == "__main__":
    main()
