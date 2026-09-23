# Nova Development Framework v1.1.0

## Status

**`v1.1.0` — minor release, 2026-09-23 — not a pre-release.**
**Release decision: `GO_WITH_NOTES`**, made by the Human Maintainer on 2026-09-23.

`GO_WITH_NOTES` means the release is authorised with the known limitations listed below carried into it — visible and unresolved, not converted into a plain `GO`. `v1.1.0` follows `v1.0.0` (final release, 2026-07-10) and stays within the full v1.x compatibility promise (ADR-0031), which has been active since `v1.0.0` and remains active. The annotated tag `v1.1.0` and the GitHub release are created manually by the Human Maintainer on the commit that carries these notes; no AI agent performs, or is authorised to perform, any tag, release, or push action.

## Overview

v1.1 is the first post-v1.0 work cycle: **Validation, Enablement & Operational Maturity.** Its focus was to operationally reduce items that v1.0 carried as future improvements or accepted limitations — without any breaking change. The cycle ran as NDF-WP-151 through NDF-WP-159, all docs-only, all within the active v1.x compatibility promise. NDF-WP-159 synthesized that work into the reviewable release package; the release decision itself (`GO_WITH_NOTES`, 2026-09-23) was made separately by the Human Maintainer.

## Highlights

- A token/context-efficiency baseline and a framework-wide prompt execution contract, both additive.
- Six P0 skills hardened for consistency and routing without adding, removing, or renaming any skill (pack stays at 38 docs-only skills).
- A public, step-evidenced external validation run against a generic, NDF-naive code-bearing fixture, materially deepening (but not closing) external-validation evidence.
- A public enablement dry-run clarifying the PREPARED-vs-AUTHORIZED boundary in the Project Adapter's intake phase.
- Documentation polish resolving eight prior findings, including a historical public-neutrality migration authorised explicitly by the Human Maintainer.
- A nine-dimension readiness review (WP-158) finding no blocking issue anywhere in the v1.1 path.

## Governance Improvements

- **Prompt Execution Contract Baseline** (WP-153): a framework-wide session-declaration model (four values, with a non-breaking legacy fallback), a complete-execution-instruction rule, complete-replacement semantics (`STATUS`/`SUPERSEDES`), and prompt-over-skill output precedence — anchored across the work-package lifecycle, prompt modes, templates, the Git standard, and the skill security policy.
- **Skills Pack P0 Hardening** (WP-154): exactly six `SKILL.md` files hardened (`ndf-work-package-runner` as the primary docs-only execution router; `ndf-compact-context-summary-runner`; `ndf-changelog-writer`; `ndf-release-safety`; `ndf-release-notes-runner`; `ndf-v1-readiness-review` marked historical). No skill added, removed, or renamed. Only `description` frontmatter text changed on these six files — integrity records any consumer holds for them are now stale and should be refreshed before normative reliance (see Migration / Consumer Notes).
- The Nova-vs-Human-Maintainer authority boundary (`NOVA_REVIEW != HUMAN_ACCEPTANCE`, `READY != RELEASED`, `PASS != PROMOTED`) is reaffirmed identically across every WP-151…159 artifact; no document in this release package claims acceptance, release, or authorization that has not actually happened.

## Prompt / Context Efficiency

- **Token Efficiency & Context Budget Baseline** (WP-152): context budgets B0–B4 (B1 "Lean" as the preferred normal case; B4 "Exceptional" never standard), additive prompt profiles (Lean / Handoff / Review-only / Fix) layered on the unchanged Full/Standard/Short modes, an eight-element lean work-package prompt core, a short-report format, and a skill-selection rule (do not activate the whole 38-skill pack by default).
- This WP-159 release-prep package itself was executed at the declared budget (B2 target, B3 maximum, B4 not authorised).

## Skills Pack

The pack remains **38 docs-only, fail-closed skills** under `.claude/skills/`, ADR-0032-compliant. No skill was added, removed, or renamed anywhere in v1.1. WP-154 hardened six of them (frontmatter `description` text only); `ndf-work-package-runner` is now documented as the primary execution router with 0–3 support-skill selection per work package. `ndf-v1-readiness-review` is marked historical/specialist — post-v1.0 readiness and release work routes through `ndf-release-safety` and `ndf-release-notes-runner` instead.

