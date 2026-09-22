# NDF-WP-153 — Prompt Execution Contract Baseline Validation

> Work Package: `NDF-WP-153` — Prompt Execution Contract Baseline (including the final rework / governance closure)
> Type: docs-only governance implementation — no runtime, tooling, or enforcement machinery
> Normative block: [BLOCK_EXECUTION_CONTRACT.md](../../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md) · WP notes: [WP_153 notes](../../../project-brain/WP_153_PROMPT_EXECUTION_CONTRACT_BASELINE_NOTES.md)

## Status

Implementation complete, pending Nova / Human-Maintainer acceptance. No release claim. This document declares no GO on behalf of Nova or the Human Maintainer.

## Baseline

- Starting revision: `c4c1c34` (`docs(context): add token efficiency baseline`) on `main`; the local `origin/main` tracking ref was identical; clean working tree and empty index at start; no fetch.
- `v1.0.0` remains the latest released baseline; the full v1.x promise stays active (ADR-0031).
- v1.1 remains planning only — no scope lock, no release prep.
- The WP-153 commit is created by the Human Maintainer and is not recorded here.

## Scope

- **Session Declaration** — `SESSION` is exactly one of `SAME_SESSION_ALLOWED`, `SAME_SESSION_RECOMMENDED`, `NEW_SESSION_RECOMMENDED`, `NEW_SESSION_REQUIRED`; `SESSION REASON` for every value except `SAME_SESSION_ALLOWED`; mandatory for newly authored execution prompts; legacy fallback `NEW_SESSION_RECOMMENDED` + `SESSION_DECLARATION_MISSING_LEGACY`.
- **Complete Execution Instruction** — one self-contained active contract; stable rules referenced, not copied; `COMPLETE != VERBOSE`.
- **Complete Replacement** — after a contract change the successor is issued in full (`STATUS: COMPLETE REPLACEMENT`, `SUPERSEDES`); delta-only executable corrections are invalid.
- **Option-selection exception** — a Human-Maintainer choice among fully defined options needs no replacement unless scope, authority, files, operations, commands, acceptance criteria, or STOP conditions change.
- **Prompt-over-Skill precedence** — the active authorised prompt's return format wins over a generic Skill output contract; higher normative minimum content is fitted in; real conflicts fail closed.
- **CLI applicability** — agent prompts and Human-Maintainer command sequences: PowerShell, Bash/sh, CMD, Git, Docker/Docker Compose, infrastructure CLI, other executable blocks.
- **Roadmap insertion** — WP-153 Prompt Execution Contract Baseline and WP-154 Skills Pack P0 Hardening inserted; former WP-153…157 → WP-155…159.

## Human-Maintainer Decisions

Binding decisions implemented by this WP (from the Human-Maintainer-authorised WP-153 execution contract):

1. Every newly authored execution instruction declares one of the four session values; a reason is required except for `SAME_SESSION_ALLOWED`.
2. Missing declaration: new prompt → prompt defect (REWORK + complete replacement); legacy prompt → non-blocking fallback `NEW_SESSION_RECOMMENDED` + `SESSION_DECLARATION_MISSING_LEGACY` (v1.x compatibility).
3. A pure Human-Maintainer option selection needs no replacement only while scope, authority, files, operations, commands, acceptance criteria, and STOP conditions stay unchanged.
4. Every executable instruction set — agent prompt or Human-Maintainer command sequence — is one complete, self-contained contract; complete ≠ verbose.
5. Corrections are regenerated in full and marked as superseding; delta-only corrections are invalid.
6. The active prompt's output format wins over generic Skill output contracts; higher normative reporting stays binding.
7. Human-Maintainer command sequences name shell, working directory, preconditions, ordered commands, expected result, verification, and STOP condition.
8. ADR-0032's private-consumer Skill scope needs a separate ADR (candidate ADR-0033); ADR-0032 is not changed here.
9. Roadmap: WP-153/154 inserted, WP-155…159 follow; v1.1 stays planning only.
10. Final rework: README current-state line, prompt-index registration, this validation document, and the WP notes.

## Compatibility

| Class | Result |
|---|---|
| Additive | yes — new block, header fields, sections, index entry, roadmap rows, evidence artifacts |
| Clarification | yes — Skill output precedence, historical labelling in Prompt Modes, core skill set reconciled with the Skills-first baseline |
| Behavioral non-breaking | yes — legacy prompts stay executable (fallback); Full/Standard/Short and the WP-152 profiles unchanged; Git authority unchanged |
| Breaking change | none |
| ADR-0032 private-consumer scope | deferred to a separate ADR decision; ADR-0032 unchanged |

## Acceptance Evidence

Original WP-153 acceptance criteria → evidence (repo-relative paths and checks):

