#!/usr/bin/env bash
# Deck-Werkzeug. Rendert und prueft die Fusszeilen-Ueberlappung.
# Stdin wird ueberall geschlossen, damit kein Aufruf auf Eingaben warten kann.
#   ./build.sh          rendern + pruefen
#   ./build.sh --list   zusaetzlich das Folienverzeichnis ausgeben
set -euo pipefail
cd "$(dirname "$0")"
DECK=docs/presentations/it4science-days-2026-agentic-ai-workshop

command -v marp >/dev/null 2>&1 || {
  echo "marp fehlt. Einmalig: npm install -g @marp-team/marp-cli" >&2; exit 2; }

marp "$DECK.md" -o "$DECK.html" </dev/null >/dev/null 2>&1
echo "gerendert: $DECK.html"

[ "${1:-}" = "--list" ] && python3 tools/list_slides.py "$DECK.html" </dev/null

python3 tests/check_footer.py "$DECK.html" </dev/null
