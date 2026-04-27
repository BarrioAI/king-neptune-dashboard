#!/usr/bin/env python3
"""
Build a self-contained index.html for El Barrio Mission Control.
Embeds state.json + activity.ndjson directly into the HTML so no server is needed.
"""

import json
import re
from pathlib import Path

SRC = Path(__file__).parent / "public"
DEST_DIR = Path(__file__).parent.parent / "elbarrio-mission-control"
DEST_DIR.mkdir(exist_ok=True)

# ---------- 1. Updated state data (Thu Apr 24, 2026) ----------
state = {
  "schema_version": "1.0",
  "generated_at": "2026-04-24T12:00:00Z",
  "generated_by": "adolfo",
  "today": {
    "label": "THU 04\u00b724",
    "owner_agent_id": "adolfo",
    "owner_agent_emoji": "\U0001f9e0",
    "owner_agent_name": "Adolfo",
    "summary": "El Barrio dashboards going live \u2014 3 deployments shipped to Render today",
    "agents_online": 11,
    "escalations": 0
  },
  "hubs": [
    {
      "id": "casa-de-goldie",
      "name": "Casa De Goldie",
      "tag": "Personal HQ \u00b7 Home Base",
      "accent": "#FFC371",
      "stats": [
        {"label": "projects", "value": "5"},
        {"label": "agents", "value": "4"},
        {"label": "scholarships", "value": "2k+"}
      ],
      "footer_left": "biohacking \u00b7 finance \u00b7 KN dash",
      "footer_right": "\u25b6 live",
      "label_line_1": "personal HQ",
      "label_line_2": "4 active",
      "detail": {
        "title": "Casa De Goldie",
        "subtitle": "Personal HQ \u00b7 Home Base",
        "sections": [
          {
            "heading": "\U0001f464 Owner",
            "items": [
              {"label": "Name", "value": "Javier Vergara (Goldie)"},
              {"label": "Base", "value": "Miami, FL"},
              {"label": "Timezone", "value": "EDT (UTC-4)"}
            ]
          },
          {
            "heading": "\U0001f3d7\ufe0f Active Hubs",
            "items": [
              {"label": "Businesses", "value": "3 active"},
              {"label": "Agents Running", "value": "12 total"},
              {"label": "King Neptune", "value": "Emilio scholarship dashboard live"}
            ]
          }
        ]
      }
    },
    {
      "id": "goldie-endeavor",
      "name": "Goldie Endeavor",
      "tag": "Booking Agency",
      "accent": "#FF3CAC",
      "stats": [
        {"label": "artists", "value": "\u2014"},
        {"label": "workflows", "value": "TBD"},
        {"label": "contracts", "value": "0"}
      ],
      "footer_left": "artist contracts \u00b7 calendar",
      "footer_right": "build phase",
      "label_line_1": "booking",
      "label_line_2": "workflows TBD",
      "detail": {
        "title": "Goldie Endeavor",
        "subtitle": "Booking Agency \u00b7 Build Phase",
        "sections": [
          {
            "heading": "\U0001f4cb Status",
            "items": [
              {"label": "Stage", "value": "Build phase"},
              {"label": "Artists", "value": "TBD"},
              {"label": "Contracts", "value": "0 active"},
              {"label": "Next Step", "value": "Define artist roster"}
            ]
          }
        ]
      }
    },
    {
      "id": "colombia-care",
      "name": "Colombia Care",
      "tag": "Stem Cell \u00b7 Medical",
      "accent": "#FF8AAA",
      "stats": [
        {"label": "IG", "value": "12.4k"},
        {"label": "assets", "value": "6"},
        {"label": "cta", "value": "!"}
      ],
      "footer_left": "Quintero shipped 6 assets",
      "footer_right": "review",
      "label_line_1": "medical",
      "label_line_2": "12.4k IG",
      "detail": {
        "title": "ColombiaCareGroup",
        "subtitle": "Stem Cell \u00b7 Medical Tourism \u00b7 Anti-Aging",
        "sections": [
          {
            "heading": "\U0001f4ca Metrics",
            "items": [
              {"label": "Instagram", "value": "@colombiacaregroup"},
              {"label": "Followers", "value": "12.4K"},
              {"label": "Website", "value": "colombiacaregroup.com (not live)"}
            ]
          },
          {
            "heading": "\U0001f3af Pipeline",
            "items": [
              {"label": "Bradley Roby Deck", "value": "Built \u2014 needs redesign"},
              {"label": "Dr. Bilal Sheikh", "value": "Referral partner \u2014 plan needed"},
              {"label": "Services Doc", "value": "Needs resend to Goldie"}
            ]
          }
        ]
      }
    },
    {
      "id": "varsity-lg",
      "name": "Varsity LG",
      "tag": "Lifestyle \u00b7 LIV / Kingpin",
      "accent": "#FFC371",
      "stats": [
        {"label": "IG", "value": "18.0k"},
        {"label": "wk", "value": "+312"},
        {"label": "events", "value": "5"}
      ],
      "footer_left": "Fri @ LIV \u00b7 Kingpin booked",
      "footer_right": "\u2191 growing",
      "label_line_1": "18.0k IG",
      "label_line_2": "LIV / Kingpin",
      "detail": {
        "title": "VarsityLG",
        "subtitle": "Lifestyle \u00b7 Events \u00b7 LIV / Kingpin",
        "sections": [
          {
            "heading": "\U0001f4ca Social",
            "items": [
              {"label": "Instagram", "value": "@varsitylg"},
              {"label": "Followers", "value": "18K"},
              {"label": "Weekly Growth", "value": "+312"}
            ]
          },
          {
            "heading": "\U0001f3aa Events",
            "items": [
              {"label": "Upcoming", "value": "5 events booked"},
              {"label": "Venues", "value": "LIV, Kingpin"}
            ]
          }
        ]
      }
    },
    {
      "id": "godspeed",
      "name": "Godspeed Retail",
      "tag": "Acquisition \u00b7 Hellstar FL",
      "accent": "#FF8A3C",
      "stats": [
        {"label": "leads", "value": "841"},
        {"label": "priority", "value": "23"},
        {"label": "today", "value": "+8"}
      ],
      "footer_left": "Jordan running outreach",
      "footer_right": "\u25b6 live",
      "label_line_1": "841 leads",
      "label_line_2": "23 Hellstar FL",
      "detail": {
        "title": "Godspeed Retail",
        "subtitle": "Streetwear \u00b7 Florida Hellstar Acquisition",
        "sections": [
          {
            "heading": "\U0001f4ca Pipeline",
            "items": [
              {"label": "Total Store Leads", "value": "765"},
              {"label": "Florida Hellstar Targets", "value": "23"},
              {"label": "Caribbean Leads", "value": "47"},
              {"label": "Warm Accounts", "value": "1 (HYP Miami)"},
              {"label": "Outreach Status", "value": "Awaiting go-signal"}
            ]
          },
          {
            "heading": "\U0001f43a Sales Agent",
            "items": [
              {"label": "Agent", "value": "Jordan Belfort"},
              {"label": "Strategy", "value": "Hellstar stockists first"},
              {"label": "Priority", "value": "23 FL Hellstar stores"},
              {"label": "Warm Contact", "value": "HYP Miami \u2014 carries Godspeed"},
              {"label": "Next Action", "value": "Goldie go-signal needed"}
            ]
          }
        ]
      }
    },
    {
      "id": "barrio-music",
      "name": "Barrio Music Group",
      "tag": "Music \u00b7 Bizzy \u00b7 A&R",
      "accent": "#A064D8",
      "stats": [
        {"label": "artist", "value": "1"},
        {"label": "promo", "value": "v3"},
        {"label": "scouting", "value": "\u221e"}
      ],
      "footer_left": "Bizzy \u00b7 talent scouting live",
      "footer_right": "active",
      "label_line_1": "Bizzy",
      "label_line_2": "talent scouting",
      "detail": {
        "title": "Barrio Music Group",
        "subtitle": "Music \u00b7 A&R \u00b7 Artist Management",
        "sections": [
          {
            "heading": "\U0001f3b5 Active",
            "items": [
              {"label": "Artist", "value": "Bizzy Crook"},
              {"label": "Current Single", "value": "Risky ft. Rick Ross & C Stunna"},
              {"label": "Label", "value": "EZMNY Records (Ty Dolla \u2019)"},
              {"label": "Producer", "value": "ACRAZE"},
              {"label": "Released", "value": "March 27, 2026"}
            ]
          },
          {
            "heading": "\U0001f4cb Campaign Assets",
            "items": [
              {"label": "Marketing Deck", "value": "\u2705 Built"},
              {"label": "TikTok Influencers", "value": "50 identified"},
              {"label": "Video Treatment", "value": "\u2705 Built"},
              {"label": "TikTok Pipeline", "value": "\u23f3 Pending build"}
            ]
          }
        ]
      }
    },
    {
      "id": "translation-mkt",
      "name": "Translation Mkt",
      "tag": "Marketing Engine \u00b7 Feeds All",
      "accent": "#2EE6CA",
      "stats": [
        {"label": "hubs fed", "value": "7"},
        {"label": "content", "value": "\u221e"},
        {"label": "lead", "value": "Jay5"}
      ],
      "footer_left": "content strategy + creation",
      "footer_right": "\u25b6 broadcasting",
      "label_line_1": "feeds all hubs",
      "label_line_2": "content engine",
      "detail": {
        "title": "Translation Marketing",
        "subtitle": "Content Engine \u00b7 Feeds All Hubs",
        "sections": [
          {
            "heading": "\U0001f3af Lead",
            "items": [
              {"label": "CMO", "value": "Jay Cinco"},
              {"label": "Hubs Fed", "value": "7 active"},
              {"label": "Mode", "value": "Broadcasting"}
            ]
          }
        ]
      }
    },
    {
      "id": "shark-tank",
      "name": "Shark Tank",
      "tag": "Ideas \u00b7 Incubator",
      "accent": "#FF3CAC",
      "stats": [
        {"label": "ideas", "value": "\u221e"},
        {"label": "workflows", "value": "\u2014"},
        {"label": "staged", "value": "?"}
      ],
      "footer_left": "workshop \u00b7 what's next",
      "footer_right": "open",
      "label_line_1": "ideas",
      "label_line_2": "incubator",
      "detail": {
        "title": "Shark Tank",
        "subtitle": "Ideas \u00b7 Incubator \u00b7 What's Next",
        "sections": [
          {
            "heading": "\U0001f4a1 Concept Pool",
            "items": [
              {"label": "Status", "value": "Open \u2014 pitch anything"},
              {"label": "Staged Ideas", "value": "TBD"},
              {"label": "Evaluator", "value": "Adolfo + Goldie"}
            ]
          }
        ]
      }
    },
    {
      "id": "cia",
      "name": "CIA",
      "tag": "Agent Infra HQ",
      "accent": "#2EE6CA",
      "stats": [
        {"label": "agents", "value": "12"},
        {"label": "flows", "value": "23"},
        {"label": "memory", "value": "\u221e"}
      ],
      "footer_left": "where the AI lives",
      "footer_right": "\u25b6 live",
      "label_line_1": "12 agents",
      "label_line_2": "infra HQ",
      "detail": {
        "title": "CIA \u2014 Agent Infra HQ",
        "subtitle": "Where The AI Lives",
        "sections": [
          {
            "heading": "\U0001f916 Agents",
            "items": [
              {"label": "Total Agents", "value": "12"},
              {"label": "Active Now", "value": "4 (Adolfo, Raj, Bentley, Vito)"},
              {"label": "Coordinator", "value": "Adolfo"},
              {"label": "Memory Layer", "value": "Chroma DB (live)"}
            ]
          },
          {
            "heading": "\u2699\ufe0f Infrastructure",
            "items": [
              {"label": "Gateway", "value": "\u2705 Running (port 18789)"},
              {"label": "Gmail", "value": "\u2705 Connected"},
              {"label": "Google Calendar", "value": "\u2705 Connected"},
              {"label": "Render Deploy", "value": "\u2705 Mission Control v2 live"}
            ]
          }
        ]
      }
    }
  ],
  "cadence": {
    "name": "King Neptune",
    "context": "Inside Casa De Goldie \u00b7 Apr 20 \u2192 Apr 24",
    "days": [
      {
        "day": "Mon",
        "status": "done",
        "tick": "DONE",
        "agent_emoji": "\U0001f577\ufe0f",
        "agent_name": "Wilmar",
        "what": "Scanned scholarship sources \u2014 47 records added"
      },
      {
        "day": "Tue",
        "status": "done",
        "tick": "DONE",
        "agent_emoji": "\U0001f52c",
        "agent_name": "Newton",
        "what": "Classified 47 records \u00b7 12 STEM priority flagged"
      },
      {
        "day": "Wed",
        "status": "done",
        "tick": "DONE",
        "agent_emoji": "\U0001f574\ufe0f",
        "agent_name": "Vito",
        "what": "Re-scored & ranked \u00b7 top 12 ready for Jay"
      },
      {
        "day": "Thu \u00b7 TODAY",
        "status": "now",
        "tick": "\u25b6 LIVE",
        "agent_emoji": "\U0001f3af",
        "agent_name": "Jay Cinco",
        "what": "Drafting essays for top picks"
      },
      {
        "day": "Fri",
        "status": "queued",
        "tick": "QUEUED",
        "agent_emoji": "\U0001f4bc",
        "agent_name": "Bentley",
        "what": "Send Goldie the deadline queue"
      }
    ]
  },
  "agents": [
    {
      "id": "adolfo",
      "name": "Adolfo",
      "emoji": "\U0001f9e0",
      "role": "Master Coordinator",
      "status": "live",
      "status_label": "HUB",
      "task": "3 Render deployments shipped today. Mission Control v2 live. Coordinating Jay\u2019s KN essay run.",
      "model": "Sonnet",
      "latency": "~140ms",
      "operates_from": "cia"
    },
    {
      "id": "raj",
      "name": "Raj Patel",
      "emoji": "\U0001f4bb",
      "role": "Tech & Dev",
      "status": "live",
      "status_label": "BUILDING",
      "task": "Mission Control v2 deployed to Render as static site \u2014 no server needed. Self-contained HTML build.",
      "model": "Sonnet",
      "latency": "~1.8s",
      "operates_from": "cia"
    },
    {
      "id": "jay-cinco",
      "name": "Jay Cinco",
      "emoji": "\U0001f3af",
      "role": "CMO \u00b7 Marketing",
      "status": "live",
      "status_label": "WORKING",
      "task": "KN essay drafts underway \u00b7 3 of 12 priority picks done. CCG carousel queued.",
      "model": "Haiku \u2192 Sonnet",
      "latency": "~900ms",
      "operates_from": "translation-mkt"
    },
    {
      "id": "bentley",
      "name": "Bentley",
      "emoji": "\U0001f4bc",
      "role": "Personal Assistant",
      "status": "live",
      "status_label": "WORKING",
      "task": "Friday queue staged. Deadline reminders set for KN submission window.",
      "model": "Haiku \u00b7 GCal",
      "latency": "~640ms",
      "operates_from": "casa-de-goldie"
    },
    {
      "id": "newton",
      "name": "Newton",
      "emoji": "\U0001f52c",
      "role": "R&D \u00b7 Research",
      "status": "idle",
      "status_label": "STANDBY",
      "task": "KN classification complete \u2014 47/47 done. Handed off to Vito Wed. Available for next task.",
      "model": "Haiku \u2192 Sonnet",
      "latency": "\u2014",
      "operates_from": "casa-de-goldie"
    },
    {
      "id": "warren",
      "name": "Warren Buffet",
      "emoji": "\U0001f4b0",
      "role": "Finances",
      "status": "idle",
      "status_label": "STANDBY",
      "task": "Godspeed burn $12,840 \u2014 under budget by $1,160. Casa De Goldie books synced.",
      "model": "Haiku",
      "latency": "\u2014",
      "operates_from": "casa-de-goldie"
    },
    {
      "id": "brian-steele",
      "name": "Brian Steele",
      "emoji": "\u2696\ufe0f",
      "role": "Legal & Compliance",
      "status": "idle",
      "status_label": "ON-DEMAND",
      "task": "Last engagement: Hanifa lease (closed). Goldie Endeavor contracts queued for review.",
      "model": "Sonnet",
      "latency": "\u2014",
      "operates_from": "goldie-endeavor"
    },
    {
      "id": "jordan",
      "name": "Jordan Belfort",
      "emoji": "\U0001f43a",
      "role": "Sales",
      "status": "live",
      "status_label": "OUTREACH",
      "task": "Sent follow-ups to 8 Hellstar FL prospects. 12 opens, 2 replies. Awaiting go-signal.",
      "model": "Haiku",
      "latency": "~480ms",
      "operates_from": "godspeed"
    },
    {
      "id": "vito",
      "name": "Vito",
      "emoji": "\U0001f574\ufe0f",
      "role": "Data Intelligence",
      "status": "idle",
      "status_label": "STANDBY",
      "task": "KN scoring complete \u2014 top 12 ranked & delivered to Jay. Godspeed conversion +4.2% wow.",
      "model": "Haiku \u2192 Sonnet",
      "latency": "\u2014",
      "operates_from": "casa-de-goldie"
    },
    {
      "id": "el-pibe",
      "name": "El Pibe",
      "emoji": "\U0001f4da",
      "role": "Memory & Archivist",
      "status": "live",
      "status_label": "LOGGING",
      "task": "3 deploy sessions logged. Memory updated with Render infrastructure config.",
      "model": "Haiku",
      "latency": "~210ms",
      "operates_from": "cia"
    },
    {
      "id": "wilmar",
      "name": "Wilmar Barrios",
      "emoji": "\U0001f577\ufe0f",
      "role": "Data Collection",
      "status": "idle",
      "status_label": "STANDBY",
      "task": "KN sweep complete. Next run Mon 04\u00b727 04:00 ET. Scanning buzzing artists for Barrio Music.",
      "model": "GPT-4o Mini",
      "latency": "\u2014",
      "operates_from": "casa-de-goldie"
    },
    {
      "id": "quintero",
      "name": "Quintero",
      "emoji": "\U0001f3a8",
      "role": "Media Builder",
      "status": "escal",
      "status_label": "NEEDS REVIEW",
      "task": "\"Risky\" promo v3 ready (Barrio Music). CCG carousel shipped to Jay via Translation Mkt.",
      "model": "GPT-4.1",
      "latency": "~3.4s",
      "operates_from": "translation-mkt"
    }
  ]
}

