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
- **Zielgruppe:** Wissenschaftliches Personal und Forschende (keine Devs, aber Python-tauglich)
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
| Guided practice | Anwendung 1: Thema X direkt agentisch im eigenen Harness — ohne Spec (Übung 1) | 10:20–10:45 | 14 % | T / C |
| Concept kompakt | Spezifikation & Token | 10:45–11:00 | 8 % | C+T / — |
| Independent practice | Anwendung 2: Thema X via Spec aufs Demo-Repo (skeleton-research + OpenSpec-Change, gemergte Übung 2) | 11:00–11:25 | 14 % | C / T |
| Debrief | Outcomes, Q&A, Wrap | 11:30–12:00 | 17 % | T / C |

### Zeitplan (Minutie) — Referenz nur für uns

Die Agenda (Deck + README) trägt keine Block-Zeiten mehr, nur die Pausen haben
feste Uhrzeiten. Diese Minutie ist die interne Referenz. Folien-Nummern = Marp.

| Zeit | Block | Folien | Wer | Zeit-Kern |
|---|---|---|---|---|
| 09:00–09:15 | Ankommen · Wer wir sind · Blitzlicht (Thema X + KI-Selbsteinschätzung) · Erwartungen · Agenda | 01–05 | C (+T) | Blitzlicht ~3, hart timen |
| 09:15–09:30 | Grundlagen: Begriffe · Bausteine · Prompt/Vertrag · Metapher/Pyramide | 06–11 | C | |
| 09:30–09:50 | Foundation Models: Entwicklungen · Katalog · Praxis-Einordnung | 12–14 | C+T | Live-Checks 5 |
| 09:50–10:10 | Toolbox: Harness-Reichweite · Chat→Terminal · Zwei Harnesses (Live-Demo) · pi · M1 Thumb-Vote | 15–19 | T (+C: kommerziell 2) | Vergleich 12 · Mapping 3 · pi 2 |
| 10:10–10:20 | ☕ Pause (M2 Stop-Light um 10:08) | 20 | — | |
| 10:20–10:45 | Anwendung 1: Modes · Übung 1 (direkt agentisch, ohne Spec) · AGENTS.md | 21–24 | T (C roamt) | Modes 2 · Übung 1 15 · AGENTS 3 · Puffer 5 |
| 10:45–11:00 | Theorie: Spec (Drei Ebenen · Schulen · Showcase) + Token | 25–29 | C+T | Showcase kürzbar bei Zeitnot |
| 11:00–11:25 | Anwendung 2: skeleton · Pipeline · Jump-Start (M3 Fehlschlag) · OpenSpec-Change · Messen | 30–35 | C (T roamt) | skeleton 3 · Pipeline 2 · Jump-Start 8 · Change 8 · Messen 2 |
| 11:25–11:30 | ☕ Pause | 36 | — | |
| 11:30–11:45 | Outcomes: TN zeigen (M5 Think-Pair-Share, M6 Whiteboard-Revisit) | 37–38 | T | |
| 11:45–12:00 | Q&A · Muster übertragen · Resources · Danke | 39–42 | T+C | |

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
| M1 | 09:50–10:10 (nach pi-Folie) | **Thumb-Vote**: „Wer würde sofort eines dieser Tools installieren?“ — Momentaufnahme, sichtbare Hände | 04, 05 |
| M2 | 10:08 (vor Pause 1) | **Stop-Light**: rot/gelb/grün — „Wo stehen Sie nach dem Toolbox-Block?“ Wer rot: in der Pause 1:1 | 02, 05 |
| M3 | 11:00–11:25 (Anw2, Jump-Start) | **Geplanter Fehlschlag**: live eine generierte Datei editieren → Pipeline rot → Ursache zeigen → restore. Der Moment mit der höchsten Behaltensleistung | 32, 33 |
| M4 | 10:43 (Ende Anw1) | **1-Minuten-Rekap**: jede TN schreibt einen Satz: „Ohne Spec war der Agenten-Lauf …“ — roh, unaufgeräumt, Quellen unklar | 23 |
| M5 | 11:28 (Start Outcomes) | **Think-Pair-Share**: erst 2 min mit Nachbar:in über Ergebnis sprechen, dann Freiwillige — senkt die Barriere | 02, 03 |
| M6 | 11:30–11:45 (Outcomes) | **Whiteboard-Revisit**: Blitzlicht-Wünsche durchgehen — welche wurden heute adressiert? (= Post-Assessment gegen die Prä-Erhebung) | 04, 05 |
| M7 | 11:55 (Wrap) | **Exit-Ticket**: „Was nehmen Sie mit? Was ist noch unklar?" (Zettel oder QR) | 05 |
| M8 | 09:00–12:00 | **Roamer-Rolle** nach Tabelle Arc: der Nicht-Leadende geht durch die Reihen, löst leise fest | 02 |
| M9 | durchgehend | **Fehler normalisieren**: „Bei uns bricht das auch regelmäßig" — Versuchsanordnungs-Ton (Christians Hook macht das vor) | 02, 07 |

