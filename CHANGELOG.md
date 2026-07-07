# Changelog

All notable changes to the Nova Development Framework will be documented in this file.

## [Unreleased] - Foundation 0.6 Scope Locked

Status: Scope locked, release-blocking work packages defined. Not v1.0.

### Added

- docs(roadmap): Foundation 0.6 planning draft — adoption confidence & governance hardening: plan, work package candidates (084–095), release criteria draft (WP-084)
- docs(roadmap): locked Foundation 0.6 scope — blocking core 085/086/088/089/094/095, ADR decision duty (adopt or drop, no third deferral), WP-088 8-condition downgrade valve via WP-094, WP-090 merged into WP-089 (WP-085)
- docs(governance): adopted minimal ADR policy — new ADRs in docs/adr/ with cross-folder numbering (next: ADR-0031), roles, status values, no mass migration; closes the open v1.0 ADR criterion as met with notes (WP-086)
- docs(validation): recorded public SampleProject runbook validation — independently and positively confirmed, PASS WITH NOTES, no blockers; valve not needed, WP-087 skipped; v1.0 external validation now met with notes (WP-088)
- docs(quality): reviewed Public Quality Gate maintenance and CI denylist effectiveness — evidence level strong (incl. synthetic local test), WP-090 not needed (WP-089)

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
