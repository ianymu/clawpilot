---
name: ops-content-gen
description: OpsShrimp 内容生成 Skill — 接收话题，生成多平台内容，通过 QA 门控后推送
---

# OpsShrimp 内容生成

## 触发
- Telegram 消息匹配: "写|生成|发布|content"
- Cron 触发: 每日 08:00 运营简报

## 执行流程

### 内容生成模式
1. 解析用户请求（话题/URL/关键词）
2. 调用 LLM 生成内容（模型从 config 读取）
3. 生成配图（如需要）
4. 调用 content_qa.py 质量检查
5. QA PASS → 保存到 draft + 通知
6. QA FAIL → 重写一次 → 仍 FAIL → 上报

### 运营简报模式
1. 从 Supabase 读取昨日各平台数据
2. 计算环比变化
3. 基于热点推荐今日选题
4. 格式化推送到 Telegram

## 安全
- API Key 从 env 读取 + .strip()
- 不在内容中泄露用户私密数据
