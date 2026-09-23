# v1.1.0 Release Evidence Index

## Purpose

Maps the major claims made about v1.1.0 in `V1_1_0_RELEASE_NOTES.md` and `V1_1_0_GO_NO_GO.md` to their actual source work package and artifact. No claim below is invented; every "Source" cell names a file that exists in this repository at the time of writing.

## Evidence Table

| Claim | Source | Evidence Type | Status |
|---|---|---|---|
| v1.1 stays within the active v1.x compatibility promise (ADR-0031); no breaking change | `docs/adr/ADR-0031-v1x-compatibility-policy.md`; `docs/validation/v1-1/V1_1_READINESS_REVIEW.md` §R2 | ADR + governance readiness review | Confirmed non-breaking across WP-151…158 |
| Prompt execution contract established (session declaration, complete-replacement semantics, output precedence) | `framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md`; `docs/validation/v1-1/PROMPT_EXECUTION_CONTRACT_BASELINE.md` | Framework artifact + validation record | WP-153, accepted, committed `70446a3` |
| Token efficiency & context budget baseline established | `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` | Guide + templates | WP-152, GO WITH NOTES, committed `c4c1c34` |
| Six P0 skills hardened; no skill added/removed/renamed; pack stays at 38 | `docs/validation/v1-1/SKILLS_PACK_P0_HARDENING.md`; `.claude/skills/README.md` §Pack Model | Validation record + skills index | WP-154, accepted, committed `07b2884` |
| G-13 external-validation depth addressed; independence/externality unchanged; `MATERIALLY_REDUCED`, not closed | `docs/validation/v1-1/EXTERNAL_VALIDATION_IMPROVEMENT.md` | Evidence-only validation record | WP-155, PASS WITH NOTES, committed `243225d` |
| Project enablement PREPARED-vs-AUTHORIZED boundary validated; EVI-007 clarified as intentional, not a defect | `docs/validation/v1-1/PROJECT_ENABLEMENT_VALIDATION.md` | Evidence-only validation record | WP-156, GO WITH NOTES, committed `270c6c5` |
| Documentation consistency findings (EVI-001…006/008, PEV-001/002/003/005) resolved documentarily; PEV-004 retained as an honest limitation | `docs/validation/v1-1/PUBLIC_DOCUMENTATION_POLISH.md` | Validation record with Finding Outcome Matrix | WP-157, IMPLEMENTED — NOVA REVIEW PASSED, committed `4cf5aec` |
| Historical public-neutrality migration completed (8 files renamed, 11 IDs migrated, no history rewrite) | `docs/validation/v1-1/PUBLIC_DOCUMENTATION_POLISH.md`; `docs/validation/cross-project-feedback/` (renamed files present on disk) | Filesystem check + validation record | WP-157, verified present |
| v1.1 readiness result: `GO_WITH_NOTES` — ready for release-prep entry only, no dimension REWORK/BLOCKED | `docs/validation/v1-1/V1_1_READINESS_REVIEW.md`; `project-brain/WP_158_V1_1_READINESS_REVIEW_NOTES.md` | Nine-dimension governance/compatibility/evidence review | WP-158, REVIEW COMPLETE, baseline `4cf5aec` |
| Public Quality Gate passes locally at the WP-159 baseline (0 errors, 0 warnings, 3 notices) | Direct tool output, this WP (`python scripts/check_public_quality.py --strict` / `--self-test`) | Direct read-only tool run | Confirmed at baseline `e37f2c7`, consistent with WP-155…158's own runs |
| WP-158 committed at `e37f2c7`; WP-159 is the current, final v1.1 release-prep work package; no WP-160 exists | `git log` (commit `e37f2c7 docs(v1): review v1.1 readiness`); `docs/roadmap/V1_1_PLAN.md` | Git history + roadmap | Confirmed |
| Single-maintainer structural bottleneck remains an accepted, tracked limitation | `docs/roadmap/V1_1_PLAN.md` §Risks; every WP-151…158 "Limitations" section | Roadmap + repeated self-disclosure | Confirmed, non-blocking |
| ADR-0032 private-consumer-skill-use scope remains deferred (candidate ADR-0033), not resolved by v1.1 | `docs/adr/ADR-0032-skill-security-policy.md`; `docs/roadmap/V1_1_PLAN.md` §Risks; `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md` §Accepted ADRs | ADR + roadmap + context pack | Confirmed deferred, unchanged by WP-159 |
| i18n status remains mixed/partial, not fully bilingual | `docs/i18n/TRANSLATION_STATUS.md` | Status matrix | Confirmed, honestly tracked |

## Notes on Evidence Classes

Consistent with the classification WP-155/156/158 already applied: repository-internal (validation records, ADRs, guides), direct tool output (Public Quality Gate runs, `git log`), and roadmap/context-pack cross-references are kept distinct from — and never aggregated with — project-local, Human-Maintainer, independent, or invented evidence. No project-local, independent, user, team, feedback, integration, or adoption evidence is claimed or used in this index; where such evidence exists (e.g., the first real project-feedback intake referenced by WP-155/156), it is cited only through its own already-public, already-neutralised validation record, never reproduced here.

## What This Index Does Not Claim

This index does not claim v1.1.0 is released, tagged, published, or Human-Maintainer-accepted. It does not claim G-13 is closed or that external validation is independent. It does not claim ADR-0032's private-consumer-skill-use question is resolved. It maps claims to sources; it does not itself constitute a release decision.
