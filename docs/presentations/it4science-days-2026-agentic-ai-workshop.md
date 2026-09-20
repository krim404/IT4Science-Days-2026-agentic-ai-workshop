---
marp: true
theme: default
paginate: true
footer: 'IT4Science Days 2026 · Agentic AI Workshop'
style: |
  section {
    background-color: #1a1a1a;
    color: #e8e8e8;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    padding-bottom: 64px;
  }
  section.smaller table { font-size: 16px; }
  section.smaller table th, section.smaller table td { padding: 4px 9px; }
  h1, h2, h3 {
    color: #ffffff;
    font-weight: 700;
  }
  table {
    margin: 0 auto;
    font-size: 20px;
    border-collapse: collapse;
  }
  table th, table td {
    background-color: #2a2a2a;
    padding: 7px 11px;
    border: 1px solid #555;
    color: #e8e8e8;
  }
  table thead th {
    background-color: #383838;
    color: #ffffff;
    border-bottom: 2px solid #666;
  }
  table tbody tr:nth-child(even) td {
    background-color: #252525;
  }
  p:has(img) {
    margin: 0;
    line-height: 0;
  }
  img.hero {
    border-radius: 8px;
    max-height: 430px;
    max-width: 1123px;
    object-fit: contain;
    display: block;
    margin: 0 auto;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
  .columns.smaller { font-size: 20px; }
  /* Speaker badges */
  .speaker {
    position: absolute;
    top: 32px;
    right: 40px;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 0.3px;
    z-index: 10;
  }
  .speaker-christian { background: #14432a; color: #7ee2a8; border: 1px solid #2f9e5f; }
  .speaker-tobias    { background: #1a2f52; color: #8ab8ff; border: 1px solid #3b6fc4; }
  /* Placeholder boxes for content to be added */
  .todo {
    background: #3a2a10;
    border: 1px dashed #c8902e;
    color: #ffd88a;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 19px;
    margin-top: 8px;
  }
  .todo strong { color: #ffe9b0; }
  /* Stoic Unix principles (shown through deeds, not named) */
  .unix {
    background: #1a2450;
    border-left: 4px solid #3b6fc4;
    border-radius: 0 8px 8px 0;
    padding: 8px 14px;
    font-size: 18px;
    color: #cfe0ff;
    margin: 6px 0;
  }
  .unix strong { color: #8ab8ff; }
  blockquote {
    background: #242424;
    border-left: 4px solid #666;
    border-radius: 0 8px 8px 0;
    padding: 10px 16px;
    font-style: italic;
    color: #d0d0d0;
  }
  code {
    background: #2a2a2a;
    border-radius: 4px;
    padding: 1px 5px;
    color: #9ecbff;
  }
  pre code {
    background: #101010;
    display: block;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 17px;
    line-height: 1.45;
  }
  .rank { color: #ffd88a; font-weight: 700; }
---

<!-- _class: lead -->

# Agentic AI in der Praxis

## Vom Spec zum produktiven Workflow: ein Workshop mit Hands-on

**IT4Science Days 2026 · Agentic AI Workshop** · 09:00–12:00

Christian Uhl · Tobias Weiß

<!-- notes:
Begrüßung (~1 min). Kurz vorstellen: Wer wir sind, worum es geht.
Ziel: Teilnehmende verlassen den Raum mit eigenem Research-Repo, das per CI
validiert wird, und haben einen OpenSpec-Change selbst angewendet.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Wer wir sind: zwei Beispiele aus der Praxis

<div class="columns smaller">
<div>

**Christian Uhl**
Zentrum für angewandte Informatik & Data Science, Uni Gießen

> **Aus der Praxis:** Ein unbekannter, kaum dokumentierter Chip ohne Firmware; ein
> einzelner Fehler hätte ihn zerstört. Offen war, wie weit man in 24 Stunden kommt.
> Ergebnis: eine **FIDO2-fähige Firmware**, **spezifikations- und testgetrieben**.

</div>
<div>

**Tobias Weiß**
DevOps Engineer, Uni Marburg

> **Aus der Praxis:** Research-Pipelines & IT-Betrieb agentisch.
> Dieses Foliendeck selbst ist ein Artefakt derselben Pyramide:
> mit pi + OpenSpec aus Specs gebaut.

</div>
</div>

<!-- notes:
CHRISTIAN — führt durch die Vorstellung (~3 min); Tobias trägt sein Beispiel
selbst vor (~1 min). Eigenes Beispiel ~60-90 s. Badge mitbringen, hochhalten, durch den Raum geben —
das Objekt trägt die Folie, nicht der Text.
Die Prämisse ausdrücklich als Versuchsanordnung darstellen, nicht als Erfolgs-
geschichte: Die Ausgangsfrage lautete, wie weit man unter denkbar ungünstigen
Bedingungen kommt. Der Ausgang war offen.
Erzählbogen in fünf Schritten, in dieser Reihenfolge vortragen:
(1) Die Hardware war vorhanden, jedoch ohne jede Firmware und damit funktionslos.
    Der Chip war uns unbekannt, seine Dokumentation unzureichend.
(2) Die Konferenz lief bereits; ein Zeitfenster für reguläre Hardwareentwicklung
    bestand nicht.
(3) Hinzu kam das Risiko: Ein einzelner Fehler am Secure Element hätte das Gerät
    dauerhaft unbrauchbar gemacht.
(4) Damit liegt ein Zielkonflikt vor, der ausdrücklich benannt werden sollte:
    Sorgfältiges Vorgehen war zeitlich ausgeschlossen, unsorgfältiges Vorgehen
    war wegen des Risikos ausgeschlossen.
(5) Aufgelöst wurde der Konflikt durch spezifikations- und testgetriebene
    Entwicklung. Das Ergebnis lag binnen 24 Stunden vor: eine vollständige
    Custom-Firmware, die als FIDO2-Sicherheitsschlüssel einsetzbar ist — also
    ein sicherheitsrelevantes System, kein Demonstrator.
Kernsatz zum Aussprechen: "Das Tempo war nur deshalb vertretbar, weil die
Testsuite jeden Fehler abfängt, bevor er das Gerät erreicht."
Technische Mechanik für Rückfragen: Die Testsuiten laufen auf dem Entwicklungs-
rechner, nicht auf dem Gerät. Ein Fehlversuch kostet dort nichts, weshalb die
Iterationsschleife kurz bleibt, obwohl die Zielhardware unverzeihlich ist.
Übertragung auf das Publikum (zentral, bitte nicht auslassen): Das Äquivalent in
der Forschung ist nicht der zerstörte Chip, sondern die verbrauchte Messzeit oder
die Auswertung, die bereits publiziert ist. Die Ausgangslage ist dieselbe —
knappe Zeit bei teuren Fehlern — und damit auch die Lösung.
Ton: nicht als Kunststück erzählen. Die Methode ist der Held, nicht der Sprecher.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Ihre Reihe: Blitzlicht

- **Name · Fachrichtung · eine Aufgabe**, die agentisch für Sie arbeiten soll.
- ≤ 30 Sekunden je Person, wir sammeln Wünsche an die Whiteboard-Wand.
- Diese Wünsche checken wir am Ende gegen die Outcomes.

> Bei großen Runden: 5–6 Stichworte aus dem Raum, Rest per Karte/Zettel.

<!-- notes:
CHRISTIAN — moderiert (~4 min). Die gesammelten Wünsche sichtbar notieren —
Wrap-Up greift sie auf. Zeit hart timen.
-->

---

<!-- _class: lead smaller -->

# Agenda (3h)

| Zeit | Block | Dauer | Wer |
|------|-------|-------|-----|
| 09:00–09:15 | Ankommen, Vorstellung (Praxisbeispiele + TN-Runde), Ablauf | 15 min | Christian |
| 09:15–09:30 | Grundlagen & Definition | 15 min | Christian |
| 09:30–09:50 | Foundation Models: aktuelle Entwicklungen | 20 min | Christian + Tobias |
| 09:50–10:10 | Open-Source Toolbox | 20 min | Tobias + Christian |
| 10:10–10:20 | ☕ Pause | 10 min | — |
| 10:20–10:45 | Anwendung 1: Eigenes Research-Repo | 25 min | Tobias |
| 10:45–11:00 | Spec Driven & Token-optimized Development | 15 min | Christian + Tobias |
| 11:00–11:25 | Anwendung 2: Spec selbst anwenden | 25 min | Christian |
| 11:25–11:30 | ☕ Pause | 5 min | — |
| 11:30–11:45 | Outcomes: TN präsentieren ihre Ergebnisse | 15 min | Tobias |
| 11:45–12:00 | Q&A, Diskussion, Wrap Up | 15 min | Tobias |

<!-- notes:
Agenda auf 1 min durchgehen. Zwei Hands-on-Blöcke: (1) eigenes Research-Repo,
(2) OpenSpec selbst anwenden. Christian: Vorstellung, Grundlagen (2), Spec-Teil von Block 7.
Tobias: Toolbox (4), Anwendung 1 (6), Token-Teil von 7, Outcomes (10), Q&A (11). Gemeinsam: 3, 7.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Begriffe, bei denen wir uns festlegen

| Begriff | Worüber gestritten wird | Unsere Festlegung für heute |
|---------|-------------------------|------------------------------|
| **Agent** | von „Chatbot mit Schleife" bis „autonomes System" | Das Modell bestimmt die nächsten Schritte. Feste Abfolge = Workflow. |
| **Reasoning** | ob das „Denken" ist, ist offen | mehr Rechenzeit zur Laufzeit; keine Aussage über Kognition |
| **Halluzination** | Begriff selbst umstritten (eher: Konfabulation) | nicht belegte Ausgabe, der Grund für die Testebene |
| **Open Source** | offene Gewichte sind nicht Open Source (OSI) | wir sagen **offene Gewichte**, wenn wir das meinen |
| **Reproduzierbarkeit** | gleiche Eingabe, abweichendes Ergebnis | geprüft wird das **Ergebnis**, nicht der Weg dorthin |

<!-- notes:
CHRISTIAN. Nicht alle fünf Zeilen gleich lang
behandeln, die letzten beiden tragen das Publikum.
Rahmensatz zu Beginn: Bei diesen Begriffen ist sich die Fachwelt nicht einig.
Wir entscheiden uns für heute auf eine Lesart, damit wir nicht aneinander
vorbeireden. Das ist eine Setzung, kein Stand der Forschung.

ABLAUF FOLIE 6

(1) Agent
    Trennlinie ist die Frage, wer den Ablauf bestimmt.
    Modell bestimmt die nächsten Schritte: Agent.
    Feste, vorher festgelegte Abfolge: Workflow, kein Agent.
    Damit ist auch gesagt, was kein Agent ist: Ein Skript mit fester
    Reihenfolge bleibt ein Skript, auch wenn ein Modell darin vorkommt.

(2) Reasoning
    Bewusst nüchtern halten: mehr Rechenzeit zur Laufzeit, mehr Zwischenschritte.
    Keine Aussage darüber, ob das Denken ist. Diese Frage ist für unsere Zwecke
    unerheblich und kostet nur Diskussionszeit.

(3) Halluzination
    Der Begriff selbst ist umstritten, in der Literatur eher Konfabulation.
    Nicht beschwichtigen, sondern als Konstruktionsbedingung benennen: Ein
    Modell, das das nächste Token vorhersagt, kann nicht zwischen belegt und
    plausibel unterscheiden.
    Daraus folgt der Umgang: Wir verifizieren maschinell, statt zu vertrauen.
    Genau dafür existiert die Testebene, die gleich kommt.

(4) Open Source
    Frei verfügbare Gewichte sind nicht dasselbe wie Open Source im Sinne der
    OSI-Definition. Trainingsdaten und Verfahren bleiben meist verschlossen.
    Wir sagen "offene Gewichte", wenn wir das meinen. Betrifft die Folien zu
    Foundation Models und zur Toolbox unmittelbar und ist in einer Rückfrage
    verteidigbar.

(5) Reproduzierbarkeit
    Der wichtigste Punkt für dieses Publikum, hier Zeit lassen.
    Die Sorge offen aussprechen: Gleiche Eingabe, abweichendes Ergebnis. Das
    widerspricht allem, was wissenschaftliches Arbeiten verlangt.
    Die Antwort: Der Weg ist nicht reproduzierbar, das Ergebnis muss es sein.
    Geprüft wird nicht, wie der Agent gearbeitet hat, sondern ob das Ergebnis
    die Prüfung besteht.
    Rückverweis auf das eigene Beispiel von Folie 2: Genau so war die Anordnung
    beim Chip. Niemand hat dem Agenten geglaubt, die Testsuite hat entschieden.
    Übergang zur Pyramide: Damit sind wir bei der Struktur, die den ganzen
    Vormittag trägt.

Wenn die Zeit knapp wird: (2) und (4) auf je einen Satz. (5) niemals kürzen.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Worüber wir sprechen: vier Bausteine

| Baustein | Was es ist | Was es **nicht** ist |
|----------|------------|----------------------|
| **Modell** (LLM) | Gewichte; sagt das jeweils nächste Token voraus | kein Wissensspeicher, keine Datenbank |
| **Kontext** | was im Eingabefenster steht: Repo, Spezifikation, Verlauf | kein Gedächtnis; endet mit der Sitzung |
| **Werkzeuge** | Zugriff auf Dateien, Shell, Netz, Schnittstellen | keine Rechte jenseits des Freigegebenen |
| **Harness** | führt aus, was das Modell verlangt: Kontext stellen, Werkzeuge aufrufen, Ergebnisse zurückspeisen, Schleife beenden | trifft die Entscheidungen nicht selbst |

<!-- notes:
CHRISTIAN.
Warum zuerst: Über Spezifikation und Verifikation lässt sich nicht sprechen,
solange offen ist, wer oder was hier eigentlich handelt.

ABLAUF FOLIE 5

(1) Einstieg
    Der Raum ist gemischt: Ein Teil hat noch nie mit einem Sprachmodell
    gearbeitet, ein anderer täglich. Beide meinen mit "KI" etwas anderes.
    Ansage: Wir zerlegen den Begriff einmal, dann reden wir über dasselbe.

(2) Modell
    Ein Sprachmodell sagt das jeweils nächste Token voraus, nichts weiter.
    Abgrenzung: kein Wissensspeicher, keine Datenbank, kein Nachschlagewerk.
    Konsequenz: Was es nicht im Kontext hat, kann es nur rekonstruieren.
    Damit ist der Begriff Halluzination vorbereitet (kommt auf Folie 6).

(3) Kontext
    Alles, was im Eingabefenster steht: Repository, Spezifikation, Verlauf.
    Abgrenzung: kein Gedächtnis. Mit der Sitzung ist es weg.
    Wichtigste Folgerung des Vormittags: Deshalb gehören Regeln in Dateien
    und nicht in Sitzungen. Verweis voraus auf AGENTS.md in Anwendung 1.

(4) Werkzeuge
    Erst hiermit darf das System handeln statt nur zu antworten: Dateien,
    Shell, Netz, Schnittstellen.
    Abgrenzung: keine Rechte jenseits des Freigegebenen. Wer nichts freigibt,
    bekommt einen Gesprächspartner, keinen Agenten.

(5) Harness
    Die Ausführungsschicht: Kontext zusammenstellen, Werkzeuge aufrufen,
    Ergebnisse zurückspeisen, Schleife beenden.
    Arbeitsteilung sauber trennen: Das Modell entscheidet, was geschehen
    soll; das Harness sorgt dafür, dass es geschehen kann.
    Falls nachgefragt wird: "Harness" ist Jargon aus der Praxis der
    Coding-Agenten. In der Forschungsliteratur heißt dieselbe Schicht
    überwiegend "Scaffolding". Wir setzen den Begriff hier fest, statt ihn
    als gesicherten Stand der Wissenschaft auszugeben.

(6) Abschluss
    Alle vier zusammen sind das, was umgangssprachlich "KI" heißt.
    Übergabesatz für Block 3 von Tobias: Dasselbe Modell, ein anderes
    Harness, ein anderes Ergebnis. Das wird dort vorgeführt, nicht behauptet.

Wenn die Zeit knapp wird: (4) auf zwei Sätze kürzen. (3) und (5) nicht kürzen,
darauf baut der Rest des Vormittags auf.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Was ist agentisches Arbeiten? Eine Definition

- Der **Engpass ist nicht das Programmieren**, sondern die **Anforderungsklärung**.
- Ein Agent braucht einen **präzisen Auftrag** und einen **stabilen Kontext**; das Ergebnis ist nur so gut wie der **Vertrag** davor.
- **Agentisches Arbeiten** heißt: Verträge für Maschinen verfassen statt Anweisungen für Menschen.

> **Modell + Kontext + Werkzeuge + Harness = Agent.**
> Umgangssprachlich heißt das zusammen „KI".

<!-- notes:
CHRISTIAN — Block 1 · 09:15–09:30. Weg von "Prompting" hin zu "Contracts".
-->

---

<!-- _class: lead -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

# <span style="color:#8ab8ff">Spezifikation</span> · <span style="color:#ffd88a">Vertrag</span> · <span style="color:#7ee2a8">Tests</span>

## Die Struktur, auf die wir den ganzen Vormittag zurückkommen

<!-- notes:
CHRISTIAN. Abschnittstrenner, kurz halten, etwa zwei Saetze.
Die drei Woerter sind in den Farben gesetzt, in denen die naechste Folie die
Ebenen zeigt. Das ist beabsichtigt: Der Trenner kuendigt das Bild an.
Ansage: Ab hier geht es nicht mehr um Werkzeuge, sondern um die Arbeitsweise.
Dieselbe Struktur taucht heute noch dreimal auf, im Research-Repository, in
OpenSpec und in der eigenen Uebung am Nachmittag.
Begriffsklaerung, falls jemand stutzt: In den Werkzeugen heissen diese Ebenen
englisch Spec, Contract und Test. Gemeint ist dasselbe.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Eine Metapher für den ganzen Workshop

<img class="hero" src="../../assets/spec-contract-test-pyramid.png" alt="Spec · Contract · Test Pyramide"/>

<!-- notes:
CHRISTIAN — die Pyramide als roter Faden. Spec oben (Source of Truth), Contract in
der Mitte (Delta-Spec = Agenten-Prompt), Tests unten (objektive Verifikation).
Wir kommen auf dieses Bild immer wieder zurück.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Was bedeutet die Pyramide?

| Ebene | Legt fest | Im Repository |
|-------|-----------|---------------|
| **Spezifikation** | Was gelten soll, als überprüfbare Anforderung formuliert | `specs/`, `AGENTS.md`: die verbindlichen Regeln |
| **Vertrag** | Was sich in genau diesem Schritt ändert, und woran man das misst | ein Change: Vorschlag, Entwurf, Spezifikation, Aufgabenliste |
| **Tests** | Ob die Anforderung erfüllt ist, ohne Ermessensspielraum | Testsuite, Validierung, automatische Prüfung bei jeder Änderung |

> **Erledigt ist eine Aufgabe erst, wenn die Prüfung bestanden ist.**
> Nicht, wenn der Agent erklärt, er sei fertig.

<!-- notes:
CHRISTIAN. Diese Folie erklaert das Bild der vorigen Folie Ebene fuer Ebene.

ABLAUF

(1) Einstieg
    Rueckverweis auf das eigene Beispiel: Genau diese drei Ebenen lagen beim
    Chip vor. Die Spezifikation war das erwartete Verhalten des Geraets, der
    Vertrag war der jeweils naechste Arbeitsschritt, die Tests waren die
    Testsuite auf dem Entwicklungsrechner.

(2) Spezifikation
    Entscheidend ist die Formulierung: nicht "das Geraet soll sicher sein",
    sondern eine Anforderung, deren Erfuellung sich pruefen laesst.
    Fuer dieses Publikum uebersetzen: Das entspricht einer Hypothese, die so
    formuliert ist, dass ein Experiment sie widerlegen koennte. Eine
    Anforderung, die keine Pruefung zulaesst, ist eine Absichtserklaerung.

(3) Vertrag
    Der Agent bekommt nicht die gesamte Spezifikation, sondern die Differenz:
    Das ist der Stand, das soll sich aendern, daran wird es gemessen.
    Analogie: das Versuchsprotokoll fuer einen einzelnen Durchlauf, nicht die
    gesamte Projektbeschreibung.

(4) Tests
    Die Ebene, die entscheidet. Kein Gespraech, keine Einschaetzung, kein
    Vertrauen: bestanden oder nicht bestanden.
    Hier laesst sich die Sorge von Folie 5 aufloesen: Der Weg des Agenten ist
    nicht reproduzierbar, das Ergebnis wird es durch diese Ebene.

(5) Rueckfluss
    Der Pfeil im Bild ist der eigentliche Punkt. Was die Tests zutage foerdern,
    fliesst als neue Anforderung zurueck nach oben. Die Spezifikation ist kein
    Dokument, das am Anfang geschrieben und dann abgelegt wird.

(6) Abschluss
    Den Merksatz stehen lassen und bewusst betonen: Erledigt ist erledigt,
    wenn die Pruefung bestanden ist. Dieser Satz kommt in Uebung 2 zurueck und
    ist dort das Bewertungskriterium.

Glossar, falls im Raum Rueckfragen kommen:
SHALL, MUST, SHOULD sind die ueblichen Signalwoerter fuer verbindliche,
zwingende und empfohlene Anforderungen.
"Gegeben, wenn, dann" ist eine Schablone fuer Szenarien: Ausgangslage, Eingriff,
erwartetes Ergebnis. Wer Versuchsprotokolle schreibt, kennt die Struktur.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

# Foundation Models: aktuelle Entwicklungen

<!-- notes:
CHRISTIAN — Block 2 · 09:30–09:50 (20 min), Lead. Tobias ergänzt die
Tooling-/Souveränitäts-Sicht. Thema nach Relevanz gerankt.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Wo stehen die Modelle 2026? Ein Ranking

<div class="columns smaller">
<div>

**1. Reasoning reif**: planen statt komplettieren

**2. Kontext explodiert**: 200K → 1M+ Token

**3. MCP wird Standard**: „USB-C der Tools“

</div>
<div>

**4. Tool-Use produktionsreif**: strukturiert, parallel

**5. OpenSource holt auf**: Kosten-Kollaps

**6. Lokal & souverän**: DSGVO ohne Qualitätsverlust

</div>
</div>

> SAIA-Katalog (09/2026): GLM 4.7 · Qwen3.8 · DevStral 2 · DeepSeek V4 Flash · Llama 3.1 8B, geroutet über Aliase (`best-for-*` / `budget` / `fastest`).

<!-- notes:
CHRISTIAN — Ranking 1–6, je ~1 min. Details pro Punkt:
(1) Rechenzeit skalieren statt Parameter — o-Serie, DeepSeek-R1, Claude-Thinking:
planen, verifizieren, korrigieren.
(2) 200K → 1M+ (Gemini 3.1 Pro): ganze Codebases & Specs im Kontext → echte Agenten.
(3) Model Context Protocol entkoppelt Modell ↔ Tool.
(4) Strukturierte Ausgaben, parallele Tool-Calls, Multi-Agent — Produktionsreife.
(5) Qwen 3.6/3.5 (MoE), GLM 4.7/5, DeepSeek V4, GPT-OSS, Llama, Gemma 4 —
für viele Tasks reicht ein kleines Modell.
(6) Ollama, vLLM, llama.cpp auf eigener Hardware. MPG-Bezug: sensible
Forschungsdaten → lokale Modelle (DSGVO); GWDG/SAIA-Zugang existiert institutsseitig.
TOBIAS nach #5/#6 (2 min Praxis-Sicht): SAIA-Katalog — welche Modelle wirklich
laufen, Routing über Aliase → vertieft in Block 5.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Foundation Models: Praxis-Einordnung

| Aufgabe | Derzeit stark | Anmerkung |
|---------|---------------|-----------|
| Freie Textproduktion, Übersetzung | **GPT-6** | derzeit führend bei Prosa |
| Räumliche Aufgaben, 3D-Modellierung | **GPT-6** | in eigenen Tests überzeugend |
| Code schreiben, größere Umbauten | **Claude**, zunehmend **GLM** | Claude teuer, aber oft auf Anhieb erfolgreich |
| Code gezielt umschreiben | **Qwen3.8-Flash-Next**, **GLM** | offene Gewichte, schnell, günstig |
| Abläufe mit Werkzeugen steuern | **GLM 4.7**, Claude | verlässliche Werkzeugaufrufe |
| Sensible Forschungsdaten | **lokal**: Ollama, vLLM, llama.cpp | die Daten verlassen das Haus nicht |
| Viele gleichartige Fälle | kleine Modelle, z. B. **DeepSeek V4 Flash** | Geschwindigkeit und Kosten entscheiden |

> **Die offenen Modelle holen massiv auf.** In vielen Aufgaben ist der Abstand
> inzwischen kleiner als der Preisunterschied.

<div style="font-size:15px; color:#9a9a9a; margin-top:4px;">
Quelle: eigene Erfassung
</div>

<!-- notes:
CHRISTIAN. Diese Folie beantwortet die Frage, die im Raum tatsaechlich gestellt
wird: Welches Modell soll ich denn nun nehmen? Bewusst nicht auf agentisches
Arbeiten beschraenkt, der Raum arbeitet auch schreibend und auswertend.

ABLAUF

(1) Rahmen setzen
    Die Landschaft aendert sich schneller, als eine Folie altern kann. Deshalb
    keine Rangliste, sondern ein Auswahlkriterium, das auch naechstes Jahr traegt:
    Man waehlt nach Aufgabe, nicht nach Ruf des Anbieters. Kein Modell ist in
    allem vorn.

(2) Die beiden oberen Zeilen
    Fuer viele im Raum die relevantesten, weil sie taeglich schreiben und nicht
    taeglich programmieren. GPT-6 ist bei freier Textproduktion derzeit vorn.
    Der 3D-Punkt ueberrascht erfahrungsgemaess und lohnt einen Satz: raeumliche
    Aufgaben galten lange als Schwaeche dieser Modelle.

(3) Die Code-Zeilen
    Ehrlich einordnen: Claude ist bei groesseren Umbauten oft auf Anhieb
    erfolgreich und entsprechend teuer. Fuer gezielte Umschreibungen leistet
    Qwen3.8-Flash-Next inzwischen mehr als die vorher spezialisierten
    Coder-Modelle, bei offenen Gewichten und einem Bruchteil der Kosten.
    GLM steht in beiden Zeilen, weil es in beiden Faellen brauchbar arbeitet und
    dabei am schnellsten aufholt. Das ist der Beleg fuer den Schlusssatz der
    Folie: Der Abstand schrumpft dort am deutlichsten, wo er lange am groessten war.

(4) Untere Zeilen
    Sensible Daten: fuer Forschungsdaten der entscheidende Punkt, oft vorab
    entschieden. Viele gleichartige Faelle: der haeufigste Denkfehler ist, fuer
    jede Aufgabe das groesste Modell zu nehmen.

(5) Schlusssatz und Ausblick
    Der Abstand zwischen offenen und proprietaeren Modellen schrumpft schneller,
    als die Preise fallen. Praktische Folge: sich nicht auf einen Anbieter
    festlegen, sondern die Steuerungsebene austauschbar halten. Das leitet zu
    Tobias ueber.

(6) Optional, wenn Zeit bleibt
    Kurze Live-Demonstration. Faellt bei Zeitdruck ersatzlos weg.

Zur Quellenangabe auf der Folie: Die Einschaetzungen stammen aus dem eigenen
laufenden Einsatz, nicht aus Benchmarks. Genau so vortragen, das ist
glaubwuerdiger als eine geliehene Rangliste.
Begruendung fuer Rueckfragen: Objektives Benchmarking ist bei diesen Modellen
methodisch schwierig. Testdaten geraten in Trainingsdaten, die Ergebnisse haengen
stark von Aufgabenzuschnitt und Umgebung ab, und zwischen Veroeffentlichung und
Vortrag liegen oft mehrere Modellgenerationen. Wer Zahlen moechte, bekommt den
Verweis auf docs/research-foundation-models-toolbox.md.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Beim agentischen Arbeiten entscheidet das Harness

- **Einzelne Frage** → das Modell entscheidet
- **Mehrere Schritte, Werkzeuge, Selbstkorrektur** → das Harness entscheidet
- Mehrfach unabhängig beobachtet: günstiges Modell im guten Harness vor teurem im schlechten
- Reihenfolge in der Praxis: erst das Harness, dann die Modellfrage

> **Auch das beste Modell ist nur so gut wie sein Harness.**

<div style="font-size:15px; color:#9a9a9a; margin-top:4px;">
Quelle: eigene Erfassung
</div>

<!-- notes:
CHRISTIAN. Diese Folie ist der Angelpunkt des Vormittags und zugleich die
Uebergabe an Tobias. Sie beantwortet die Frage, die die vorige Folie aufwirft:
Wenn die Modellwahl so von der Aufgabe abhaengt, worauf kommt es dann wirklich an?

(1) Zuerst die Einschraenkung setzen, sonst entsteht ein Widerspruch zur
    vorigen Folie: Fuer eine einzelne Aufgabe, etwa einen Text oder eine
    Uebersetzung, entscheidet weiterhin das Modell. Die Aussage dieser Folie gilt
    fuer agentisches Arbeiten, also mehrere Schritte, Werkzeugaufrufe und
    Selbstkorrektur. Erst dort summieren sich die Einfluesse der Umgebung.

(2) Ausformulierung fuer den zweiten Punkt, die Folie traegt nur das Stichwort:
    Bei einer einzelnen Frage, etwa einer Uebersetzung, entscheidet das Modell.
    Sobald es ueber mehrere Schritte arbeitet, Werkzeuge benutzt und sich selbst
    korrigiert, verschiebt sich das Gewicht zum Harness, weil sich dessen
    Einfluesse ueber die Schritte summieren.

(3) Die Beobachtung nuechtern vortragen
    Es handelt sich nicht um eine einzelne Messung, sondern um ein Muster, das
    sich in mehreren unabhaengigen Versuchen gezeigt hat. Genau so formulieren,
    ohne Zahl. Eine erfundene Prozentangabe wuerde die Aussage schwaechen.

(4) Warum das so ist, in einem Satz
    Das Modell sieht nur, was die Umgebung ihm zeigt, darf nur, was sie erlaubt,
    und laeuft nur so lange, wie sie es laufen laesst. Ein starkes Modell mit
    schlechtem Kontext arbeitet an der falschen Aufgabe, nur eloquenter.

(5) Rueckverweis auf die Bausteinfolie
    Dort wurde die Arbeitsteilung bereits gesetzt: Das Modell entscheidet, was
    geschehen soll, die Umgebung sorgt dafuer, dass es geschehen kann. Hier ist
    die praktische Konsequenz daraus.

(6) Entlastung fuer den Raum
    Das ist eine gute Nachricht und sollte auch so gesagt werden: Niemand muss
    das teuerste Abonnement abschliessen, um brauchbar zu arbeiten. Wer seine
    Spezifikationen und Pruefungen in Ordnung bringt, kommt mit guenstigen oder
    lokal betriebenen Modellen weit.

(7) Uebergabe an Tobias
    Genau das ist der Gegenstand des naechsten Blocks. Tobias zeigt drei
    Umgebungen im Vergleich und fuehrt vor, dass dasselbe Modell darin
    unterschiedliche Ergebnisse liefert. Uebergabesatz: Was das konkret bedeutet,
    zeigt Tobias jetzt am lebenden Objekt.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Open-Source Toolbox

## Harnesses: die Steuerungsebene über dem Modell

<!-- notes:
TOBIAS — Block 3 · 09:50–10:10 (20 min), Lead. Christian ergänzt.
Die Harnesses nach Stage/Use-Case ranken.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Drei Harnesses im Vergleich

<div class="columns smaller">
<div>

**1. OpenCode**: der Allrounder
- Agent im Terminal (CLI/TUI): `opencode run "…"`, Modell je Agent.
- LSP, Plugins, Skills, MCP · mit OmO: AST-Grep, Background-Agents.

**2. pi**: das Minimal-Harness
- Skills · Prompt-Templates · Extensions · Themes.
- „Adapt pi, nicht umgekehrt“.

**3. zot**: das schlanke Agent-Harness
- Single-Binary (Go), TUI + JSON-RPC (fernsteuerbar) + MCP.
- Ollama/llama.cpp → lokale Modelle, souverän.

</div>
<div>

**Ranking nach Einsatz:**

| Platz | Tool | Für |
|-------|------|-----|
| 1 | **OpenCode** | tägliche Coding-Agents, Routing |
| 2 | **pi** | kontrollierte, minimalistische Workflows |
| 3 | **zot** | RPC/Headless-Integration, eigene Automation |

> Ein **Harness ist die Steuerungsebene**: gleiche Modelle, unterschiedliche Ergebnisse, je nach Harness.

**Claude Code** (kommerziell) als Vergleichsmaßstab, Open-Source spielt oben mit.

</div>
</div>

<!-- notes:
TOBIAS — Timing (20 min): 12 min Vergleich inkl. Live-Demo — derselbe Prompt in
allen dreien, Ergebnis-Differenz zeigen: „gleiche Modelle, unterschiedliche
Ergebnisse“ wird bewiesen, nicht behauptet. 3 min Ranking. Danach Tooling-Folie.
Details: OpenCode mit OmO → AST-Grep (25 Sprachen), parallele Background-Agents.
Glossar für Nicht-Devs (Zielgruppe Postdocs): LSP = Language Server (Code-Verständnis
im Editor), MCP = Model Context Protocol, AST-Grep = strukturelle Code-Suche.
pi: nichts eingebacken, alles baubar. zot: Extensions, Slash-Commands,
`zot "prompt"` · `zot -p` · `zot rpc` — RPC für eigene Automation.
Ranking: OpenCode Tagesgeschäft, pi minimal & erweiterbar, zot Skripting/RPC.
**Claude Code** (kommerziell) als Vergleichsmaßstab, Open-Source spielt oben mit.
pi steckt dahinter, wie dieser Workshop entstanden ist.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Die kommerzielle Gegenprobe

| Harness | Zuschnitt |
|---------|-----------|
| **Claude Code** (Anthropic) | auf die eigenen Modelle abgestimmt, hoher Token-Verbrauch |
| **Codex** (OpenAI) | auf die eigenen Modelle abgestimmt |
| **Antigravity CLI** (Google) | auf die eigenen Modelle abgestimmt, löst Gemini CLI ab |

- Für die Modelle des Anbieters optimiert → **nicht übertragbar**
- In unabhängigen Vergleichen eher **Mittelfeld**
- Stärke: **ohne Konfiguration sofort brauchbar**

> Bequemlichkeit gegen Kontrolle. Wer nichts einstellen möchte, fährt gut.
> Wer optimieren will, stößt an Grenzen.

<div style="font-size:15px; color:#9a9a9a; margin-top:4px;">
Quelle: eigene Erfassung
</div>

<!-- notes:
CHRISTIAN. Kurzer Einschub nach Tobias' Vergleich der offenen Harnesses, damit
niemand den Raum mit dem Eindruck verlaesst, Open Source sei hier eine
ideologische Entscheidung.

(1) Warum ueberhaupt erwaehnen
    Ein Teil des Raums nutzt genau diese Werkzeuge oder hat davon gehoert. Wer
    sie verschweigt, wirkt unglaubwuerdig.

(2) Die Staerke zuerst nennen, sie ist echt
    Installieren und loslegen. Keine Konfiguration, keine Modellwahl, keine
    Einrichtung. Fuer den Einstieg ist das ein erheblicher Vorteil, und fuer
    viele Aufgaben reicht es dauerhaft.

(3) Der Preis dafuer
    Die Optimierung gilt dem jeweils eigenen Modell. Was dort gut funktioniert,
    laesst sich nicht auf andere Modelle uebertragen. In unabhaengigen
    Vergleichen landen diese Systeme deshalb eher im Mittelfeld.
    Claude Code ist ausserdem dafuer bekannt, sehr viele Token zu verbrauchen.
    Das ist bei einem Institutsbudget ein reales Argument.

(4) Das Muster ist die eigentliche Aussage
    Drei grosse Anbieter, drei eigene Harnesses, jedes auf die eigenen Modelle
    abgestimmt. Genau daraus folgt die fehlende Uebertragbarkeit.
    Zum Namen, falls jemand Gemini CLI kennt: Google hat es im Juni 2026 auf
    Antigravity CLI umgestellt. Fuer Pro-, Ultra- und Gratis-Zugaenge ist Gemini
    CLI abgeschaltet, ueber Code-Assist-Lizenzen laeuft es weiter. Antigravity CLI
    benutzt dasselbe Harness wie die gleichnamige Desktop-Anwendung.
    Nicht zu verwechseln mit Antimatter, einer Oberflaeche zur Steuerung mehrerer
    Agenten mit Projektbrettern und Kanaelen. Andere Produktkategorie.

(5) Schluss und Rueckbindung
    Der Merksatz traegt den Einschub: Bequemlichkeit gegen Kontrolle. Beides ist
    legitim, es haengt davon ab, ob man ein Werkzeug benutzen oder es formen will.
    Rueckverweis auf die eigene Folie zuvor: Auch hier entscheidet nicht das
    Modell, sondern wie gut die Umgebung zur Aufgabe passt.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Weiteres Agentic-Tooling

| Tool | Funktion |
|------|----------|
| **OpenSpec** | Delta-Specs als Agenten-Prompts |
| **SAIA Accelerator** | GWDG-Modelle für OpenCode/zot/pi, Auto-Sync |
| **oh-my-opencode** | Routing je Aufgabe, AST-Grep, Background-Agents |
| **skeleton-research** | Forkbares Corpus-Skeleton, Hands-on in Anwendung 1 |
| **Superpowers** | TDD, Debugging, Review als Routinen |
| **rtk** | Filtert Tool-Output: **−60–90 % Input-Token** |
| **ponytail / caveman** | Skills: minimale Lösungen, knappe Prosa |
| **Ollama / vLLM / llama.cpp** | Lokales Modell-Serving |

> **Das Modell ist das Gehirn, die Workflows sind der Muskel.**

<!-- notes:
TOBIAS — Tooling-Landschaft ranken. OpenSpec ist die Brücke zu Block 5 (Spec & Token).
oh-my-opencode leitet innerhalb von Block 5 zum Token-Teil über.
rtk + ponytail/caveman als Token-Hebel vorwegnehmen: „Output filtern, knapp reden,
minimal bauen — Zahlen dazu gleich im Token-Teil.“
-->

---

<!-- _class: lead -->


# ☕ Pause

10 Minuten.

<!-- notes:
Pause 10:10–10:20.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Anwendung 1: Eigenes Research-Repo

<!-- notes:
TOBIAS — Block 4 · 10:20–10:45 (25 min), Lead (Christian unterstützt). Herzstück: Wie Teilnehmende mit
skeleton-research ihre eigene Forschung unterstützen. Tobias führt das Repo.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## skeleton-research: Ein Fork für Ihre Forschung

**Jeder verlässt den Raum mit einem eigenen, CI-validierten Research-Repo.**

- **Literatur-Corpus als reiner Text**: `papers.yaml` = Source of Truth.
- **Eine Config** (`config/taxonomy.yaml`) steuert alles.
- Pipeline: **validieren → generieren → Stats → Reports**.
- **CI** (Prüf-Pipeline) holt wöchentlich neue Papers → **GitHub Pages**.

```bash
git clone https://github.com/tobias-weiss-ai-xr/skeleton-research.git my-research
cd my-research
```

<!-- notes:
TOBIAS — Kernnutzen: “Wie unterstützt das meine Forschung?” Ein Repo = strukturierter,
reproduzierbarer, auto-validierter Stand des Literaturwissens. CI macht es lebendig.
Danach: config/taxonomy.yaml anpassen, papers.yaml seeden, Pipeline laufen lassen.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Die Pipeline: jede Datei hat einen Zweck

```
config/taxonomy.yaml  ──►  papers.yaml  ──►  validate ──►  generate_readme
                                                  │             │
                             standard_stats ◄─────┘             ▼
                                                  │        generate_reports
                                                   ▼              │
                                              CI pass/fail        ▼
                                                            docs/ (GitHub Pages)
```

<div class="unix"><strong>Ein Tool, ein Job.</strong> Jedes Skript tut genau eine Sache
(validate / generate / stats / reports), und sie komponieren sich zur Pipeline.</div>
<div class="unix"><strong>Text ist die Schnittstelle.</strong> YAML + Markdown, kein GUI nötig.
Ein Mensch kann genauso lesen wie ein Agent.</div>
<div class="unix"><strong>Die Pipeline ist der Richter.</strong> Vom Agenten erzeugte Edits müssen
die Validierung bestehen, objektiv und nicht nach Meinung.</div>

<!-- notes:
TOBIAS — der Unix-Geist wird durch die Struktur gezeigt, nicht benannt:
ein Tool/ein Job, Text als Schnittstelle, Pipeline als objektiver Richter.
papers.yaml = Spec, Pipeline = Contract, CI = Test → die Pyramide in Aktion.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Jump-Start in 5 Schritten

1. **Forken**: `skeleton-research` klonen.
2. **Taxonomie setzen**: `config/taxonomy.yaml`, nur `categories:` anpassen.
3. **Seeden**: Start-Papers in `papers.yaml` (echte URLs!).
4. **Pipeline**: `python scripts/pipeline.py`, validiert & generiert.
5. **Pushen**: CI validiert & deployed auf GitHub Pages.

> **Nie generierte Dateien von Hand editieren**, sie regenerieren sich aus `papers.yaml`.

<!-- notes:
TOBIAS — live zeigen. Wichtig: „Niemals generierte Dateien editieren“ (README.md,
docs/papers.json, reports) — sie werden regeneriert. Das ist “Lösche & Regeneriere”.
YAML-Beispiel Schritt 2: `categories: - id: agentic-ai` (id + name + description).
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Wie der Agent Ihre Forschung unterstützt

| Agentische Aufgabe | Werkzeug im Repo |
|--------------------|------------------|
| Neue Papers entdecken | Discovery: arXiv, OpenAlex, dblp, Crossref, EUPMC + Code-Hosts |
| Dem Topic zuordnen | automatische Taxonomie-Zuordnung |
| Validiert halten | `validate_papers.py`: echte URLs, Schema, keine Erfindungen |
| README & Berichte | `generate_readme.py`, `generate_reports.py` |
| Trends & Zeitgeist | `trend_scanner.py`, `landscape_analyzer.py`, `topic_planner.py` |
| Kurz-Briefings | `brief_generator.py` |

> **Sie kuratieren, der Agent erledigt das Rauschen.** CI hält den Corpus gesund: wöchentlich ein Discovery-PR (Änderungsvorschlag).

<!-- notes:
TOBIAS — das ist der eigentliche Wert: nicht das Repo selbst, sondern dass der
Agent die Pflege (Discovery, Validierung, Trends) übernimmt, während der Mensch
die Qualität kuratiert. Der Mensch bleibt in der Verantwortung.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## AGENTS.md: der Contract für den Agenten

```yaml
# AGENTS.md (Auszug)
- NEVER edit README.md — it is auto-generated from papers.yaml.
- NEVER edit docs/papers.json, statistics.json or docs/research/*.md by hand.
- NEVER invent papers; every entry MUST have a real, resolvable URL.
- After ANY papers.yaml change, ALWAYS re-run the full pipeline.
- Validate (exit 0) before committing.
```

<div class="unix"><strong>Die Spec ist der Vertrag.</strong> Der Agent wird nicht im Prompt
gefragt, sondern per Datei geführt: stabil, wiederholbar, review-bar.
Zuwiderhandlungen deckt die Pipeline objektiv auf.</div>

<!-- notes:
TOBIAS — AGENTS.md = die "Contract"-Ebene der Pyramide. Kein Gespräch pro Session,
kein Wiedereinlernen — die Regeln liegen im Repo. Die Pipeline erzwingt sie.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

# Spezifikation und Token

## Präzise Verträge schreiben, sparsam mit Kontext umgehen

<!-- notes:
CHRISTIAN und TOBIAS. Block 5, 10:45 bis 11:00, zwei Themen in einem Block.
Aufteilung: Christian der Spezifikationsteil, Tobias der Token-Teil. Das
Showcase-Beispiel ist kuerzbar, wenn die Zeit knapp wird.
Verbindung beider Haelften ausdruecklich benennen, sonst wirkt der Block
zusammengewuerfelt: Eine praezise Spezifikation ist selbst die wirksamste
Einsparung. Wer den Auftrag genau beschreibt, muss ihn nicht dreimal erklaeren.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Wo die drei Ebenen im Projekt liegen

| Ort | Was dort liegt | Rolle |
|-----|----------------|-------|
| `openspec/specs/` | das dauerhaft gültige Verhalten | **Spezifikation**: gilt, bis sie geändert wird |
| `openspec/changes/<name>/` | die eine Änderung, die gerade ansteht | **Vertrag**: genau das bekommt der Agent |
| `openspec/archive/` | alle abgeschlossenen Änderungen | **Begründung**: warum wurde das so entschieden |

> Der Agent liest nie das ganze Projekt, sondern den Vertrag.
> Das ist zugleich die wirksamste Einsparung an Kontext.

<!-- notes:
CHRISTIAN. Diese Folie wiederholt nicht die Pyramide, sondern zeigt, wo die drei
Ebenen als Dateien liegen. Der Zugewinn gegenueber vorhin ist die dritte Zeile.

(1) Erste Zeile, Spezifikation
    Was dort steht, gilt dauerhaft. Es wird nicht pro Sitzung neu verhandelt.

(2) Zweite Zeile, Vertrag
    Nur die Differenz. Nicht "baue mir ein Analysewerkzeug", sondern "ergaenze
    diese eine Auswertung, gemessen an diesem Kriterium".

(3) Dritte Zeile, Archiv
    Der fuer Forschende interessanteste Teil und der am haeufigsten unterschaetzte.
    Abgeschlossene Aenderungen bleiben mitsamt Begruendung liegen. In einem halben
    Jahr ist die Frage "warum haben wir das so gerechnet" noch beantwortbar. Das
    ist Methodendokumentation, die nebenbei entsteht.

(4) Ueberleitung zum Token-Teil von Tobias
    Der Schlusssatz ist die Bruecke: Ein praeziser Vertrag ist zugleich die
    wirksamste Einsparung, weil er Wiederholung ersetzt.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Zwei Schulen: Spec-Kit und OpenSpec

| | **Spec-Kit** | **OpenSpec** |
|---|---|---|
| Grundidee | beschreiben, **was gebaut** werden soll | beschreiben, **wie sich Bestehendes ändert** |
| Typischer Fall | Neubau, neue Funktionen | laufende Weiterentwicklung |
| Quelle der Wahrheit | eine Spezifikation je Vorhaben | eine dauerhafte Spezifikation plus Änderungen |
| Ablauf | specify · clarify · plan · tasks · implement | new change → instructions → validate → archive |
| Aufwand | höher, dafür mehr Prozessführung | niedriger |

> **Neues Vorhaben: Spec-Kit. Bestehendes System, das wächst: OpenSpec.**
> Wir bearbeiten heute ein bestehendes Repository, deshalb OpenSpec.

<!-- notes:
CHRISTIAN. Diese Folie beantwortet vorab die Frage, warum ausgerechnet OpenSpec.
Ohne sie wirkt die Werkzeugwahl beliebig. Kurz halten, es geht um die Denkweise,
nicht um einen Werkzeugvergleich.

(1) Der eigentliche Unterschied in einem Satz
    Spec-Kit denkt in Vorhaben, OpenSpec denkt in Aenderungen. Beides ist
    spezifikationsgetrieben, der Zuschnitt ist verschieden.

(2) Spec-Kit
    Pro Funktion ein eigener Satz Dokumente: Spezifikation, Plan, Aufgaben. Das
    traegt sehr gut, solange ein System entworfen wird. Der Preis zeigt sich
    spaeter: Nach fuenfzig Vorhaben liegen fuenfzig Momentaufnahmen vor, und die
    Frage, welche davon den heutigen Zustand beschreibt, ist nicht mehr leicht
    zu beantworten.

(3) OpenSpec
    Eine dauerhafte Spezifikation, daneben Aenderungen als Differenz, ausgewiesen
    als ADDED, MODIFIED oder REMOVED. Nach dem Abschluss wandert die Aenderung in
    die Hauptspezifikation. Das entspricht einem Versionsverlauf: aktueller
    Zustand, Differenz, neuer Zustand.

(4) Analogie fuer den Raum
    Spec-Kit ist das Architekturdokument je Bauabschnitt. OpenSpec ist die
    Migration mit vorher festgelegtem Schema-Unterschied. Wer lieber ein Bild
    aus der Forschung will: einmal das Studienprotokoll je Teilstudie, einmal das
    fortgeschriebene Handbuch mit Aenderungsnachweis.

(5) Praktische Empfehlung, falls gefragt wird
    Beides schliesst sich nicht aus. Wer ein Vorhaben neu aufsetzt, faehrt mit
    Spec-Kit komfortabler, weil es mehr fuehrt. Wer ein bestehendes Repository
    laufend umbaut, empfindet OpenSpec als leichter. Der Hauptgewinn von OpenSpec
    ist, dass die Frage "welche Spezifikation gilt eigentlich noch" gar nicht
    erst entsteht.

(6) Bezug zur Uebung
    In Anwendung 2 wird OpenSpec verwendet, weil dort ein bestehendes Repository
    weiterentwickelt wird. Das ist der Grund, kein Werturteil.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## OpenSpec-Showcase: ai-literacy-research

**Ein live implementierter Change steht bereit**, im Repo `ai-literacy-research`.

- **Corpus**: 9.600+ Papers, 20 Kategorien, lebende systematische Übersicht.
- **OpenSpec-Struktur** am echten Beispiel:
  - `openspec/specs/`: paper-corpus · discovery-pipeline · analysis-reporting (Source of Truth)
  - `openspec/changes/archive/2026-08-23-add-research-gap-analysis/`: proposal → design → specs → tasks
  
> Gap-Score = **0.6 × Dünne (thinness) + 0.4 × Momentum + Floor-Bonus**
> → rankt Bereiche mit wenig Literatur und starkem Wachstum.

<!-- notes:
TOBIAS — der fertige Change als Referenz für den Hands-on-Block 6. Die Teilnehmenden
sehen eine echte, vollständige Spec/Change/Tasks-Struktur und können sie nachbauen.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Weniger Token, gleiche Qualität

> Praktisch gemessen: **3–5× weniger Token** bei gleicher Ergebnisqualität, zwei Hebel.

<div class="columns smaller">
<div>

**Routing**: das richtige Modell pro Aufgabe
- omO: benannte Agents → Modell je Kategorie.
- SAIA-Aliase: `best-for-coding`, `budget`, `fastest`.

**Caching & Kontext-Hygiene**
- Prompt-/KV-Caching, Kompaktion: nur behalten, was zählt.

</div>
<div>

<div class="unix"><strong>Klein ist schön.</strong> Ein kleines Modell für eine kleine Aufgabe.
Nicht jede Aufgabe braucht den größten Verstand.</div>
<div class="unix"><strong>Komponiere, nicht wiederhole.</strong> Skills & Specs vorschreiben,
statt in jeder Session alles neu zu erklären.</div>
<div class="unix"><strong>Speichere Wissen, nicht Prompt-Stücke.</strong>
pi-memory / Knowledge Graph persistieren Erfahrung außerhalb des Kontexts.</div>

</div>
</div>

<!-- notes:
TOBIAS — Block 5 · ~7 min: 4 min Routing (Live: SAIA-Alias-Wahl für dieselbe
Aufgabe — best-for-coding → Qwen3-Coder-Next, best-for-agentic → GLM 4.7,
budget → DeepSeek V4 Flash; omO: Sisyphus/Prometheus/Oracle je Kategorie),
2 min Caching/Kontext-Hygiene (kleiner, präziser Kontext = weniger Wiederholung),
1 min Prinzipien → Brücke zu Anwendung 2 („Ihre Spec ist auch Token-Optimierung:
der Contract ersetzt Wiederholung"). Glossar: KV-Cache = Modell merkt sich
Kontext-Berechnungen über Schritte; Kompaktion = alten Kontext zusammenfassen/verwerfen.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-christian">👤 Christian Uhl</div>

# Anwendung 2: Ihre eigene Spezifikation

## Von einem Satz zu einer überprüften Änderung

<!-- notes:
CHRISTIAN. Block 6, 11:00 bis 11:25, Christian fuehrt, Tobias unterstuetzt am Platz.
Praktische Uebung im eigenen Research-Repository aus Anwendung 1.
Vor dem Start ansagen, dass niemand fertig werden muss. Ziel ist, die Struktur
einmal selbst geschrieben zu haben, nicht ein fertiges Werkzeug.
Beide Referenten gehen durch den Raum. Erfahrungsgemaess scheitert der Einstieg
seltener am Verstaendnis als an der Installation.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Übung 2: Ihre eigene Auswertung

- **Ziel**: eine überprüfbare Anforderung und eine Aufgabenliste dazu.
- **Klein halten**: eine Auswertung, eine Kennzahl. Nicht das ganze Vorhaben.
- **Fertig heißt**: die Prüfung läuft durch. Nicht: der Agent meldet Vollzug.

```bash
npm install -g openspec            # falls noch nicht vorhanden
openspec new change trend-auswertung
openspec validate --changes        # entscheidet, ob es zählt
```

> **Ohne OpenSpec** genauso möglich: dieselbe Struktur als Markdown-Datei.

<!-- notes:
CHRISTIAN. Der haeufigste Zeitfresser in diesem Block ist die Installation, nicht
die Aufgabe. Deshalb steht der Ausweg auf der Folie und nicht nur im Kopf.

(1) Vor dem Start
    Kurz abfragen, bei wem openspec laeuft. Wer es nicht installiert bekommt,
    arbeitet sofort mit der Markdown-Variante weiter, ohne Wartezeit.

(2) Waehrend der Uebung
    Beide Referenten gehen durch den Raum. Haeufigster inhaltlicher Fehler: zu
    grosser Zuschnitt. Gegenfrage, die fast immer hilft: Woran wuerden Sie
    merken, dass es falsch ist?

(3) Referenz
    Der fertige Change add-research-gap-analysis in ai-literacy-research liegt als
    Vorlage bereit und darf abgeschrieben werden.

(4) Am Ende
    Zwei oder drei kurze Ergebnisse einsammeln, die im naechsten Block gezeigt
    werden. Freiwillige jetzt ansprechen, nicht erst nach der Pause.
-->

---

<div class="speaker speaker-christian">👤 Christian Uhl</div>

## Übung 2: Woran Sie Ihr Ergebnis messen

| Ebene | Mindestziel | Vollständig |
|-------|-------------|-------------|
| **Spezifikation** | ein Satz, der widerlegt werden kann | Szenario mit Ausgangslage, Eingriff, erwartetem Ergebnis |
| **Vertrag** | eine Aufgabenliste mit drei Punkten | Vorschlag, Entwurf, Spezifikation, Aufgaben |
| **Tests** | eine Prüfung, die fehlschlagen könnte | die Prüfung läuft automatisch und besteht |

> **Erledigt ist, was die Prüfung besteht.**
> Wer nur das Mindestziel erreicht, hat die Methode trotzdem verstanden.

<!-- notes:
CHRISTIAN. Bewusst zweistufig. Bei fuenfundzwanzig Minuten erreicht ein Teil des
Raums die rechte Spalte nicht, und das ist kein Scheitern.

(1) Mindestziel ansagen, bevor gearbeitet wird
    Wer die linke Spalte erreicht, hat die Struktur verstanden. Das nimmt Druck
    und erhoeht erfahrungsgemaess die Zahl derer, die ueberhaupt anfangen.

(2) Die linke Spalte der ersten Zeile ist der eigentliche Lerninhalt
    Ein Satz, der widerlegt werden kann. Wer das hinbekommt, hat den Kern der
    Methode verstanden, auch ohne eine einzige Zeile Code.

(3) Dritte Zeile erklaeren
    Eine Pruefung, die nicht fehlschlagen kann, prueft nichts. Das ist derselbe
    Gedanke wie bei einem Experiment ohne moegliches Negativergebnis.

(4) Schlusssatz stehen lassen
    Er kommt aus der Pyramide und wird im Wrap-Up erneut aufgegriffen.
-->

---

<!-- _class: lead -->


# ☕ Pause

5 Minuten.

<!-- notes:
Pause 11:25–11:30.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Outcomes: Ihre Ergebnisse

<!-- notes:
TOBIAS — Block 7 · 11:30–11:45 (15 min), Moderation. 3–4 Freiwillige präsentieren
à 3–4 min. Mit der stärksten Demo starten. Zeit hart timen: bei 3 min Warnsignal.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Outcomes: das zeigen wir

- **3–4 Freiwillige**, je 3–4 min: eigenes Research-Repo + eigener Mini-Change.
- Live-Demo oder Screenshot, Hauptsache **Pipeline grün, Change validiert**.
- Bewertung an der Pyramide: ein SHALL-Satz (Spec), ein Change (Contract), ein grüner Check (Test).

> Das Publikum reviewed mit: Was würde die Pyramide an Ihrem Projekt bemängeln?

<!-- notes:
TOBIAS — Ergebnis-Kriterien wie in Übung 2. Wünsche aus der Vorstellungsrunde
aufgreifen: „Hat das jemand von Ihnen angestoßen?“
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Q&A · Diskussion · Wrap Up

<!-- notes:
TOBIAS — Block 8 · 11:45–12:00 (15 min), Moderation. Offene Fragen, Diskussion,
Wrap-Up — Wünsche aus der Vorstellungsrunde Revue passieren lassen.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Das Muster auf eigene Projekte übertragen

1. **Klein starten**: eine Spec für ein vorhandenes Modul (Given/When/Then).
2. **Delta-Specs nutzen**: erster Change mit 3 Tasks → Agent implementieren lassen.
3. **Verifikation erzwingen**: Tests + CI als Pflicht: Agenten iterieren, bis grün.
4. **Wissen persistieren**: pi-memory / Knowledge Graph ab Session 1, nicht in Prompt-Stücken.
5. **Loop institutionalisieren**: Betriebserkenntnisse werden neue Changes (Spec evolves).

> Die **Pyramide** ist überall: papers.yaml=Spec · Pipeline=Contract · CI=Test.

<!-- notes:
TOBIAS — jeder Block des Workshops folgte derselben Pyramide — auch OpenSpec.
Jetzt aufs eigene Projekt übertragen.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Resources

<div class="columns smaller">
<div>

- **OpenCode**: github.com/sst/opencode
- **pi**: pi.dev · @earendil-works/pi-coding-agent
- **zot**: zot.sh · github.com/patriceckhart/zot
- **OpenSpec**: npmjs.com/package/openspec
- **SAIA Accelerator**: codeberg.org/graphwiz-ai/opencode-saia-plugin
- **oh-my-opencode**: github.com/code-yeongyu/oh-my-opencode

</div>
<div>

- **skeleton-research**: github.com/tobias-weiss-ai-xr/skeleton-research
- **ai-literacy-research**: github.com/tobias-weiss-ai-xr/ai-literacy-research
- **Superpowers**: github.com/obra/superpowers
- **rtk**: github.com/rtk-ai/rtk
- **ponytail**: github.com/DietrichGebert/ponytail · **caveman**: github.com/JuliusBrussee/caveman

</div>
</div>

<!-- notes:
Links können als QR-Code oder Handout ergänzt werden.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Questions & Discussion

Vielen Dank!

> Materialien & Folien: dieses Repo. Fragen danach gern als GitHub-Issue.

Diskussionsthemen:
- Wo liegt das größte Potenzial, und wo die größte Skepsis?
- Governance-Regeln für agentische Systeme?
- Eigene Modelle auf lokaler Hardware (Souveränität)?
- Agentische Literatur-Reviews für Ihre Forschung?

<!-- notes:
TOBIAS — Moderation: Erfahrungsaustausch & Anwendungsfälle aus Teilnehmenden-Perspektive.
-->

---

# License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Christian Uhl · Tobias Weiß, except where otherwise noted.
