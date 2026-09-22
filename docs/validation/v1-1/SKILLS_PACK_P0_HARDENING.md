# NDF-WP-154 — Skills Pack P0 Hardening Validation

> Work Package: `NDF-WP-154` — Skills Pack P0 Hardening
> Type: docs-only / compatibility-sensitive Skill implementation — no new, removed, or renamed skill; no runtime, tooling, or provider mechanics
> Basis: [Execution Contract](../../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md) (WP-153) · [Token Efficiency & Context Budget Baseline](../../guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md) (WP-152) · [Skills README](../../../.claude/skills/README.md) · WP notes: [WP_154 notes](../../../project-brain/WP_154_SKILLS_PACK_P0_HARDENING_NOTES.md)

## Status

Implementation complete; the Nova implementation review passed. Human-Maintainer acceptance becomes effective through the commit carrying this record. No release claim; this document accepts nothing on its own and declares no verdict on behalf of Nova or the Human Maintainer.

## Baseline

- Starting revision `70446a3` (`docs(governance): add prompt execution contract baseline` — WP-153, accepted, committed, and pushed) on `main`; the local `origin/main` tracking ref was identical; clean working tree, empty index, no merge / rebase / cherry-pick / revert / bisect in progress; no fetch.
- `v1.0.0` remains the latest release; the ADR-0031 v1.x compatibility promise is active since `v1.0.0`.
- v1.1 remains planning only — no scope lock, no release prep.
- The WP-154 commit is created by the Human Maintainer and is not recorded here.

## Scope

P0 hardening only, authorised after WP-151, WP-152, two project-local WP-152 pilots, the read-only Skills Pack Optimization Review, and WP-153:

- harden `ndf-work-package-runner` into the primary docs-only execution router;
- reconcile `ndf-compact-context-summary-runner` with the active prompt's output format and `SESSION_HANDOFF`;
- remove stale v1.0 release semantics from the release skills and the changelog writer's false v1.x invariant;
- mark `ndf-v1-readiness-review` historical / specialist;
- reconcile the skills README (pack model, output precedence, v1.0 wording, integrity-lock note);
- record the changes, their compatibility class, and the integrity-lock implications; update the minimum current-state pointers.

Not in scope: the other 32 skills; a mass trigger rewrite (P1/P2); provider mapping; the ADR-0032 private-consumer scope; formal deprecations (P3); Foundation-0.9 Context Pack drift (P1).

## Skills Changed

Exactly six `SKILL.md` files under `.claude/skills/`:

1. `ndf-work-package-runner/SKILL.md`
2. `ndf-compact-context-summary-runner/SKILL.md`
3. `ndf-changelog-writer/SKILL.md`
4. `ndf-release-safety/SKILL.md`
5. `ndf-release-notes-runner/SKILL.md`
6. `ndf-v1-readiness-review/SKILL.md`

Frontmatter: only the text of the existing `description` field changed (trigger precision: USE WHEN / DO NOT USE / USE INSTEAD); `name` unchanged; no key added or removed. Every original section is preserved (the 13 required fields, plus the existing release/governance section where present). Added sections are additive: runner — *Execution start*, *Support-skill selection*, *Output precedence*; summary runner — *Format precedence*, *Next-step and handoff essentials*; release safety — *Human-Maintainer command guidance*; v1 readiness — *Status*.

## Human-Maintainer Decisions Respected

| Decision (binding) | How respected |
|---|---|
| P0 scope = exactly the six named skills | six `SKILL.md` changed; the other 32 unchanged |
| Core candidate set: runner, summary runner, neutrality guard, context-pack maintainer; changelog writer = support skill | runner routing table and README pack model; neutrality guard and context-pack maintainer unchanged |
| Core skills are not forced blindly | "selected per task, not forced blindly" (runner, README) |
| Provider-neutrality boundary | no `disable-model-invocation`, `allowed-tools`, plugin / marketplace metadata, or installation mechanics; AUTO_CORE / EXPLICIT / LEGACY_CANDIDATE documented only as NDF semantic categories |
| ADR-0032 private-consumer scope unresolved | ADR-0032 unchanged, no ADR-0033; the runner keeps only a reserved, explicitly inactive placeholder |
| `ndf-v1-readiness-review` kept, not deprecated | name and file kept; "not deprecated"; no version-specific replacement created |
| `ndf-public-release-body-reviewer` kept | unchanged; referenced as the dedicated release-body reviewer |

## Per-Skill Before / After Intent

