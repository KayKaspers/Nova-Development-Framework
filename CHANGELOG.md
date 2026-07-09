# Changelog

All notable changes to the Nova Development Framework will be documented in this file.

## [Unreleased] - Foundation 0.9 Scope Locked

Status: scope-locked. Not released. Not v1.0.

### Added

- docs(roadmap): started Foundation 0.9 planning for Adoption, Validation & Optional Enablement — plan, candidate work packages (120–128, optional 129–133), release criteria draft; optional enablement means evaluation/decision first, implementation never automatic; not scope-locked, not released, not v1.0, no skills created (WP-120)
- docs(roadmap): scope-locked Foundation 0.9 for Adoption, Validation & Optional Enablement — validation-first; blocking core 121/122/123/124/126/127/128, WP-124 a release-blocking decision (no implementation), WP-125 optional/conditional, WP-129 docs-only skills implementation optional and not activated, WP-130/131/132 optional assessments, WP-133 post-release candidate; Foundation 0.8 optional WPs 112/116/117/118 re-evaluated not overwritten; no skills/scripts created; not released, not v1.0 (WP-121)
- docs(validation): review Context Economy adoption — GO WITH NOTES; 16-point adoption matrix confirms Compact Context Summary, Context Packs and prompt modes are practically adopted in Foundation 0.9; safety/neutrality boundaries preserved, no active skill pack; deeper prompt/context-pack validation stays with WP-123, v1.0-path evidence with WP-126 (WP-122)
- docs(validation): validate prompt modes and context packs — GO WITH NOTES; 28-point validation matrix confirms Full/Standard/Short prompt modes are clearly bounded (Short with explicit forbidden cases, no gate or human-review bypass), the Context Pack template is complete and the Foundation 0.9 pack current; no active skill pack, skills decision stays with WP-124 (WP-123)

## [0.8.0-foundation] - 2026-07-08

Agent Enablement & Context Economy Pre-Release. Status: **Published** as Foundation pre-release on 2026-07-08 (tag `v0.8.0-foundation`). Not v1.0. Full v1.x compatibility promise not active. No active Claude Skills Pack. Release notes: `docs/release/FOUNDATION_0_8_RELEASE_NOTES.md`

### Added

- docs(roadmap): started Foundation 0.8 planning for Agent Enablement & Context Economy — plan, candidate work packages (107–115, optional 116–118), release criteria draft, MVP skill set design (planned only, no skills created); not scope-locked, not released, not v1.0 (WP-107)
- docs(roadmap): scope-locked Foundation 0.8 for Agent Enablement & Context Economy — blocking core 108/109/110/111/113/114/115, WP-112 skills MVP implementation kept optional (Option A) with an upgrade rule, ADR-0032 (skill security policy) to be created in WP-110; no skills/scripts created; not released, not v1.0 (WP-108)
- docs(agent-workflows): define NDF Context Economy concept — five context layers, Compact Context Summary as a binding handover, Context Packs and Full/Standard/Short prompt modes (concept only; templates in WP-113); safety boundaries (no chain-of-thought, no raw chat history, no autonomous git/release, gate mandatory); no skills created (WP-109)
- docs(adr): add ADR-0032 Skill Security Policy (Accepted) — fail-closed governance for NDF skills; forbids autonomous commit/push/tag/release, network access, secret processing, scripts in the MVP, and third-party skill import; human-maintainer gates and public quality gate mandatory; next free ADR number 0033 (WP-110)
- docs(agent-workflows): add NDF Skill Security Policy — operative rule set referenced by WP-111/112; no active skill pack, no skills/scripts created; not v1.0 (WP-110)
- docs(agent-workflows): design NDF Claude Skills Pack MVP — six MVP skills (ndf-token-economy, -feedback-to-nova, -work-package-runner, -public-neutrality-guard, -release-safety, -adr-governance) with per-skill specs, a review matrix, shared rules and WP-112 boundary; design only, no active skill pack, no .claude/skills or scripts created; WP-112 stays optional (WP-111)
- docs(agent-workflows): add NDF Prompt Modes and Context Pack templates — Full/Standard/Short prompt modes with selection and forbidden-short-prompt rules, a reusable Context Pack template (incl. Report-to-Nova structure), and a first Foundation 0.8 Context Pack; no chain-of-thought, no active skills; not released, not v1.0 (WP-113)
- docs(release): Foundation 0.8 release readiness review: GO WITH NOTES — 20-point readiness matrix, no blockers; filesystem check confirms no active skill pack, no .claude/skills, no new skill scripts; WP-112 optional and not activated; not released, not v1.0 (WP-114)
- docs(release): prepared Foundation 0.8 release notes, Go/No-Go checklist and tagging guide (presumably `v0.8.0-foundation`, release-prepared / tag pending); post-release cleanup candidate NDF-WP-119; no active skill pack, WP-112 optional and not activated; not released, not v1.0 (WP-115)
- docs(release): marked Foundation 0.8 as published (`v0.8.0-foundation`, 2026-07-08); post-release status cleanup — tag (annotated) and GitHub pre-release verified read-only; no active skill pack; not v1.0 (WP-119)

