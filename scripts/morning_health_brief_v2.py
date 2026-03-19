#!/usr/bin/env python3
"""
morning_health_brief.py — CareShrimp 每日健康早报 V2

升级内容:
- 拆分为 3 条消息（睡眠身体 / 建议 / 饮食）
- 专业标准引用（AASM/NIH/Mayo Clinic/Lifelines Cohort）
- HRV 7日均值驱动饮食建议
- 精力曲线预测
- 网站锚点链接
- 手机 Shortcuts 提醒链接

用法:
  python3 morning_health_brief_v2.py              # 生成并推送
  python3 morning_health_brief_v2.py --dry-run    # 只打印不推送
  python3 morning_health_brief_v2.py --age 30     # 指定年龄

Cron (openclaw.json):
  schedule: "30 7 * * *"  # 每天 07:30 北京时间
"""

import os
import sys
import json
import logging
import argparse
import time as _time
from datetime import datetime, timedelta, timezone
from pathlib import Path

BJT = timezone(timedelta(hours=8))
def now_bjt():
    return datetime.now(BJT)

# 复用 apple_health_sync 的核心函数
sys.path.insert(0, str(Path(__file__).parent))
from apple_health_sync import (
    load_json,
    load_standards,
    analyze_health,
    is_reminder_allowed,
    HEALTH_LOG_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("morning_health_brief")

WEB_URL = "http://18.221.160.170/shrimp"


# === HRV 年龄正常值 (Lifelines Cohort Study) ===
HRV_NORMS = {
    "20-29": {"low": 25, "normal": 40, "good": 60},
    "30-39": {"low": 20, "normal": 35, "good": 50},
    "40-49": {"low": 15, "normal": 30, "good": 45},
    "50-59": {"low": 12, "normal": 25, "good": 38},
    "60+": {"low": 10, "normal": 20, "good": 30},
}


def _age_to_hrv_key(age: int) -> str:
    """将年龄映射到 HRV 正常值区间"""
    if age < 30:
        return "20-29"
    elif age < 40:
        return "30-39"
    elif age < 50:
        return "40-49"
    elif age < 60:
        return "50-59"
    return "60+"


def generate_brief(health_log: dict, analysis: dict, user_age: int = 30) -> tuple:
    """生成 3 条消息的健康早报，返回 (msg1, msg2, msg3) 三元组"""
    msg1 = _generate_msg1_sleep_body(health_log, analysis, user_age)
    msg2 = _generate_msg2_suggestions(health_log, analysis, user_age)
    msg3 = _generate_msg3_diet(health_log, user_age)
    return (msg1, msg2, msg3)


def _generate_msg1_sleep_body(health_log: dict, analysis: dict, user_age: int) -> str:
    """消息 1: 睡眠 + 心率 + HRV + 倦怠状态"""
    today = now_bjt().strftime("%m月%d日")
    weekday_map = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    weekday = weekday_map[now_bjt().weekday()]

    lines = [f"*健康虾早报* — {today} {weekday}", ""]

    # --- 睡眠总览 ---
    sleep_hours = health_log.get("sleep_hours_estimated")
    sleep_data = health_log.get("sleep_data", {})

    if sleep_hours:
        eff = sleep_data.get("efficiency_pct")
        emoji = "OK" if sleep_hours >= 7 else "!!" if sleep_hours >= 5 else "!!!"
        eff_str = f"（效率 {eff}%）" if eff else ""
        lines.append(f"[{emoji}] *睡眠 {sleep_hours}h{eff_str}*")

        # 深度睡眠 — 带 AASM 标准
        deep_pct = sleep_data.get("deep_pct")
        if deep_pct is not None:
            deep_h = round(sleep_hours * deep_pct / 100, 1)
            deep_status = "OK" if deep_pct >= 15 else "LOW"
            lines.append(f"  深度睡眠 {deep_h}h ({deep_pct}%) [{deep_status}]")
            lines.append(f"     AASM 建议 10-20% (身体修复阶段)")
            if deep_pct < 15:
                lines.append(f"     偏低，今晚试试：睡前 1h 不看屏幕")

        # REM — 带 AASM 标准
        rem_pct = sleep_data.get("rem_pct")
        if rem_pct is not None:
            rem_h = round(sleep_hours * rem_pct / 100, 1)
            rem_status = "OK" if rem_pct >= 20 else "LOW"
            lines.append(f"  REM 睡眠 {rem_h}h ({rem_pct}%) [{rem_status}]")
            lines.append(f"     AASM 标准 20-25% (记忆巩固阶段)")

        # 入睡时间
        latency = sleep_data.get("latency_min")
        if latency is not None:
            lat_status = "OK" if latency <= 15 else "LONG" if latency <= 30 else "!!!"
            lines.append(f"  入睡耗时 {int(latency)}min [{lat_status}]")
            if latency > 20:
                lines.append(f"     偏长，试试 4-7-8 呼吸法")
    else:
        lines.append("*睡眠*: 暂无数据")

    lines.append("")

    # --- 心率 ---
    rhr = health_log.get("resting_hr_bpm")
    if rhr:
        status = "正常" if 60 <= rhr <= 75 else "偏高，注意压力" if rhr > 75 else "偏低"
        lines.append(f"*静息心率* {rhr} bpm（{status}）")

    # --- HRV 带年龄正常值 ---
    hrv = health_log.get("hrv_latest_ms")
    hrv_history = health_log.get("hrv_history", [])
    if hrv:
        recent_hrv = [h.get("avg", 0) for h in hrv_history[-7:]] if hrv_history else []
        avg_7d = sum(recent_hrv) / len(recent_hrv) if recent_hrv else 0
        change = hrv - avg_7d if avg_7d > 0 else 0
        change_str = f"{'↑' if change >= 0 else '↓'}{abs(change):.0f}ms vs 周均" if avg_7d > 0 else ""

        hrv_key = _age_to_hrv_key(user_age)
        norms = HRV_NORMS[hrv_key]
        hrv_status = "良好" if hrv >= norms["good"] else "正常" if hrv >= norms["normal"] else "偏低" if hrv >= norms["low"] else "低"
        lines.append(f"*HRV* {hrv}ms {change_str} ({hrv_status})")
        lines.append(f"  HRV = 心跳间隔变化，越高代表身体恢复越好")
        lines.append(f"  {user_age}岁正常值: {norms['normal']}-{norms['good']}ms (Lifelines Cohort)")
        if change > 0:
            lines.append(f"  比 7 天平均高 {abs(change):.0f}ms，休息不错")
        elif change < -5:
            lines.append(f"  比 7 天平均低 {abs(change):.0f}ms，身体恢复偏差")

    lines.append("")

    # --- 告警 ---
    alerts = analysis.get("alerts", [])
    burnout = analysis.get("burnout", {})
    critical = [a for a in alerts if a["severity"] == "critical"]
    warnings = [a for a in alerts if a["severity"] == "warning"]

    if critical:
        lines.append("*[!!!] 需要注意:*")
        for a in critical:
            lines.append(f"  - {a['message']}")
        lines.append("")

    if warnings:
        lines.append("*[!!] 建议关注:*")
        for a in warnings[:3]:
            lines.append(f"  - {a['message']}")
        lines.append("")

    # --- 倦怠状态 ---
    severity = burnout.get("severity", "normal")
    signals = burnout.get("signals_active", 0)
    if severity == "critical":
        lines.append(f"*倦怠风险: 高* ({signals}/7 信号)")
        lines.append("  强烈建议今天减量，你先休息。")
    elif severity == "warning":
        lines.append(f"*倦怠风险: 中* ({signals}/7 信号)")
    elif severity == "monitor":
        lines.append(f"*身体状态: 需留意* ({signals}/7 信号)")
    else:
        lines.append("*身体状态: 良好*")

    lines.append("")
    lines.append(f"详情 → {WEB_URL}/health#overview")

    return "\n".join(lines)


def _generate_msg2_suggestions(health_log: dict, analysis: dict, user_age: int) -> str:
    """消息 2: 今日建议 + 专业标准引用"""
    lines = ["*今日建议*", ""]

    suggestions = _generate_suggestions_v2(health_log, analysis)
    for s in suggestions:
        lines.append(f"  - {s}")

    # 专业标准引用
    lines.append("")
    lines.append("*参考标准:*")
    lines.append("  - 睡眠时长: NIH 建议成人 7-9h/晚")
    lines.append("  - 深度/REM: AASM 2017 睡眠阶段指南")

    hrv = health_log.get("hrv_latest_ms")
    if hrv:
        hrv_key = _age_to_hrv_key(user_age)
        norms = HRV_NORMS[hrv_key]
        lines.append(f"  - HRV 正常值 ({hrv_key}岁): {norms['normal']}-{norms['good']}ms (Lifelines Cohort 2019)")

    rhr = health_log.get("resting_hr_bpm")
    if rhr:
        lines.append("  - 静息心率: Mayo Clinic 正常值 60-100bpm")

    lines.append("")
    lines.append(f"详情 → {WEB_URL}/health#suggestions")

    return "\n".join(lines)


def _generate_msg3_diet(health_log: dict, user_age: int) -> str:
    """消息 3: 饮食建议(基于7日HRV) + 拍照提醒 + Shortcuts 链接"""
    lines = ["*饮食建议*", ""]

    hrv_history = health_log.get("hrv_history", [])
    recent_hrv = [h.get("avg", 0) for h in hrv_history[-7:]] if hrv_history else []
    avg_7d = sum(recent_hrv) / len(recent_hrv) if recent_hrv else 0

    hrv_key = _age_to_hrv_key(user_age)
    norms = HRV_NORMS[hrv_key]

    sleep_hours = health_log.get("sleep_hours_estimated", 0)

    if avg_7d > 0 and avg_7d < norms["normal"]:
        # 恢复期饮食
        lines.append(f"7 日 HRV 均值 {avg_7d:.0f}ms，低于正常值 {norms['normal']}ms")
        lines.append("身体处于 *恢复期*，需要抗炎 + 高蛋白饮食:")
        lines.append("")
        lines.append("*午餐 (恢复型):*")
        lines.append("  - 鸡胸肉/三文鱼 + 深色蔬菜 (菠菜/西兰花)")
        lines.append("  - 避免油炸和高糖，加重炎症反应")
        lines.append("  - 餐后散步 10min，帮助消化")
        lines.append("")
        lines.append("*晚餐 (助眠型):*")
        lines.append("  - 含色氨酸: 火鸡/香蕉/温牛奶")
        lines.append("  - 含镁: 坚果/深色绿叶菜")
        lines.append("  - 睡前 2h 不吃重食")
    elif avg_7d > 0 and avg_7d > norms["good"]:
        # 状态良好
        lines.append(f"7 日 HRV 均值 {avg_7d:.0f}ms，高于良好值 {norms['good']}ms")
        lines.append("身体状态 *良好*，正常均衡饮食即可:")
        lines.append("")
        lines.append("  - 午餐: 蛋白质 + 蔬菜 + 适量碳水")
        lines.append("  - 下午茶: 水果 + 坚果")
        lines.append("  - 全天饮水 2000ml (8 杯)")
    elif sleep_hours and sleep_hours < 7:
        # 睡眠不足的压力期
        lines.append("昨晚睡眠不足，身体处于 *压力期*:")
        lines.append("")
        lines.append("*午餐 (能量型):*")
        lines.append("  - 牛肉面/鸡排饭 + 一份蔬菜")
        lines.append("  - 避免纯碳水 (炒饭/面包)，容易犯困")
        lines.append("")
        lines.append("*加餐:*")
        lines.append("  - 下午 3 点: 一杯咖啡 + 坚果 (最后一杯)")
        lines.append("  - 全天饮水 2000ml (8 杯)")
    else:
        # 默认建议
        lines.append("正常均衡饮食:")
        lines.append("")
        lines.append("  - 午餐: 蛋白质 + 蔬菜 + 适量碳水")
        lines.append("  - 下午茶: 水果 + 坚果")
        lines.append("  - 全天饮水 2000ml (8 杯)")

    lines.append("")
    lines.append("中午记得给我拍照，我好给你更精准的饮食建议!")
    lines.append("")
    lines.append(f"[设置午餐提醒](shortcuts://run-shortcut?name=午餐提醒)")
    lines.append("")
    lines.append(f"详情 → {WEB_URL}/health#diet")
    lines.append("")
    lines.append("_— 健康虾，守护你的每一天_")

    return "\n".join(lines)


def _generate_suggestions_v2(health_log: dict, analysis: dict) -> list:
    """基于数据生成具体、可执行的建议"""
    suggestions = []
    sleep_hours = health_log.get("sleep_hours_estimated", 0)
    sleep_data = health_log.get("sleep_data", {})
    rhr = health_log.get("resting_hr_bpm")
    hrv = health_log.get("hrv_latest_ms")
    burnout = analysis.get("burnout", {})
    severity = burnout.get("severity", "normal")

    # 精力曲线预测
    bedtime = sleep_data.get("bedtime", "")
    is_late = False
    if bedtime:
        try:
            bt = datetime.strptime(bedtime.split(" ")[-1] if " " in bedtime else bedtime, "%H:%M")
            is_late = bt.hour >= 1 and bt.hour < 6
        except (ValueError, IndexError):
            try:
                bt_full = datetime.fromisoformat(bedtime)
                is_late = bt_full.hour >= 1 and bt_full.hour < 6
            except (ValueError, TypeError):
                pass

    if is_late and sleep_hours and sleep_hours < 7:
        suggestions.append("昨晚熬夜了，上午精力可能在 10 点前走下坡")
        suggestions.append("建议 10:30 前完成最重要的决策性工作")
    elif sleep_hours and sleep_hours < 7:
        deficit = round(7 - sleep_hours, 1)
        suggestions.append(f"昨晚少睡了 {deficit}h，中午补个 20min 午睡能恢复 60% 精力")

    # 深度睡眠不足
    deep_pct = sleep_data.get("deep_pct")
    if deep_pct is not None and deep_pct < 10:
        suggestions.append("深度睡眠严重不足，今晚：睡前 1h 不看屏幕 + 房间 18-20°C (AASM)")

    # 心率偏高
    if rhr and rhr > 80:
        suggestions.append(f"心率 {rhr}bpm 偏高 (Mayo Clinic 正常 60-100)，每 2h 做 3 次深呼吸")

    # HRV 偏低
    if hrv and hrv < 25:
        suggestions.append("HRV 偏低，身体恢复不足 (NIH)，避免长时间高强度工作")

    # 饮水
    suggestions.append("全天目标饮水 2000ml（约 8 杯），每 2h 喝一杯")

    # 倦怠
    if severity in ("warning", "critical"):
        suggestions.append("倦怠信号明显，工作量减少 30%，每 50min 起身走 5min")

    # 通用
    if not any("精力" in s or "少睡" in s or "熬夜" in s for s in suggestions):
        suggestions.insert(0, "状态不错! 保持这个节奏")

    return suggestions[:6]


def send_tg(message: str):
    """发送到 Telegram"""
    token = os.environ.get("TG_SHRIMPILOT_TOKEN", "").strip()
    chat_id = os.environ.get("TG_SHRIMPILOT_CHAT_ID", "").strip()
    if not token or not chat_id:
        log.warning("TG 未配置 (TG_SHRIMPILOT_TOKEN / TG_SHRIMPILOT_CHAT_ID)")
        return False

    import urllib.request
    import urllib.parse
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode(
        {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    ).encode()
    try:
        urllib.request.urlopen(url, data, timeout=15)
        log.info("TG 消息已推送")
        return True
    except Exception as e:
        log.error("TG 推送失败: %s", e)
        # Retry without Markdown
        try:
            data_plain = urllib.parse.urlencode(
                {"chat_id": chat_id, "text": message}
            ).encode()
            urllib.request.urlopen(url, data_plain, timeout=15)
            return True
        except Exception:
            return False


def main():
    parser = argparse.ArgumentParser(description="CareShrimp 每日健康早报 V2")
    parser.add_argument("--dry-run", action="store_true", help="只打印不推送 TG")
    parser.add_argument("--age", type=int, default=30, help="用户年龄 (默认 30)")
    args = parser.parse_args()

    # 检查是否允许发送提醒
    if not args.dry_run and not is_reminder_allowed("sleep"):
        log.info("当前处于静音状态，跳过早报推送")
        return

    # 读取健康数据
    health_log = load_json(HEALTH_LOG_PATH, {})
    if not health_log:
        log.warning("health_log.json 为空，使用默认数据")
        health_log = {"date": now_bjt().strftime("%Y-%m-%d")}

    # 加载专业标准
    standards = load_standards()
    log.info("已加载 health_standards.json: %d 项", len(standards) if isinstance(standards, dict) else 0)

    # 分析
    analysis = analyze_health(health_log, user_age=args.age)

    # 生成 3 条消息
    msg1, msg2, msg3 = generate_brief(health_log, analysis, user_age=args.age)

    if args.dry_run:
        print("=== 消息 1: 睡眠+身体 ===")
        print(msg1)
        print("\n=== 消息 2: 建议 ===")
        print(msg2)
        print("\n=== 消息 3: 饮食 ===")
        print(msg3)
        print("\n[dry-run] 未推送 TG")
    else:
        for i, msg in enumerate([msg1, msg2, msg3], 1):
            print(f"=== 发送消息 {i}/3 ===")
            print(msg)
            send_tg(msg)
            if i < 3:
                _time.sleep(2)
        log.info("3 条早报消息已全部推送")


if __name__ == "__main__":
    main()
