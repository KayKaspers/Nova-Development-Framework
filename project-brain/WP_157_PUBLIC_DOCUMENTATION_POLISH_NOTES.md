# WP-157 — Public Documentation Polish (Notes)

## Work Package

`NDF-WP-157 – Public Documentation Polish` — resolve the documentation-quality and cross-artifact-consistency findings recorded by WP-155 (EVI-001…006, EVI-008) and WP-156 (PEV-001…005), plus a deferred historical public-neutrality drift, without changing NDF's governance model or adding functionality. Profile: Public Documentation Polish / Cross-Artifact Consistency, Prompt Mode Full, budget B2 target / B3 maximum, B4 not authorised. Support skill: `ndf-work-package-runner` (routing).

## Baseline

Revision `270c6c519d420c4bc16869bf67ff9c6abc265361`, branch `main`, working tree clean, index empty at preflight, `origin/main` at the same commit. v1.0.0 final released, v1.x promise active (ADR-0031); v1.1 planning only.

## Resolved Paths

Manifest: `docs/project-system/PROJECT_MANIFEST_SPEC.md`, `framework/project-system/templates/project-manifest.template.yaml`, `framework/project-starter/templates/INITIAL_PROJECT_MANIFEST.yaml`, `docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml`, `examples/minimal-ndf-project/project-system/project-manifest.yaml`. Output structure: `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`, `docs/project-starter/PROJECT_ADAPTER_V0_2.md`. i18n: same two plus `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md` and `docs/i18n/TRANSLATION_STATUS.md`. Enablement/authority: `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` (§7.1), the adapter guide (§4, §6), the intake template (per-field labels). Historical neutrality: identified, reported, then migrated under Human-Maintainer Option A — 8 files renamed (`docs/validation/cross-project-feedback/CROSS_PROJECT_FEEDBACK_001_*`, `project-brain/CROSS_PROJECT_FEEDBACK_001_*_NOTES.md`), 10 further files neutralised in place — see below.

## Finding Outcome Matrix

| Finding | Status |
|---|---|
| EVI-001 | RESOLVED |
| EVI-002 | RESOLVED |
| EVI-003 | RESOLVED |
| EVI-004 | RESOLVED |
| EVI-005 | RESOLVED |
| EVI-006 | RESOLVED |
| EVI-008 | RESOLVED |
| PEV-001 | RESOLVED |
| PEV-002 | RESOLVED |
| PEV-003 | CLARIFIED (documentation-only; `SKILL.md` untouched) |
| PEV-004 | RETAINED_LIMITATION |
| PEV-005 | RESOLVED |
| Historical Neutrality Drift | RESOLVED (via Human-Maintainer Option A migration) |

## Skill Clarification

**Not required.** PEV-003 was fully resolved by a cross-reference added in `docs/project-starter/PROJECT_ADAPTER_V0_2.md` §6, stating which of the nine intake fields `ndf-existing-project-analysis-runner`'s output can (six, AGENT-PREPARABLE) and cannot (three, HUMAN-REQUIRED) cover. `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md` was not opened for editing; no behavior change, no integrity-lock impact for consumers holding a verification record of that skill.

## Manifest Decision

No `MANIFEST_CANONICAL_FORMAT_DECISION_REQUIRED` was triggered. The source hierarchy already had a clear, cross-referenced answer: `PROJECT_ADAPTER_CONVENTIONS.md` (WP-059, self-described as binding), the adapter guide's Phase-3 row, and the output-structure template all independently state `PROJECT_MANIFEST.md` (Markdown, embedded YAML/JSON allowed) is canonical. Only `PROJECT_MANIFEST_SPEC.md` (zero mentions of Markdown/canonical) and the shipped YAML artifacts disagreed. The spec and four shipped YAML artifacts were aligned to the existing convention; no new representation was invented.

## Public Neutrality Outcome

Repository-wide manual search (`NDF_PUBLIC_NEUTRALITY_DENYLIST` not configured locally) found one historical drift item: a legacy file family named and described a specific external project across what the initial pass counted as 12 files and 11 embedded work-package/candidate IDs. That pass was first reported as `HISTORICAL_PATH_NEUTRALITY_DECISION_REQUIRED` rather than resolved silently, since a content-only prose edit would have left the identifier exposed in every file name and ID.

