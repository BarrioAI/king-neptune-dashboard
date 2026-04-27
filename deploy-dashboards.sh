#!/bin/bash
# deploy-dashboards.sh
# Run this AFTER completing: gh auth login
# It will create 3 GitHub repos and push all dashboards.

set -e

echo "🚀 El Barrio Dashboard Deployment Script"
echo "========================================="

# Verify gh is authenticated
if ! gh auth status &>/dev/null; then
  echo "❌ Not logged into GitHub. Run: gh auth login"
  exit 1
fi

GH_USER=$(gh api user --jq .login)
echo "✅ Logged in as: $GH_USER"

# ─── TASK 1: El Barrio Dashboard ───────────────────────────────────────────
echo ""
echo "📦 [1/3] Deploying El Barrio Dashboard..."
cd /Users/elbarrio/.openclaw/workspace/elbarrio-dashboard

# Create GitHub repo (public)
gh repo create elbarrio-dashboard \
  --public \
  --description "El Barrio AI multi-agent operations hub" \
  --source=. \
  --remote=origin \
  --push \
  2>/dev/null || {
    echo "   Repo may already exist — setting remote and pushing..."
    git remote set-url origin "https://github.com/$GH_USER/elbarrio-dashboard.git" 2>/dev/null \
      || git remote add origin "https://github.com/$GH_USER/elbarrio-dashboard.git"
    git push -u origin main
  }

echo "   ✅ https://github.com/$GH_USER/elbarrio-dashboard"

# ─── TASK 2: Godspeed Dashboard ────────────────────────────────────────────
echo ""
echo "📦 [2/3] Deploying Godspeed Dashboard..."
cd /Users/elbarrio/.openclaw/workspace/godspeed-dashboard

gh repo create godspeed-dashboard \
  --public \
  --description "Godspeed Retail Intelligence Dashboard" \
  --source=. \
  --remote=origin \
  --push \
  2>/dev/null || {
    echo "   Repo may already exist — setting remote and pushing..."
    git remote set-url origin "https://github.com/$GH_USER/godspeed-dashboard.git" 2>/dev/null \
      || git remote add origin "https://github.com/$GH_USER/godspeed-dashboard.git"
    git push -u origin main
  }

echo "   ✅ https://github.com/$GH_USER/godspeed-dashboard"

# ─── TASK 3: King Neptune ──────────────────────────────────────────────────
echo ""
echo "📦 [3/3] Deploying King Neptune..."
cd /Users/elbarrio/.openclaw/workspace/king-neptune/dashboard

gh repo create king-neptune-dashboard \
  --public \
  --description "King Neptune — College Cash Dashboard for Emilio" \
  --source=. \
  --remote=origin \
  --push \
  2>/dev/null || {
    echo "   Repo may already exist — setting remote and pushing..."
    git remote set-url origin "https://github.com/$GH_USER/king-neptune-dashboard.git" 2>/dev/null \
      || git remote add origin "https://github.com/$GH_USER/king-neptune-dashboard.git"
    git push -u origin main
  }

echo "   ✅ https://github.com/$GH_USER/king-neptune-dashboard"

# ─── SUMMARY ───────────────────────────────────────────────────────────────
echo ""
echo "🎉 All 3 repos pushed to GitHub!"
echo ""
echo "GitHub URLs:"
echo "  El Barrio:   https://github.com/$GH_USER/elbarrio-dashboard"
echo "  Godspeed:    https://github.com/$GH_USER/godspeed-dashboard"
echo "  King Neptune: https://github.com/$GH_USER/king-neptune-dashboard"
echo ""
echo "Next: Deploy each on Render.com → see RENDER-DEPLOY.md for instructions"