## [0.7.0-foundation] - 2026-07-08

v1.0 Path Consolidation & Compatibility Governance Pre-Release. Status: **Published** as Foundation pre-release on 2026-07-08 (tag `v0.7.0-foundation`).
Not v1.0. Not a v1.0 release candidate.
Full v1.x compatibility promise activates only with a future v1.0 release.
Release notes: `docs/release/FOUNDATION_0_7_RELEASE_NOTES.md`

### Added

- docs(roadmap): Foundation 0.7 planning candidate — v1.0 path consolidation & compatibility governance: plan, work package candidates (097–105), release criteria draft (WP-097)
- docs(roadmap): locked Foundation 0.7 scope — blocking core 098/099/100/101/104/105, WP-099 checklist decision corridor (prioritize/keep-optional/drop, no fourth deferral), WP-100 ADR-0031 preferred path, WP-102 optional with upgrade valve (WP-098)
- docs(roadmap): decided Checklist DE/EN path for Foundation 0.7 — Option B (optional with final rationale); not a release blocker, no more auto-carry, no follow-up work package (WP-099)
- docs(adr): added ADR-0031 v1.x compatibility policy (Accepted) — governance framework with compatibility categories, breaking/deprecation rules; the active full v1.x promise activates only at v1.0; v1.0 criterion now met with notes (WP-100)
- docs(validation): reviewed Project Adapter convention stability — Stable with notes (conventions unchanged across 0.4→0.7); fixed two stale manifest .yaml references to canonical .md; v1.0 adapter-maturity criterion now met with notes (WP-101)
- docs(release): Foundation 0.7 release readiness review: GO WITH NOTES — no blockers; notes are deliberate non-blockers (full v1.x promise only at v1.0, convention stability with notes, PSV-001 v1.0-tracked, WP-102/103 optional and not activated) (WP-104)
- docs(release): prepared Foundation 0.7 release — release notes with known limitations and operational notes, 26-item go/no-go checklist, tagging guide (presumably `v0.7.0-foundation`, tag pending); one future-candidate hint noted (NDF Agent Enablement & Context Economy incl. a small public-neutral Claude Skills Pack) — not scope, not blocking (WP-105)

## [0.6.0-foundation] - 2026-07-07

Adoption Confidence & Governance Hardening Pre-Release. Status: **Published** as Foundation pre-release on 2026-07-07 (tag `v0.6.0-foundation`). Not v1.0. Release notes: `docs/release/FOUNDATION_0_6_RELEASE_NOTES.md`

### Added