The Human Maintainer then authorised **Option A — full neutralisation**. Re-discovery during the migration found the true scope was 18 files (the initial case-sensitive-only search had missed 2 mixed-case mentions). Executed: 8 files renamed to a neutral `CROSS_PROJECT_FEEDBACK_001`/`CPF` naming scheme (file-family prefix and all three ID families), 11 IDs migrated, and 10 further files (including the current `CHANGELOG.md` entry and this WP's own artifacts) had their prose neutralised — 18 files total. No Git history was rewritten, no tag or release was altered, and no pending status was changed to accepted. A post-migration repo-wide scan for the legacy token and its ID patterns returned 0 current-tree matches. No new private identifier was introduced anywhere in this WP's own edits.

## Compatibility

CLARIFICATION / DOCUMENTATION-ONLY / ADDITIVE. No breaking change. No skill, ADR, prompt, template, standard, spec, adapter, or example *design* changed — content aligned to already-established conventions, one stale example corrected, three documents made bilingual, cross-reference notes added. No phase added/removed/resequenced. ADR-0031/0032 unchanged; ADR-0032's private-consumer scope question stays reserved for a separate, separately authorised ADR (candidate ADR-0033). Needs ADR: no.

## Limitations

PEV-004 stays a thin, accepted evidence limitation (1 of 7 feedback candidates enablement-relevant; its own adoption still pending) — not addressed here, not falsely claimed resolved. The historical-neutrality item is now resolved (Option A migration complete). `docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml`'s own `ndf_level`/quality-flag consistency (independent of EVI-004) was observed but is outside this WP's authorised scope. Single-maintainer bottleneck untouched, consistent with every prior v1.1 WP. No token counts (no instrumentation under ADR-0032).

## Validation Summary

Public Quality Gate self-test and strict mode both passed locally against the full changed tree (0 errors, 0 warnings). `git diff --check` clean. All relative Markdown links in changed/renamed files resolve. Index empty throughout (no staging performed at any point, including the migration). No skill, ADR, or Project-Adapter-version file changed. The 8 renames are the only filesystem renames in this WP; all are within the authorised historical-neutrality migration scope. No new private identifiers introduced. Post-migration scan: 0 current-tree matches for the legacy token or its IDs. No network use. No stage, commit, push, fetch, tag, or release.

## Next WP if Accepted

`NDF-WP-158 – v1.1 Readiness Review` — next planned, **not started**; requires its own complete execution prompt. **WP-158 must not start before Human-Maintainer acceptance (commit) of WP-157 is complete and verified.** The historical-neutrality migration (Option A) is complete and folded into WP-157's own scope; it is no longer a separate blocker for acceptance.

## Forbidden Premature Work

No WP-158 start; no further, unauthorised neutrality cleanup beyond the Option-A-derived scope; no ADR change and no ADR-0033; no `SKILL.md` change beyond what was actually needed (none was); no Project-Adapter redesign or version change; no expansion of the ADR-0032 consumer scope; no real project migration or adapter installation; no consumer Skill install; no provider mechanics; no runtime; no v1.1 scope lock or release prep; no git write action of any kind.

## Compact Context Summary

WP-157 resolved the documentation-consistency findings WP-155 and WP-156 recorded but explicitly did not fix, entirely from already-established NDF authority — no new representation, phase, or governance rule was invented. **Manifest (EVI-001…004):** `PROJECT_MANIFEST.md` (Markdown, embedded YAML/JSON) was already the clearly cross-referenced canonical format across three sources; the one outlier spec and four shipped YAML templates/examples were aligned to it, and one stale example's `status`/`ndf_level` corrected to the spec's own enum/ladder. **Output structure (EVI-005/006):** the minimal-variant list now matches the actual minimal phase chain (Project Brain removed, since Phase 4 doesn't run there); the full-variant `docs/ndf/*` files are now attributed to the bundled Phase 2–8 execution that actually produces them (`PROJECT_SYSTEM_BASELINE_PROMPT.md` — a file WP-155's own reproduce grep had excluded). **i18n (EVI-008):** the three previously German-only adapter-path documents are now bilingual using NDF's existing paired-heading convention, with `TRANSLATION_STATUS.md` reconciled. **Enablement/authority (PEV-001/002/003/005):** the `NDF-B0`…`NDF-B4`/`NDF-Lean` namespacing rule, the PREPARED-vs-AUTHORIZED split, and per-field AGENT-PREPARABLE/HUMAN-REQUIRED labels are now documented in the guide/template themselves; PEV-003 was resolved by a documentation cross-reference without touching `SKILL.md`. **PEV-004** stays an honest, visible, accepted evidence limitation. **Historical neutrality:** one drift item (a legacy file family built around a specific external project's name, spanning what re-discovery showed was 18 files and 11 embedded IDs — more than the initial case-sensitive-only estimate) could not be repaired proportionately by content edits alone in its first pass and was reported as `HISTORICAL_PATH_NEUTRALITY_DECISION_REQUIRED`. On explicit Human-Maintainer authorisation (Option A, full neutralisation), it was then migrated: 8 files renamed to a neutral `CROSS_PROJECT_FEEDBACK_001`/`CPF` scheme, 11 IDs migrated, all current-tree references updated, no Git history rewritten, no tag/release altered, post-migration scan 0 matches. No ADR, Skill, or Project-Adapter version changed; compatibility CLARIFICATION/DOCUMENTATION-ONLY/additive; gate green (0 errors/warnings); artifacts are the validation record `docs/validation/v1-1/PUBLIC_DOCUMENTATION_POLISH.md` and these notes. **IMPLEMENTED — NOVA REVIEW PASSED; HUMAN-MAINTAINER ACCEPTANCE EFFECTIVE THROUGH THE COMMIT CARRYING THIS RECORD.** WP-158 is next planned and not started.
