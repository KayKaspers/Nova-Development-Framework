# Foundation 0.9 – Work Package Queue

> Status: **Released / published — reconciliation documented** als `v0.9.0-foundation` (2026-07-10, NDF-WP-133). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_9_SCOPE_LOCK.md](FOUNDATION_0_9_SCOPE_LOCK.md). Nicht v1.0, kein aktives Skill Pack. / Released as `v0.9.0-foundation`; not v1.0, no active skill pack.

## Queue

| ID | Titel | Typ | Scope Lock |
|---|---|---|---|
| NDF-WP-120 | Foundation 0.9 Planning | docs-only / planning | **erledigt** (Planung, 2026-07-08) |
| NDF-WP-121 | Foundation 0.9 Scope Lock | docs-only / planning-gate | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument) |
| NDF-WP-122 | Context Economy Adoption Review | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Adoption Review](../validation/context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md); Adoption belegt, 16-Punkte-Matrix, kein aktives Skill Pack) |
| NDF-WP-123 | Prompt Modes and Context Pack Validation | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Validation](../validation/context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md); 28-Punkte-Matrix, Short Prompt sicher begrenzt, Template vollständig) |
| NDF-WP-124 | Optional Skills MVP Implementation Decision | docs-only / decision | **release-blocking** — **erledigt: Option B (Blueprint-first, implementation-not-activated)** ([Decision](../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md); WP-125 empfohlen aber optional, WP-129 nicht aktiviert) |
| NDF-WP-125 | Skills MVP Implementation Blueprint | docs-only / design | **optional / conditional — erledigt: GO WITH NOTES** ([Blueprint](../validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md); vom Human Maintainer für den Blueprint aktiviert; 4-Skill-MVP empfohlen, WP-129 mit engem docs-only Scope bedingt empfohlen; **keine Implementierung**, kein aktives Skill Pack) |
| NDF-WP-126 | Adoption Evidence and v1.0 Path Review | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Review](../validation/foundation-0-9/ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md); 28-Punkte-Evidence-Matrix, v1.0-Pfad gestärkt aber nicht geschlossen) |
| NDF-WP-127 | Foundation 0.9 Release Readiness Review | review-only | **release-blocking** — **erledigt: GO WITH NOTES** ([Readiness Review](../release/FOUNDATION_0_9_READINESS_REVIEW.md); 18-Punkte-Criteria-Check, keine Blocker, kein aktives Skill Pack) |
| NDF-WP-128 | Foundation 0.9 Release Prep | docs-only / release-prep | **release-blocking** — **erledigt** ([Release Notes](../release/FOUNDATION_0_9_RELEASE_NOTES.md), [Go/No-Go](../release/FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md), [Tagging-Guide](../release/FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md)); Release am 2026-07-10 veröffentlicht |
| NDF-WP-133 | Foundation 0.9 Post-Release Reconciliation Cleanup | docs-only / post-release-cleanup | **erledigt** in WP-133 (2026-07-10: `v0.9.0-foundation` veröffentlicht und read-only verifiziert; Status auf released/published gehoben; Tag-Cut bei WP-126 transparent dokumentiert, kein Tag-Move; [Reconciliation Notes](../../project-brain/WP_133_FOUNDATION_0_9_POST_RELEASE_RECONCILIATION_CLEANUP_NOTES.md)) |
| NDF-WP-134 | Skills-first Operating Mode & Prompt Compression Validation | docs-only / validation | **erledigt: GO WITH NOTES** — Skills-first Operating Mode dokumentiert, Prompt-Kompression validiert (strukturell hoch–sehr hoch), DSK-001 **Partially closed**; keine neuen/Extended Skills ([Compression Validation](../validation/foundation-0-9/SKILLS_PROMPT_COMPRESSION_VALIDATION.md), [Operating Mode](../validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md), [Notes](../../project-brain/WP_134_SKILLS_FIRST_OPERATING_MODE_NOTES.md)) |

## Optionale / bedingte Work Packages (verbindlich / binding)

| ID | Titel | Scope Lock |
|---|---|---|
| NDF-WP-129 | Docs-only Skills MVP Implementation | **erledigt: GO WITH NOTES** — per ausdrücklichem Human-Maintainer-Scope-Change nach WP-125 aktiviert; genau vier docs-only MVP-Skills implementiert (`.claude/skills/`), keine Extended Skills, keine Scripts, strikt ADR-0032-konform ([Validation](../validation/foundation-0-9/DOCS_ONLY_SKILLS_MVP_VALIDATION.md), [Notes](../../project-brain/WP_129_DOCS_ONLY_SKILLS_MVP_IMPLEMENTATION_NOTES.md)) |
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