- docs(roadmap): Foundation 0.6 planning draft — adoption confidence & governance hardening: plan, work package candidates (084–095), release criteria draft (WP-084)
- docs(roadmap): locked Foundation 0.6 scope — blocking core 085/086/088/089/094/095, ADR decision duty (adopt or drop, no third deferral), WP-088 8-condition downgrade valve via WP-094, WP-090 merged into WP-089 (WP-085)
- docs(governance): adopted minimal ADR policy — new ADRs in docs/adr/ with cross-folder numbering (next: ADR-0031), roles, status values, no mass migration; closes the open v1.0 ADR criterion as met with notes (WP-086)
- docs(validation): recorded public SampleProject runbook validation — independently and positively confirmed, PASS WITH NOTES, no blockers; valve not needed, WP-087 skipped; v1.0 external validation now met with notes (WP-088)
- docs(quality): reviewed Public Quality Gate maintenance and CI denylist effectiveness — evidence level strong (incl. synthetic local test), WP-090 not needed (WP-089)
- docs(release): Foundation 0.6 release readiness review: GO WITH NOTES — no blockers, notes are non-blocking known-limitation candidates (WP-094)
- docs(release): prepared Foundation 0.6 release — release notes with known limitations and operational notes, 22-item go/no-go checklist, tagging guide, criteria update (WP-095)
- docs(release): marked Foundation 0.6 as published (`v0.6.0-foundation`, 2026-07-07); post-release status cleanup (WP-096)

## [0.5.0-foundation] - 2026-07-07

External Validation & 1.0 Path Hardening Pre-Release. Status: **Released** as Foundation pre-release on 2026-07-07 (tag `v0.5.0-foundation`). Not v1.0. Release notes: `docs/release/FOUNDATION_0_5_RELEASE_NOTES.md`

### Added

- docs(roadmap): Foundation 0.5 planning draft — external validation & 1.0 path hardening: plan, work package queue draft, release criteria draft (WP-071)
- docs(roadmap): locked Foundation 0.5 scope — blocking core 072/073/074/079/081/082, WP-074 downgrade valve (8 conditions via WP-081), WP-076 prioritize-or-drop rule (WP-072)
- docs(validation): prepared independent adapter validation — preparation doc, runbook, validator brief, feedback + outreach templates, independent-runs result location; run itself (WP-074) still open (WP-073)
- docs(release): added v1.0 readiness criteria draft (12 categories, honest status, explicit non-goals) and v1.0 path summary — draft only, NDF is not v1.0 (WP-079)
- docs(validation): recorded neutralized independent adapter validation result — private reference context, PASS WITH NOTES, no blockers; downgrade valve not needed (WP-074)
- docs(release): Foundation 0.5 release readiness review: GO WITH NOTES — no blockers, notes are non-blocking known-limitation candidates (WP-081)
- docs(release): prepared Foundation 0.5 release — release notes with known limitations, go/no-go checklist, tagging guide, criteria update (WP-082)
- docs(release): marked Foundation 0.5 as published (`v0.5.0-foundation`, 2026-07-07); post-release status cleanup (WP-083)

### Maintenance

- docs(maintenance): closed Foundation 0.4 manual follow-ups after release — custom neutrality denylist secret verified, Foundation 0.2 release title verified correct (WP-070)

## [0.4.0-foundation] - 2026-07-04

Adoption Hardening & Public Usability Pre-Release. Status: **Released** as Foundation pre-release on 2026-07-04 (tag `v0.4.0-foundation`). Release notes: `docs/release/FOUNDATION_0_4_RELEASE_NOTES.md`

### Added

- Foundation 0.4 planning documents and draft work package queue (WP-057)
- Foundation 0.4 scope lock and release-blocking work package definition (WP-058)
- Project adapter conventions (manifest, output path, health score) and first-safe-WP template (WP-059)
- Prompt library DE/EN priority pass: five adoption prompts fully bilingual, prioritized security/gate prompts DE/EN core (WP-060)
- Foundation 0.4 release readiness review: GO WITH NOTES (WP-067)
- Prepared Foundation 0.4 release: release notes, go/no-go checklist, tagging guide, criteria update (WP-068)
- Marked Foundation 0.4 as released (`v0.4.0-foundation`, 2026-07-04); post-release status cleanup (WP-069)