| Skill | Before (problem) | After (intent) | Class |
|---|---|---|---|
| `ndf-work-package-runner` | generic WP scaffold; no execution-header, profile/budget, or support-skill routing; "missing / ambiguous context → request Full Prompt Mode"; no output precedence; pre-WP-153 authority wording | primary docs-only execution router: header (`SESSION` / `STATUS` / `SUPERSEDES`, legacy fallback), complete / `COMPLETE REPLACEMENT` handling and delta-only STOP, mode / profile / budget recognition without lowering, fail-closed escalation within the declared maximum, preflight, visible frame, 0–3 support skills, prompt-over-skill precedence, explicit non-runtime boundary, WP-153 authority wording, inactive consumer placeholder | behavioral non-breaking + additive + clarification |
| `ndf-compact-context-summary-runner` | "Two blocks only" — a fixed shape that could conflict with the active prompt's return format; no handoff essentials | format precedence (prompt format → mandatory minimum content → Short Report for B0/B1 → standard Report to Nova → blocked report); next-step session, profile / budget, do-not-reload, forbidden work, invariants; no duplication of prompt-carried `SESSION_HANDOFF` fields | behavioral non-breaking + additive |
| `ndf-changelog-writer` | false "not v1.0 / no RC / full v1.x promise not active" invariant; no scope-based trigger | status only from authoritative records (v1.x promise active since `v1.0.0`); honest `[Unreleased]` entries; compatibility class where relevant; used only when the CHANGELOG is in the authorised scope | clarification + behavioral non-breaking |
| `ndf-release-safety` | RC / final-v1.0 framing; promise activation described as a future final-v1.0 step | version-neutral: pre-release / final, major / minor / patch, ADR-0031 compatibility checks (active since `v1.0.0`), criteria from the current release scope, Human-Maintainer command guidance per the Execution Contract | clarification + additive |
| `ndf-release-notes-runner` | RC / Foundation / final framing; promise described as a final-v1.0 step | version-neutral labels; compatibility statement; migration notes; visible known notes and limitations; release-body checks (flags, known notes, compatibility claims, neutrality) | clarification + additive |
| `ndf-v1-readiness-review` | implied v1.0 still pending and the promise awaiting activation; read as the general readiness process | historical / specialist status; post-v1.0 readiness redirected to `ndf-release-safety`; name kept, not deprecated | clarification |

## Compatibility

ADR-0031 classes:

| Class | Result |
|---|---|
| Clarification | v1.0 / v1.x status wording in the four release-related skills and the skills README; authority wording (Nova verdict ≠ Human-Maintainer acceptance) in the runner and the summary runner; trigger descriptions |
| Behavioral non-breaking | runner escalation follows the fail-closed step instead of "request Full"; the summary shape follows the active prompt (the standard Report to Nova stays the default where no prompt format exists); the changelog writer triggers only with the CHANGELOG in scope |
| Additive | new sections (execution start, support-skill selection, output / format precedence, handoff essentials, command guidance, status); skills README pack-model, output-precedence, and integrity-lock sections |
| Breaking | none |
| Needs ADR | none — the ADR-0032 private-consumer scope stays deferred to a separate ADR |

Checks: no skill name removed or renamed; no public entry point removed; Full / Standard / Short semantics unchanged; WP-152 profiles and budgets unchanged; no deprecation declared.

## Integrity-Lock Implications

Governance: [Skill Provenance and Integrity Lock](../../agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md).

- **NDF holds no governed integrity record for its own skills:** no lock, manifest, or digest file exists — no JSON / YAML / TOML / lock file references `.claude/skills` or `SKILL.md`, and the governance itself states "Tooling Status: Not implemented". No repository-owned lock must change; `INTEGRITY_LOCK_SCOPE_DECISION_REQUIRED` was not triggered.
- **Stale records:** any consumer hash or lock entry for the six changed files no longer matches — verification would report `modified` (§13). Before relying on the changed versions for normative or security-sensitive work, a consumer must refresh and re-verify those records (§15, §20: review, new integrity values, Human-Maintainer approval). Records for the other 32 skills are unaffected by WP-154.
- No consumer lock was modified and no consumer is assumed to exist. This neither authorises nor extends private consumer-project use (ADR-0032 question open).
- **Pre-change content identification** (evidence only, not a lock record) — SHA-256 over the committed file bytes at `70446a3`:

