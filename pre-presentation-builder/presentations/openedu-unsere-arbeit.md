---
marp: true
theme: default
paginate: true
footer: 'openEDU · Souveräne Workplace-Suite · Uni Marburg'
style: |
  section {
    background-color: #1a1a1a;
    color: #e8e8e8;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    padding-bottom: 64px;
  }
  section.smaller table { font-size: 18px; }
  section.smaller table th, section.smaller table td { padding: 4px 8px; }
  h1, h2, h3 { color: #ffffff; font-weight: 700; }
  table { margin: 0 auto; font-size: 22px; border-collapse: collapse; }
  table th, table td {
    background-color: #2a2a2a; padding: 6px 11px;
    border: 1px solid #555; color: #e8e8e8;
  }
  table thead th {
    background-color: #383838; color: #ffffff; border-bottom: 2px solid #666;
  }
  table tbody tr:nth-child(even) td { background-color: #252525; }
  .speaker {
    position: absolute; top: 32px; right: 40px;
    padding: 6px 16px; border-radius: 20px; font-size: 18px;
  }
  .speaker-tobias { background: #1a2f52; color: #8ab8ff; border: 1px solid #3b6fc4; }
---

<!-- _class: lead -->

# openEDU — unsere Arbeit

## Souveräne digitale Dienste für Forschung, Lehre und Verwaltung

Tobias Weiß · DevOps, Universität Marburg

Stand: September 2026

<!-- notes:
Kurzer Rahmen (1 min): openEDU = Bildungsvariante der souveränen
Workplace-Suite openDesk. Ein Betrieb für drei Zielgruppen:
Forschung, Lehre, Verwaltung. Diese Folie nur als Anker stehen lassen.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Warum souverän, warum wir

- Mail, Chat, Files, Wiki, Projekte: digitale Grundversorgung wie Strom und Wasser.
- Souveränität ist keine Haltung, sondern Betrieb — sie entsteht an Ingress, Secrets und Datenbanken.
- Die Basis heißt openDesk, die Bildungs-Schicht openEDU: Wir erben die Suite — Tenants, HRZ, Groupware bleiben unsere Arbeit.

> Souveränität entscheidet sich nicht auf Folien, sondern im nächsten Deployment-Commit.

<!-- notes:
These (2 min): Was hier "unsere Arbeit" heißt: Betrieb + Anpassung einer
großen Open-Source-Suite unter Universitätsbedingungen. Betonung:
Souveränität ist für uns kein Marketingwort, sondern ein Betriebsthema —
jede der folgenden Folien zeigt konkrete Arbeit dahinter.
-->

---

<!-- _class: smaller -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Die Suite: acht Bausteine, ein Login

| Baustein | Dienst | Rolle im Alltag |
|---|---|---|
| Identität | **Keycloak** | Single Sign-On für alles |
| Wiki | **XWiki** | Dokumentation, Wissensbasis |
| Files | **OpenCloud** | Speicher, Zusammenarbeit |
| Groupware | **SOGo** | Mail, Kalender, Kontakte |
| Chat | **Matrix / Synapse** | asynchrone Kommunikation |
| Projekte | **OpenProject** | Planung, Tickets |
| Videokonferenz | **Intercom / Jitsi** | Lehr- und Besprechungsräume |
| Portal | **collab-dashboard** | ein Einstieg für alle Dienste |

> Ein Login, acht Dienste — dieser eine Satz ist unsere Baustelle.

<!-- notes:
Diese Folie erklärt, warum SSO der zentrale Baustein ist: 8 Dienste,
die alle dasselbe Identitätsversprechen halten müssen. Das ist der
Übergang zur Architektur- und SSO-Folie. Komponenten wie im Cluster
im Einsatz (Client-Namen: xwiki, openproject, intercom, matrix,
opendesk-opencloud, sogo-Familie, home-portal, admin-home-portal).
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Architektur: GitOps mit Erbe

- Der Cluster ist deklariert: Kubernetes (SCS) mit ArgoCD — Abweichungen werden sichtbar.
- openDesk CE läuft als Git-Submodul; der Upstream-Sprung ist eingespielt.
- Darüber die Uni-Schicht mit eigenen Commits für Helmfiles und Umgebungen.
- MariaDB/Galera und HAProxy — unspektakulär und kritisch.

> Upstream mitführen statt forken: der Verschnitt bleibt klein genug für das monatliche Upgrade.

<!-- notes:
Kernbotschaft: Wir pflegen einen sauberen Drei-Schicht-Stapel —
Upstream-CE (Submodul), Uni-Anpassungen (umr-edu), Betrieb (ArgoCD).
Reconciliation 2026-08-20: 99 umr-edu + 62 Upstream-Commits integriert.
Wer Details will: Galera via ClusterIP statt ExternalName (Flannel-Routing-
Workaround), Ingress über HAProxy. Diese Folie bewusst ohne Diagramm —
die Schichten stehen im Text.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## SSO: das Herzstück, konsolidiert

- Ein Realm (`opendesk`) trägt alle Dienste: jeder OIDC-Client e2e verifiziert, jede Prüfung grün.
- Home- und Admin-Portal laufen über oauth2-proxy unter `home.openedu.graphwiz.ai`.
- Logout je Client-Typ gelöst; native Clients gehen eigene Wege.
- Sessions dauern einen Uni-Tag — der Logout-Knopf entscheidet, nicht der Timer.

> „Ein Login für alles" war ein Versprechen — jetzt ist es eine Test-Suite.

<!-- notes:
Zeitstrahl: 2026-08-24 Realm-weite Client-Scopes repariert (vorher nur
offline_access), Logout-Wiring aller Dienste. 2026-09-10: alle 15 Clients
e2e (tests/sso/test-sso-e2e.sh, 29 Checks). 2026-09-26: Portal-Konsolida-
tion auf openedu.graphwiz.ai + 18h-TTL. 2026-09-27: Tenant-Clients +
sso-test-User. Näher dran: SSO war über Monate der breite Graben zwischen
"Suite installiert" und "Suite nutzbar".
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Tests als Sicherheitsnetz

- Die SSO-Suite ist grün; jede Warnung ist ein dokumentierter Beschluss.
- Bei realen Ausfällen schlug der Portal-Login-Regressionstest zuerst an — vor jedem Nutzer-Ticket.

> Jede Warnung im Testlauf hat einen Beschluss. „Egal" existiert in der Suite nicht.

<!-- notes:
tests/sso/test-sso-suite.sh (2026-09-27: 59/0/6). Die 6 Warnungen:
frontchannel-logout fehlt auf NATIVE-Clients opendesk-opencloud,
matrix, intercom, sogo — die haben eigene Mechanismen (sogo6-api-*-
Clients, Intercom-Backchannel). Die beiden Outages 09-05/09-06: Der
e2e-Portal-Login-Test war der Erste, der rot wurde.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Betrieb ist Debugging

- **Keycloak im CrashLoop.** Ein DB-Hostname löste falsch auf — behoben mit ClusterIP statt ExternalName.
- **503 auf dem Portal.** Eine Egress-Policy blockte Keycloak, ein zweiter Ingress konkurrierte — Ursachen getrennt, Regeln verfeinert.
- **oauth2-proxy rot.** Veraltetes Secret im Pod, Cookie-Secret im falschen Format — Secret-Management verschärft.

> Jeder gefundene Fehler wird ein Test, bevor er wiederkommt.

<!-- notes:
Drei echte Incidents (alle 2026-09, alle vollständig resolved):
1) KC_DB_URL über ExternalName/Flannel-Routing-Problem.
2) Egress-Netpol + Double-Ingress — klassisches Zusammenspiel zweier
harmloser Änderungen.
3) oauth2-proxy: home-client-secret war im Pod-Stand alt (Env-Snapshot),
Cookie-Secret Hex-Bug. Kernbotschaft ist der Merksatz: Test nach jedem
Incident — so ist die SSO-Suite überhaupt entstanden.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Multi-Tenancy: zwei Welten, ein Cluster

