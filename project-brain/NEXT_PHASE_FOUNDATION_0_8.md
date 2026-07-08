# Next Phase – Foundation 0.8

## Current status

**Released / published** als `v0.8.0-foundation` (2026-07-08, NDF-WP-119). Foundation 0.8 ist veröffentlicht, **nicht v1.0**, keine aktive volle v1.x-Zusage, kein aktives Skill Pack. Verbindliche Einstufung: `docs/roadmap/FOUNDATION_0_8_SCOPE_LOCK.md`. Release-blocking (alle done): 108 · 109 · 110 (ADR-0032) · 111 · 113 · 114 (GO WITH NOTES) · 115 · 119 (released/published, Tag + GitHub Pre-Release read-only verifiziert). **WP-112 (Skills MVP Implementation) optional (Option A)**, nur per Human-Maintainer-Scope-Change hochstufbar. Optional/nicht aktiviert: 112/116/117/118.

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

**Foundation 0.8 ist released / published** als `v0.8.0-foundation` (2026-07-08, GitHub Pre-Release; Tag annotated → Commit `a39f50b`; in WP-119 read-only verifiziert; [Post-Release Status](../docs/release/FOUNDATION_0_8_POST_RELEASE_STATUS.md)). Keine offenen 0.8-blocking Follow-ups. WP-112/116/117/118 optional, nicht aktiviert; kein aktives Skill Pack. **Nächster sinnvoller Schritt: Foundation 0.9 Planning** — Kandidat „Adoption, Validation & Optional Enablement" (kein aktiver Scope). Nächste freie ADR-Nummer: 0033. Kein v1.0, keine aktive volle v1.x-Zusage.