```text
3d231df07dd350b31f027ce569d683331485cbd8b1fc2891696e4e7617b36ae5  .claude/skills/ndf-work-package-runner/SKILL.md
cc8ec4ff0dbe0dc1ea6952cd125ed64ecb58af8b800ae0ff9105c72a7c660a65  .claude/skills/ndf-compact-context-summary-runner/SKILL.md
77e9b316303edf5b69a27ed26eba991c0ae8c6c7ce15145d7eb0f18929dc3b56  .claude/skills/ndf-changelog-writer/SKILL.md
4168e0e88ec3ccf40a7b926c3d81e79c6ac26993673f48acdeb5aad5b02a9fd1  .claude/skills/ndf-release-safety/SKILL.md
1204ef76a7923c0be4525f76f1ff8f9626de81a83efdbe560ddcfb10b27f2ab1  .claude/skills/ndf-release-notes-runner/SKILL.md
3e0107c4f3f5158792919dbba5d32b8dc862e45ac2bdd85a14552a7ee56ff71a  .claude/skills/ndf-v1-readiness-review/SKILL.md
```

Post-change digests are deliberately not recorded: the accepted content is fixed only by the Human-Maintainer commit, from which re-verification computes them.

## Validation

Final state, checked read-only:

- `git diff --check`: clean; the two new files have no trailing whitespace.
- `git diff --cached --name-only`: empty (index empty).
- Scope: 12 modified and 2 created paths (14), all within the authorised WP-154 file set; `git diff --name-only -- '.claude/skills/*/SKILL.md'` → exactly the six skills; no other `SKILL.md`; no change under `docs/adr/` or `framework/prompts/blocks/`.
- Frontmatter (script comparison against `70446a3`): keys unchanged (`name`, `description`) in all six; `name` values unchanged; descriptions 369–497 characters without YAML-breaking `": "` / `" #"` sequences (PyYAML is not installed locally; the local agent client listed all six skills with their new descriptions — an observation, not a provider guarantee).
- Sections: every pre-change section heading is still present in all six files.
- Stale-phrase scan (six skills + skills README): no hit for "promise not active", "activate the (v1.x) promise", "only at final", "final-v1.0 step", "not v1.0", "no RC", "Two blocks only", "request Full Prompt Mode", "RC / Foundation / final".
- Runner semantics present: Execution Contract link, all four `SESSION` values, `SESSION REASON`, `COMPLETE` / `COMPLETE REPLACEMENT`, `SUPERSEDES`, legacy fallback, delta-only STOP, Lean / Handoff / Review-only / Fix, B0–B4, "never lower", 0–3 support skills, Rule 4 precedence, non-runtime list.
- Public quality gate: `python scripts/check_public_quality.py --self-test` passed; `--strict` passed (0 errors, 0 warnings; new files scanned). No local denylist is configured, so the denylist-term scan did not run locally; CI with `NDF_PUBLIC_NEUTRALITY_DENYLIST` stays authoritative.
- Relative links: all 182 relative links in the 14 changed / created Markdown files resolve; 0 broken.
- No network access, no package installation, and no Git write by Claude; HEAD remained at `70446a3` throughout implementation, the state-closure rework, and validation.

## Acceptance Evidence

