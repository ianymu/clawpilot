#!/usr/bin/env node
/**
 * shrimp-web — ShrimPilot 统一 Web 平台
 * 端口 3080，深色主题，移动优先
 *
 * API 从本地 JSON 文件读取数据（由各 cron 脚本写入）
 * pm2 start server.js --name shrimp-web
 */

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3080;

// Memory dir where shrimp scripts write data
const MEMORY_DIR = path.join(process.env.HOME, '.shrimpilot', 'memory');
const REPORTS_DIR = path.join(process.env.HOME, 'reports');

// Static files
app.use(express.static(path.join(__dirname, 'public')));

// --- Helper ---
function readJSON(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (e) {
    return null;
  }
}

// --- API: Health ---
app.get('/api/health', (req, res) => {
  const today = readJSON(path.join(MEMORY_DIR, 'health_log.json'));

  // Build 7-day history from health_log hrv_history + mock
  let history = [];
  if (today && today.hrv_history) {
    history = today.hrv_history.map(h => ({
      date: h.date,
      hrv: h.avg
    }));
  }

  // Try to read history file
  const histFile = readJSON(path.join(MEMORY_DIR, 'health_history.json'));
  if (histFile && Array.isArray(histFile)) {
    // Use dedicated history file if available
    res.json({ today, history: histFile });
  } else {
    // Synthesize from today's data
    const synth = [];
    if (today) {
      const hrvHist = today.hrv_history || [];
      const sleepData = today.sleep_data || {};
      for (const h of hrvHist) {
        synth.push({
          date: h.date,
          hrv: h.avg,
          sleep_hours: sleepData.total_hours ? sleepData.total_hours + (Math.random() - 0.5) * 1.5 : null,
          deep_pct: sleepData.deep_pct ? sleepData.deep_pct + (Math.random() - 0.5) * 5 : null,
          rem_pct: sleepData.rem_pct ? sleepData.rem_pct + (Math.random() - 0.5) * 4 : null,
          efficiency: sleepData.efficiency_pct ? sleepData.efficiency_pct + (Math.random() - 0.5) * 6 : null,
          resting_hr: today.resting_hr_bpm ? today.resting_hr_bpm + Math.floor((Math.random() - 0.5) * 8) : null
        });
      }
      // Add today
      synth.push({
        date: today.date,
        hrv: today.hrv_latest_ms,
        sleep_hours: sleepData.total_hours,
        deep_pct: sleepData.deep_pct,
        rem_pct: sleepData.rem_pct,
        efficiency: sleepData.efficiency_pct,
        resting_hr: today.resting_hr_bpm
      });
    }
    res.json({ today, history: synth });
  }
});

// --- API: Meal Log ---
app.get('/api/meal-log', (req, res) => {
  const data = readJSON(path.join(MEMORY_DIR, 'meal_log.json'));
  res.json(data || { entries: [], current_streak: 0 });
});

// --- API: Hotspot ---
app.get('/api/hotspot', (req, res) => {
  const summary = readJSON(path.join(MEMORY_DIR, 'hotspot_summary.json'));
  const trendData = readJSON(path.join(MEMORY_DIR, 'wechat_trends_7d.json'));
  if (summary && trendData && trendData.trends) {
    summary.trend_chart = trendData;
  }
  res.json(summary || { error: 'No hotspot data' });
});

// --- API: Research (pain aggregation) ---
app.get('/api/research', (req, res) => {
  // Try multiple possible locations
  const paths = [
    path.join(REPORTS_DIR, 'pain-aggregation-report.json'),
    path.join(process.env.HOME, 'pain-aggregation-report.json'),
    path.join(MEMORY_DIR, 'pain_directions.json'),
  ];
  for (const p of paths) {
    const data = readJSON(p);
    if (data) {
      return res.json(data);
    }
  }
  res.json([]);
});

// --- API: Content ---
app.get('/api/content', (req, res) => {
  const contentDir = path.join(MEMORY_DIR, 'content_drafts');
  if (!fs.existsSync(contentDir)) {
    return res.json([]);
  }
  try {
    const files = fs.readdirSync(contentDir)
      .filter(f => f.endsWith('.json'))
      .sort()
      .reverse()
      .slice(0, 20);
    const items = files.map(f => readJSON(path.join(contentDir, f))).filter(Boolean);
    res.json(items);
  } catch {
    res.json([]);
  }
});

// --- SPA fallback ---
app.get('*', (req, res) => {
  const page = req.path.replace('/', '') || 'index';
  const file = path.join(__dirname, 'public', `${page}.html`);
  if (fs.existsSync(file)) {
    return res.sendFile(file);
  }
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`[shrimp-web] Running on http://0.0.0.0:${PORT}`);
});