- Die Tenants `opendesk-staff` und `opendesk-students` — getrennte Namespaces, eigene SSO-Clients.
- SOGo6 je Tenant; Admin-Passwörter leben nur im Cluster, nie im Git.
- Tenants sind Kundenumgebungen, keine Plattform — deshalb bewusst außerhalb von ArgoCD geführt.

> Ein Cluster, zwei Zielgruppen, klare Trennung — Staff zuerst, Studierende folgen.

<!-- notes:
2026-08-27: sogo6-admin-Secrets in beiden Tenants (OOTB, Passwort nur im
Cluster). Tenants bewusst NICHT ArgoCD-managed — Entscheidung gegen
ApplicationSet, weil Tenant-Lebenszyklen sich anders verhalten als
Plattform-Deployments. Git-Kustomization war anfangs broken (c93cc00),
Cluster-Ops danach fertig.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Groupware-Pflege: SOGo unter HRZ-Bedingungen

- SOGo bauen wir aus dem Source — Security-Updates nachziehen ist Routine.
- Der Fallstrich: Patches aus der Vorversion crashen den neuen Build — alte Patches raus, Image neu taggen.
- Parallel wächst die sogo6-Familie für die Tenants.

> Security-Rebuilds sind bei uns kein Ausnahmezustand, sondern ein Monatsthema mit Test.

