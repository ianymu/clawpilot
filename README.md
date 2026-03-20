# ClawPilot

**一人公司 AI 联合创始人团队**

3 个 AI Agent 在 EC2 上 24/7 运行，覆盖健康管理、内容运营、产品研究三大领域。基于 [OpenClaw](https://openclaw.com) + Claude Sonnet 4.6 构建。

> OpenClaw Hackathon 2026 参赛作品

---

## 架构概览

![ClawPilot](https://raw.githubusercontent.com/ianymu/clawpilot/main/assets/poster.png)

ClawPilot 由 3 个 AI Agent 组成，通过共享记忆实现自主协调：

| Agent | 职责 | 核心能力 |
|-------|------|---------|
| CareClaw 健康龙虾 | 健康管理 | Apple Watch 数据 → 睡眠分析、倦怠预警、饮食建议 |
| OpsClaw 运营龙虾 | 内容运营 | 热点追踪 → YouTube 素材匹配 → 自动生成文章 |
| GuardClaw 产研龙虾 | 产品研究 | 23K+ 痛点数据 → 趋势追踪 → LP 生成 → 9-Agent 协调 |

---

## 工作原理

### CareClaw 健康龙虾

**数据链路：** Apple Watch Ultra → Health Auto Export (iOS) → EC2 Flask (:3001) → `health_log.json`

- 读取 7 天滚动健康数据
- 对比 AASM 国际标准分析睡眠质量
- 7 项倦怠信号实时监测
- 基于身体状态推荐营养素
- Claude 多模态拍照识菜

**输出：** 每天 07:00 推送 3 条 Telegram 消息 + Web 健康看板

### OpsClaw 运营龙虾

**数据链路：** 微信公众号博主文章 → AI 评分标签 → YouTube 素材库匹配（500+ 视频）

- 自动热点追踪，AI 评分 + 分类标签
- 素材库自动匹配：回复 Y → 3 分钟生成文章
- 无匹配时：AI 深度扩写，自动调研成文
- 7 日趋势看板

**输出：** Telegram 热点简报 + 一键生成文章 + Web 热点看板

### GuardClaw 产研龙虾

**数据链路：** V7 Pipeline 6 个 Agent → 痛点聚合 → 趋势分析

- Top 5 痛点方向周波动追踪
- 凌晨 3:00 自动安全审计
- 一键生成 iPhone 风格 Landing Page
- 9-Agent 全链路协调演示（45 秒，零人工干预）

**输出：** Telegram 产研日报 + LP 生成 + 9-Agent 演示

---

## 共享记忆协调

3 只龙虾通过共享记忆文件实现自主协调——不是 if-else 编程，是 AI 通过 SOUL.md 自主判断：

- CareClaw 检测到倦怠 → 写入 `health_log.json`
- OpsClaw 读取倦怠状态 → 自动减少推送（5→2 条）
- GuardClaw 读取倦怠状态 → 推迟非紧急扫描

---

## 技术栈

| 组件 | 技术 |
|------|------|
| AI 引擎 | Claude Sonnet 4.6（通过 OpenClaw） |
| Agent 框架 | OpenClaw（9 个 Agent） |
| 硬件 | Apple Watch Ultra（真实健康数据） |
| 服务器 | AWS EC2（t3.large，24/7 运行） |
| 数据库 | Supabase（23K+ 痛点数据） |
| 消息 | Telegram Bot API |
| Web 看板 | Express.js + 原生 HTML |
| 定时任务 | 12 个活跃 Cron（健康/内容/产研/安全） |

---

## 项目结构

```
clawpilot/
├── openclaw.json          # 9-Agent OpenClaw 配置
├── agents/                # Agent SOUL.md 定义
│   ├── CareClaw-SOUL.md
│   ├── OpsClaw-SOUL.md
│   └── GuardClaw-SOUL.md
├── scripts/               # Python 脚本（EC2 运行）
│   ├── shrimpilot_bot.py          # Telegram Bot 主路由
│   ├── unified_tg_router.py      # 统一消息路由
│   ├── morning_health_brief.py   # CareClaw 健康晨报
│   ├── apple_health_sync.py      # Apple Watch 数据接收
│   ├── hotspot_monitor.py        # OpsClaw 热点追踪
│   ├── hotspot/                   # 热点采集子包
│   │   ├── collectors/            # 微信/小红书/X 采集器
│   │   ├── trend_analyzer.py      # 趋势分析
│   │   └── summary.py            # 摘要生成
│   ├── research_morning_brief.py # GuardClaw 产研日报
│   ├── research_lp_gen.py        # 一键 LP 生成
│   ├── demo_coordination.py      # 9-Agent 协调演示
│   └── ...
├── skills/                # Skill 定义
├── web/                   # Express.js 看板
│   ├── server.js
│   └── public/            # 健康/热点/产研看板
└── docs/                  # 项目文档（含 PDF 说明书）
```

---

## 已有成果（真实数据）

| 指标 | 数值 |
|------|------|
| 痛点数据 | 23,234 条 |
| AI Agent | 9 个 |
| Cron 定时任务 | 12 个 |
| Web 看板 | 3 个 |
| YouTube 素材 | 500+ |
| 运行时长 | 2+ 周，24/7 |

---

## 硬件创新

ClawPilot 是本次黑客松中少数将 AI Agent 与真实硬件打通的项目：

- 每天佩戴 Apple Watch Ultra
- 真实的睡眠、心率、HRV 数据（非模拟）
- 每小时通过 HTTPS 同步到 EC2
- CareClaw 基于真实身体数据自主决策

---

## 链接

- Telegram: `@clawpilot_bot`
- 基于: [OpenClaw](https://openclaw.com) + [Claude Sonnet 4.6](https://anthropic.com)

---

*为 OpenClaw Hackathon 2026 构建*
