#!/usr/bin/env python3
"""
ops_daily_tg.py — 运营虾每日TG推送
顺序: 1.7日趋势 → 2.今日热点 → 3.素材匹配
铁律 #1: 所有 os.environ 必须 .strip()
"""
import json, os, sys, time, httpx
sys.path.insert(0, "/home/ec2-user/scripts")

TG_TOKEN = os.environ.get("TG_SHRIMPILOT_TOKEN", "").strip()
TG_CHAT_ID = os.environ.get("TG_CHAT_ID", "").strip()
MEMORY = os.path.expanduser("~/.shrimpilot/memory")
HOTSPOT_URL = "http://18.221.160.170/shrimp/hotspot"

def tg(text):
    httpx.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        json={"chat_id": TG_CHAT_ID, "text": text, "parse_mode": "Markdown",
              "disable_web_page_preview": True}, timeout=10)

with open(os.path.join(MEMORY, "hotspot_summary.json")) as f:
    data = json.load(f)
with open(os.path.join(MEMORY, "wechat_trends_7d.json")) as f:
    trends = json.load(f)

topics = data.get("top_topics", [])
total = data.get("total_items", 0)
daily = trends.get("daily_breakdown", [])
trend_topics = trends.get("trends", [])

# === Msg 1: 7日趋势 ===
lines1 = ["\U0001f4c8 *7 \u65e5\u8d8b\u52bf\u901f\u89c8*", ""]
for t in trend_topics[:5]:
    icon = "\U0001f680" if t["trend_direction"] == "rising" else "\u27a1\ufe0f"
    lines1.append(f"{icon} *{t['topic']}* \u2014 {t['article_count']}\u7bc7")
lines1.append("")
lines1.append("*\u6bcf\u65e5\u6587\u7ae0\u91cf:*")
for d in daily[-5:]:
    date = d["date"][5:]
    nz = {k: v["count"] for k, v in d.get("topics", {}).items() if v.get("count", 0) > 0 and k != "\u5176\u4ed6"}
    top3 = sorted(nz.items(), key=lambda x: -x[1])[:3]
    detail = " ".join(f"{k}({v})" for k, v in top3)
    lines1.append(f"  {date}: {detail}")
lines1.append("")
lines1.append(f"\U0001f4ca [\u8be6\u60c5\u8bf7\u53c2\u89c1]({HOTSPOT_URL})")
tg("\n".join(lines1))
print("Msg 1 sent: 7d trends")
time.sleep(1)

# === Msg 2: 今日热点 ===
lines2 = ["\U0001f525 *\u8fd0\u8425\u867e \u00b7 \u4eca\u65e5\u70ed\u70b9\u901f\u62a5*",
           f"\u5171\u91c7\u96c6 *{total}* \u7bc7 | 7 \u4e2a\u516c\u4f17\u53f7", ""]
for i, t in enumerate(topics[:6], 1):
    topic = t["topic"]
    count = t["article_count"]
    arts = t.get("articles", [])
    sources = list(set(a.get("source_name", "") for a in arts if a.get("source_name")))
    src_str = "\u3001".join(sources[:3])
    if len(sources) > 3:
        src_str += f" \u7b49{len(sources)}\u4eba"
    lines2.append(f"*{i}. {topic}* ({count}\u7bc7)")
    lines2.append(f"   {src_str}")
    for a in arts[:2]:
        title = a.get("title", "")[:35]
        url = a.get("source_url", "")
        if url:
            lines2.append(f"   \u00b7 [{title}]({url})")
        else:
            lines2.append(f"   \u00b7 {title}")
    lines2.append("")
lines2.append(f"\U0001f4ca [\u8be6\u60c5\u8bf7\u53c2\u89c1]({HOTSPOT_URL})")
tg("\n".join(lines2))
print("Msg 2 sent: hotspot report")
time.sleep(1)

# === Msg 3: 素材匹配 ===
from hotspot.auto_match_notify import run as match_run
match_run()
print("Msg 3 sent: material match")
