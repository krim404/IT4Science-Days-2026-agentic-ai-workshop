#!/usr/bin/env bash
# Deck-Werkzeug. Rendert und prueft die Fusszeilen-Ueberlappung.
# Stdin wird ueberall geschlossen, damit kein Aufruf auf Eingaben warten kann.
#   ./build.sh          rendern + pruefen
#   ./build.sh --list   zusaetzlich das Folienverzeichnis ausgeben
#   ./build.sh --dev    Livesuche: bei jedem Speichern der .md neu rendern + pruefen
set -euo pipefail
cd "$(dirname "$0")"
DECK=docs/presentations/it4science-days-2026-agentic-ai-workshop

command -v marp >/dev/null 2>&1 && MARP=(marp) || MARP=(npx --yes @marp-team/marp-cli)

render() { "${MARP[@]}" "$DECK.md" -o "$DECK.html" </dev/null >/dev/null 2>&1
           echo "gerendert: $DECK.html"; }
# in dev (Argument "dev") ist ein FAIL nicht toedlich, der Watcher laeuft weiter
check()  { python3 tests/check_footer.py "$DECK.html" </dev/null || [ "${1:-}" = dev ]; }

if [ "${1:-}" = "--dev" ]; then
  echo "dev: beobachte $DECK.md (Strg-C beendet)"
  render; check dev
  last=$(md5sum "$DECK.md" | cut -d' ' -f1)
  while true; do
    cur=$(md5sum "$DECK.md" | cut -d' ' -f1)
    if [ "$cur" != "$last" ]; then
      last="$cur"
      echo "--- Änderung $(date +%H:%M:%S) ---"
      render; check dev
    fi
    sleep 1
  done
fi

render
[ "${1:-}" = "--list" ] && python3 tools/list_slides.py "$DECK.html" </dev/null
check