## [0.3.0-foundation] - 2026-07-04

Foundation Adoption Pre-Release. Status: **Released** as Foundation pre-release on 2026-07-04 (tag `v0.3.0-foundation`). Release notes: `docs/release/FOUNDATION_0_3_RELEASE_NOTES.md`

### Added

- Foundation 0.3 planning documents and draft work package queue (WP-044)
- Foundation 0.3 scope lock and release-blocking work package definition (WP-045)
- Neutral example project v0.2 (SampleProject) as adapter validation fixture (WP-046)
- Project adapter v0.2 practically validated against SampleProject: PASS WITH NOTES (WP-047)
- Public quality gate v0.2: new-file neutrality check for untracked files, --tracked-only flag, extended self-tests and denylist documentation rules (WP-052)
- Foundation 0.3 release readiness review: GO WITH NOTES (WP-054)
- Prepared Foundation 0.3 release: release notes, go/no-go checklist, tagging guide, criteria update (WP-055)
- Marked Foundation 0.3 as released (`v0.3.0-foundation`, 2026-07-04); post-release status cleanup (WP-056)

## [0.2.0-foundation] - 2026-07-03

Foundation Stabilization Pre-Release. Status: **Released** as Foundation pre-release on 2026-07-03 (tag `v0.2.0-foundation`). Release notes: `docs/release/FOUNDATION_0_2_RELEASE_NOTES.md`

### Added

- Work Package Type Standard (WP-027)
- Destructive Action Toolkit (WP-028)
- Security Prompt Library (WP-029)
- Public Repository Quality Gate: script, CI workflow, denylist concept (WP-032)
- Project Adapter v0.2: guide, templates, checklist and prompts (WP-034)
- DE/EN language standard, translation status matrix, and updated prompt index (WP-035)
- Improved README as bilingual DE/EN public entry point (WP-036)
- Clarified Nova as the ChatGPT-based planning and review role and improved workflow DE/EN guidance (WP-037)
- Improved DE/EN alignment for core workflow documentation (WP-038)
- Improved DE/EN alignment for core prompts and checklists (WP-039)
- Added Foundation 0.2 release readiness review (WP-040)
- Prepared Foundation 0.2 release: release notes, criteria update, go/no-go checklist, tagging guide (WP-041)

### Changed

- Public neutralization: private project references replaced by neutral reference projects, root cleaned, import packages archived under `docs/import-history/` (WP-030)
- Maintainer neutralization: personal references replaced by neutral roles, workflow generalized to Nova → Implementation Agent → Human Maintainer (WP-031)
- Repository link and structure consistency review: ADR structure documented, root policy aligned with the quality gate (WP-033)

## [0.1.0-foundation] - Released

### Added

- Foundation architecture
- Constitution
- Governance
- Master Plan
- Strategic Blueprint
- Domain Model
- Practical Workflow
- Prompt Library v0.1
- Template Library v0.1
- Project System v0.1
- Toolkit v0.1
- Project Starter Manual Flow v0.1
- Academy Band 1 Skeleton v0.1
- Export Concept v0.1
- Website Concept v0.1
- Foundation Readiness Review
- Repository Structure Cleanup Plan
- Branding Bible v0.1
- Minimal Example Project
- Foundation 0.1 Release Package

### Changed

- Beginner workflow standard uses VS Code and GitHub Desktop.
- Cursor remains optional, not required.
- Project Adapter evolved into Project System.

### Known Limitations

- Academy content is not fully written.
- Website and export pipeline are conceptual.
- Toolkit is not yet a CLI.
- Automation checks are planned for later.
