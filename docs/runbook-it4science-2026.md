# Runbook — Agentic AI in der Praxis (IT4Science Days 2026)

**Termin: Mi 30.09.2026, 09:00–12:00 · Manfred-Eigen-Saal, MPI-NAT · Streaming + interne Aufzeichnung zugesagt** ([Indico](https://plan.events.mpg.de/event/670/contributions/4047/)).

Ops-Dokument für die Referenten (nicht Teil der Folien). Struktur nach
`workshops-best-practices/examples/workshop-runbook-template.md`, Maßnahmen
abgeleitet aus dem Corpus `docs/01–09` (active learning, engagement,
assessment, CS specials).

## 1. Plan

- **Titel:** Agentic AI in der Praxis
- **Primäres Lernziel** (ein Satz, messbar): *Jede Teilnehmende verlässt den
  Raum mit einem eigenen, CI-validierten Research-Repo und hat mindestens
  einen Spec-Change gesehen, der agentisch umgesetzt wurde.*
- **Zielgruppe:** Postdocs / Forschende der MPG (keine Devs, aber Python-tauglich)
- **Dauer:** 180 min (09:00–12:00) · **Modus:** Präsenz · **Größe:** k.A. (bei >15: Roaming wichtiger)
- **Voraussetzungen:** GitHub-Account, git, Python ≥3.11, Browser (siehe README)
- **Erfolgsmessung:**
  1. ≥ 60 % der TN mit validiertem Repo am Ende (grüner CI-Check)
  2. ≥ 3 TN-Präsentationen im Outcomes-Block
  3. Exit-Ticket: ≥ 70 % nennen einen konkreten nächsten Schritt
  4. Whiteboard-Wünsche aus der Blitzlicht-Runde: wie viele im Outcomes adressiert?

## 2. Arc (Agenda → Phasen)

| Phase | Blöcke | Zeit | Anteil | Lead / Roam |
|---|---|---|---|---|
| Hook/framing | Ankommen, Beispiele, Blitzlicht | 09:00–09:15 | 8 % | C / T |
| Concept | Grundlagen, FM, Toolbox | 09:15–10:10 | 31 % ⚠️ | C / T, dann T / C |
| Guided practice | Anwendung 1 (skeleton-research) | 10:20–10:45 | 14 % | T / C |
| Concept kompakt | Spezifikation & Token | 10:45–11:00 | 8 % | C+T / — |
| Independent practice | Anwendung 2 (eigene Spec) | 11:00–11:25 | 14 % | C / T |
| Debrief | Outcomes, Q&A, Wrap | 11:30–12:00 | 17 % | T / C |

⚠️ Concept-Anteil liegt über der Empfehlung (15–20 %). Kompensation: die
Concept-Blöcke interaktiv halten (Maßnahmen M1, M3) statt kürzen — Agenda bleibt stabil.

## 3. Materials & Environment

- [ ] **Preflight-Versand** an TN (spätestens 23.09.): GitHub-Account anlegen, `git --version`, `python3 --version`
- [ ] **Rescue-Umgebung**: fertiger Fork eines Referenten-Repos als Fallback, wenn eigene Maschine/Setup versagt (TN arbeitet dann auf Referenten-Fork weiter)
- [ ] **Demo-Abhängigkeiten vorgetestet**: skeleton-research-Klon + Pipeline end-to-end am Vortag; opencode/SAIA kurz anpingen
- [ ] **Fallback je Live-Demo**: Screenshots der Pipeline-Läufe im Repo (`docs/demo-fallback/`), falls Netz/Tool versagt
- [ ] Whiteboard/Stellwand für Blitzlicht-Wünsche + Marker
- [ ] Exit-Ticket-Zettel oder QR-Code auf Wrap-Folie

## 4. Engagement & Assessment (Maßnahmen im Ablauf)

Maßnahmen sind bewusst NICHT auf die Folien geschrieben — sie leben hier und
in den Köpfen der Referenten.

| # | Wann | Was | Quelle |
|---|---|---|---|
| M1 | 09:50 (nach Toolbox-Ranking) | **Thumb-Vote**: „Wer würde sofort eines dieser Tools installieren?" — Momentaufnahme, sichtbare Hände | 04, 05 |
| M2 | 10:08 (vor Pause 1) | **Stop-Light**: rot/gelb/grün — „Wo stehen Sie nach Anwendung 1?" Wer rot: in der Pause 1:1 | 02, 05 |
| M3 | 10:20–10:45 (Anw1-Demo) | **Geplanter Fehlschlag**: live eine generierte Datei editieren → Pipeline rot → Ursache zeigen → restore. Der Moment mit der höchsten Behaltensleistung | 09 |
| M4 | 10:43 (Ende Anw1) | **1-Minuten-Rekap**: jede TN schreibt einen Satz: „papers.yaml ist …" | 05 |
| M5 | 11:28 (Start Outcomes) | **Think-Pair-Share**: erst 2 min mit Nachbar:in über Ergebnis sprechen, dann Freiwillige — senkt die Barriere | 02, 03 |
| M6 | 11:30–11:45 (Outcomes) | **Whiteboard-Revisit**: Blitzlicht-Wünsche durchgehen — welche wurden heute adressiert? (= Post-Assessment gegen die Prä-Erhebung) | 04, 05 |
| M7 | 11:55 (Wrap) | **Exit-Ticket**: „Was nehmen Sie mit? Was ist noch unklar?" (Zettel oder QR) | 05 |
| M8 | 09:00–12:00 | **Roamer-Rolle** nach Tabelle Arc: der Nicht-Leadende geht durch die Reihen, löst leise fest | 02 |
| M9 | durchgehend | **Fehler normalisieren**: „Bei uns bricht das auch regelmäßig" — Versuchsanordnungs-Ton (Christians Hook macht das vor) | 02, 07 |

## 5. Nach dem Workshop

- [ ] Exit-Tickets auswerten, 2 Verbesserungen notieren (dieses Runbook aktualisieren)
- [ ] Folien + Materialien an TN mailen (Repo-Link genügt: CC-BY-Lizenzfolie); Aufzeichnungs-Link ergänzen, sobald internal publiziert
- [ ] Follow-up nach 2 Wochen (≈ 14.10.): 1 Frage — „Wenden Sie etwas an?" (Verhaltens-Messgröße, die eigentlich zählt)
- [ ] Feedback-Umfrage (3 Fragen: Relevanz, Tempo, Weiterempfehlung) als Link per Mail

## 6. Indico-Eintrag aktualisieren (offen)

Der offizielle Abstract beschreibt noch das alte Format (Vortrag + OpenDesk-Edu-Use-Case,
der 08/2026 aus der Agenda entfernt wurde). Vorschlag für die Aktualisierung in Indico:

> Christian Uhl (Universität Gießen) und Tobias Weiß (Universität Marburg) zeigen in
> einem dreistündigen, interaktiven Workshop, wie Large Language Models heute agentisch
> genutzt werden: aktuelle Foundation Models im Überblick, Open-Source-Harnesses
> (OpenCode, pi, zot) und Spec-Driven Development. Im Zentrum stehen zwei Hands-ons:
> Jede Teilnehmende verlässt den Raum mit einem eigenen, CI-validierten Research-Repo
> (skeleton-research) und erlebt einen Spec-Change, der agentisch umgesetzt wird.
> Abgeschlossen wird mit einem Outcomes-Block, in dem Teilnehmende ihre Ergebnisse
> präsentieren. Voraussetzungen: GitHub-Account, git, Python — kein Dev-Hintergrund nötig.
> Vortragssprache: Deutsch.
