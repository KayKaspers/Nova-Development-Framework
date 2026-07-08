# Next Phase – Foundation 0.8

## Current status

**Scope locked** (NDF-WP-108, 2026-07-08). Foundation 0.8 ist gelockt, **nicht released**, **nicht v1.0**. Kein Skill Pack erstellt. Verbindliche Einstufung: `docs/roadmap/FOUNDATION_0_8_SCOPE_LOCK.md`. Release-blocking: 108 (done) · 109 (Context Economy Concept — **done**) · 110 (Skill Security Policy / ADR-0032 — **done**) · 111 (Skills MVP Design — **done**) · 113 (Context Pack Template & Prompt Modes — **done**) · 114 (Release Readiness Review — **done: GO WITH NOTES**, `docs/release/FOUNDATION_0_8_READINESS_REVIEW.md`) · 115 (Release Prep — **nächster Schritt**). **WP-112 (Skills MVP Implementation) optional (Option A)**, nur per Human-Maintainer-Scope-Change hochstufbar. Optional: 112/116/117/118.

## Working title

**Foundation 0.8 – Agent Enablement & Context Economy.** Kontrollierte, dokumentationsgetriebene NDF-Erweiterung — kein großer Feature-Release.

## Proposed goals

Context Economy als offizielles Workflow-Prinzip; Context Packs + Compact Context Summary standardisieren; kleines public-neutrales Claude Skills Pack (MVP, nur Design in dieser Phase); Skill Security Policy (fail closed, keine Git-/Release-/Netz-/Secret-Zugriffe, Human-Gates); Skill Review Checklist; Skill-vs-Prompt-vs-Workflow-Entscheidungskriterien; Release Safety.

## Candidate WPs

108 Scope Lock · 109 Context Economy Concept · 110 Skill Security Policy (ggf. ADR-0032) · 111 Skills Pack MVP Design · 112 Skills Pack MVP Implementation · 113 Context Pack Template & Prompt Modes · 114 Readiness · 115 Release Prep. Optional: 116 Skill-to-Cursor-Export-Assessment, 117 Workflow-Builder-Evaluation, 118 Docs-Polish-Skill-Evaluation.

## Proposed MVP skill set (planned only, not created)

`ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`. Optional später: `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`.

## Known constraints

Public Quality Gate v0.2 Pflicht; Skills docs-only zuerst; keine Scripts im MVP ohne ausdrücklichen Scope-Lock; keine Netzwerkzugriffe/Secrets/privaten Projektinfos; keine Git-Schreibaktionen; Human-Maintainer-Gates verbindlich; jeder WP-bezogene Skill unterstützt Rückmeldung an Nova + Compact Context Summary. Kein v1.0-Claim, keine aktive volle v1.x-Zusage; keine Drittanbieter-Skill-Inhalte. Nächste freie ADR-Nummer: 0033 (ADR-0032 in WP-110 angenommen).

## Baseline

Foundation 0.7 released as `v0.7.0-foundation` (2026-07-08); vollständig abgeschlossen (WP-106), keine offenen 0.7-Follow-ups.

## Next WP

**NDF-WP-115 – Foundation 0.8 Release Prep.** WP-114 Readiness Review abgeschlossen (GO WITH NOTES, keine Blocker); alle release-blocking WPs außer WP-115 erledigt. WP-112 optional, nicht aktiviert; kein aktives Skill Pack. Release Prep erstellt Release Notes, Go/No-Go, Tagging-Guide für voraussichtlich `v0.8.0-foundation`. Nächste freie ADR-Nummer: 0033. Kein v1.0, keine aktiven Skills.