## External Validation

**G-13 (external validation evidence depth) is `MATERIALLY_REDUCED` — explicitly not closed.** WP-155 executed NDF's own published Independent Adapter Validation Runbook end to end (all six steps, all eleven adapter phases individually evidenced) against a generic, adversarially built, NDF-naive, code-bearing fixture held outside the repository. This addresses the **depth** limb of G-13 (the previously unevidenced runbook steps, and the "no real code" / "monorepo not covered" limits). It does **not** address the **externality/independence** limb: the run was agent-executed and the fixture was agent-authored, so it remains weaker on independence than the two pre-existing genuinely independent runs. Closing G-13 fully requires at least one genuinely independent run against a code-bearing fixture — something no single docs-only work package can produce on its own authority.

This release does not claim external validation is complete, does not claim G-13 is closed, and does not claim WP-155 achieved independent validation.

## Project Enablement

WP-156 ran a public enablement dry-run testing Project Adapter Phase 0 (Intake) and Phase 1 (Read-only Review) mechanics field-by-field against the already-public WP-155 fixture — without installing the adapter, engaging a real project, or installing any consumer skill. It found the path portable in its **PREPARED** half (agent-derivable fields) and correctly gated in its **AUTHORIZED** half (Maintainer Goals, Public/Private Status, Safety Notes remain human-only by construction). This PREPARED-vs-AUTHORIZED distinction is now documented directly in the adapter guide. **PREPARED does not mean AUTHORIZED**, and nothing in this release authorizes private-consumer-project skill use — that question remains explicitly deferred to a separate, separately authorised ADR (candidate ADR-0033).

## Public Documentation

WP-157 resolved eight prior findings (manifest-format canonicalization onto the already-dominant `PROJECT_MANIFEST.md` convention, output-structure alignment between the minimal/full adapter variants, i18n expansion of three previously German-only adapter-path documents, and PREPARED/AUTHORIZED plus terminology-namespacing clarification) without changing governance substance, ADRs, or skill behavior. One historical public-neutrality item — a private external project identifier woven into legacy file names and IDs — was migrated to a neutral scheme under explicit Human-Maintainer authorisation (8 files renamed, 11 IDs migrated, no Git history rewritten, no tag/release altered).

## Compatibility

**Fully compatible with the active v1.x promise (ADR-0031).** Every WP-151…158 artifact is additive, clarification-only, evidence-only, or non-breaking with a disclosed legacy fallback (WP-153's session-declaration requirement). No skill, ADR, prompt template, adapter convention, or public entry point was removed or incompatibly changed. No deprecation was issued. No new ADR was required or opened by WP-151…158; the one open ADR question (ADR-0032's private-consumer-skill-use scope) remains deliberately deferred, consistent with ADR-0031's "needs ADR" category — this release does not resolve it and does not need to.

## Known Limitations

The following are carried into `v1.1.0`, honestly and visibly, and are **not** resolved by this release — which is why the Human Maintainer's release decision is `GO_WITH_NOTES`, not a plain `GO`:

- **G-13 externality/independence** — `KNOWN_LIMITATION`. Depth addressed (WP-155); independence unchanged. Closure needs a genuinely independent run, outside any docs-only WP's authority.
- **PEV-004 (thin project-enablement feedback evidence)** — `KNOWN_LIMITATION`. Only one of seven feedback candidates from the first real project-feedback intake was enablement-relevant; honestly disclosed, not fabricated or resolved by assertion.
- **Single-maintainer structural bottleneck** — `STRUCTURAL`. Cannot be resolved by any docs-only work package.
- **ADR-0032 private-consumer-skill-use scope** — `DEFERRED`. Reserved for a separate, separately authorised ADR (candidate ADR-0033); neither WP-158 nor WP-159 was authorised to open it, and this release does not open it.
- **Local public-neutrality denylist not configured in the local release-prep environment** — `STRUCTURAL`. The denylist is a secret, never repository-stored; CI remains the authoritative check, as for every prior NDF release.
- **Mixed/partial i18n status** — `NON_BLOCKING`. Tracked honestly in `docs/i18n/TRANSLATION_STATUS.md`; improving incrementally, not claimed complete.
- **Stale consumer integrity records for the six WP-154-hardened skills** — `CONSUMER_ACTION`. Any consumer holding an integrity lock on `ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-changelog-writer`, `ndf-release-safety`, `ndf-release-notes-runner`, or `ndf-v1-readiness-review` should refresh and re-verify it before relying on the changed versions. NDF itself holds no governed skill lock to refresh.
- **Foundation-0.9 Context Pack field drift** — `NON_BLOCKING`. Tracked since WP-153/154; not yet actioned by any v1.1 work package.

