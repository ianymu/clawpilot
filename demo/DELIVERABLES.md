# ClawPilot 黑客松最终交付物清单

> 截止: 2026-03-19 17:00 CST

---

## W1: 大赛材料 (本窗口)

| # | 交付物 | 文件 | 状态 |
|---|--------|------|------|
| 1.0 | TG 静音修复 | reminder_config.json | ✅ DONE |
| 1.1 | 项目说明书-中文 | demo/项目说明书-ClawPilot.md | ✅ DONE |
| 1.2 | 项目说明书-英文 | demo/ClawPilot-Project-Overview.md | ✅ DONE |
| 1.3a | 视频脚本-叙事版 | demo/视频脚本-叙事版.md | ✅ DONE |
| 1.3b | 视频脚本-功能版 | demo/视频脚本-功能版.md | ✅ DONE |
| 1.4 | 海报 HTML | demo/poster.html | ✅ DONE |
| 1.5 | 整合验证 | — | ⏳ 等待 W2/W3 |
| 1.6 | Git push | — | ⏳ 等待 W2/W3 |

## W2: 健康龙虾改造

| # | 交付物 | EC2 文件 | 状态 |
|---|--------|---------|------|
| 2.1 | TG 晨报拆 3 条 | morning_health_brief.py (v2) | ✅ DONE (已验证发送) |
| 2.2 | health.html 锚点 | shrimp-web/public/health.html | ⏳ W2 |
| 2.3 | TG 建议专业化 | morning_health_brief.py | ✅ DONE (AASM/NIH 引用) |
| 2.4 | TG 饮食建议 | morning_health_brief.py | ✅ DONE (消息3) |
| 2.5 | 网站建议丰富化 | health.html | ⏳ W2 |
| 2.6 | 图表说明 | health.html | ⏳ W2 |
| 2.7 | 拍照识菜 | shrimpilot_bot.py | ⏳ W2 |
| 2.8 | 每日打卡 | shrimpilot_bot.py + health.html | ⏳ W2 |
| 2.9 | 手机提醒联动 | — | ⏳ W2 |
| 2.10 | 部署验证 | — | ⏳ W2 |

## W3: 运营龙虾改造

| # | 交付物 | EC2 文件 | 状态 |
|---|--------|---------|------|
| 3.1 | XHS 数据修复 | hotspot/collectors/xhs.py | ⏳ W3 |
| 3.2 | 文章可跳转 | hotspot.html | ⏳ W3 |
| 3.3 | 分数说明 | hotspot.html | ⏳ W3 |
| 3.4 | 7日趋势图 | hotspot.html | ⏳ W3 |
| 3.5 | TG 热点增强 | shrimpilot_bot.py | ⏳ W3 |
| 3.6 | YouTube 素材匹配 | shrimpilot_bot.py | ⏳ W3 |
| 3.7 | WeChat 全文爬取 | 新脚本 | ⏳ W3 |
| 3.8 | Gemini 分析 | gemini_analyzer.py | ⏳ W3 |
| 3.9 | AI 扩写 | shrimpilot_bot.py | ⏳ W3 |
| 3.10 | 部署验证 | — | ⏳ W3 |

## W4: 产研龙虾 + War Room

| # | 交付物 | EC2 文件 | 状态 |
|---|--------|---------|------|
| 4.1 | 产研龙虾晨报 | research_morning_brief.py | ✅ DONE |
| 4.3 | 9-Agent 演示 | demo_coordination.py | ✅ DONE |
| 4.4 | 路由集成 | unified_tg_router.py | ✅ DONE |
| 4.5 | iPhone LP 生成 | research_lp_gen.py | ✅ DONE |
| 4.6 | 部署验证 | — | ✅ DONE |
| 4.7 | Cron 注册 | crontab | ✅ DONE |

---

## 验证清单 (最终)

| # | 验证项 | 窗口 | 状态 |
|---|--------|------|------|
| 1 | TG 晨报分 3 条发送 | W2 | ✅ 已验证 |
| 2 | 锚点链接跳转 | W2 | ⏳ |
| 3 | 建议引用 WHO/NIH/AASM | W2 | ✅ 已验证 |
| 4 | 拍照识菜 | W2 | ⏳ |
| 5 | 打卡记录 | W2 | ⏳ |
| 6 | 图表图例 | W2 | ⏳ |
| 7 | AI 分析标记 | W2 | ⏳ |
| 8 | XHS 有数据 | W3 | ⏳ |
| 9 | 文章可跳转 | W3 | ⏳ |
| 10 | 分数说明 | W3 | ⏳ |
| 11 | 7日趋势图 | W3 | ⏳ |
| 12 | YouTube 匹配 | W3 | ⏳ |
| 13 | AI 扩写 | W3 | ⏳ |
| 14 | 产研晨报 | W4 | ✅ |
| 15 | 痛点波动 | W4 | ✅ |
| 16 | 9-Agent 演示 | W4 | ✅ |
| 17 | iPhone LP | W4 | ✅ |
| 18 | 说明书 CN/EN | W1 | ✅ |
| 19 | 视频脚本 x2 | W1 | ✅ |
| 20 | 海报 | W1 | ✅ |
| 21 | Git push | W1 | ⏳ |
