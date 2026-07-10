# NDF Docs-only Skills Pack

## Purpose

This directory holds the **NDF Docs-only Skills Pack** — a minimal, documentation-only skill pack that helps shorten Claude prompts for repeating NDF work without weakening NDF governance. Each skill encapsulates a stable, public-neutral block of NDF behavior (role, guardrails, closing formats, neutrality, context-pack upkeep) so that a work-package prompt can carry only the WP-specific parts.

The **core MVP** was implemented under NDF-WP-129 (based on the [Skills MVP Implementation Blueprint](../../docs/validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md), WP-125); the **extended core skills** were implemented under NDF-WP-137 (based on the [Extended Skills Pack Blueprint](../../docs/validation/foundation-0-9/EXTENDED_SKILLS_PACK_BLUEPRINT.md), WP-136). All skills follow the [Skill Security Policy](../../docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md) / [ADR-0032](../../docs/adr/ADR-0032-skill-security-policy.md).

## Included Skills

### Core MVP skills (WP-129)

1. [`ndf-work-package-runner`](ndf-work-package-runner/SKILL.md) — standardized NDF work-package execution with less prompt overhead.
2. [`ndf-compact-context-summary-runner`](ndf-compact-context-summary-runner/SKILL.md) — uniform, short, reusable Compact Context Summary and Report-to-Nova structure for handover.
3. [`ndf-public-neutrality-guard`](ndf-public-neutrality-guard/SKILL.md) — a public-neutrality reminder/guard for NDF artifacts (not a CI gate).
4. [`ndf-context-pack-maintainer`](ndf-context-pack-maintainer/SKILL.md) — keeps Context Packs consistent and short for lower-token handover.

### Extended core skills (WP-137)

5. [`ndf-skill-quality-reviewer`](ndf-skill-quality-reviewer/SKILL.md) — reviews NDF skill docs for quality, scope, ADR-0032 compliance, neutrality, overlap, and fail-closed behavior (advisory).
6. [`ndf-existing-project-analysis-runner`](ndf-existing-project-analysis-runner/SKILL.md) — structures a neutral, advisory analysis of an existing project for NDF onboarding.
7. [`ndf-docs-polish-runner`](ndf-docs-polish-runner/SKILL.md) — improves documentation clarity, structure, and consistency (advisory, no substance change).
8. [`ndf-changelog-writer`](ndf-changelog-writer/SKILL.md) — helps write consistent, neutral, WP-referenced changelog entries (never triggers a release).

## Non-Goals

- No active automation, tool orchestration, or autonomous execution.
- No optional/extended skills beyond those listed above (`ndf-release-safety`, `ndf-adr-governance-review`, `ndf-v1-readiness-review`, `ndf-prompt-mode-selector`) — deferred, not implemented here.
- No scripts, no executable files, no network access, no secret access, no private data.
- No git/release/tag actions and no autonomous commit/push/tag/release.
- No activation of optional WPs (WP-130/131/132) and no v1.0 / v1.0-RC / full v1.x promise activation.

## Security Boundaries (ADR-0032)

All skills are **docs-only** and **fail-closed**: whatever is not explicitly allowed is forbidden. No skill may run scripts, access the network, read or document secrets, embed private data, or trigger git/release/tag actions. Every skill output is a **suggestion**; the Human Maintainer decides GO / GO WITH NOTES / REWORK / STOP and performs all commit/push/tag/release actions.

## Public Neutrality

Skills and their outputs must stay public-neutral: no private project names, real private domains, secret values, private search patterns, real reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value/content must never be named, reconstructed, or output. The Public Quality Gate v0.2 (`scripts/check_public_quality.py --strict`) stays authoritative and is triggered separately (human/CI).

## Token-Economy Goal

Move the stable, repeating prompt frame (role, hard limits, neutrality/secret rules, closing format, Report to Nova, Compact Context Summary, self-check) out of the per-WP prompt and into these skills, so that prompts carry only WP-specific goals, file paths, and the proposed commit message. Target: fewer usage-limit problems, less repetition, no safety regression.

## Important Reminders

- Skills are aids for **prompt compression**, not decision-makers.
- Skills **do not replace human review** or the Public Quality Gate.
- Skills **must not** perform git/release actions.
- Skills **must not** bypass gates or activate optional WPs.
