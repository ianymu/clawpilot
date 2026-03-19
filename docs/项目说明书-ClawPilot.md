# ClawPilot — 一人公司 AI 联合创始人团队

> 三只 AI 龙虾，一个人的创业军团

---

## 一、为什么做 ClawPilot？

### 一人公司正在成为全球趋势

全球范围内，一人公司（Solopreneur / One-Person Business）正在经历爆发式增长：

- **美国**：2024 年新注册公司中超过 40% 是 solopreneur，年收入超 $100K 的独立创业者已超 500 万人（Statista, 2024）
- **中国**：2025 年自媒体从业者超 1.5 亿，个体经济贡献 GDP 占比持续攀升
- **工具层爆发**：AI 工具（Claude、Cursor、Midjourney）让一个人可以完成原本需要 5-10 人团队的工作

但一人公司创业者面临三大核心痛点：

| 痛点 | 数据支撑 | 来源 |
|------|---------|------|
| **健康管理缺位** | 72% 的独立创业者报告工作倦怠，平均每天工作 11.2h | Indie Hackers 2024 调研 |
| **运营效率低下** | 平均每天 3.5h 花在内容分发、数据追踪等重复劳动 | Buffer State of Remote Work |
| **产品方向迷茫** | 65% 的 solo founder 在第一年选错赛道导致失败 | CB Insights, 2024 |

### ClawPilot 的答案

> 如果一个人不够用，那就给他一个 AI 联合创始人团队。

ClawPilot 部署了 **3 只 AI 龙虾**（Agent），24/7 覆盖健康管理、运营自动化、产品研究三大领域。它们不是独立工具，而是通过**共享记忆 + 事件驱动**实现自主协调的 Agent 团队。

---

## 二、ClawPilot 做什么？

### 三龙虾分工

```
┌──────────────────────────────────────────────────────────┐
│                    ClawPilot 系统                        │
│                                                          │
│  🦞 健康龙虾        📊 运营龙虾        🔬 产研龙虾              │
│  CareClaw      OpsClaw       GuardClaw            │
│                                                          │
│  守护创始人健康    自动化运营       产品安全+研究           │
│  Apple Watch →    热点追踪 →      安全审计 →              │
│  睡眠/心率/HRV    内容生成 →      痛点分析 →              │
│  倦怠预警 →       多平台发布       竞品监控                │
│  饮食管理                                                │
└──────────────────────────────────────────────────────────┘
```

### 一天的工作场景

| 时间 | 谁在工作 | 做什么 |
|------|---------|--------|
| 07:00 | 🦞 健康龙虾 | 推送睡眠分析 + 个性化饮食建议（基于 Apple Watch 数据） |
| 07:30 | 📊 运营龙虾 | 推送四平台热点简报（微信/小红书/Reddit/X） |
| 10:00 | 🔬 产研龙虾 | 夜间安全审计报告 + 痛点波动分析 |
| 12:00 | 🦞 健康龙虾 | 用户拍午饭照片 → AI 识别菜品 → 热量分析 → 晚餐建议 |
| 14:00 | 📊 运营龙虾 | 匹配 YouTube 素材库 → 一键生成微信/小红书文章 |
| 18:00 | 🦞 健康龙虾 | 工作时长告警 + 喝水提醒 |
| 22:00 | 🦞 健康龙虾 | 情绪 check-in（你今天还好吗？） |
| 22:30 | 📊 运营龙虾 | 今日运营数据汇总 |
| 03:00 | 🔬 产研龙虾 | 夜间自动安全扫描（代码 + 基础设施） |

### 核心功能清单

