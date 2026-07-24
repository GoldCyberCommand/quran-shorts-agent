#!/bin/bash
# Install the daily launchd job (macOS). Run from anywhere:
#   bash automation/install-schedule.sh
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$PROJECT_DIR/automation/com.quran-shorts-agent.plist.template"
PLIST="$HOME/Library/LaunchAgents/com.quran-shorts-agent.plist"

mkdir -p "$PROJECT_DIR/logs" "$HOME/Library/LaunchAgents"
sed "s|__PROJECT_DIR__|$PROJECT_DIR|g" "$TEMPLATE" > "$PLIST"

launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"
echo "Installed: $PLIST (daily at 17:00; logs in $PROJECT_DIR/logs/run.log)"
echo "Uninstall with: launchctl unload \"$PLIST\" && rm \"$PLIST\""
