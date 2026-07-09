# Foundation 0.9 – Work Package Queue

> Status: **Scope locked** (NDF-WP-121, 2026-07-08). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_9_SCOPE_LOCK.md](FOUNDATION_0_9_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

## Queue

| ID | Titel | Typ | Scope Lock |
|---|---|---|---|
| NDF-WP-120 | Foundation 0.9 Planning | docs-only / planning | **erledigt** (Planung, 2026-07-08) |
| NDF-WP-121 | Foundation 0.9 Scope Lock | docs-only / planning-gate | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument) |
| NDF-WP-122 | Context Economy Adoption Review | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Adoption Review](../validation/context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md); Adoption belegt, 16-Punkte-Matrix, kein aktives Skill Pack) |
| NDF-WP-123 | Prompt Modes and Context Pack Validation | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Validation](../validation/context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md); 28-Punkte-Matrix, Short Prompt sicher begrenzt, Template vollständig) |
| NDF-WP-124 | Optional Skills MVP Implementation Decision | docs-only / decision | **release-blocking** — **erledigt: Option B (Blueprint-first, implementation-not-activated)** ([Decision](../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md); WP-125 empfohlen aber optional, WP-129 nicht aktiviert) |
| NDF-WP-125 | Skills MVP Implementation Blueprint | docs-only / design | **optional / conditional** — von WP-124 empfohlen, aber **nicht aktiviert**; Start nur auf ausdrücklichen Human-Maintainer-Wunsch; höchstens Blueprint, keine Implementierung |
| NDF-WP-126 | Adoption Evidence and v1.0 Path Review | review-only | **release-blocking** — **nächster Schritt** |
| NDF-WP-127 | Foundation 0.9 Release Readiness Review | review-only | **release-blocking** |
| NDF-WP-128 | Foundation 0.9 Release Prep | docs-only / release-prep | **release-blocking** |

## Optionale / bedingte Work Packages (verbindlich / binding)

| ID | Titel | Scope Lock |
|---|---|---|
| NDF-WP-129 | Docs-only Skills MVP Implementation | **optional — nicht durch WP-121 aktiviert**; nur per ausdrücklichem Human-Maintainer-Scope-Change nach WP-124/WP-125; strikt ADR-0032-konform |
| NDF-WP-130 | Skill-to-Cursor Rules Export Assessment | **optional** — nur Assessment |
| NDF-WP-131 | Workflow Builder Evaluation | **optional** — nur Evaluation |
| NDF-WP-132 | Docs Polish Skill Evaluation | **optional** — nur Evaluation |
| NDF-WP-133 | Foundation 0.9 Post-Release Status Cleanup | **post-release candidate** — nach manuellem Release: Tag + GitHub Release read-only verifizieren, Status auf released/published heben |

## Beziehung zu den Foundation-0.8-Optional-WPs

Die 0.8-Optional-WPs bleiben unangetastet und können durch 0.9-Kandidaten **neu bewertet** werden (nicht überschrieben): WP-112 → WP-124/WP-129 (Skills-Implementierungs-Entscheidung/-Umsetzung), WP-116 → WP-130 (Cursor-Export-Assessment), WP-117 → WP-131 (Workflow-Builder-Evaluation), WP-118 → WP-132 (Docs-Polish-Skill-Evaluation).

## Deferred / Nicht-Ziele (Kandidaten / candidates)

- v1.0 Release Candidate / v1.0-Vorbereitung
- Skill-Script-Ausführung / netzwerkfähige Skills
- Autonome Git-/Release-Automation durch Skills
- Cursor-Rules-Export-Implementierung / Workflow-Implementierung (nur Assessment/Evaluation)
- Drittanbieter-Skill-Import / private projektspezifische Skills
- Vollständige Doku-Website / volle i18n

## Regeln / Rules

- Die Einstufung ist mit NDF-WP-121 **verbindlich gelockt**. Änderungen (inkl. WP-129-Aktivierung) nur gemäß den Change-Control-Regeln in [FOUNDATION_0_9_SCOPE_LOCK.md](FOUNDATION_0_9_SCOPE_LOCK.md).
- Blocking Kern: Gates (121/127/128) + Adoption Review (122) + Prompt/Context Validation (123) + Skills-**Entscheidung** (124) + Adoption Evidence & v1.0 Path Review (126). **WP-125 optional/conditional; WP-129 optional, nicht aktiviert; WP-130/131/132 optionale Assessments; WP-133 Post-Release-Kandidat.**
- **Optional Enablement heißt: zuerst Bewertung oder Entscheidung. Implementierung ist nie automatisch.** WP-129/130/131/132 werden nicht still aktiviert; keine Skills-Implementierung ohne ausdrückliche Human-Maintainer-Entscheidung.
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock; kein neues release-blocking WP ohne expliziten Scope-Change; kein Scope Creep.
- Jede spätere Skill-Umsetzung muss ADR-0032 einhalten (keine Scripts/Netz/Secrets/privaten Daten/autonomen Git-Release-Aktionen; Human-Maintainer-Kontrolle).
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim; kein aktives Skill Pack behaupten.
