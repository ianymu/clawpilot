# ClawPilot — AI Co-Founder Team for Solopreneurs

> Three AI Lobster Agents. One founder. A full startup team.

---

## 1. Why ClawPilot?

### The Rise of the One-Person Company

The solopreneur economy is exploding globally:

- **USA**: 40%+ of new businesses in 2024 are solopreneurs; 5M+ earn over $100K/year (Statista, 2024)
- **China**: 150M+ content creators in 2025, individual economy GDP share rising
- **AI Tooling Boom**: Claude, Cursor, Midjourney enable one person to do the work of 5-10

But solopreneurs face three critical pain points:

| Pain Point | Data | Source |
|-----------|------|--------|
| **Health neglect** | 72% report burnout; avg 11.2h/day work | Indie Hackers 2024 Survey |
| **Operations overhead** | 3.5h/day on content distribution & tracking | Buffer State of Remote Work |
| **Direction paralysis** | 65% of solo founders pick the wrong market in Y1 | CB Insights, 2024 |

### ClawPilot's Answer

> If one person isn't enough, give them an AI co-founder team.

ClawPilot deploys **3 AI Lobster Agents** running 24/7, covering health management, operations automation, and product research. They coordinate autonomously through **shared memory + event-driven architecture**.

---

## 2. What Does ClawPilot Do?

### Three Lobsters, Three Roles

```
┌─────────────────────────────────────────────────────┐
│                  ClawPilot System                    │
│                                                      │
│  🦞 CareClaw    📊 OpsClaw    🔬 GuardClaw    │
│                                                      │
│  Health Guardian   Ops Autopilot   Security+Research │
│  Apple Watch →     Hotspot Track → Security Audit →  │
│  Sleep/HR/HRV      Content Gen →   Pain Analysis →   │
│  Burnout Alert →   Multi-Platform  Competitor Intel   │
│  Diet Management   Publishing                        │
└─────────────────────────────────────────────────────┘
```

### A Day in the Life

| Time | Who | What |
|------|-----|------|
| 07:00 | 🦞 CareClaw | Sleep analysis + personalized diet advice (Apple Watch data) |
| 07:30 | 📊 OpsClaw | 4-platform hotspot briefing (WeChat/XHS/Reddit/X) |
| 10:00 | 🔬 GuardClaw | Overnight security audit + pain point trend report |
| 12:00 | 🦞 CareClaw | User photos lunch → AI food recognition → calorie analysis |
| 14:00 | 📊 OpsClaw | YouTube library match → one-click article generation |
| 18:00 | 🦞 CareClaw | Work duration alert + hydration reminder |
| 22:00 | 🦞 CareClaw | Evening mood check-in |
| 03:00 | 🔬 GuardClaw | Automated infrastructure + code security scan |

### Core Features

#### 🦞 CareClaw — Health Guardian
- **Apple Watch Integration**: Real-time sync of sleep, heart rate, HRV
- **Professional Analysis**: Based on WHO/NIH/AASM medical standards
- **Burnout Detection**: 7-signal monitoring (normal → monitor → warning → critical)
- **AI Food Recognition**: Photo → dish identification → nutrition analysis → meal logging
- **Personalized Diet**: Weekly body data → specific food recommendations
- **Energy Curve Prediction**: Sleep data → today's peak/low energy forecast
- **Health Dashboard**: Web-based real-time charts and history

#### 📊 OpsClaw — Operations Autopilot
- **4-Platform Hotspot Tracking**: WeChat, XHS (Xiaohongshu), Reddit, X
- **AI Scoring System**: Multi-dimensional 🔥 score + cross-platform comparison
- **YouTube Library Match**: 500+ video assets auto-matched to hot topics
- **One-Click Content**: Hotspot → WeChat article / XHS post / X thread
- **AI Deep Writing**: Auto-generated research articles when no video match
- **7-Day Trend Analysis**: Line charts + blogger info + cross-platform aggregation

#### 🔬 GuardClaw — Security & Research
- **Nightly Security Audit**: Automated code + infrastructure vulnerability scan
- **Pain Point Tracking**: 23,000+ data points, Top 5 trend analysis
- **V7 Pipeline Integration**: Connected to 6-Agent product discovery system
- **iPhone Preview Generation**: One-click Landing Page generation