| AC | Criterion | Evidence |
|---|---|---|
| AC-01 | exactly six `SKILL.md` modified | `git diff --name-only -- '.claude/skills/*/SKILL.md'` → 6 |
| AC-02 | no seventh `SKILL.md` | `git status --porcelain -- .claude/skills` → the six plus `README.md` |
| AC-03 | no skill created / renamed / removed | 38 skill directories unchanged; no untracked path under `.claude/skills/` |
| AC-04 | runner understands WP-153 headers | runner *Execution start* 1–2 |
| AC-05 | runner recognises WP-152 profiles and budgets | runner *Execution start* 3 |
| AC-06 | bounded support-skill selection | runner *Support-skill selection* (0–3, per-budget totals, never the whole pack) |
| AC-07 | no direct Full escalation on unclear context | runner *Execution start* 3 and *Fail-closed behavior* |
| AC-08 | prompt-over-skill output precedence | runner *Output precedence* |
| AC-09 | no conflicting fixed summary shape | summary *Format precedence* ("No fixed block count"); "Two blocks only" removed |
| AC-10 | next-step session / handoff essentials | summary *Next-step and handoff essentials* |
| AC-11 | no false v1.x-inactive invariant | changelog writer *Expected outputs*; stale scan clean |
| AC-12 | changelog writer only with CHANGELOG in scope | changelog writer description and *When to use* |
| AC-13 | release safety version-neutral, ADR-0031 active | release safety *Expected outputs* and *Release/governance limitations* |
| AC-14 | command guidance per Complete Execution Instruction | release safety *Human-Maintainer command guidance* |
| AC-15 | release notes version-neutral with compatibility / migration notes | release notes *Expected outputs* |
| AC-16 | v1 readiness points to `ndf-release-safety` | v1 readiness description, *Status*, *When to use* |
| AC-17 | v1 readiness not deleted / renamed / deprecated | file and `name` unchanged; *Status* "not deprecated" |
| AC-18 | README documents output precedence | skills README *Output Precedence* |
| AC-19 | README reconciles the core / support model | skills README *Pack Model* |
| AC-20 | README has no stale promise-activation claim | skills README *Non-Goals* and item 11; stale scan clean |
| AC-21 | integrity-lock implications documented | skills README *Integrity Locks*; this document; WP notes |
| AC-22 | private consumer scope unresolved, not expanded | runner *Required inputs* (reserved, not active); README note; ADR-0032 unchanged |
| AC-23 | no provider mechanics | frontmatter keys unchanged; no provider keys added |
| AC-24 | no ADR changed | no change under `docs/adr/` |
| AC-25 | no execution-contract semantics changed | `framework/prompts/blocks/` unchanged; the skills reference the block |
| AC-26 | WP-153 completed at `70446a3` | `README.md`, `docs/roadmap/V1_1_PLAN.md`, Context Pack, Next Phase |
| AC-27 | WP-154 not prematurely completed | superseded by the state-closure replacement instruction: the state artifacts record WP-154 as completed through the Human-Maintainer acceptance commit carrying this record; no commit hash is invented |
| AC-28 | roadmap WP-153…159 as authorised | `V1_1_PLAN.md` WP table — no renumbering |
| AC-29 | v1.1 planning only | `V1_1_PLAN.md` status and decision; `CHANGELOG.md` `[Unreleased]` |
| AC-30 | validation artifact exists | this document |
| AC-31 | WP notes exist | `project-brain/WP_154_SKILLS_PACK_P0_HARDENING_NOTES.md` |
| AC-32 | public neutrality gate passes locally | Validation (self-test + strict) |
| AC-33 | `git diff --check` passes | Validation |
| AC-34 | only authorised paths | Validation (scope) |
| AC-35 | index empty | Validation |
| AC-36 | no stage / commit / push / fetch / tag / release | HEAD unchanged at `70446a3`; index empty |

## Known Notes

- The WP-154 execution header used the `STATUS` literal `COMPLETE EXECUTION PROMPT` plus a `SUPERSEDES` line (the Execution Contract defines `SUPERSEDES` for `COMPLETE REPLACEMENT`). Read as `COMPLETE`; non-blocking, since no earlier instruction version existed in the session to merge.
- `ndf-public-release-body-reviewer` stays unchanged; it remains a future consolidation / deprecation candidate, not decided here.
- Trigger review of the other 32 skills remains P1/P2; provider mapping of AUTO_CORE / EXPLICIT / LEGACY_CANDIDATE remains later work.
- A formal deprecation of `ndf-v1-readiness-review` is P3 and requires the ADR-0031 process.
- ADR-0032 private consumer-project use requires a separate ADR (candidate ADR-0033); nothing is authorised here.
- Older Foundation-0.9 Context Pack drift (Status, Known Notes, What Must Not Be Claimed) remains — P1 state hardening, not touched here.
- The skills README *Security Boundaries* section keeps the pre-WP-153 phrase "the Human Maintainer decides GO / GO WITH NOTES / REWORK / STOP". It is not contradictory (the Human Maintainer remains the final owner) and lies outside the P0 changes; aligning it with the Nova-verdict wording is a P1 candidate.
- The read-only Skills Pack Optimization Review has no repository artifact; its findings enter only via the Human-Maintainer-authorised WP-154 contract.
- After the Nova implementation review, a bounded state-closure rework adjusted only the lifecycle and current-state wording (README, v1.1 plan, Context Pack, Next Phase, this record, the WP notes, and the changelog entry's state clause) so the accepting commit does not immediately invalidate its own state documents. No `SKILL.md` and no skills README change was part of that rework; the six Skill files stayed byte-for-byte identical (verified by SHA-256 before and after).

## Result

**IMPLEMENTED — NOVA REVIEW PASSED; HUMAN-MAINTAINER ACCEPTANCE EFFECTIVE THROUGH THE COMMIT CARRYING THIS RECORD**
