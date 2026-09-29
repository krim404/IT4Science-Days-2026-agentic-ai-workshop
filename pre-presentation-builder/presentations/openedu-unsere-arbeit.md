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

- **Digitale Dienste als Infrastruktur** — Mail, Chat, Files, Wiki, Projekte: Grundversorgung wie Strom und Wasser.
- **Souveränität ist keine Haltung, sondern Betrieb** — DSGVO, Lizenzfreiheit und kontrollierte Datenflüsse entstehen durch Arbeit an Ingress, Secrets und Datenbanken.
- **openDesk als Basis, openEDU als Bildungs-Schicht** — wir erben die Suite, aber der Uni-Alltag (Tenants, HRZ, Groupware) bleibt unsere Aufgabe.

> Nicht die Folie entscheidet über Souveränität, sondern der nächste Deployment-Commit.

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

> Ein Login, acht Dienste — der Aufwand steckt in genau dieser Aussage.

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

- **Kubernetes (SCS k3s) + ArgoCD** — der Cluster ist deklariert, Drift wird sichtbar.
- **openDesk CE als Git-Submodul** — Upstream 1.16.2 → 1.18.0 (62 Commits Reconciliation).
- **Uni-Schicht darüber**: 99 umr-edu-Commits eigener Helmfile-/Umgebungslogik.
- **Basisdienste**: MariaDB/Galera, HAProxy-Ingress — unspektakulär und kritisch.

> Upstream mitführen statt forken: unser Verschnitt bleibt klein genug für jeden Monat Upgrade.

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

- **Ein Realm, alle Dienste**: Keycloak-Realm `opendesk`, 15 OIDC-Clients e2e verifiziert — 29 Checks, 0 Fehler.
- **Portal-Login über oauth2-proxy**: home-Portal und Admin-Portal laufen unter `openedu.graphwiz.ai`.
- **Logout sauber gelöst**: Front-/Backchannel je Client-Typ; Native-Clients (OpenCloud, Matrix, Intercom, SOGo) nutzen eigene Mechanismen.
- **Sessions für den Uni-Tag**: 18 h TTL statt 30 min Idle — Logout-Knopf entscheidet, nicht der Timer.

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

- **SSO-Suite**: 59 bestanden · 0 fehlerhaft · 6 Warnungen (dokumentiert und beabsichtigt).
- **Zwei reale Ausfälle sofort gefangen** — Portal-Login-Regressionstest schlug an, bevor Nutzer es gemeldet hätten.
- **Warnungen sind Design, nicht Schulden**: Native-Clients ohne Frontchannel-Logout stehen bewusst mit Begründung in der Suite.

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

## Betrieb ist Debugging: drei Storys

- **Keycloak im CrashLoop** — DB-Hostname `galera-headless` löste über ExternalName falsch auf → ClusterIP + CoreDNS-Loop behoben.
- **503 auf dem Portal** — Egress-NetworkPolicy blockte Keycloak-Verkehr + doppelter Ingress konkurrierte → Ursachen getrennt, Regeln verfeinert.
- **oauth2-proxy rot** — stale Secret im Pod + Cookie-Secret im falschen Format → Secret-Management verschärft.

> Das Muster: jeder gefundene Fehler wird ein Test, bevor er ein zweites Mal ein Fehler wird.

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

- **Tenants `opendesk-staff` und `opendesk-students`** — getrennte Namespaces, getrennte SSO-Clients.
- **SOGo6-Rollover je Tenant**: Admin-Secrets nur im Cluster, nie im Git.
- **Bewusst außerhalb von ArgoCD** — Tenants sind Kundenumgebungen, keine Plattform; Kustomizations je Tenant, kein ApplicationSet-Zwang.

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

- **SOGo 5.12.11 als Source-Rebuild** — HRZ-Inhouse-Basis, Security-Updates nachziehen ist Routine.
- **Der Fallstrich**: 5.11-Ära-Patches (`.m`-Quelldateien) crashen die 5.12.11 — alte Patches strippen, Image neu taggen.
- **Die sogo6-Familie** (inkl. `sogo6-api-*`-Clients) wächst parallel für die Tenants.

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

- **openEDU- & openSME-Website** — Next.js, vier Sprachen (de/en/fr/zh), Blog mit Backup-/Betriebsthemen.
- **Server-Konsolidierung**: kompletter Web-Stack auf einer Maschine, Traefik-File-Router übernimmt Redirects der Alt-Hosts.
- **Eigene Marke statt Fremd-Branding** — `openedu.graphwiz.ai` / `opensme.graphwiz.ai`, aufgeräumt bis auf externe Fakten.

> Auch die Website ist Infrastruktur: deploybar, getestet, konsolidiert.

<!-- notes:
2026-09-25: kompletter Web-Stack auf v77986 (Traefik v2 File-Router,
Legacy-Redirects der 1blu-vHosts). De-Branding-Sweep auf Wunsch:
github/codeberg-Links und openDesk-Referenzen aus eigenen Sites raus,
übrig blieb nur der externe Matrix-Raum #opendesk. Website: Next.js
App Router, next-intl, Vitest; Blog-Artikel u. a. Backup (k8up).
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Die Schwester: openSME mit Rust/Go-Blaupausen

- **Gleiche Methode, andere Zielgruppe**: Mittelstand statt Universität — der Stack ist bewusst anders gewählt.
- **Vorhandene Software statt Eigenbau**: Kanidm (IdP) · Stalwart (Mail) · Conduit (Matrix) · Garage (Objekt-Speicher) · ocis · Vikunja · LiveKit · Forgejo · Caddy.
- **Grüne Builds, klare Lizenzen** — jedes Bauteil muss aus dem Source bauen und bleiben.

> „Rust-basiert" heißt bei uns: fertige, gepflegte Software wählen — nie ein eigenes Identitäts-Binärprogramm schreiben.

<!-- notes:
Entscheidung 2026-09-09 (Ponytail-Architektur): Security-Kern nicht
selbst schreiben. Kanidm als IdP, Stalwart statt Dovecot-Stack, Garage
statt S3-Fremddienst. Diese Folie kurz halten — sie zeigt Reichweite
der Methode, openSME ist eigene Story.
-->

---

<div class="speaker speaker-tobias">👤 Tobias Weiß</div>

## Agentic AI im openEDU-Betrieb

- **Upstream-Reconciliation**: 161 Commits aus zwei Richtungen einsortiert — Agenten-Fleet mit exakten Acceptance-Gates.
- **Test-Suiten entstehen agentisch**: SSO-Suite und e2e-Checks wuchsen in Task-Batches, jedes Ergebnis verifizierbar.
- **Spezifikation vor Ausführung** — OpenSpec-Changes im openEDU-spec-Repo, gleiche Pyramide wie im Workshop: Spec · Contract · Test.

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

- **Stabil**: Portal, SSO für 15 Clients, Test-Suiten grün, Web-Stack konsolidiert.
- **In Arbeit**: DNS-Flip auf die neuen Domains, Tenant-Rollover für Studierende.
- **Nächst**: openSME-Übertragung, weitere Security-Rebuilds im Monatsrhythmus.

> Eine Suite ist nie fertig. Sie ist im Betrieb — und genau das ist der Beweis.

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
