# Beiträge zu diesem Repo — Schritt für Schritt

Zielgruppe: Tobias & Christian (und alle, die Folien oder Doku bearbeiten).
Kurzform: **Branch → Folien editieren → `./build.sh` muss PASS sagen → Commit → Merge nach `main` → beide Remotes pushen.**

## 0. Voraussetzungen (einmalig)

```bash
npm install -g @marp-team/marp-cli   # oder: build.sh nutzt npx als Fallback
python3                              # für tests/check_footer.py
chromium                             # headless, für den Fußzeilen-Check
```

## 1. Starten & Branch anlegen

```bash
git checkout main && git pull          # immer frisch starten — zwei Leute editieren parallel
git checkout -b feature/<thema>       # z. B. feature/jlu-feedback
```

Regel: ein Thema = ein Branch = kleine Commits. Große Umbauten bitte vorher per VC absprechen (Konfliktgefahr, wir editieren dieselben Dateien).

## 2. Bearbeiten

Hauptdatei: `pre-presentation-builder/presentations/it4science-days-2026-agentic-ai-workshop.md` (Marp-Deck, ~43 Folien).

**Deck-Konventionen:**

- **Anrede:** Folien in der Sie-Form; Sprechernoten (`<!-- notes: … -->`) locker.
- **Notizen-Format:** erste Zeile `SPEAKER — Block · Zeit (min), Lead`. Details, Quellen und Moderator-Anleitungen gehören in die Notizen, nicht auf die Folie.
- **Speaker-Badge:** `<div class="speaker speaker-tobias">👤 Tobias Weiß</div>` bzw. `speaker-christian`.
- **Marp-Fallen:**
  - Bei mehreren `_class`-Direktiven gewinnt die **letzte** — kombinieren per Leerzeichen (`<!-- _class: lead smaller -->`).
  - Beim Einfügen einer Folie vor einer bestehenden: deren `<!-- _class: … -->`-Direktive steht *über* dem Badge/Content — nicht versehentlich der neuen Folie zuordnen (die alte rendert dann groß und überlappt).
  - Marp passt übergroße Code-Blöcke asynchron an — Messwerte direkt nach dem Rendern können raced sein (die Suite fängt das mit Mehrfachläufen ab).
- **Fakten-Standard:** jede Zahl/jeder Werkzeug-Claim braucht eine nennbare Quelle. Eigene Messungen: `Quelle: eigene Erfassung` als graue Zeile (Vorlage: Suche nach „Quelle:" im Deck). Werkzeug-Claims gegen die **tatsächlichen Projekt-READMEs** verifizieren, nicht gegen ältere Audit-Notizen.
- **Überlappungen:** zuerst Text kürzen oder in die Notizen verschieben, nicht das Layout verbiegen.

## 3. Bauen & prüfen (Pflicht vor jedem Commit)

```bash
./build.sh            # rendert HTML + Fußzeilen-Check → muss „PASS ✅" liefern
./build.sh --list     # Folienverzeichnis mit Nummern (zum Verweisen in Besprechungen)
```

**Achtung Pipes:** `./build.sh | tail -1` verschluckt den Exit-Code — ein FAIL kann so ungeprüft in einen Commit rutschen. Immer die PASS-Zeile sehen oder `set -o pipefail` nutzen.

**Grenze des Checks:** headless-Chromium nutzt eingefrorene Font-Metriken. Echte Browser (Noto/Segoe) können höher rendern — der Check kann PASS sagen, während im Vortrags-Browser trotzdem etwas überlappt. Deshalb: nach Layout-Nähe am Schluss einmal **im eigenen Browser** durchblättern. Korrekturmittel: Schrift/Padding der betroffenen Klasse im Frontmatter-CSS (Tabellen, Blockquotes) verkleinern.

## 4. Committen

```bash
git add -A
git commit -m "Imperativ: was + warum (Quelle/Fix-Grund in Klammern)"
```

## 5. Merge & Push (beide Remotes!)

```bash
git checkout main
git merge --ff-only feature/<thema>   # fast-forward hält die Historie linear
git push origin main                  # GitHub (Primary)
git push codeberg HEAD:master         # Codeberg (Mirror, Master-Branch heißt anders!)
```

Danach aufräumen: `git branch -d feature/<thema>` und Remote-Branch löschen, wenn gepusht (`git push origin --delete feature/<thema>`).

Für größere Reviews: Branch pushen, PR öffnen, zweiter Speaker reviewed, dann wie oben mergen.

## 6. Dateien-Landkarte

| Datei | Inhalt |
|---|---|
| `pre-presentation-builder/presentations/it4science-days-2026-agentic-ai-workshop.md` | Das Deck (einzige Folienquelle; HTML ist Build-Artefakt) |
| `pre-presentation-builder/runbook-it4science-2026.md` | Durchführungs-Drehbuch: Arc, Maßnahmen M1–M12, Fallbacks, Indico-Abstract |
| `pre-presentation-builder/research-foundation-models-toolbox.md` | Recherchestand Modell-/Toolbox-Fakten |
| `README.md` | Überblick, Lernziele, Voraussetzungen, Agenda, Links |
| `tests/check_footer.py` + `build.sh` | Build-Gate (siehe Schritt 3) |
| `tools/list_slides.py` | Folienverzeichnis für `--list` |

**Änderungen immer im Markdown/Repo vornehmen** — nie das generierte HTML direkt editieren (wird bei jedem Build überschrieben) und nie gleichzeitig in zwei Branches dieselbe Folie umbauen.
