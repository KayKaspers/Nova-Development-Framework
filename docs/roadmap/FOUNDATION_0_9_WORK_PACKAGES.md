# Foundation 0.9 – Work Package Queue (Candidates)

> Status: **Planning candidate** (NDF-WP-120). **Nicht scope-locked.** Die verbindliche blocking/optional/deferred-Einstufung entsteht erst in NDF-WP-121 (Scope Lock). / Planning candidate; not scope-locked — the binding classification is created only in NDF-WP-121.

## Vorgeschlagene Queue / Proposed Queue

| ID | Titel | Typ | Ziel |
|---|---|---|---|
| NDF-WP-120 | Foundation 0.9 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, Brain-Notes |
| NDF-WP-121 | Foundation 0.9 Scope Lock | docs-only / planning-gate | Umfang einfrieren; blocking/optional/deferred; WP-124-Entscheidungskorridor; Änderungsregeln |
| NDF-WP-122 | Context Economy Adoption Review | review-only | Prüfen, ob Context Economy in echten WPs hilft; Adoption-Beobachtungen dokumentieren |
| NDF-WP-123 | Prompt Modes and Context Pack Validation | review-only | Prompt Modes (Full/Standard/Short) + Context Pack Template auf Verständlichkeit/Sicherheit validieren |
| NDF-WP-124 | Optional Skills MVP Implementation Decision | docs-only / decision | Entscheiden, ob eine docs-only Skills-MVP-Implementierung sinnvoll ist (priorisieren / optional / verwerfen) |
| NDF-WP-125 | Skills MVP Implementation Blueprint | docs-only / design | Falls gescopt: Implementation Blueprint gemäß ADR-0032 (docs-only, keine Scripts/Netz/Secrets) |
| NDF-WP-126 | Adoption Evidence and v1.0 Path Review | review-only | Adoption-/Validation-Evidence sammeln; v1.0-Kriterien-Draft ehrlich fortschreiben |
| NDF-WP-127 | Foundation 0.9 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.9-Kriterien |
| NDF-WP-128 | Foundation 0.9 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.9.0-foundation`) |

## Optionale Kandidaten / Optional Candidates (candidate only)

| ID | Titel | Ziel |
|---|---|---|
| NDF-WP-129 | Docs-only Skills MVP Implementation | Erste docs-only Skill-Umsetzung — **nur** wenn WP-124 es befürwortet und WP-121 es scoped; strikt ADR-0032-konform |
| NDF-WP-130 | Skill-to-Cursor Rules Export Assessment | Prüfen, ob/wie NDF-Skills nach Cursor-Rules exportierbar wären — **nur Assessment** |
| NDF-WP-131 | Workflow Builder Evaluation | Bewerten, ob ein Workflow-Konzept sinnvoll ist — **nur Evaluation** |
| NDF-WP-132 | Docs Polish Skill Evaluation | Bewerten eines Docs-Polish-Skills — **nur Evaluation** |
| NDF-WP-133 | Foundation 0.9 Post-Release Status Cleanup | Nach manuellem Release: Tag + GitHub Release read-only verifizieren, Status auf released/published heben |

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

- Die endgültige blocking/optional/deferred-Trennung passiert **erst in WP-121 Scope Lock**. In WP-120 werden nur Kandidaten vorgeschlagen.
- **Optional Enablement heißt: zuerst Bewertung oder Entscheidung. Implementierung ist nie automatisch.** WP-129/130/131/132 werden nicht still aktiviert.
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock; kein neues release-blocking WP wird in WP-120 final festgelegt; kein Scope Creep.
- Jede spätere Skill-Umsetzung muss ADR-0032 einhalten (keine Scripts/Netz/Secrets/privaten Daten/autonomen Git-Release-Aktionen; Human-Maintainer-Kontrolle).
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim; kein aktives Skill Pack behaupten.