No limitation above is claimed resolved, closed, or converted into a non-issue by this release or by its release decision.

## Migration / Consumer Notes

- Consumers holding an integrity lock on any of the six WP-154-hardened skills should refresh and re-verify their lock before treating the updated `description` text as authoritative.
- Consumers relying on `ndf-v1-readiness-review` for post-v1.0 readiness work should route to `ndf-release-safety` instead; `ndf-v1-readiness-review` is not deprecated, only marked historical/specialist.
- No consumer action is required for the token-efficiency baseline, the execution contract, or the documentation-polish changes — all are additive and backward-compatible.
- Private-consumer-project use of NDF skills remains outside ADR-0032's literal public-repository scope; this stays an open, deferred question (candidate ADR-0033), not something this release activates or authorizes.

## Changelog

The complete change list is in `CHANGELOG.md`, section `[1.1.0] - 2026-09-23`. Besides the NDF-WP-151…159 entries, that section also carries the v1.1 planning entry (NDF-WP-150) and three additive governance adoptions from a cross-project feedback package (NDF-ADOPT-CPF-001A/B/C) — all committed after `v1.0.0` and therefore part of `v1.1.0`.

## Verification

- Release-prep baseline (NDF-WP-159): `e37f2c783732cef9feff2f31145e915f23a9bdde` (branch `main`; `origin/main` at the same commit; working tree clean; index empty).
- Release-decision baseline: `fcefb4798aa75a877c53553b144c3f6bd9fa5510` (NDF-WP-159's acceptance commit; branch `main`; `origin/main` at the same commit; working tree clean; index empty). The release-state commit carrying these notes is prepared on top of it; the `v1.1.0` tag identifies that commit.
- Public Quality Gate run locally at the release-prep baseline and again for the release-state change: `--self-test` passed; `--strict` passed with 0 errors, 0 warnings, 3 notices each time (consistent with every prior WP-155…159 run; the local neutrality denylist is not configured in the local environment, a pre-existing structural condition, not a regression). CI remains the authoritative neutrality check.
- Nine-dimension governance/compatibility/evidence readiness review (WP-158, `docs/validation/v1-1/V1_1_READINESS_REVIEW.md`): all nine dimensions PASS or PASS_WITH_NOTES, none REWORK or BLOCKED.
- Release prep (WP-159) and the recording of the release decision used read-only git commands only (for example `git status -sb`, `git rev-parse HEAD`, `git rev-parse origin/main`, `git diff --cached --name-only`); no AI agent performed any stage, commit, push, fetch, tag, or release action.

## Human-Maintainer Release Authority

The release decision is the Human Maintainer's: **`GO_WITH_NOTES`, 2026-09-23**, recorded in `docs/release/V1_1_0_GO_NO_GO.md`. The Human Maintainer alone performs any staging, commit, push, tag, or GitHub release action for `v1.1.0` and alone sets the GitHub release flags. Nova's reviews (GO / GO WITH NOTES / REWORK / STOP) are evaluations, not acceptances; the WP-159 package's own `GO_WITH_NOTES` result (see `docs/validation/v1-1/V1_1_RELEASE_PREP_REVIEW.md`) concerned release-*prep* readiness only, never the release decision. `docs/release/V1_1_0_TAGGING_AND_RELEASE_GUIDE.md` remains reference only and does not itself authorise any command.