---

## 3. How It Works — Architecture

### Three-Layer Architecture

```
┌─────────────────────────────────────────────────┐
│         User Layer — Telegram Bot                 │
│   Single entry point for all commands & feedback  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│         Orchestration — EC2 (OpenClaw Gateway)    │
│                                                   │
│  unified_tg_router.py                             │
│  ┌──────┐  ┌──────┐  ┌──────┐                    │
│  │Care  │  │Ops   │  │Guard │   ← 3 AI Agents    │
│  │ Claw │  │ Claw │  │ Claw │     Claude Sonnet   │
│  └──┬───┘  └──┬───┘  └──┬───┘                    │
│     │         │         │                         │
│  Shared Memory: ~/.shrimpilot/memory/*.json       │
│  Event-Driven: Agents coordinate via file events  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│         Data Layer — Supabase + Apple Watch       │
│                                                   │
│  pain_points (23,234 records)                     │
│  content_hotspots                                 │
│  health_log.json (Apple Watch Ultra real-time)    │
│  health_standards.json (WHO/NIH/AASM standards)   │
└───────────────────────────────────────────────────┘
```

### OpenClaw — AI Agent Orchestration Engine

ClawPilot runs on [OpenClaw](https://github.com/anthropics/openclaw), an open-source AI Agent orchestration framework:

- **Agent Definition**: JSON config for roles, models, toolsets
- **Shared Memory**: Agents share state via `memory/*.json` files
- **Event-Driven**: One agent's output triggers another agent's action
- **Cron Scheduling**: Built-in task scheduling with timezone support

### Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| AI Model | Claude Sonnet 4.6 | Best cost-performance, Vision support |
| Agent Platform | OpenClaw (EC2) | Open source, flexible, multi-agent |
| Database | Supabase (PostgreSQL) | Free tier sufficient, built-in API |
| Health Data | Apple Watch Ultra | Most accurate consumer wearable |
| Messaging | Telegram Bot API | Cross-platform, rich text, great API |
| Web Display | Static HTML + Chart.js | Lightweight, zero dependency, mobile-friendly |
| Process Manager | pm2 | Unified Node.js/Python management |
| Search | Perplexity + Brave | Real-time + breadth |

---

## 4. Technical Highlights

### 1. Shared Memory Coordination

Unlike traditional multi-agent systems where agents work in isolation, ClawPilot's three lobsters coordinate through a **shared memory directory**:

```
Scenario: CareClaw detects burnout → OpsClaw auto-reduces work notifications

CareClaw writes: memory/health_log.json
  → fatigue_level: "warning", burnout_signals: 4

OpsClaw reads: memory/health_log.json
  → Detects warning state
  → Reduces hotspot push from 5 to 2 items, adds "take it easy" note

GuardClaw reads: memory/health_log.json
  → Postpones non-urgent security scans
  → Sends simplified pain point report
```

This isn't hardcoded if-else logic — each agent's SOUL.md (role definition) contains coordination rules, and the AI autonomously decides how to respond.

### 2. Real Apple Watch Data

ClawPilot uses real health data, not simulations:

- **Health Auto Export** App → EC2 Flask API → health_log.json
- Fields: sleep duration, deep/REM ratios, sleep latency, resting HR, HRV
- Last sync: 2026-03-18 08:47 UTC

### 3. 9-Agent Full Pipeline (V7 Integration)

ClawPilot connects to the V7 product discovery pipeline (6 agents), forming a **9-Agent end-to-end system**:

```
V7 Pipeline (Product Discovery):
  Orchestrator → DataCollector → PainAnalyzer
  → MarketValidator → CompetitorAnalyzer → BusinessDesigner

ClawPilot (Execution):
  GuardClaw (Security) → CareClaw (Founder Status) → OpsClaw (Content)

Full Pipeline: From data collection to product launch content — 9 agents, zero human intervention
```

### 4. Professional Health Standards

Health advice goes beyond "drink more water" — it references international standards:

- **AASM**: Deep sleep should be 15-25% of total
- **NIH**: Normal HRV range 30-50ms
- **WHO**: Adults need 2000ml water/day
- **Mayo Clinic**: Magnesium-rich foods improve deep sleep

---

## 5. Demo Showcase

### CareClaw Morning Report (3 Telegram Messages)

**Message 1 — Sleep & Body Status**
```
🦞 CareClaw Morning Report — Mar 19

😴 Sleep 7.2h (Efficiency 86%)
  💤 Deep 1.0h (13.8%) ⚠️
  🧠 REM 1.4h (20%) ✅
  ⏱ Latency 12min ✅

💚 Resting HR 72bpm | HRV 36ms (↑6ms)
✅ Status: Good
```

**Message 2 — Professional Advice** (citing AASM/NIH standards)

**Message 3 — AI Diet Recommendation** (based on weekly body data)

### AI Food Recognition
```
📸 User sends lunch photo →

🍽 Lunch Analysis Complete
  1. Tomato Scrambled Eggs — 180kcal | 🟢 Healthy
  2. Braised Pork — 350kcal | 🔴 High Fat
  3. Rice — 230kcal | 🟡 High Carb

📊 Total: 760kcal
✅ Logged! 3-day streak 🎉
```

### 9-Agent Coordination Demo

Send `demo` command → 9 agents report in sequence, showcasing the full pipeline from data collection to content preparation.

---

## 5. Apple Watch Hardware Innovation

> **Bonus Category** — Lobster Agent Meets Smart Wearable Hardware

ClawPilot is one of the **few hackathon projects that integrates AI Agents with real hardware devices**. This is not a simulated demo — it's a live system driven by real Apple Watch Ultra health data.

### Technical Pipeline

```
Apple Watch Ultra → Health Auto Export App → HTTPS POST
→ EC2 Flask API (:3001) → health_log.json
→ CareClaw Agent reads → Professional analysis + Cross-Agent coordination
```

### Why Is This Innovative?

1. **Real Data, Not Simulated** — Live Apple Watch Ultra collection. Last sync: 2026-03-18. Sleep, heart rate, HRV — all from real wearing data.
2. **AI Agent Autonomous Decisions** — Not just data display. CareClaw autonomously decides: Burnout alert → Notify OpsClaw to reduce frequency → System-wide response.
3. **3 Agents Share Health Data** — Health data isn't just for CareClaw — all three lobsters read it, enabling cross-role coordination.
4. **International Medical Standards** — Integrates AASM / NIH / WHO / Mayo Clinic standards. AI analysis is evidence-based.

### Health Data Fields

| Data Field | Source Device | AI Analysis Dimension |
|-----------|--------------|----------------------|
| Total Sleep / Efficiency | Apple Watch Ultra | AASM standard assessment |
| Deep Sleep / REM Ratio | Apple Watch Ultra | Sleep quality grading |
| Sleep Latency | Apple Watch Ultra | Sleep onset difficulty |
| Resting Heart Rate | Apple Watch Ultra | Cardiovascular health |
| HRV (Heart Rate Variability) | Apple Watch Ultra | Stress/recovery state |
| Active Calories (kcal) | Apple Watch Ultra | Activity level assessment |

### Future Hardware Expansion

- **iPhone Posture Detection**: Gyroscope + accelerometer → Sedentary alerts + posture correction
- **AirPods Pro Ambient Noise**: Environmental noise monitoring → Work environment optimization

---

## 6. Competitive Analysis — Why ClawPilot Is Different

No existing product combines **health management + operations automation + product research** in a single AI Agent system.

| Dimension | General AI (ChatGPT) | Standalone Tools | ClawPilot |
|-----------|---------------------|-----------------|-----------|
| Health Mgmt | ❌ No hardware | Oura/Whoop (standalone) | ✅ Apple Watch + AI analysis |
| Ops Automation | Manual prompting | Buffer + Notion (siloed) | ✅ 4-platform auto-track + gen |
| Product Research | Manual prompting | No mature solution | ✅ 23K pain point database |
| Agent Coordination | ❌ Single conversation | ❌ Tools don't talk | ✅ Shared memory + events |
| Hardware Integration | ❌ None | Standalone apps, no linking | ✅ Apple Watch real-time data |
| 24/7 Autonomous | ❌ Needs human trigger | Partial (separate configs) | ✅ 12 Cron Jobs always-on |
| Health↔Ops Linking | ❌ | ❌ Completely siloed | ✅ Burnout → auto-reduce ops |

**Core Differentiator**: ClawPilot isn't another AI chat tool or a tool bundle. It's an autonomous agent team — when CareClaw detects fatigue, OpsClaw automatically reduces work notifications.

---

## 7. Business Model

### Target Users
Solopreneurs / Indie Hackers / Content Creators / Freelance Developers

### Pricing

| Plan | Price | Includes |
|------|-------|----------|
| Basic | $19/mo | CareClaw (sleep + burnout) |
| Pro | $49/mo | CareClaw + OpsClaw (hotspots + content) |
| Enterprise | $99/mo | All 3 Lobsters + V7 Pipeline + Custom Agents |

### Market Size
- TAM: $8.5B (Global Solopreneur SaaS)
- SAM: $1.2B (AI-first founder tools)
- SOM: $24M (Y1, based on 2,000 users × $99/mo)

### Moat
1. **Data Flywheel**: More usage → better recommendations
2. **Agent Network Effects**: 3 coordinated agents > 3 independent tools
3. **Professional Standards**: WHO/NIH/AASM integration not easily replicated
4. **V7 Pipeline Integration**: Complete discovery-to-execution loop

---

## 8. Team & Traction

### Team

**Ian Mu** — Solopreneur, the only human member of ClawPilot
- Full-stack development + AI Agent architecture design
- Built 9-Agent system from scratch, solo operations
- First user and strictest tester of ClawPilot

**3 AI Lobsters** — 24/7 AI co-founder team
- 🦞 CareClaw — Health Guardian (Claude Sonnet 4.6)
- 📊 OpsClaw — Ops Autopilot (Claude Sonnet 4.6)
- 🔬 GuardClaw — Security & Research (Claude Sonnet 4.6)

### Traction

| Metric | Data | Details |
|--------|------|---------|
| Pain Points | 23,234 | Reddit / HN / X / IH |
| Health Data | 7 days | Real Apple Watch wearing, continuous sync |
| AI Agents | 9 | EC2 + OpenClaw 24/7 |
| Cron Jobs | 12 | Fully automated scheduling |
| Web Dashboards | 3 | Health / Hotspot / Research |
| YouTube Assets | 500+ | Auto-matched to hotspots |

> ClawPilot is not a concept demo. All agents are running 24/7 on EC2, and the founder has been the first real user for over 2 weeks.

---

## 9. Roadmap

| Phase | Timeline | Content | Status |
|-------|----------|---------|--------|
| Hackathon MVP | Q1 2026 | 3 Agent core + Apple Watch + Telegram + 9-Agent pipeline | ✅ Complete |
| Public Beta | Q2 2026 | 100 beta users + Multi-language + Agent personalization + Privacy compliance | Planned |
| Deep Hardware | Q3 2026 | Apple Watch deep API + iPhone posture + iOS App + AirPods | Planned |
| Paid Launch | Q4 2026 | SaaS subscription + Custom Agents + Team plan + Open API | Planned |

---

## Appendix

### Technical Specifications
- **Infrastructure**: AWS EC2 t3.large (Amazon Linux 2)
- **AI Model**: Claude Sonnet 4.6 (Anthropic)
- **Database**: Supabase (PostgreSQL 15)
- **Process Management**: pm2 (3 persistent processes)
- **Cron Jobs**: 12 scheduled tasks
- **Data Scale**: 23,234 pain points, 7-day health history
- **Data Sources**: Apple Watch Ultra, Reddit, Hacker News, WeChat, XHS, X

### Team
**Ian Mu** — Solopreneur, the only human member of ClawPilot
3 AI Lobster — 24/7 AI co-founder team

---

*ClawPilot — The power of a team, for a team of one 🦞*
