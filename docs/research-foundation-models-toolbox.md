# Recherche: Foundation Models & Toolbox — IT4Science Days 2026

> Stand: August 2026 · Quelle: lokale Repos (pi, OpenCode, oh-my-opencode, zot, SAIA,
> skeleton-research, dev-agent, predictive-agent), pi-Doku, SAIA-Modellkatalog,
> oh-my-opencode-Features, agent-*-research-Corpora.
>
> **Korrektur 09/2026 (wissenschaftliche Prüfung):** SAIA-Katalog = Open-Modelle
> (GLM 4.7, Qwen3.8, Qwen3-Coder-Next, DevStral 2, DeepSeek V4 Flash, Llama 3.1 8B;
> Routing-Aliase `best-for-*`/`budget`/`fastest` laut SAIA-Plugin-opencode.json).
> OpenCode: kein LiteLLM-Routing, kein "30+ parallele Agents" belegt — AST-Grep/
> Background-Agents stammen aus dem omO-Plugin ("5+ parallel").
> zot = zot.sh (patriceckhart/zot): Go-Single-Binary, TUI+JSON-RPC, MCP,
> Ollama/llama.cpp. Update 09/2026: SAIA-Plugins existieren für alle drei Harnesses
> (pi-saia-plugin · opencode-saia-plugin · zot-saia-plugin, repos siehe README-Links).

---

## 1. Foundation Models — aktuelle Entwicklungen (Block: Christian + Tobias, 20 min)

### Modell-Landschaft (über SAIA academic cloud + pi-Katalog, Stand 08/2026)

| Modell | Klasse | Kontext | Bemerkung |
|--------|--------|---------|-----------|
| Claude Opus 4.6 / Sonnet 4.6 / Haiku 4.5 | proprietär, reasoning | 200K–1M | Adaptive Thinking, strict tools, agentic |
| GPT-5.4 / 5.6 (Sol/Terra/Luna) / 5-nano | proprietär, reasoning | 272K–1.05M | Multimodal, Grammar-Tools, Prompt-Caching-Tiers |
| Gemini 3.1 Pro / Gemma 4 (31B) | proprietär / open | 262K–1M | Multimodal, lange Kontexte |
| **Qwen 3.5 397B-A17B** | open weights, MoE | 131K | 397B gesamt, 17B aktiv — Reasoning |
| Qwen 3.6 35B-A3B / 27B | open weights, MoE | 131K | Kleine aktive Parameter → effizient |
| Qwen3-Coder-Next | open weights, coder | 131K | Coding-spezialisiert |
| Qwen3-Omni 30B-A3B | open weights, vision | 32K | Multimodal (Text+Bild) |
| GLM 4.7 / GLM 5 | open weights, agentic | 131K | Z.AI, starkes Tool-Using |
| DeepSeek V4 Flash | open weights, general | 131K | Reasoning, konkurrenzfähig |
| DevStral 2 (123B) | open weights, agentic | 131K | Mistral, coding-orientiert |
| Mistral Medium 3.5 (128B) | open weights, agentic | 131K | General + tool use |
| GPT-OSS 120B | open weights | 131K | Open-Weights-GPT |
| Llama 3.1 8B / Apertus 70B | open weights, klein | 32–131K | Lokal, Ollama-tauglich |
| Kimi K2.5 | proprietär, coding | 262K | Lange Kontexte, Coding |
| Grok Code Fast 1 | proprietär, coder | — | Schnelle Codebase-Exploration |
| MiniMax M2.7 | proprietär | — | Docs/Library-Analyse |

### Ranking der Themen (nach Workshop-Relevanz für IT4Science)

| Rang | Thema | Warum relevant |
|------|-------|----------------|
| **1** | **MoE & Open-Weights-Surge** | Qwen 397B/17B aktiv, GPT-OSS, GLM, DeepSeek — open weights konkurrieren mit proprietär. Kern für IT4Science (Souveränität, lokale/HPC-Deployment). |
| **2** | **Reasoning / Test-Time-Compute** | Thinking-Levels (off→max), adaptives Denken, System-2. Größter Capability-Sprung; pi/OpenCode steuern `reasoning_effort` pro Modell. |
| **3** | **Lange Kontexte & Prompt-Caching** | 1M-Token-Fenster (GPT-5.6), KV-Cache, Cache-Retention (1h). Direkter Kosten-/Latenz-Hebel für lange Agent-Sessions. |
| **4** | **Coding-spezialisierte Modelle** | Qwen3-Coder-Next, DevStral 2, Grok-Code. Direkt relevant für den Workshop (agentisches Programmieren). |
| **5** | **Lokale & souveräne Modelle** | Ollama, vLLM, LM Studio, GPT-OSS, Llama. Daten verlassen nicht das Haus — IT4Science-Kernanliegen. |
| **6** | **Modell-Routing & Multi-Model-Orchestrierung** | Kategorie-basierte Delegation (oh-my-opencode: Sisyphus/Hephaestus/Oracle/Librarian/Explore). Brücke zum Toolbox-Block. |
| **7** | **Multimodal** | Qwen-Omni, Gemini, GPT-5.4 — Vision in Agenten. Aufsteigend, aber nachrangig für Coding-Workshop. |

### Schlüsseltrends 2026→2027
- **MoE als Standard**: Große Gesamt-Parametrisierung, kleine aktive Parameter → Effizienz bei Capability.
- **Adaptive Thinking**: Modelle steuern eigenen Reasoning-Aufwand (`thinking.type: adaptive`).
- **Cache-Hierarchien**: Prompt-Cache (Anthropic 1h, OpenAI 24h), KV-Cache → Agent-Sessions bezahlbar.
- **Open-Weights-Hochlauf**: Qwen, GLM, DeepSeek, GPT-OSS, Llama — lokale Deployment-Qualität nähert sich Cloud-Niveau.
- **Grammar-Tools / Strict-Mode**: Strukturierte Tool-Ausgaben (Lark/Regex-Grammar) — weniger Halluzinationen in Tool-Calls.

