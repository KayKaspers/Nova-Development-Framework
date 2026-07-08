# Foundation 0.8 – Work Package Queue (Candidates)

> Status: **Planning candidate** (NDF-WP-107). **Nicht scope-locked.** Die verbindliche blocking/optional/deferred-Einstufung entsteht erst in NDF-WP-108 (Scope Lock). / Planning candidate; not scope-locked — the binding classification is created only in NDF-WP-108.

## Vorgeschlagene Queue / Proposed Queue

| ID | Titel | Typ | Ziel | Herkunft / Origin |
|---|---|---|---|---|
| NDF-WP-107 | Foundation 0.8 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, MVP-Skill-Set-Design, Brain-Notes | 0.7 Future Candidate (WP-106) |
| NDF-WP-108 | Foundation 0.8 Scope Lock | docs-only / planning-gate | Umfang einfrieren; blocking/optional/deferred; WP-112-Blocking-Frage; docs-only-vs-scripts-Entscheidung; Änderungsregeln | WP-107 |
| NDF-WP-109 | NDF Context Economy Concept | docs-only / concept | Context Economy als NDF-Prinzip: Token-/Kontextregeln, wann kürzen, wann Context Pack laden | WP-108 |
| NDF-WP-110 | NDF Skill Security Policy | docs-only / adr-policy | Security-/Human-Gate-Regeln für Skills; ggf. als ADR-0032; fail closed, keine Git-/Release-/Netz-/Secret-Zugriffe | WP-108 |
| NDF-WP-111 | NDF Claude Skills Pack MVP Design | docs-only / design | Design des kleinen public-neutralen MVP-Skill-Sets (Struktur, Grenzen, Human-Gates, Rückmeldung an Nova) | WP-108 |
| NDF-WP-112 | NDF Claude Skills Pack MVP Implementation | docs-only oder skills-mvp (Scope-Lock entscheidet) | Erstes MVP-Skill-Set gemäß Design + Security Policy erstellen | WP-110, WP-111 |
| NDF-WP-113 | NDF Context Pack Template and Prompt Modes | docs-only / template | Context-Pack-Template + Prompt-Modi (kompakt/normal/tief) standardisieren | WP-109 |
| NDF-WP-114 | Foundation 0.8 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.8-Kriterien | blocking WPs done |
| NDF-WP-115 | Foundation 0.8 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.8.0-foundation`) | WP-114 |

## Optionale Kandidaten / Optional Candidates (candidate only)

| ID | Titel | Ziel |
|---|---|---|
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

- Die endgültige blocking/optional/deferred-Trennung passiert **erst in WP-108 Scope Lock**. In WP-107 werden nur Kandidaten vorgeschlagen.
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock; kein neues blocking WP wird in WP-107 final festgelegt; kein Scope Creep.
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim; kein aktives Skill Pack behaupten.