| AC | Criterion | Evidence |
|---|---|---|
| AC-01 | block defines the four rules, no runtime machinery | `framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md` (Rules 1–4, header note) |
| AC-02 | templates declare session and status | `docs/templates/LEAN_WP_PROMPT_TEMPLATE.md`, `REVIEW_ONLY_PROMPT_TEMPLATE.md`, `FIX_PROMPT_TEMPLATE.md`; `SESSION_HANDOFF_TEMPLATE.md` (`Session for next step`) |
| AC-03 | legacy fallback non-breaking | block Rule 1; `docs/agent-workflows/NDF_PROMPT_MODES.md` (Execution Header DE/EN) |
| AC-04 | new prompts must declare | block Rule 1; `NDF_PROMPT_MODES.md`; `framework/standards/WORK_PACKAGE_LIFECYCLE.md` §3 |
| AC-05 | complete replacement, no delta | block Rule 3; lifecycle §6/§13; template notes; `standards/git-standard.md` |
| AC-06 | narrow option-selection exception | block Rule 3; lifecycle §13 |
| AC-07 | CLI coverage | block scope line and Rule 2; `standards/git-standard.md` (Befehlsfolgen für den Human Maintainer) |
| AC-08 | COMPLETE != VERBOSE; WP-152 intact | block Rule 2; `NDF_PROMPT_MODES.md`; `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` §9 |
| AC-09 | prompt-over-Skill precedence | block Rule 4; `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (Ausgabevorrang DE/EN) |
| AC-10 | no ADR-0032 scope expansion | policy text states no scope change; `docs/adr/` unchanged; `docs/roadmap/V1_1_PLAN.md` risks |
| AC-11 | no SKILL.md change | `git status -- .claude/skills` → no change |
| AC-12 | roadmap WP-153…159 | `docs/roadmap/V1_1_PLAN.md` (WP table, mapping, decision) |
| AC-13 | no stale WP-152 pre-commit claim | `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`, `project-brain/NEXT_PHASE_FOUNDATION_0_9.md` (search clean) |
| AC-14 | no scope-lock / release-prep claim | `V1_1_PLAN.md` decision; `CHANGELOG.md` [Unreleased] |
| AC-15 | public neutrality | public quality gate (Validation); no URLs, domains, emails, or private names added |
| AC-16 | `git diff --check` passes | Validation |
| AC-17 | only authorised files | `git diff --name-only` and the untracked list (Validation) |
| AC-18 | index empty | `git diff --cached --name-only` → empty |
| AC-19 | no Git write by Claude | HEAD unchanged at `c4c1c34`; no stage/commit/push/fetch/tag/release |

## Validation

Final state, checked read-only after the final rework:

- `git diff --check`: clean; the new files have no trailing whitespace.
- Public quality gate: `python scripts/check_public_quality.py --self-test` passed; `--strict` passed (0 errors, 0 warnings; new files scanned). No local denylist is configured, so the denylist-term scan did not run locally; CI with `NDF_PUBLIC_NEUTRALITY_DENYLIST` stays authoritative.
- Link validation: all 165 relative links in the 18 WP-153 changed/created files resolve; 0 broken.
- No `SKILL.md` changes; no `docs/adr/` changes.
- Index empty (`git diff --cached --name-only`).
- No Git write by Claude; all changes stay uncommitted for Human-Maintainer review.
- Scope: 15 modified and 3 created paths, all within the authorised WP-153 file set.

## Known Notes

- README drift (current WP still WP-152) — fixed by the final rework.
- `PROMPT_INDEX.md` omission of the new block — fixed by the final rework.
- Older Foundation-0.9 Context Pack drift (Status, Known Notes, What Must Not Be Claimed) remains — P1 state hardening, not touched here.
- ADR-0032 private-consumer Skill scope requires a separate ADR decision (candidate ADR-0033); nothing is authorised here.
- No release, no tag, no v1.1 scope lock, no release prep.
- Resolved by the final authority reconciliation: Nova issues review verdicts, while the Human Maintainer remains the final owner of normative acceptance, scope changes, ADR acceptance, and Git/release actions (`NOVA_REVIEW != HUMAN_ACCEPTANCE`; block, lifecycle §6, Skill Security Policy, and the v1.1 plan's Human-Maintainer-only row aligned; ADR-0032 unchanged). "Legacy" means authored before the Human-Maintainer commit accepting NDF-WP-153 (no hash embedded). The authority vocabulary (`DERIVE != DECLARE` …) is confirmed by that reconciliation.
- The read-only Skills Pack Optimization Review has no repository artifact; its findings enter only via the Human-Maintainer-authorised WP-153 contract.

## Result

**IMPLEMENTED — PENDING NOVA / HUMAN-MAINTAINER ACCEPTANCE**
