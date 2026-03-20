import json, os
from collections import defaultdict
from supabase import create_client

sb = create_client(os.environ["SUPABASE_URL"].strip(), os.environ["SUPABASE_SERVICE_ROLE_KEY"].strip())

r = sb.table("content_hotspots").select("*").eq("platform", "wechat").order("collected_at", desc=True).limit(200).execute()
articles = r.data
print(f"Fetched {len(articles)} articles")

TOPIC_KW = {
    "AI Agent/龙虾": ["agent","龙虾","openclaw","manus","养虾","skill","claw"],
    "AI公司动态": ["英伟达","nvidia","openai","anthropic","阿里","百度","腾讯","小米","kimi","deepseek","minimax","meta","谷歌","google"],
    "大模型/架构": ["transformer","大模型","mamba","架构","推理","token","参数"],
    "AI编程/工具": ["claude","gpt","编程","copilot","工具","mcp","dispatch"],
    "学术/论文": ["cvpr","iclr","icml","tpami","论文"],
    "AI视频/多模态": ["视频","sora","veo","多模态","3d","图像"],
    "机器人/具身": ["机器人","robot","具身"],
    "创业/融资": ["创业","融资","独立开发"],
}

def classify(title):
    tl = title.lower()
    for topic, kws in TOPIC_KW.items():
        for kw in kws:
            if kw.lower() in tl:
                return topic
    return "其他"

topic_articles = defaultdict(list)
for a in articles:
    topic = classify(a.get("title", ""))
    topic_articles[topic].append(a)

top_topics = []
for topic, arts in sorted(topic_articles.items(), key=lambda x: -len(x[1])):
    avg_score = sum(a.get("hotspot_score", 0) for a in arts) / max(len(arts), 1)
    platforms = list(set(a.get("platform", "") for a in arts))
    sources = list(set(a.get("source_name", "") for a in arts))

    article_list = []
    for a in arts[:8]:
        article_list.append({
            "source_name": a.get("source_name", ""),
            "title": a.get("title", ""),
            "platform": a.get("platform", ""),
            "score": a.get("hotspot_score", 0),
            "keywords": a.get("keywords", []),
            "source_url": a.get("source_url", "") or "",
        })

    top_topics.append({
        "topic": topic,
        "avg_score": round(avg_score, 1),
        "article_count": len(arts),
        "platforms": platforms,
        "cross_platform_count": len(platforms),
        "blogger_count": len(sources),
        "articles": article_list,
    })

by_platform = defaultdict(int)
for a in articles:
    by_platform[a.get("platform", "unknown")] += 1

unique_sources = len(set(a.get("source_name", "") for a in articles))
summary = {
    "date": articles[0].get("collected_at", "")[:10] if articles else "",
    "total_items": len(articles),
    "incremental": True,
    "by_platform": dict(by_platform),
    "summary_text": f"采集 {len(articles)} 篇文章，覆盖 {unique_sources} 个公众号",
    "top_topics": top_topics,
}

with open("/home/ec2-user/.shrimpilot/memory/hotspot_summary.json", "w") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"Written: {len(articles)} articles, {len(top_topics)} topics")
for t in top_topics[:5]:
    arts = t["articles"]
    url_example = arts[0]["source_url"][:50] if arts and arts[0]["source_url"] else "EMPTY"
    print(f"  {t['topic']}: {t['article_count']} articles, url={url_example}")
