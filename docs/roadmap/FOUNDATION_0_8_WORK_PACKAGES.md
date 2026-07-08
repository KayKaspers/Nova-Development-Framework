# Foundation 0.8 – Work Package Queue

> Status: **Scope locked** (NDF-WP-108, 2026-07-08). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_8_SCOPE_LOCK.md](FOUNDATION_0_8_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

## Queue

| ID | Titel | Typ | Ziel | Scope Lock |
|---|---|---|---|---|
| NDF-WP-107 | Foundation 0.8 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, MVP-Skill-Set-Design, Brain-Notes | **erledigt** (Planung, 2026-07-08) |
| NDF-WP-108 | Foundation 0.8 Scope Lock | docs-only / planning-gate | Umfang einfrieren; blocking/optional/deferred; WP-112-Entscheidung; ADR-0032-Pfad; Änderungsregeln | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument) |
| NDF-WP-109 | NDF Context Economy Concept | docs-only / concept | Context Economy als NDF-Prinzip: Token-/Kontextregeln, wann kürzen, wann Context Pack laden | **release-blocking** — **erledigt** ([`NDF_CONTEXT_ECONOMY.md`](../agent-workflows/NDF_CONTEXT_ECONOMY.md); 5 Kontext-Schichten, Compact Context Summary, Context Packs + Prompt Modes konzeptionell) |
| NDF-WP-110 | NDF Skill Security Policy / ADR-0032 | docs-only / adr-policy | Security-/Human-Gate-Regeln für Skills; **ADR-0032 wird hier erstellt**; fail closed, keine Git-/Release-/Netz-/Secret-Zugriffe | **release-blocking** — **erledigt** ([ADR-0032](../adr/ADR-0032-skill-security-policy.md) Accepted + [Skill Security Policy](../agent-workflows/NDF_SKILL_SECURITY_POLICY.md); fail closed; nächste freie ADR-Nummer 0033) |
| NDF-WP-111 | NDF Claude Skills Pack MVP Design | docs-only / design | Design des kleinen public-neutralen MVP-Skill-Sets (Struktur, Grenzen, Human-Gates, Rückmeldung an Nova) — **nur Design** | **release-blocking** — **erledigt** ([MVP Design](../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md); 6 Skills spezifiziert + Review Matrix; kein aktives Skill Pack) |
| NDF-WP-112 | NDF Claude Skills Pack MVP Implementation | docs-only oder skills-mvp | Erstes MVP-Skill-Set gemäß Design + Security Policy erstellen | **optional** — Option A; nur per Human-Maintainer-Scope-Change hochstufbar (Regel im Scope Lock); nicht release-blocking |
| NDF-WP-113 | NDF Context Pack Template and Prompt Modes | docs-only / template | Context-Pack-Template + Prompt-Modi (kompakt/normal/tief) standardisieren | **release-blocking** — **nächster Schritt** |
| NDF-WP-114 | Foundation 0.8 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.8-Kriterien | **release-blocking** |
| NDF-WP-115 | Foundation 0.8 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.8.0-foundation`) | **release-blocking** |

## Optionale Work Packages (verbindlich / binding)

| ID | Titel | Ziel |
|---|---|---|
| NDF-WP-112 | NDF Claude Skills Pack MVP Implementation | Optional; siehe WP-112-Upgrade-Regel im Scope Lock |
| NDF-WP-116 | Skill-to-Cursor Rules Export Assessment | Prüfen, ob/wie NDF-Skills nach Cursor-Rules exportierbar wären — nur Assessment |
| NDF-WP-117 | Workflow Builder Evaluation | Bewerten, ob ein Workflow-Konzept sinnvoll ist — nur Evaluation |
| NDF-WP-118 | Docs Polish Skill Evaluation | Bewerten eines Docs-Polish-Skills — nur Evaluation |

## Vorgeschlagenes MVP Skill Set (nur geplant / planned only)

**Nicht in WP-107 erstellt.** Kandidaten für das erste MVP (Detail-Design in WP-111):

- `ndf-token-economy`
- `ndf-feedback-to-nova`
- `ndf-work-package-runner`
- `ndf-public-neutrality-guard`
- `ndf-release-safety`
- `ndf-adr-governance`

Optional später / optional later: `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`.

## Deferred / Nicht-Ziele (Kandidaten / candidates)

- v1.0 Release Candidate / v1.0-Vorbereitung
- Skill-Script-Ausführung mit Netzwerkzugriff
- Autonome Git-/Release-Automation durch Skills
- Import von Drittanbieter-Skills / externen Skill-Inhalten
- Große Automatisierungsplattform
- Cursor-Rules / Workflows in dieser Planungsphase
- Vollständige Doku-Website / volle i18n

## Regeln / Rules

- Die Einstufung ist mit NDF-WP-108 **verbindlich gelockt**. Änderungen (inkl. WP-112-Upgrade-Regel) nur gemäß den Change-Control-Regeln in [FOUNDATION_0_8_SCOPE_LOCK.md](FOUNDATION_0_8_SCOPE_LOCK.md).
- Blocking Kern: Gates (108/114/115) + Context Economy (109) + Skill Security Policy/ADR-0032 (110) + Skills MVP **Design** (111) + Context Pack Template & Prompt Modes (113). **Skills-MVP-Implementierung (112) bleibt optional (Option A).**
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock; kein neues release-blocking WP ohne expliziten Scope-Change; keine Skills-Implementierung vor abgeschlossener Security Policy (WP-110); kein Scope Creep.
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim; kein aktives Skill Pack behaupten.