---

## 2. Toolbox — Harnesses & agentic Tooling (Block: Tobias + Christian, 20 min)

### Die Harness-Ebene (Steuerung über dem Modell)

| Tool | Rolle | Stoic-Unix-Signatur |
|------|-------|---------------------|
| **pi** | Minimaler Terminal-Coding-Harness; Skills/Extensions/Prompt-Templates; Multi-Provider; Session-Branching/Compaction | "No MCP, no sub-agents, no plan-mode, no built-in to-dos" — do one thing, compose |
| **OpenCode** | Agentischer Coding-Terminal; Multi-Model (Provider/Modell je Agent); LSP; Plugins, Skills, MCP | CLI-first, erweiterbar |
| **oh-my-opencode (OmO)** | OpenCode-Plugin: Sisyphus/Prometheus/Oracle/Librarian/Explore/Hephaestus; Background Agents ("5+ Spezialisten parallel"); Ralph Loop; Kategorie-basierte Modell-Delegation; Hash-Anchored Edits; AST-Grep (25 Sprachen); LSP; eingebaute MCPs | "Discipline Agent" — läuft bis 100% done |
| **Claude Code** | Kommerzielle Referenz (Anthropic) | Vendor-Lock-in-Vergleichsmaßstab |
| **zot** | Go-Single-Binary-Harness: TUI + JSON-RPC, Extensions, Slash-Commands, MCP; Ollama/llama.cpp-Anbindung ([zot.sh](https://www.zot.sh), patriceckhart/zot) | Lokale/souveräne Modellwahl |

### Tooling rund um den Harness

| Tool | Funktion |
|------|----------|
| **OpenSpec** | Spec-driven Development: `specs/` (Source of Truth) + `changes/` (Delta) + `archive/` (Decision Log) |
| **SAIA-Plugins** | pi-saia-plugin (auto-registriert alle SAIA-Modelle), opencode-saia-plugin, zot-saia-plugin |
| **skeleton-research** | Forkbares Corpus-Skeleton für agentic Literature Review (Taxonomie → Discovery → Validate → Reports → CI) |
| **dev-agent / opendesk-dev-agent** | Knowledge Graph (Neo4j) + Experience-Memory (pi-memory) per Slash-Command |
| **predictive-agent** | Predictive K8s-Health: Kalman-Filter, Markov-Chain, Bayes-Risk-Scoring |
| **MCP (Model Context Protocol)** | Standard für Tool-Schnittstellen; pi baut es bewusst nicht ein (Unix-Philosophie: CLI-Tools statt Protokoll-Lock-in) |
| **Skills-Standard (agentskills.io)** | Portable Capability-Packages; pi, OpenCode, Claude Code, Codex kompatibel |
| **pi-memory / Graphiti** | Experientielles Gedächtnis + Knowledge Graph über Sessions hinweg |

### Ranking der Toolbox-Themen

| Rang | Thema | Warum |
|------|-------|-------|
| **1** | **Harness-Konzept** | "Gleiche Modelle, unterschiedliche Ergebnisse je nach Steuerung" — der zentrale Gedanke |
| **2** | **pi** | Der Host-Agent dieses Workshops; minimal, komponierbar, Skills/Extensions |
| **3** | **OpenCode + oh-my-opencode** | Multi-Model, parallele Agenten, Ralph Loop, LSP/AST — der Workhorse |
| **4** | **zot + SAIA** | Akademische Cloud-Modelle für IT4Science — Souveränität in der Praxis |
| **5** | **OpenSpec** | Brücke zum Hands-on: Spec als Vertrag |
| **6** | **skeleton-research** | Brücke zum Hands-on: agentic Literature Review |
| **7** | **MCP & Skills-Standard** | Standardisierung vs. Unix-Philosophie (pi bewusst ohne MCP) |
| **8** | **Memory & Knowledge Graphs** | Cross-Session-Kontinuität (pi-memory, Graphiti) |

---

## 3. Stoic Unix Philosophy — verkörpert, nicht genannt

Die Werkzeuge und Beispiele im Workshop verkörpern die Philosophie durch ihre Taten:

- **Do one thing well**: pi ist ein „minimal terminal coding harness" — kein MCP, keine Sub-Agents, kein Plan-Mode eingebaut. Erweiterbar via Skills/Extensions.
- **Compose via text**: OpenSpec = Markdown-Specs; skeleton-research = `papers.yaml` + Taxonomie-YAML; alles textbasiert, git-diff-bar.
- **Generate, don't hand-edit**: skeleton-research: „Never edit README.md directly — it is auto-generated." Die Pipeline ist der Richter.
- **One config, one re-run**: `config/taxonomy.yaml` ändern → Pipeline laufen lassen → objektiver Pass/Fail.
- **The spec is the contract**: OpenSpec-Delta = der Agent-Prompt; keine Klärungsrunden.
- **Verify, don't trust**: CI validiert, `validate_papers.py` ist Gate; Agenten beschleunigen, Menschen verantworten.
- **Small, composable tools**: `validate_papers.py`, `generate_readme.py`, `standard_stats.py` — jedes Skript eine Aufgabe, verkettet zur Pipeline.

Auf den Folien wird die Philosophie nicht beim Namen genannt — die Struktur der Beispiele (ein Config-File, eine Pipeline, ein Spec-Vertrag, CI als Richter) macht sie sichtbar.
