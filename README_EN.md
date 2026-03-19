# ClawPilot

**AI Co-Founder Team for Solo Entrepreneurs**

3 AI Agents running 24/7 on EC2, covering Health, Content Operations, and Product Research. Built with [OpenClaw](https://openclaw.com) + Claude Sonnet 4.6.

> OpenClaw Hackathon 2026 Entry

---

## Architecture

![ClawPilot](https://raw.githubusercontent.com/ianymu/clawpilot/main/assets/poster.png)

ClawPilot consists of 3 AI Agents that coordinate through shared memory:

| Agent | Role | Key Capability |
|-------|------|----------------|
| CareClaw | Health | Apple Watch data → sleep analysis, burnout detection, diet advice |
| OpsClaw | Content Ops | Hotspot tracking → YouTube matching → auto article generation |
| GuardClaw | Product Research | 23K+ pain points → trend tracking → LP generation → 9-Agent coordination |

---

## How It Works

### CareClaw (Health)

**Data Flow:** Apple Watch Ultra → Health Auto Export (iOS) → EC2 Flask (:3001) → `health_log.json`

- Reads 7 days of rolling health data
- Sleep quality analysis against AASM standards
- 7-signal burnout detection system
- Nutrition recommendations based on body state
- Photo food recognition via Claude multimodal

**Output:** 3 Telegram messages daily at 07:00 + Web health dashboard

### OpsClaw (Content Operations)

**Data Flow:** WeChat blogger articles → AI scoring & tagging → YouTube library matching (500+ videos)

- Auto hotspot tracking with AI scoring
- Material library matching: reply "Y" → 3min article generation
- No match: AI deep research & writing
- 7-day trend dashboard

**Output:** Telegram hotspot briefing + one-click article generation + Web hotspot dashboard

### GuardClaw (Product Research)

**Data Flow:** V7 Pipeline 6 Agents → pain point aggregation → trend analysis

- Top 5 pain point direction weekly fluctuation tracking
- Security audit at 03:00 daily
- One-click iPhone-style Landing Page generation
- 9-Agent full-chain coordination demo (45 seconds, zero human intervention)

**Output:** Telegram research daily report + LP generation + 9-Agent demo

---

## Shared Memory Coordination

The 3 agents coordinate autonomously through shared memory files — not if-else programming, but AI judgment via SOUL.md:

- CareClaw detects burnout → writes to `health_log.json`
- OpsClaw reads burnout state → reduces push notifications (5→2)
- GuardClaw reads burnout state → postpones non-urgent scans

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Engine | Claude Sonnet 4.6 (via OpenClaw) |
| Agent Framework | OpenClaw (9 Agents) |
| Hardware | Apple Watch Ultra (real health data) |
| Server | AWS EC2 (t3.large, 24/7) |
| Database | Supabase (23K+ pain points) |
| Messaging | Telegram Bot API |
| Web Dashboard | Express.js + vanilla HTML |
| Cron Jobs | 12 active (health, content, research, security) |

---

## Project Structure

```
clawpilot/
├── openclaw.json          # 9-Agent OpenClaw configuration
├── agents/                # Agent SOUL.md definitions
│   ├── CareClaw-SOUL.md
│   ├── OpsClaw-SOUL.md
│   └── GuardClaw-SOUL.md
├── scripts/               # Python scripts (EC2)
│   ├── shrimpilot_bot.py          # Main Telegram bot router
│   ├── unified_tg_router.py      # Unified TG message router
│   ├── morning_health_brief.py   # CareClaw daily health report
│   ├── apple_health_sync.py      # Apple Watch data receiver
│   ├── hotspot_monitor.py        # OpsClaw hotspot tracker
│   ├── research_morning_brief.py # GuardClaw daily report
│   ├── research_lp_gen.py        # One-click LP generator
│   ├── demo_coordination.py      # 9-Agent coordination demo
│   └── ...
├── skills/                # Skill definitions
├── web/                   # Express.js dashboard
│   ├── server.js
│   └── public/            # Health, hotspot, research dashboards
├── demo/                  # Hackathon assets
│   ├── ClawPilot-Dark.excalidraw  # Architecture diagram
│   └── images/
└── docs/                  # Project documentation
```

---

## Traction (Real Data)

| Metric | Value |
|--------|-------|
| Pain Points Collected | 23,234 |
| AI Agents | 9 |
| Cron Jobs | 12 |
| Web Dashboards | 3 |
| YouTube Materials | 500+ |
| Running Duration | 2+ weeks, 24/7 |

---

## Hardware Innovation

ClawPilot is one of the few hackathon projects that integrates AI Agents with **real hardware**:

- Apple Watch Ultra worn daily
- Real sleep, heart rate, HRV data (not simulated)
- Data synced to EC2 every hour via HTTPS
- CareClaw makes autonomous decisions based on real body data

---

## Links

- Telegram: `@clawpilot_bot`
- Built with: [OpenClaw](https://openclaw.com) + [Claude Sonnet 4.6](https://anthropic.com)

---

*Built for OpenClaw Hackathon 2026*