#### 🦞 健康龙虾 CareClaw
- **Apple Watch 数据接入**：实时同步睡眠、心率、HRV（心率变异性）
- **专业健康分析**：基于 WHO/NIH/AASM 标准的科学解读
- **倦怠预警系统**：7 项信号监测，从 normal → monitor → warning → critical
- **AI 拍照识菜**：发照片到 Telegram，AI 识别菜品 + 营养分析 + 打卡记录
- **个性化饮食建议**：根据本周身体数据推荐具体食物和搭配
- **精力曲线预测**：根据睡眠数据预测今日精力高峰/低谷
- **健康数据看板**：Web 端实时展示趋势图和历史数据

#### 📊 运营龙虾 OpsClaw
- **四平台热点追踪**：微信公众号 / 小红书 / Reddit / X 实时热点
- **AI 热点评分**：多维度评分系统（🔥 分数）+ 跨平台对比
- **YouTube 素材匹配**：500+ 视频素材库自动匹配热点话题
- **一键内容生成**：热点 → 微信文章 / 小红书图文 / X 推文
- **AI 深度扩写**：无素材匹配时自动生成研究型长文
- **7 日趋势分析**：热点走势折线图 + 博主信息 + 跨平台聚合

#### 🔬 产研龙虾 GuardClaw
- **夜间安全审计**：自动扫描代码安全 + 基础设施漏洞
- **痛点波动追踪**：23,000+ 痛点数据的 Top 5 趋势分析
- **V7 Pipeline 对接**：与 6-Agent 产品发现系统联动
- **iPhone 预览生成**：一键生成 Landing Page 预览网站

---

## 三、怎么做？—— 技术架构

### 三层架构

```
┌─────────────────────────────────────────────────┐
│         用户层 — Telegram Bot                     │
│   统一入口：一个 Bot 接收所有指令和反馈             │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│         调度层 — EC2 (OpenClaw Gateway)           │
│                                                   │
│  unified_tg_router.py                             │
│  ┌──────┐  ┌──────┐  ┌──────┐                    │
│  │Care  │  │Ops   │  │Guard │   ← 3 AI Agent     │
│  │ Claw │  │ Claw │  │ Claw │     Claude Sonnet   │
│  └──┬───┘  └──┬───┘  └──┬───┘                    │
│     │         │         │                         │
│  共享记忆: ~/.shrimpilot/memory/*.json             │
│  事件驱动: Agent 间通过文件事件协调                  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│         数据层 — Supabase + Apple Watch           │
│                                                   │
│  pain_points (23,234 条)                          │
│  content_hotspots                                 │
│  health_log.json (Apple Watch Ultra 实时数据)      │
│  health_standards.json (WHO/NIH/AASM 标准)        │
└───────────────────────────────────────────────────┘
```

### OpenClaw — AI Agent 编排引擎