# ---------- 2. Updated activity feed ----------
activity = [
  {"ts":"2026-04-24T16:00:00Z","agent_id":"raj","agent_name":"Raj","emoji":"\U0001f4bb","hub_id":"cia","hub_name":"CIA","msg":"Mission Control v2 deployed to Render \u2014 static build, no server needed. \u2705","when":"just now"},
  {"ts":"2026-04-24T15:15:00Z","agent_id":"adolfo","agent_name":"Adolfo","emoji":"\U0001f9e0","hub_id":"cia","hub_name":"CIA","msg":"3rd Render deployment confirmed. El Barrio dashboard live at render URL.","when":"45 min ago"},
  {"ts":"2026-04-24T14:30:00Z","agent_id":"jay-cinco","agent_name":"Jay Cinco","emoji":"\U0001f3af","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"KN essay drafts: 3 of 12 done. First-gen STEM batch leading.","when":"1.5 hr ago"},
  {"ts":"2026-04-24T13:00:00Z","agent_id":"vito","agent_name":"Vito","emoji":"\U0001f574\ufe0f","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"KN scoring complete \u2014 top 12 ranked, handed to Jay Cinco.","when":"3 hr ago"},
  {"ts":"2026-04-24T11:00:00Z","agent_id":"bentley","agent_name":"Bentley","emoji":"\U0001f4bc","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"Friday deadline queue staged. 3 reminders set for Goldie.","when":"5 hr ago"},
  {"ts":"2026-04-23T18:00:00Z","agent_id":"jordan","agent_name":"Jordan","emoji":"\U0001f43a","hub_id":"godspeed","hub_name":"Godspeed","msg":"Sent follow-ups to 8 Hellstar FL prospects. 12 opens, 2 replies.","when":"22 hr ago"},
  {"ts":"2026-04-23T14:00:00Z","agent_id":"quintero","agent_name":"Quintero","emoji":"\U0001f3a8","hub_id":"translation-mkt","hub_name":"Translation Mkt","msg":"6 CCG IG assets delivered to Jay Cinco for review.","when":"1 day ago"},
  {"ts":"2026-04-23T10:00:00Z","agent_id":"warren","agent_name":"Warren","emoji":"\U0001f4b0","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"Godspeed monthly burn $12,840 \u2014 under budget.","when":"1 day ago"},
  {"ts":"2026-04-22T14:00:00Z","agent_id":"newton","agent_name":"Newton","emoji":"\U0001f52c","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"KN classification 100% \u2014 47/47 done. 12 STEM priority flagged.","when":"2 days ago"},
  {"ts":"2026-04-21T00:08:00Z","agent_id":"wilmar","agent_name":"Wilmar","emoji":"\U0001f577\ufe0f","hub_id":"casa-de-goldie","hub_name":"Casa De Goldie","msg":"Monday sweep complete \u2014 47 records added.","when":"3 days ago"}
]

# ---------- 3. Read original HTML ----------
html_path = SRC / "mission-control.html"
html = html_path.read_text(encoding="utf-8")

# ---------- 4. Patch nav "state.json ·" text ----------
html = html.replace(
    '<div class="sync"><span class="dot"></span>state.json · <span id="last-sync">never</span></div>',
    '<div class="sync"><span class="dot"></span>embedded · <span id="last-sync">never</span></div>'
)

# ---------- 5. Replace fetch-based loadAll with embedded data ----------
# We'll inject the STATE and ACTIVITY_RAW constants and rewrite loadAll

state_json = json.dumps(state, ensure_ascii=False, indent=2)
activity_json = json.dumps(activity, ensure_ascii=False, indent=2)

old_script_header = """  const POLL_MS = 15000;
  const STATE_URL = 'state.json';
  const ACTIVITY_URL = 'activity.ndjson';"""

new_script_header = f"""  // ============================================================
  //   EMBEDDED DATA — built Thu Apr 24 2026
  //   No server required. Open directly as a static file.
  // ============================================================
  const STATE = {state_json};

  const ACTIVITY_RAW = {activity_json};"""

html = html.replace(old_script_header, new_script_header)

# Replace async loadAll with sync version
old_load_all = """  async function loadAll(){
    try {
      const [stateRes, actRes] = await Promise.all([
        fetch(STATE_URL + '?_=' + Date.now(), { cache: 'no-store' }),
        fetch(ACTIVITY_URL + '?_=' + Date.now(), { cache: 'no-store' })
      ]);
      if(!stateRes.ok) throw new Error('state.json HTTP ' + stateRes.status);
      const state = await stateRes.json();
      let activity = [];
      if(actRes.ok){
        const txt = await actRes.text();
        activity = txt.trim().split('\\n').filter(Boolean).map(l => {
          try { return JSON.parse(l); } catch { return null; }
        }).filter(Boolean);
      }
      renderToday(state.today);
      renderHubsStyleA(state.hubs || []);
      renderHubsStyleB(state.hubs || []);
      renderHubsStyleC(state.hubs || []);
      wireHubClicks(state.hubs || []);
      renderCadence(state.cadence);
      renderAgents(state.agents || []);
      renderActivity(activity);
      document.getElementById('hub-count').textContent = (state.hubs || []).length;
      updateLastSync();
      clearError();
    } catch(err){
      console.error(err);
      showError('Could not load state: ' + err.message + '. (Are you serving via http? file:// blocks fetch.)');
    }
  }

  loadAll();
  setInterval(loadAll, POLL_MS);"""

new_load_all = """  function loadAll(){
    try {
      renderToday(STATE.today);
      renderHubsStyleA(STATE.hubs || []);
      renderHubsStyleB(STATE.hubs || []);
      renderHubsStyleC(STATE.hubs || []);
      wireHubClicks(STATE.hubs || []);
      renderCadence(STATE.cadence);
      renderAgents(STATE.agents || []);
      renderActivity(ACTIVITY_RAW);
      document.getElementById('hub-count').textContent = (STATE.hubs || []).length;
      updateLastSync();
      clearError();
    } catch(err){
      console.error(err);
      showError('Could not render dashboard: ' + err.message);
    }
  }

  loadAll();
  // Static build — no polling needed"""

html = html.replace(old_load_all, new_load_all)

# ---------- 6. Write output ----------
out_path = DEST_DIR / "index.html"
out_path.write_text(html, encoding="utf-8")
print(f"✅ Written: {out_path}")
print(f"   Size: {out_path.stat().st_size:,} bytes")

# Verify no fetch calls remain for state/activity
if "fetch(STATE_URL" in html or "fetch(ACTIVITY_URL" in html:
    print("❌ ERROR: fetch calls for data files still present!")
else:
    print("✅ QA: No external data fetches found")

if "const STATE = " in html:
    print("✅ QA: STATE embedded")
if "const ACTIVITY_RAW = " in html:
    print("✅ QA: ACTIVITY_RAW embedded")
if 'THU 04\u00b724' in html:
    print("✅ QA: Today label correct (THU 04·24)")
if "El Barrio dashboards going live" in html:
    print("✅ QA: Today summary correct")
if "Adolfo" in html and "today" in html:
    print("✅ QA: Owner updated to Adolfo")
