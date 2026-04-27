# Render.com Deployment Guide

## One-Time Setup: GitHub Auth + Push

```bash
# Step 1: Authenticate GitHub CLI
gh auth login
# → Choose: GitHub.com → HTTPS → Login with a web browser
# → Authorize in browser when prompted

# Step 2: Push all 3 repos (run from anywhere)
bash /Users/elbarrio/.openclaw/workspace/deploy-dashboards.sh
```

---

## Render Deploy Instructions (repeat for each app)

### 🏠 El Barrio Dashboard (Flask Web Service)

1. Go to https://render.com → **New → Web Service**
2. Connect your GitHub account if not done
3. Select repo: **elbarrio-dashboard**
4. Configure:
   - **Name:** `elbarrio-dashboard`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free
5. Click **Create Web Service**
6. Wait ~2 min → your URL: `https://elbarrio-dashboard.onrender.com`

---

### 🏃 Godspeed Dashboard (Flask Web Service)

1. Go to https://render.com → **New → Web Service**
2. Select repo: **godspeed-dashboard**
3. Configure:
   - **Name:** `godspeed-dashboard`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free
4. **Environment Variables** (optional — for Google Sheets live data):
   - Click **Advanced → Add Environment Variable**
   - `GOOGLE_TOKEN_JSON` → paste contents of `~/.openclaw/drive-token.json`
   - `GOOGLE_CREDENTIALS_JSON` → paste contents of `~/.openclaw/google-credentials.json`
5. Click **Create Web Service**
6. URL: `https://godspeed-dashboard.onrender.com`

> ⚠️ Without env vars, the dashboard deploys fine but shows empty data.
> The Google Sheets integration requires the credentials above.

---

### 🔱 King Neptune (Static Site)

1. Go to https://render.com → **New → Static Site**
2. Select repo: **king-neptune-dashboard**
3. Configure:
   - **Name:** `king-neptune-dashboard`
   - **Publish Directory:** `.` (root — the index.html is at root)
   - **Plan:** Free
4. Click **Create Static Site**
5. URL: `https://king-neptune-dashboard.onrender.com`

---

## Notes

- Free tier on Render spins down after 15 min of inactivity (cold start ~30s)
- Upgrade to Starter ($7/mo) to keep always-on
- All 3 repos are public — do NOT add credentials files to git (`.gitignore` handles this)
- Godspeed Google Sheets creds go in Render env vars only — never in the repo
