# NDF-WP-157 — Public Documentation Polish

## Status

IMPLEMENTED — NOVA REVIEW PASSED; HUMAN-MAINTAINER ACCEPTANCE EFFECTIVE THROUGH THE COMMIT CARRYING THIS RECORD

## Baseline

- Starting revision: `270c6c519d420c4bc16869bf67ff9c6abc265361`
- Branch: `main`, working tree clean, index empty at preflight; `origin/main` at the same commit; no merge/rebase/cherry-pick/revert/bisect in progress.
- Released state: **v1.0.0 final**; the full v1.x compatibility promise is active from `v1.0.0` per [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md).
- v1.1: **planning only** — not scope-locked, not released.
- Prompt profile: Public Documentation Polish / Cross-Artifact Consistency · Prompt Mode Full · context budget B2 target, B3 maximum, B4 not authorised.
- Support skill: `ndf-work-package-runner` (routing).
- No network access, no package installation, no git write action, no Skill created/removed/renamed, no ADR change.

## Scope

Resolve the documentation-quality and cross-artifact-consistency findings recorded by [WP-155](EXTERNAL_VALIDATION_IMPROVEMENT.md) (EVI-001…006, EVI-008) and [WP-156](PROJECT_ENABLEMENT_VALIDATION.md) (PEV-001…005), plus one historical public-neutrality drift. The drift was first reported as a blocked decision, then resolved by a bounded rename/ID/link migration under explicit Human-Maintainer authorisation (Option A) once that decision was made — see [Historical Neutrality Migration](#historical-neutrality-migration). Neither the original repair pass nor the migration changed NDF's governance model or added functionality. This is documentation polish, consistency repair, and a scoped public-neutrality migration — not new governance, not a new adapter version, not a new Skill design, not Project Enablement, not external validation, not v1.1 readiness or release prep.

## Resolved Document Paths

Located before editing, per finding:

| Finding(s) | Path |
|---|---|
| EVI-001/002/003 | `docs/project-system/PROJECT_MANIFEST_SPEC.md` |
| EVI-002 | `framework/project-system/templates/project-manifest.template.yaml`, `framework/project-starter/templates/INITIAL_PROJECT_MANIFEST.yaml`, `docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml` |
| EVI-002/004 | `examples/minimal-ndf-project/project-system/project-manifest.yaml` |
| EVI-005/006 | `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`, `docs/project-starter/PROJECT_ADAPTER_V0_2.md` |
| EVI-008 | `docs/project-starter/PROJECT_ADAPTER_V0_2.md`, `docs/project-system/PROJECT_MANIFEST_SPEC.md`, `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md`, `docs/i18n/TRANSLATION_STATUS.md` |
| PEV-001 | `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` |
| PEV-002 | `docs/project-starter/PROJECT_ADAPTER_V0_2.md` |
| PEV-003 | `docs/project-starter/PROJECT_ADAPTER_V0_2.md` (resolved outside `SKILL.md` — see [Skill Clarification](#skill-clarification)) |
| PEV-004 | no file change; visibility check only (see [Findings](#finding-matrix)) |
| PEV-005 | `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md` |
| Historical neutrality | `docs/validation/cross-project-feedback/CROSS_PROJECT_FEEDBACK_001_*.md` (renamed from a legacy-token-named family), `project-brain/CROSS_PROJECT_FEEDBACK_001_*_NOTES.md` (renamed), `CHANGELOG.md` (2 entries), `docs/governance/NDF_EXTERNAL_FRAMEWORK_TAILORING_GUIDANCE.md`, `docs/governance/NDF_DECISION_AND_STATUS_MODELING_GUIDANCE.md`, `docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md`, `docs/validation/v1-1/SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW.md`, `project-brain/WP_151_SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW_NOTES.md` — migrated under Human-Maintainer Option A, see [Historical Neutrality Migration](#historical-neutrality-migration) |

Every changed file maps to at least one named finding; state files (this record, WP notes, `CHANGELOG.md`, `README.md`, `docs/roadmap/V1_1_PLAN.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`, `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`) are the always-authorised WP-157 state artifacts.

## Finding Matrix

| Finding | Before | Source of truth | Action | Files | Validation | Status |
|---|---|---|---|---|---|---|
| EVI-001 | `PROJECT_MANIFEST_SPEC.md` never mentioned Markdown/canonical; contradicted the conventions | `PROJECT_ADAPTER_CONVENTIONS.md` (WP-059, explicitly "binding") + adapter guide Phase-3 row + output-structure template, all independently stating `PROJECT_MANIFEST.md` (Markdown) is canonical | Aligned the spec to the existing convention: added a header note and reframed the YAML as the embedded block's recommended content | `docs/project-system/PROJECT_MANIFEST_SPEC.md` | `grep -ic "markdown\|canonical" docs/project-system/PROJECT_MANIFEST_SPEC.md` now > 0 | RESOLVED |
| EVI-002 | 4 of 6 shipped manifest artifacts are standalone YAML with no pointer to the canonical Markdown format | Same as EVI-001 | Added an identical 3-line header note to all four YAML artifacts pointing to the canonical format and their own role (embedded-block content, not the canonical file) | `project-manifest.template.yaml`, `INITIAL_PROJECT_MANIFEST.yaml`, `project-manifest.reference-project.draft.yaml`, `examples/minimal-ndf-project/.../project-manifest.yaml` | `grep -l "Not the canonical manifest artifact" <4 files>` → 4/4 | RESOLVED |
| EVI-003 | Spec made `repository` mandatory; conventions allow `unknown` marking; validity of an `unknown` mandatory field undocumented | Adapter conventions' own "unknown/not evidenced/n/a/open decision" rule | Added an explicit sentence: a mandatory field must be present as a key; its value may be `unknown` etc. without being invalid | `docs/project-system/PROJECT_MANIFEST_SPEC.md` | manual read | RESOLVED |
| EVI-004 | `examples/minimal-ndf-project` manifest: `status: "example"` (not spec-enumerated); `ndf_level: 2` with `quality_gates: true`/`health_score: true` (spec ladder places these at levels 3/4) | `PROJECT_MANIFEST_SPEC.md` status enum + NDF-level ladder (unambiguously authoritative; example is stale) | Corrected the example: `status: "active"` (matches the convention used by every other shipped manifest); `ndf_level: 4` (consistent with `quality_gates`/`health_score` both `true` on the cumulative ladder) | `examples/minimal-ndf-project/project-system/project-manifest.yaml` | manual read against spec enum/ladder | RESOLVED |
| EVI-005 | Minimal-variant output list included `project-brain/PROJECT_BRAIN.md`, but the minimal phase chain (0→1→2→3→8→10) excludes Phase 4 | `PROJECT_ADAPTER_V0_2.md` §9 phase chain (normative) | Removed `PROJECT_BRAIN.md` from the minimal-variant list; added an explanatory line citing §9 | `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md` | manual cross-check vs. §9 | RESOLVED |
| EVI-006 | `docs/ndf/README.md`/`ADOPTION_NOTES.md` listed as full-variant output in two places; no phase row (§5) attributes them; WP-155's own grep excluded `framework/prompts/` and therefore missed `PROJECT_SYSTEM_BASELINE_PROMPT.md`, which *does* list them as allowed files for the bundled Phase 2–8 execution | `PROJECT_ADAPTER_V0_2.md` §5 phase table (no single-phase attribution) plus `PROJECT_SYSTEM_BASELINE_PROMPT.md` (actual producer) | Added a note in both listings attributing the two files to the bundled Phase 2–8 execution rather than a single phase — no phase added/removed/resequenced | `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`, `docs/project-starter/PROJECT_ADAPTER_V0_2.md` | manual read; DET-06 below | RESOLVED |
| EVI-008 | 3 of 6 adapter-path documents German-only (`PROJECT_ADAPTER_V0_2.md`, `PROJECT_MANIFEST_SPEC.md`, `PROJECT_ADAPTER_INTAKE_TEMPLATE.md`) | `docs/i18n/DE_EN_LANGUAGE_STANDARD.md` (established bilingual paired-heading convention, already used by `PROJECT_ADAPTER_CONVENTIONS.md`) | Made all three bilingual using the same convention; updated `docs/i18n/TRANSLATION_STATUS.md` | 4 files (3 + status matrix) | DET-13 below | RESOLVED |
| PEV-001 | No document stated the `NDF-B0`…`NDF-B4`/`NDF-Lean` namespacing convention | n/a — new clarification of an already-validated (WP-156) rule; native NDF terms unchanged | Added §7.1 to the token-efficiency baseline | `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` | DET-02 below (repeat of WP-156's search, now with a documented hit inside the intended file only) | RESOLVED |
| PEV-002 | PREPARED vs. AUTHORIZED (from WP-156) undocumented in the adapter guide/intake template themselves | WP-156's own evidenced distinction | Added the distinction to the adapter guide's role model (§4) and referenced it from the intake template's header | `docs/project-starter/PROJECT_ADAPTER_V0_2.md`, `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md` | manual read | RESOLVED |
| PEV-003 | `ndf-existing-project-analysis-runner` SKILL.md doesn't state its Phase-0 field coverage | WP-156's own field-by-field intake table | Resolved via public documentation only: added a cross-reference and field-coverage statement in the adapter guide (§6); `SKILL.md` left unmodified | `docs/project-starter/PROJECT_ADAPTER_V0_2.md` | manual read; see [Skill Clarification](#skill-clarification) | CLARIFIED |
| PEV-004 | Enablement-specific feedback signal thin (1 of 7 candidates) | n/a — evidence limitation, not a documentation defect | No fix attempted; limitation stays visible in this record's Finding Matrix and is not claimed resolved anywhere in the touched files | none | manual read of touched files for false-resolution claims | RETAINED_LIMITATION |
| PEV-005 | Intake template didn't mark agent-preparable vs. human-only fields | WP-156's own field-by-field intake table | Labelled every field `AGENT-PREPARABLE` (6, 3 of them partial) or `HUMAN-REQUIRED` (3), matching WP-156's table exactly | `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md` | manual cross-check vs. WP-156 §Intake table | RESOLVED |
| Historical Neutrality Drift | A legacy file family named, described, and cross-referenced a specific external project (`LEGACY_PRIVATE_PROJECT_TOKEN`: an independent, self-hosted operations control plane; source repository external to NDF) across 8 file names, 11 work-package/candidate IDs (`NDF-FC-LEGACY_PRIVATE_PROJECT_TOKEN-00x`, `NDF-INTAKE-LEGACY_PRIVATE_PROJECT_TOKEN-001`, `NDF-ADOPT-LEGACY_PRIVATE_PROJECT_TOKEN-001A/B/C`), and 2 `CHANGELOG.md` entries | Human-Maintainer decision (Option A, full neutralisation) superseding the initial `HISTORICAL_PATH_NEUTRALITY_DECISION_REQUIRED` report | **Migrated.** 8 files renamed to a neutral `CROSS_PROJECT_FEEDBACK_001`/`CPF` scheme; 11 IDs migrated; all current-tree prose neutralised across 18 files; no Git history rewritten; no tag/release altered — see [Historical Neutrality Migration](#historical-neutrality-migration) | 18 files (8 renamed + content, 10 content-only) | targeted repository-local scan, 0 current-tree matches (see [Deterministic Checks](#deterministic-checks)) | RESOLVED |

## Manifest Consistency

**Authoritative source:** `PROJECT_ADAPTER_CONVENTIONS.md` (NDF-WP-059, self-described as "binding conventions"), cross-referenced and matched verbatim by `PROJECT_ADAPTER_V0_2.md` §5's Phase-3 row and by `PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`'s manifest line — three independent, mutually consistent sources versus one outlier (`PROJECT_MANIFEST_SPEC.md`, which contained zero occurrences of "Markdown"/"canonical"/".md" per WP-155's DET-10). No new representation was invented; the existing, already-cross-referenced Markdown-canonical convention was made explicit in the outlier and in the four shipped YAML artifacts.

**Representation:** `PROJECT_MANIFEST.md` (Markdown) is canonical; a YAML/JSON block embedded in that file is allowed and is the same field set `PROJECT_MANIFEST_SPEC.md` documents; standalone `.yaml` files NDF ships are the embedded block's content, not the canonical artifact, and now say so.

**Changes:** `docs/project-system/PROJECT_MANIFEST_SPEC.md` (canonical-format note, bilingual, mandatory-field-vs-`unknown` clarification), 4 shipped YAML manifest artifacts (canonical-format pointer), 1 example corrected to the spec's status enum and NDF-level ladder.

**Remaining ambiguity:** none identified for the canonical-format question. `docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml` shows an independent, unnamed-finding inconsistency (`ndf_level: 3` with both `quality_gates: true` and `health_score: true`, which the ladder would place at level 4) — observed but **not corrected**, since no EVI/PEV finding names this file's level/flag consistency and fixing it would be an unauthorised scope expansion under §9.

## Adapter Consistency

**Phase/output alignment:** the minimal-variant output list now matches the §9 phase chain (0→1→2→3→8→10; `PROJECT_BRAIN.md` removed). The full-variant list is unchanged in content but now carries an explanatory note attributing `docs/ndf/README.md`/`ADOPTION_NOTES.md` to the bundled Phase 2–8 execution (`PROJECT_SYSTEM_BASELINE_PROMPT.md`) rather than to any single phase row — this is new information WP-155's own DET-12 search missed (its grep excluded `framework/prompts/`). No phase added, removed, or resequenced; no lifecycle semantics changed.

**Example alignment:** `examples/minimal-ndf-project` manifest corrected to the spec (EVI-004); no other adapter output examples were found to need reconciliation within this WP's authorised scope.

## Enablement / Authority Clarity

**PREPARED vs. AUTHORIZED:** stated in `PROJECT_ADAPTER_V0_2.md` §4 (role model) using WP-156's own language; referenced from the intake template header. Human-Maintainer authority is unchanged — only what the agent may PREPARE read-only is documented; nothing an agent produces is treated as authorising a phase advance.

**Terminology namespacing:** `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` §7.1 states the collision rule (unprefixed `B0`–`B4`/`Lean` for NDF core; `NDF-B0`…`NDF-B4`/`NDF-Lean` in an integration/enablement context on a naming collision). NDF's native unprefixed terminology is unchanged everywhere else in the document.

**Intake field authority:** every field in `PROJECT_ADAPTER_INTAKE_TEMPLATE.md` now carries `AGENT-PREPARABLE` (Project Name partial, Project Type, Local Path, Tech Stack, Deployment Model partial, Known Risks) or `HUMAN-REQUIRED` (Repository URL, Maintainer Goals, Public/Private Status, Safety Notes) — matching WP-156's field-by-field table exactly. No field lets an agent self-authorise a Human-only value.

**`ndf-existing-project-analysis-runner` boundary:** resolved via `PROJECT_ADAPTER_V0_2.md` §6, which now states exactly which intake fields the skill's output can (six, matching AGENT-PREPARABLE) and cannot (three HUMAN-REQUIRED fields) cover. `SKILL.md` was not modified.

## I18N

**Affected documents:** `docs/project-starter/PROJECT_ADAPTER_V0_2.md`, `docs/project-system/PROJECT_MANIFEST_SPEC.md`, `framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md`.

**Strategy:** NDF's existing "DE – Heading / EN – Heading" paired-section convention (`docs/i18n/DE_EN_LANGUAGE_STANDARD.md`, already used by `PROJECT_ADAPTER_CONVENTIONS.md` and `PROJECT_SYSTEM_BASELINE_PROMPT.md`) — no new i18n mechanism introduced. Technical keywords (Work Package, Project Brain, Health Score, Implementation Agent, Maintainer, Security) kept in English in both language halves per the standard's own rule. `docs/i18n/TRANSLATION_STATUS.md` updated for the three affected areas plus its "recommended order" item 4.

**Parity checks:** each DE section and its EN counterpart carry the same field/table structure and normative content (mandatory-field lists, status enum, NDF-level ladder, phase table, safety rules) — verified by side-by-side read during authoring; no divergent DE/EN semantics introduced.

## Public Neutrality

**Historical drift (resolved via migration):** a legacy file family named and described a specific external project (`LEGACY_PRIVATE_PROJECT_TOKEN`: an independent, self-hosted operations control plane; source repository external to NDF) in its own body text, with the identifier additionally embedded in 8 file names, 11 work-package/candidate IDs, and cross-references from 3 governance/agent-workflow documents plus 2 `CHANGELOG.md` entries and 2 further validation/notes documents discovered only during the migration pass (a case-sensitive search had missed the mixed-case form of the token). An initial content-only edit was rejected as insufficient — it would have left the identifier fully exposed in every file name and ID — and the item was first reported as `HISTORICAL_PATH_NEUTRALITY_DECISION_REQUIRED`. The Human Maintainer subsequently authorised **Option A (full neutralisation)**; see [Historical Neutrality Migration](#historical-neutrality-migration) for the executed migration.

**Denylist available:** no — `NDF_PUBLIC_NEUTRALITY_DENYLIST` is not set in this environment and no `.ndf/public-neutrality-terms.local.txt` exists; the gate reported this as an informational notice, not a failure (see [Deterministic Checks](#deterministic-checks)). Manual review, including a dedicated post-migration targeted scan, was performed in its place per §6/§16 of the migration instruction.

**New private identifiers:** none introduced by this WP's edits, including the migration.

## Historical Neutrality Migration

**Human-Maintainer decision:** Option A — full neutralisation, authorised in the WP-157 rework execution header.

**Migration scope:** the complete legacy file family and every current-tree reference to it, re-discovered from the repository rather than reused from the prior report's estimate (which undercounted by 2 — a case-sensitive-only search had missed the mixed-case form of the token in two files).

**Neutral naming scheme:** file family prefix `LEGACY_PRIVATE_PROJECT_TOKEN_TRANSFER_PACKAGE_001` → `CROSS_PROJECT_FEEDBACK_001`; ID infix `LEGACY_PRIVATE_PROJECT_TOKEN` → `CPF` (Cross-Project Feedback), applied to all three ID families (`NDF-INTAKE-*-001`, `NDF-FC-*-00N`, `NDF-ADOPT-*-001A/B/C`). Verified collision-free against the repository before use.

**Results:**

- **Files renamed:** 8 — `docs/validation/cross-project-feedback/CROSS_PROJECT_FEEDBACK_001_{ADOPTION_A,ADOPTION_B,ADOPTION_C,INTAKE_REVIEW}.md` and `project-brain/CROSS_PROJECT_FEEDBACK_001_{ADOPTION_A_NOTES,ADOPTION_B_NOTES,ADOPTION_C_NOTES,INTAKE_NOTES}.md`. All 8 old paths confirmed absent; all 8 new paths confirmed present.
- **IDs migrated:** 11 — `NDF-INTAKE-CPF-001`; `NDF-FC-CPF-001`…`007`; `NDF-ADOPT-CPF-001A/B/C`. Parent/child and A/B/C sequence relationships preserved; no ID reused from elsewhere in the repository.
- **Content-only neutralisations (no rename):** 10 files — `CHANGELOG.md` (2 entries: the original published adoption entry and this WP's own entry), `docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md`, `docs/governance/NDF_DECISION_AND_STATUS_MODELING_GUIDANCE.md`, `docs/governance/NDF_EXTERNAL_FRAMEWORK_TAILORING_GUIDANCE.md`, `docs/validation/v1-1/SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW.md`, `project-brain/WP_151_SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW_NOTES.md`, plus this validation record, the WP-157 notes, and the two project-brain state files this WP had already touched (`CONTEXT_PACK_FOUNDATION_0_9.md`, `NEXT_PHASE_FOUNDATION_0_9.md`).
- **Inbound references updated:** every in-repo Markdown reference to an old path or old ID, across the 18 total files touched (8 renamed + 10 content-only).
- **Prose neutralisation:** generic mentions of the source project (e.g. "no `LEGACY_PRIVATE_PROJECT_TOKEN` file changed", "the `LEGACY_PRIVATE_PROJECT_TOKEN` backlink stays pending") replaced with neutral equivalents ("no source-project file changed", "the source backlink stays pending"); the one descriptive sentence naming the source project's nature ("an independent, self-hosted operations control plane; source repository external to NDF") kept its factual content but dropped the project name.
- **Old identifiers absent from current tree:** confirmed — see [Deterministic Checks](#deterministic-checks) DET-11 (repeat scan).
- **History not rewritten:** confirmed — no `git commit --amend`, no rebase, no filter, no force-push; the two commit hashes referenced in migrated prose (`1ebffa6`, `e894c6f`, `ebf716c`) are unchanged, only the prose describing them was reworded.
- **Tags/releases untouched:** confirmed — no tag or release action was taken; `v1.0.0`/`v1.0.0-rc.1` are unaffected.
- **Pending/accepted status preserved:** every migrated document's own status field (`implemented – pending Nova review`, `Nova Review pending`, `Human-Maintainer-Commit pending`) is unchanged in meaning; no pending draft was reworded as accepted.

**Historical path issue:** yes — see above; not resolved, not renamed, reported for decision.

## Skill Clarification

**Required:** no. PEV-003's adopter-facing ambiguity (does `ndf-existing-project-analysis-runner`'s output cover Phase-0 intake fields?) is fully resolved by the new cross-reference in `docs/project-starter/PROJECT_ADAPTER_V0_2.md` §6, which states the exact field split. `SKILL.md` was not opened for editing.

**File:** n/a (not modified).

**Behavior changed:** no.

**Integrity-lock impact:** none — no consumer integrity record for `ndf-existing-project-analysis-runner` is affected, since the skill file's content and hash are unchanged.

## Deterministic Checks

Reproducible at `270c6c5` plus this WP's changes.

| ID | Check | Result |
|---|---|---|
| DET-01 | `grep -ic "markdown\|canonical" docs/project-system/PROJECT_MANIFEST_SPEC.md` | before: 0 (WP-155 DET-10); after: > 0 |
| DET-02 | `grep -rEli "NDF-B0\|NDF-Lean\|terminology.namespacing" --include=*.md docs/guides/` | before: 0 matches (WP-156 DET-02, repo-wide); after: 1 match, in the intended baseline guide |
| DET-03 | 4 shipped YAML manifest artifacts carry the new canonical-format pointer | `grep -l "Not the canonical manifest artifact" framework/project-system/templates/project-manifest.template.yaml framework/project-starter/templates/INITIAL_PROJECT_MANIFEST.yaml docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml examples/minimal-ndf-project/project-system/project-manifest.yaml` → 4/4 |
| DET-04 | `examples/minimal-ndf-project` manifest `status`/`ndf_level` match the spec | `status: active` (in enum); `ndf_level: 4` consistent with `quality_gates: true`/`health_score: true` |
| DET-05 | Minimal-variant output list no longer includes `PROJECT_BRAIN.md` | `grep -A4 "Minimale Variante" framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md` → 3 files, no `PROJECT_BRAIN.md` |
| DET-06 | `docs/ndf/*` producer clarified | `grep -n "docs/ndf" framework/prompts/project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md` → 2 hits (the actual producer WP-155's DET-12 search excluded) |
| DET-07 | DE/EN markers in the 3 EVI-008 documents | before: 3/3 German-only (WP-155 DET-13); after: 3/3 carry `## DE` / `## EN` (or DE/EN-paired subheadings) throughout |
| DET-08 | `git diff --stat` / `git diff --name-only` scope check | see [Validation](#validation) |
| DET-09 | Public Quality Gate self-test | see [Validation](#validation) |
| DET-10 | Public Quality Gate, strict mode, on the changed tree | see [Validation](#validation) |
| DET-11 | Pre-migration case-insensitive repo-wide scan for the legacy token | 18 files (higher than the case-sensitive-only estimate in the initial report, which missed 2 mixed-case mentions) |
| DET-12 | No ADR, skill, adapter spec/convention/runbook, or framework prompt/standard file removed or renamed | confirmed — the only filesystem renames are the 8 migrated cross-project-feedback files, authorised under Human-Maintainer Option A; no ADR/skill/adapter/framework-prompt path touched |
| DET-13 | Post-migration repo-wide scan, legacy token and legacy ID patterns, case-insensitive, all changed/renamed files included | **0 matches** — see [Historical Neutrality Migration](#historical-neutrality-migration) |

## Semantic Review

- **Manifest resolution was derivation, not invention.** The canonical-Markdown answer was already explicitly stated and cross-referenced by three sources before this WP started; the work was aligning the one outlier and the shipped templates to it, not choosing between equally-weighted options.
- **EVI-006 turned out to be partially a discovery gap in WP-155, not a pure documentation defect.** `PROJECT_SYSTEM_BASELINE_PROMPT.md` does produce `docs/ndf/README.md`/`ADOPTION_NOTES.md`; WP-155's own reproduce command excluded `framework/prompts/` from its grep. The fix here is attribution (which document actually produces them), not removal of a phantom output.
- **PEV-003 was solvable without touching the skill.** Nothing in `ndf-existing-project-analysis-runner`'s own contract was misleading once the adapter guide stated the field split explicitly; the ambiguity lived in the adapter-side documentation, not the skill.
- **The historical-neutrality item is the one place where "smallest safe repair" and "full resolution" genuinely diverge**, and the prompt's own fail-closed instruction is the correct answer: partial content edits would look like a fix while leaving the identifier fully exposed in every file name and ID, which is worse than an honest, visible STOP.

## Compatibility

Per [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), active since `v1.0.0`.

- **Classification: CLARIFICATION / DOCUMENTATION-ONLY / ADDITIVE.** This work package aligns documentation to already-established conventions, corrects one stale example, adds bilingual content, adds cross-reference notes, and — under explicit Human-Maintainer authorisation — renames 8 internal validation/notes documents and migrates their embedded IDs for public-neutrality reasons. It changes no interface, no phase, no lifecycle semantics, no Skill behavior.
- **Breaking changes: none.** No skill, ADR, prompt, standard, or Project-Adapter version changed. No phase added or removed. No skill name changed. No public entry point removed. The 8 renamed files are internal cross-project-feedback validation/notes records, not referenced by any adapter phase, template, or Skill contract; their old paths were referenced only from the files this migration also updated.
- **ADR-0032 unchanged and binding.** Docs-only, fail-closed, no scripts added, no network, no secrets, no private data added, no autonomous git/release action. The private-consumer scope question remains reserved for a separate ADR (candidate ADR-0033); nothing here expands it.
- **Needs ADR: no.**
- **Public Quality Gate:** self-test and strict mode run locally against the changed tree (see [Validation](#validation)); the gate remains mandatory and is not bypassed by this record.

## Remaining Notes

- PEV-004 (thin enablement feedback signal) stays an accepted, visible limitation — not this WP's to close.
- The historical public-neutrality drift is resolved: migrated under Human-Maintainer Option A (see [Historical Neutrality Migration](#historical-neutrality-migration)); a post-migration repo-wide scan found 0 remaining current-tree matches for the legacy token or its IDs.
- `docs/integrations/reference-project/project-system-draft/project-manifest.reference-project.draft.yaml`'s own `ndf_level`/flag consistency (independent of EVI-004) was observed but is out of this WP's authorised scope to fix.

## Result

IMPLEMENTED — NOVA REVIEW PASSED; HUMAN-MAINTAINER ACCEPTANCE EFFECTIVE THROUGH THE COMMIT CARRYING THIS RECORD. All EVI-001…006/EVI-008 and PEV-001/002/003/005 findings resolved documentarily from already-established authority, with no invented representation, no phase/lifecycle change, and no Skill behavior change. PEV-004 stays a retained, visible evidence limitation. The historical public-neutrality drift item, initially reported as `HISTORICAL_PATH_NEUTRALITY_DECISION_REQUIRED`, was resolved by a bounded rename/ID/link migration under explicit Human-Maintainer authorisation (Option A) — no Git history rewritten, no tag/release altered, no pending status changed to accepted.

## Next Safe Step

**HUMAN_MAINTAINER_REVIEW.**

NDF-WP-158 MUST NOT START before Nova/Human-Maintainer acceptance and commit of NDF-WP-157.