<!-- notes:
2026-09-24: SOGo 5.12.11 Source-Build (vhrz2392, /opt/sogo5-test).
Die 5.11-Ära-Dateien (SOGoSieveManager.m, UIxComponent.m,
SOGoSystemDefaults.m) mussten raus — jede Request crashte den sogod.
Fazit fürs Publikum: Inhouse-Forks tragen Zinsen in Form von
Rebuild-Arbeit; die kalkulieren wir ein, statt uns zu wundern.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Außenwirkung: Websites, Branding, Konsolidierung

- openEDU- und openSME-Website: Next.js, mehrsprachig, Blog zu Backup und Betrieb.
- Der komplette Web-Stack läuft auf einer Maschine; Traefik übernimmt die Redirects der Alt-Hosts.
- Eigene Marken — `openedu.graphwiz.ai` und `opensme.graphwiz.ai`; in den eigenen Sites bleibt keine Fremd-Referenz.

> Auch die Website ist Infrastruktur: deploybar, getestet, konsolidiert.

<!-- notes:
2026-09-25: kompletter Web-Stack auf v77986 (Traefik v2 File-Router,
Legacy-Redirects der 1blu-vHosts). De-Branding-Sweep auf Wunsch: github/codeberg-Links und openDesk-Referenzen aus eigenen
Sites raus, übrig blieb nur der externe Matrix-Raum #opendesk. Website: Next.js App
Router, next-intl (de/en/fr/zh), Vitest; Blog-Artikel u. a. Backup (k8up).
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Die Schwester: openSME mit Rust/Go-Stack

- Gleiche Methode, andere Zielgruppe: Mittelstand statt Universität.
- Der Stack besteht aus gepflegter Fremd-Software: Kanidm (IdP) · Stalwart (Mail) · Conduit (Matrix) · Garage (Objekte) · ocis · Vikunja · LiveKit · Forgejo · Caddy.
- Jedes Bauteil baut aus dem Source — grün und lizenzklar.

> „Rust-basiert“ heißt bei uns: fertige, gepflegte Software wählen — nie einen eigenen Identitätsdienst schreiben.

<!-- notes:
Entscheidung 2026-09-09 (Ponytail-Architektur): Security-Kern nicht
selbst schreiben. Kanidm als IdP, Stalwart statt Dovecot-Stack, Garage
statt S3-Fremddienst. Diese Folie kurz halten — sie zeigt Reichweite
der Methode, openSME ist eigene Story.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Agentic AI im openEDU-Betrieb

- Die Upstream-Reconciliation aus beiden Richtungen lief als Agenten-Fleet mit exakten Abnahmekriterien.
- Test-Suiten entstanden in Agenten-Batches; jedes Ergebnis ist verifizierbar.
- Vor jeder Ausführung steht die Spezifikation: OpenSpec-Changes, dieselbe Pyramide wie im Workshop — Spec · Contract · Test.

> Die Agenten arbeiten mit uns am Betrieb — aber die Testsuite entscheidet, nicht der Agent.

<!-- notes:
Brücke zum Agentic-AI-Workshop: Dieselbe Methode (Spec-Driven,
Task-Fleets, Verifikation statt Vertrauen) trägt hier echten Betrieb.
Reconciliation 2026-08-20, SSO-Suite-Bau via taskfleet (Batches mit
Acceptance-Gates). openEDU-spec-Repo: openspec/changes + docs.
Kernsatz ist der Merksatz — deckt sich mit der Workshop-These.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Bilanz — und was als Nächstes kommt

- Stabil: Portal, SSO für alle Clients, Test-Suiten grün, Web-Stack konsolidiert.
- In Arbeit: DNS-Flip auf die neuen Domains, Rollover der Studierenden-Tenants.
- Danach: openSME-Übertragung, Security-Rebuilds im Monatsrhythmus.

> Eine Suite ist nie fertig. Im Betrieb zu sein — das ist das Ergebnis.

<!-- notes:
Offene Punkte ehrlich benennen: DNS-Cutover auf openedu.graphwiz.ai
steht aus (Stand 2026-09-26), danach Legacy-Hosts ablösen. Abschluss-
satz langsam sprechen. Danach: Q&A oder Rückführung in den
Workshop-Kontext, je nach Publikum.
-->

---

<!-- _class: lead -->

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

# Vielen Dank!

Fragen am besten als Issue — Repo und Kontakt über `openedu.graphwiz.ai`.

<!-- notes:
Kontakt-Zeile ggf. anpassen. Vielen Dank!
-->
