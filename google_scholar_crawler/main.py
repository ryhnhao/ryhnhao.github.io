#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime
from scholarly import scholarly, ProxyGenerator
from scholarly._proxy_generator import MaxTriesExceededException
import time
from pathlib import Path

print("正在查找作者信息...")

RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ======================
# 代理配置（可选）
# ======================
pg = ProxyGenerator()
used_proxy = "None"

http_p  = os.getenv("HTTP_PROXY")  or os.getenv("http_proxy")
https_p = os.getenv("HTTPS_PROXY") or os.getenv("https_proxy")

if http_p or https_p:
    try:
        if pg.SingleProxy(http=http_p, https=https_p):
            scholarly.use_proxy(pg)
            used_proxy = "SingleProxy"
            print(f"[info] 使用环境代理: {used_proxy}")
    except Exception as e:
        print(f"[warn] SingleProxy 失败: {e}")

if used_proxy == "None":
    try:
        ok = pg.FreeProxies(timeout=3)
    except TypeError:
        try:
            ok = pg.FreeProxies(timeout=3, https=True)
        except Exception as e:
            ok = False
            print(f"[warn] FreeProxies 失败: {e}")
    except Exception as e:
        ok = False
        print(f"[warn] FreeProxies 失败: {e}")
    if ok:
        scholarly.use_proxy(pg)
        used_proxy = "FreeProxies"
        print(f"[info] 使用免费代理: {used_proxy}")

print(f"[info] proxy mode: {used_proxy}")

# ======================
# scholar 设置
# ======================
scholarly.set_timeout(10)
scholarly.set_retries(2)

def with_budget(fn, budget=60):
    start = time.time()
    try:
        return fn()
    except Exception as e:
        if time.time() - start > budget:
            raise TimeoutError("Budget exceeded") from e
        raise

# ======================
# 抓取作者信息
# ======================
gs_id = os.environ.get("GOOGLE_SCHOLAR_ID")
author = None
if not gs_id:
    print("[error] 缺少 GOOGLE_SCHOLAR_ID")
else:
    try:
        author = with_budget(lambda: scholarly.search_author_id(gs_id), budget=60)
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    except MaxTriesExceededException as e:
        print(f"[warn] MaxTriesExceeded: {e}")
    except Exception as e:
        print(f"[warn] 抓取失败: {e}")

# ======================
# 输出文件
# ======================
if author:
    author["updated"] = datetime.now().isoformat(timespec="seconds")
    pubs = author.get("publications", [])
    if isinstance(pubs, list):
        author["publications"] = {v.get("author_pub_id", f"idx-{i}"): v for i, v in enumerate(pubs)}

    with (RESULTS_DIR / "gs_data.json").open("w", encoding="utf-8") as f:
        json.dump(author, f, ensure_ascii=False, indent=2)

    shields = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with (RESULTS_DIR / "gs_data_shieldsio.json").open("w", encoding="utf-8") as f:
        json.dump(shields, f, ensure_ascii=False)

    print("✅ 数据抓取并保存完成")
else:
    with (RESULTS_DIR / "gs_data.json").open("w", encoding="utf-8") as f:
        json.dump({"updated": datetime.now().isoformat(timespec="seconds")}, f, ensure_ascii=False)
    with (RESULTS_DIR / "gs_data_shieldsio.json").open("w", encoding="utf-8") as f:
        json.dump({"schemaVersion": 1, "label": "citations", "message": "0"}, f, ensure_ascii=False)
    print("⚠️ 抓取失败，写入空文件占位完成")
