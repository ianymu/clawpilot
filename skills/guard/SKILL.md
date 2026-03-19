---
name: guard-security-scan
description: GuardShrimp 安全扫描 Skill — Skill 风险分析、依赖漏洞检查、夜间巡检
---

# GuardShrimp 安全扫描

## 触发
- Telegram: "扫描|scan|audit"
- Cron: 03:00 夜间安全巡检
- Event: fatigue_detected → 标记代码高风险

## Skill 安全扫描
1. 读取 Skill 源码（SKILL.md + 关联脚本）
2. 分析请求权限 vs 声明功能
3. 检测可疑模式（base64 URL、外传数据）
4. 输出风险评级: LOW/MEDIUM/HIGH/CRITICAL
5. HIGH+ 建议拒绝安装

## 依赖漏洞检查
1. 扫描 package.json / requirements.txt
2. 运行 npm audit / pip-audit
3. 汇总 CVE + 严重程度 + 修复版本
4. 生成修复建议

## 夜间巡检（03:00）
1. 检查过去 24h 新安装的包/Skill
2. 检查 .env 文件权限
3. 检查异常文件变更
4. 结果写入 security_log.json

## 疲劳联动
- 收到 fatigue_detected → 标记下次代码提交为高风险
- 触发 fatigue_code_risk → OpsShrimp 推迟发布

## 安全
- 扫描结果不含实际 Key 值
- 零信任: 每个 Skill 假设可能恶意
- 六要六不要合规
