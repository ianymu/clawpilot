---
name: care-health-check
description: CareShrimp 健康检查 Skill — Apple Health 同步 + 睡眠/心率/HRV 分析 + 倦怠检测 + 可配置提醒
---

# CareShrimp 健康管理（升级版）

## 触发
- Cron: 每 2h 工作状态检查 + Apple Health 数据分析
- Cron: 22:00 情绪 check-in + 四维健康方案
- Telegram: "感觉|mood|休息|break" → 即时健康评估
- Telegram: "静音|mute|提醒|interval|unmute" → 提醒配置
- Event: security_threat → 评估疲劳关联
- HTTP POST: Health Auto Export App → /api/health (端口 3001)

## Apple Health 数据同步
1. iPhone Health Auto Export App 自动 POST 到 EC2:3001/api/health
2. `apple_health_sync.py` 解析 sleep/heart_rate/HRV 数据
3. 基于 `health_standards.json`（WHO/NIH/Mayo Clinic 标准）分析
4. 倦怠复合检测：7 维信号 ≥3 → warning, ≥5 → critical
5. 结果写入 health_log.json + 触发 TG 告警

## 分析维度
| 维度 | 指标 | 来源 | 阈值 |
|------|------|------|------|
| 睡眠时长 | 总睡眠小时数 | Apple Health | < 7h 告警 |
| 睡眠效率 | 睡眠时间/在床时间 | Apple Health | < 85% 告警 |
| 深度睡眠 | 占比% | Apple Health | < 10% 告警 |
| 入睡时间 | 分钟 | Apple Health | > 30min 告警 |
| 静息心率 | bpm | Apple Health | > 基线+5bpm 告警 |
| HRV | RMSSD ms | Apple Health | 7日均值下降 >20% 告警 |
| 工作时长 | 连续小时 | Shell 活动 | 2h/4h/6h/10h 分级 |

## 可配置提醒（TG 指令）
- `静音2h` / `mute 30m` — 临时静音
- `取消静音` / `unmute` — 恢复提醒
- `提醒频率4h` — 调整检查间隔 (1-12h)
- `夜间静音 23:00-07:00` — 免打扰时段
- `关闭睡眠提醒` / `开启心率提醒` — 按类型开关
- `提醒状态` — 查看配置
- 注意：critical 级别告警（倦怠≥5信号）不受静音限制

## 工作追踪
1. 检查 shell 活动时间戳
2. 计算连续工作时长
3. 写入 health_log.json
4. 2h → 轻提醒 | 4h → 强提醒 | 6h → fatigue_detected 事件

## 情绪 Check-in
1. 发送互动问题
2. 记录 1-5 分评分 + 文字笔记
3. 基于 Apple Health 数据 + 历史情绪给个性化建议
4. 连续 3 天 < 3 分 → mood_low 事件

## 脚本
- `apple_health_sync.py` — 数据同步 + Flask 接收 + 分析引擎 + 静音管理
- `health_standards.json` — WHO/NIH/Mayo Clinic 专业标准

## EC2 部署
```bash
# 启动 Flask 接收端（systemd 服务）
python3 ~/scripts/apple_health_sync.py --serve --port 3001

# Mock 测试
python3 ~/scripts/apple_health_sync.py --mock          # 正常数据
python3 ~/scripts/apple_health_sync.py --mock-burnout   # 倦怠数据

# 分析现有数据
python3 ~/scripts/apple_health_sync.py --analyze --age 30
```

## 安全
- 健康数据仅本地存储 (`~/.shrimpilot/memory/`)
- 不上传外部服务
- TG 群只发简要提醒（不含详细生理数据）
- Flask API 需 `api-key` header 认证（`HAE_WRITE_TOKEN` 环境变量）
- 建议 HTTPS（nginx 反代 + Let's Encrypt）
