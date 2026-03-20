#!/usr/bin/env python3
"""
auto_match_notify.py — 热点采集后自动匹配素材库并推TG
铁律 #1: 所有 os.environ 必须 .strip()
"""
import os, sys, json, logging
sys.path.insert(0, "/home/ec2-user/scripts")
from hotspot.config import log, TG_TOKEN, TG_CHAT_ID, sb_query
from content_pipeline.youtube_matcher import match_hotspots_to_youtube
import httpx

MEMORY_DIR = os.path.expanduser("~/.shrimpilot/memory")

def tg_send(text, chat_id=None):
    chat_id = chat_id or TG_CHAT_ID
    if not TG_TOKEN or not chat_id:
        return
    try:
        httpx.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}, timeout=10)
    except Exception as e:
        log.error(f"TG send error: {e}")

def load_hotspot_topics():
    path = os.path.join(MEMORY_DIR, "hotspot_summary.json")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        data = json.load(f)
    topics = []
    for t in data.get("top_topics", []):
        keywords = []
        topic_name = t.get("topic", "")
        keywords.extend(topic_name.replace("/", " ").split())
        for art in t.get("articles", []):
            keywords.extend(art.get("keywords", []))
        keywords = list(set(k for k in keywords if len(k) >= 2))
        topics.append({
            "topic_cluster": topic_name, "title": topic_name,
            "hotspot_score": t.get("avg_score", 0) or t.get("article_count", 0) * 5,
            "keywords": keywords, "article_count": t.get("article_count", 0),
        })
    return topics

def format_tg_message(matches):
    lines = ["\U0001f4da *\u7d20\u6750\u5e93\u5339\u914d\u7ed3\u679c*", ""]
    has_match = []
    no_match = []
    for m in matches:
        score = m.get("match_score", 0)
        video = m.get("youtube_video")
        if video and score >= 0.85:
            has_match.append(m)
        else:
            no_match.append(m)

    if has_match:
        lines.append("\u2705 *\u6709\u7d20\u6750\u53ef\u76f4\u63a5\u751f\u6210:*")
        for idx, m in enumerate(has_match, 1):
            v = m["youtube_video"]
            lines.append(f"`Y{idx}` *{m['hotspot_topic']}*")
            lines.append(f"   \u2192 {v['title'][:35]} (\u5339\u914d {m['match_score']:.0%})")
        lines.append("")
        lines.append("\u56de\u590d `Y1`/`Y2`... \u6267\u884c\u751f\u6210")
        lines.append("")

    if no_match:
        lines.append("\U0001f916 *\u5efa\u8bae AI \u6269\u5199:*")
        for idx, m in enumerate(no_match, 1):
            count = m.get("article_count", "")
            count_str = f" ({count}\u7bc7\u70ed\u6587)" if count else ""
            lines.append(f"`E{idx}` *{m['hotspot_topic']}*{count_str}")
        lines.append("")
        lines.append("\u56de\u590d `E1`/`E2`... \u542f\u52a8 AI \u6df1\u5ea6\u6269\u5199")

    lines.append("")
    lines.append(f"\u5171 {len(matches)} \u4e2a\u70ed\u70b9 | {len(has_match)} \u6709\u7d20\u6750 | {len(no_match)} \u9700\u6269\u5199")
    return "\n".join(lines)

def run():
    topics = load_hotspot_topics()
    if not topics:
        return
    matches = match_hotspots_to_youtube(topics)
    pending_path = os.path.join(MEMORY_DIR, "pending_youtube_match.json")
    with open(pending_path, "w") as f:
        json.dump({"matches": matches, "timestamp": __import__("datetime").datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)
    msg = format_tg_message(matches)
    tg_send(msg)
    log.info(f"Match sent: {sum(1 for m in matches if m.get('match_score',0)>=0.85)} high, {sum(1 for m in matches if m.get('match_score',0)<0.85)} expand")

if __name__ == "__main__":
    run()