### JLU-Erfahrung (Christian, 09/2026, analoger Kurz-Kurs)

Clientel erwartete „fertige Bots" (à la Claude Cowork); Plan-Mode kannte niemand;
„was ist agentisch an OpenCode mit geladenem Skill" kam nicht an. Daraus (Deck:
Erwartungs-Folie, Spektrum-Folie, Modes-Folie):

| # | Wann | Was | Quelle |
|---|---|---|---|
| M10 | Anw1 + Anw2 | **Worked Example + Roamer**: einer führt das Beispiel vorne Schritt für Schritt, der andere geht zu den Schnelleren/High-Skillern in den Dialog — Rollentrennung fest einplanen | 02, 09 |
| M11 | bei „Ich will nur einen Bot" | **Antwortmuster, nicht abwerten**: „Danach ist ein Bot schnell gebaut — wenn klar ist, was unter ihm läuft. Genau das ist heute." Erwartung ernst nehmen | 04 |
| M12 | falls Publikum weniger technisch | **Kontingenz**: Plan-Mode-Demo statt Selbst-Ausführung, TN paaren, gewonnene Hands-on-Zeit in Dialog verwandeln | 07, 09 |

## 5. Nach dem Workshop

- [ ] Exit-Tickets auswerten, 2 Verbesserungen notieren (dieses Runbook aktualisieren)
- [ ] Folien + Materialien an TN mailen (Repo-Link genügt: CC-BY-Lizenzfolie); Aufzeichnungs-Link ergänzen, sobald internal publiziert
- [ ] Follow-up nach 2 Wochen (≈ 14.10.): 1 Frage — „Wenden Sie etwas an?" (Verhaltens-Messgröße, die eigentlich zählt)
- [ ] Feedback-Umfrage (3 Fragen: Relevanz, Tempo, Weiterempfehlung) als Link per Mail

## 6. Indico-Eintrag aktualisieren (offen)

Der offizielle Abstract beschreibt noch das alte Format (Vortrag + OpenDesk-Edu-Use-Case,
der 08/2026 aus der Agenda entfernt wurde). Vorschlag für die Aktualisierung in Indico:

> **Agentic AI in der Praxis — Vom Spec zum produktiven Workflow**
>
> Wie werden Large Language Models zuverlässige Arbeitspartner statt bloße Chat-Gegenüber?
> Christian Uhl (Zentrum für angewandte Informatik und Data Science, Universität Gießen)
> und Tobias Weiß (DevOps Engineer, Universität Marburg) beantworten diese Frage in
> einem dreistündigen, interaktiven Workshop für Forschende.
>
> Roter Faden ist eine Pyramide: **Spezifikation · Vertrag · Tests**. Darauf aufbauend:
> ein Überblick über die aktuellen Foundation Models (2026), die Open-Source-Toolbox
> der Harnesses (OpenCode, pi, zot) und wie Spec-Driven Development agentisches
> arbeitet. Zwei Anwendungen im Zentrum: erst direkt agentisch ohne Spec (Anwendung 1),
> dann dasselbe Thema via Spec aufs Demo-Repo (Anwendung 2): Jede Teilnehmende forked
> ein CI-validiertes Research-Repo (skeleton-research) für den eigenen Literatur-Alltag
> — Pipeline, wöchentliche Discovery und Reports inklusive — und erlebt live, wie ein
> Spec-Change agentisch umgesetzt und verifiziert wird. Den Abschluss bildet ein
> Outcomes-Block, in dem Teilnehmende eigene Ergebnisse präsentieren, gefolgt von
> Q&A und Diskussion.
>
> Voraussetzungen: SAIA-Account oder sonstigen LLM-Provider, git und Python — ein Software-Development-Hintergrund
> ist nicht nötig. Vortragssprache: Deutsch. Materialien werden unter CC-BY bereitgestellt.