ClawPilot 运行在 [OpenClaw](https://github.com/anthropics/openclaw) 平台上，这是一个开源的 AI Agent 编排框架：

- **Agent 定义**：通过 JSON 配置文件定义每个 Agent 的角色、模型、工具集
- **共享记忆**：Agent 间通过 `~/.shrimpilot/memory/` 目录下的 JSON 文件共享状态
- **事件驱动**：一个 Agent 的输出可以触发另一个 Agent 的行动
- **Cron 调度**：内置定时任务管理，支持 UTC/CST 时区

### 技术栈

| 组件 | 技术选型 | 原因 |
|------|---------|------|
| AI 模型 | Claude Sonnet 4.6 | 性价比最优，支持 Vision |
| Agent 平台 | OpenClaw (EC2) | 开源、灵活、支持多 Agent |
| 数据库 | Supabase (PostgreSQL) | 免费层足够，内置 API |
| 健康数据 | Apple Watch Ultra | 最精准的消费级可穿戴 |
| 消息通道 | Telegram Bot API | 跨平台、API 友好、支持富文本 |
| Web 展示 | 静态 HTML + Chart.js | 轻量、零依赖、手机友好 |
| 进程管理 | pm2 | Node.js/Python 统一管理 |
| 搜索引擎 | Perplexity + Brave | 实时性 + 广度 |

---

## 四、技术亮点

### 1. 三龙虾共享记忆协调

传统多 Agent 系统是"各干各的"。ClawPilot 的三只龙虾通过**共享记忆目录**实现自主协调：

```
场景：健康龙虾检测到倦怠 → 运营龙虾自动降低工作推送频率

健康龙虾写入: memory/health_log.json
  → fatigue_level: "warning", burnout_signals: 4

运营龙虾读取: memory/health_log.json
  → 检测到 warning 状态
  → 热点推送从 5 条减为 2 条，附加"今天少干点"提示

产研龙虾读取: memory/health_log.json
  → 推迟非紧急安全扫描
  → 痛点报告简化版
```

这不是硬编码的 if-else，而是每个 Agent 的 SOUL.md（角色定义文件）中写入了协调规则，由 AI 自主判断如何响应。

### 2. Apple Watch 真实数据驱动

ClawPilot 不用模拟数据，而是接入真实的 Apple Watch Ultra 数据：

- **Health Auto Export** App → EC2 Flask API → health_log.json
- 数据字段：睡眠时长、深度/REM 比例、入睡延迟、静息心率、HRV
- 最近一次同步：2026-03-18 08:47 UTC

### 3. V7 Pipeline 联动 — 9-Agent 全链路

ClawPilot 不是孤立系统。它与 V7 产品发现流水线（6 个 Agent）联动，形成 **9-Agent 全链路**：

```
V7 Pipeline (产品发现):
  Orchestrator → DataCollector → PainAnalyzer
  → MarketValidator → CompetitorAnalyzer → BusinessDesigner

ClawPilot (执行落地):
  GuardClaw (安全审查) → CareClaw (创始人状态) → OpsClaw (内容准备)

全链路: 从数据采集到产品上线内容准备，9 个 Agent 自主协调
```

### 4. 专业健康标准集成

健康建议不是"多喝水"这种片儿汤话，而是引用国际标准：

- **AASM**（美国睡眠医学学会）：深度睡眠应占 15-25%
- **NIH**（美国国立卫生研究院）：HRV 正常范围 30-50ms
- **WHO**（世界卫生组织）：成人每日饮水 2000ml
- **Mayo Clinic**：含镁食物改善深度睡眠

---

## 五、Demo 展示

### 健康龙虾晨报（3 条 Telegram 消息）

**消息 1 — 睡眠 + 身体状态**
```
🦞 健康龙虾早报 — 3月19日

😴 睡眠 7.2h (效率 86%)
  💤 深度 1.0h (13.8%) ⚠️
  🧠 REM 1.4h (20%) ✅
  ⏱ 入睡 12min ✅

💚 静息心率 72bpm | HRV 36ms (↑6ms)
✅ 身体状态: 良好
```

**消息 2 — 专业建议**（引用 AASM/NIH 标准）

**消息 3 — AI 饮食推荐**（基于一周身体数据）

### 运营龙虾热点简报
```
📊 运营龙虾热点 — 3月19日

🔥 85  [微信] AI Agent 2025 年十大趋势预测
🔥 82  [Reddit] Solo founder 月入 $10K 的 5 种模式
🔥 78  [小红书] 用 Claude 做自媒体的完整工作流
🔥 75  [X] OpenClaw 开源 Agent 框架发布

📹 素材库匹配: 2 个 YouTube 视频可用于内容生成
```

### 拍照识菜
```
📸 用户发送午餐照片 →

🍽 午餐识别完成
  1. 番茄炒蛋 — 180kcal | 🟢 健康
  2. 红烧肉 — 350kcal | 🔴 高油
  3. 米饭 — 230kcal | 🟡 高碳水

📊 总计: 760kcal
✅ 已打卡！连续打卡 3 天 🎉
```

### 健康数据看板

Web 端实时展示：
- 7 日睡眠趋势（深度/REM/总时长）
- HRV 变化曲线
- 心率历史
- 倦怠指数追踪
- 饮食打卡日历

### 9-Agent 协调演示

发送 `演示` 指令 → 9 个 Agent 按序汇报，展示从数据采集到内容准备的全链路自主协调。

---

## 五、Apple Watch 硬件创新

> **比赛加分项** — 龙虾接入智能穿戴硬件设备

ClawPilot 是本次黑客松中**少数将 AI Agent 与真实硬件设备打通**的项目。不是模拟数据演示，而是 Apple Watch Ultra 真实健康数据驱动的 AI 决策系统。

### 技术路线

```
Apple Watch Ultra → Health Auto Export App → HTTPS POST
→ EC2 Flask API (:3001) → health_log.json
→ CareClaw Agent 读取 → 专业分析 + 跨 Agent 协调
```

### 为什么这是创新？

1. **真实数据，不是模拟** — Apple Watch Ultra 实时采集，最近同步: 2026-03-18。睡眠、心率、HRV 全部来自真实佩戴数据。
2. **AI Agent 自主决策** — 不是单纯读数据展示。CareClaw 基于数据自主判断：倦怠预警 → 通知 OpsClaw 降频 → 全局联动。
3. **3 Agent 共享健康数据** — 健康数据不只属于 CareClaw，三只龙虾共同读取，实现跨角色协调响应。
4. **国际医学标准** — 接入 AASM / NIH / WHO / Mayo Clinic 四大标准，AI 分析有科学依据。

### 接入的健康数据字段

| 数据字段 | 来源设备 | AI 分析维度 |
|---------|---------|------------|
| 睡眠总时长 / 效率 | Apple Watch Ultra | AASM 标准评估 |
| 深度睡眠 / REM 比例 | Apple Watch Ultra | 睡眠质量分级 |
| 入睡延迟 | Apple Watch Ultra | 入睡困难检测 |
| 静息心率 | Apple Watch Ultra | 心血管健康 |
| HRV (心率变异性) | Apple Watch Ultra | 压力/恢复状态 |
| 活动消耗 (kcal) | Apple Watch Ultra | 运动量评估 |

### 未来硬件扩展

- **iPhone 姿态检测**：陀螺仪 + 加速度计 → 久坐提醒 + 姿势矫正
- **AirPods Pro 环境噪音**：环境噪音监测 → 工作环境优化建议

---

## 六、竞品对比 — 为什么 ClawPilot 不一样

市面上不存在将**健康管理 + 运营自动化 + 产品研究**整合到一个 AI Agent 系统中的产品。

| 维度 | 通用 AI (ChatGPT) | 独立工具组合 | ClawPilot |
|------|-------------------|-------------|-----------|
| 健康管理 | ❌ 无硬件接入 | Oura/Whoop（独立 App） | ✅ Apple Watch 实时 + AI 分析 |
| 运营自动化 | 需手动 prompt | Buffer + Notion（割裂） | ✅ 4 平台自动追踪 + 生成 |
| 产品研究 | 需手动 prompt | 无成熟方案 | ✅ 23K 痛点数据库自动分析 |
| Agent 协调 | ❌ 单次对话 | ❌ 工具间不通信 | ✅ 共享记忆 + 事件联动 |
| 硬件接入 | ❌ 无 | 独立 App，不联动 | ✅ Apple Watch 实时数据 |
| 24/7 自主运行 | ❌ 需人发起 | 部分（需分别配置） | ✅ 12 Cron Jobs 全天候 |
| 健康↔运营联动 | ❌ | ❌ 完全割裂 | ✅ 倦怠 → 自动降频 |

**核心差异化**：ClawPilot 不是又一个 AI 聊天工具，也不是工具合集。它是一个有自主意识的 Agent 团队——健康龙虾检测到你疲劳时，运营龙虾会自动减少工作推送。

---

## 七、商业化路径

### 目标用户

一人公司创业者 / Solopreneur / 独立开发者 / 自媒体人

### 商业模式

**SaaS 订阅制**：

| 方案 | 月费 | 包含 |
|------|------|------|
| 基础版 | $19/月 | 健康龙虾（睡眠分析 + 倦怠预警） |
| 专业版 | $49/月 | 健康龙虾 + 运营龙虾（热点 + 内容生成） |
| 旗舰版 | $99/月 | 三龙虾全开 + V7 Pipeline + 自定义 Agent |

### 市场规模

- TAM: $8.5B（全球 Solopreneur SaaS 市场）
- SAM: $1.2B（AI-first 创业者工具）
- SOM: $24M（首年可达，基于 2,000 付费用户 × $99/月）

### 护城河

1. **数据飞轮**：使用越多，健康建议越精准，热点推荐越准确
2. **Agent 协调网络效应**：三龙虾协调 > 三个独立工具之和
3. **专业标准壁垒**：WHO/NIH/AASM 标准集成不易被简单复制
4. **V7 Pipeline 联动**：产品发现 + 执行落地的完整闭环

---

## 八、团队与已有成果

### 团队

**Ian Mu** — 独立创业者，ClawPilot 唯一人类成员
- 全栈开发 + AI Agent 架构设计
- 从零搭建 9-Agent 系统并独立运维
- ClawPilot 的首个用户和最严格的测试者

**3 只 AI 龙虾** — 24/7 工作的 AI 联合创始人团队
- 🦞 CareClaw — 健康守护 (Claude Sonnet 4.6)
- 📊 OpsClaw — 运营自动化 (Claude Sonnet 4.6)
- 🔬 GuardClaw — 安全与研究 (Claude Sonnet 4.6)

### 已有成果 (Traction)

| 指标 | 数据 | 说明 |
|------|------|------|
| 痛点数据 | 23,234 条 | 来自 Reddit / HN / X / IH |
| 健康数据 | 7 天 | Apple Watch 真实佩戴，持续同步 |
| AI Agent | 9 个 | EC2 + OpenClaw 全天候运行 |
| Cron 任务 | 12 个 | 全自动调度运行 |
| Web 看板 | 3 个 | 健康 / 热点 / 研究 |
| YouTube 素材 | 500+ | 自动匹配热点话题 |

> ClawPilot 不是概念演示。所有 Agent 已在 EC2 上全天候运行，创始人已作为第一个真实用户使用超过 2 周。

---

## 九、路线图

| 阶段 | 时间 | 内容 | 状态 |
|------|------|------|------|
| 黑客松 MVP | Q1 2026 | 3 Agent 核心功能 + Apple Watch + Telegram + 9-Agent 全链路 | ✅ 已完成 |
| 公测 Beta | Q2 2026 | 100 Beta 用户 + 多语言 + Agent 个性化 + 隐私合规 | 计划中 |
| 深度硬件 | Q3 2026 | Apple Watch 深度 API + iPhone 姿态 + iOS App + AirPods | 计划中 |
| 付费上线 | Q4 2026 | SaaS 订阅 + 自定义 Agent + 团队版 + API 开放 | 计划中 |

---

## 附录

### 技术规格

- **运行环境**: AWS EC2 t3.large (Amazon Linux 2)
- **AI 模型**: Claude Sonnet 4.6 (Anthropic)
- **数据库**: Supabase (PostgreSQL 15)
- **进程管理**: pm2 (3 进程常驻)
- **定时任务**: 12 个 cron jobs
- **数据规模**: 23,234 条痛点数据，7 天健康历史
- **数据源**: Apple Watch Ultra, Reddit, Hacker News, 微信公众号, 小红书, X

### 团队

**Ian Mu** — 独立创业者，ClawPilot 唯一人类成员
3 只 AI 龙虾 — 7×24 小时工作的联合创始人团队

---

*ClawPilot — 让一个人拥有一支团队的力量 🦞*
