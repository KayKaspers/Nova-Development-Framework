# NDF-WP-155 — External Validation Improvement

## Status

IMPLEMENTED — PENDING NOVA / HUMAN-MAINTAINER ACCEPTANCE

## Baseline

- Starting revision: `07b2884f0c649e482a53434cd3210023b6c4d576`
- Branch: `main`, working tree clean, index empty, no merge/rebase/cherry-pick/revert/bisect in progress
- Released state: **v1.0.0 final**; the full v1.x compatibility promise is active from `v1.0.0` per [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md)
- v1.1: **planning only** — not scope-locked, not released
- Prompt profile: Validation / evidence improvement · Prompt Mode Full · Context budget B2 target, B3 maximum
- Support skills: `ndf-work-package-runner` (routing), `ndf-validation-evidence-reviewer` (evidence grading), `ndf-public-neutrality-guard` (neutrality gate)
- No network access, no package installation, no git write action.

## Validation Question

> What additional public, reproducible evidence would materially improve confidence that NDF can be applied outside its own repository without depending on private context or project-specific assumptions?

**Answer, derived from the prior evidence rather than assumed:** the gap was never the *verdict* — two independent runs already returned PASS WITH NOTES. The gap was that the verdict rested on material NDF itself had authored, and that the individual steps behind the verdict were never recorded. Two things therefore improve confidence:

1. **Per-step evidence** — the six runbook steps and the eleven adapter phases recorded individually, with the commands and outputs that produced each result, so a reader can check the path rather than trust a summary.
2. **An NDF-naive input** — a repository that was *not* shaped to fit the adapter, containing real code, so that "the adapter works" is not a restatement of "the fixture was built for the adapter."

This work package supplies both. It does **not** supply independence; see [Limitations](#limitations).

## Prior Evidence / G-13 Baseline

G-13 — *External Validation Evidence Depth* — is the single tracked gap from the [v1.0 Gap Review](../v1-0/V1_0_GAP_REVIEW_AND_SCOPE_LOCK.md) and the central caveat of the [v1.0 Release Criteria](../../release/V1_0_RELEASE_CRITERIA.md). The [External Validation Evidence Review](../v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md) (WP-140) graded it `Partially closed / remains tracked for RC` against nine evidence sources.

The named limitations at v1.0 final were:

| ID | Limitation | Source |
|---|---|---|
| PSV-001 | Per-step evidence for the six runbook steps **not provided**; only a positive overall verdict | [WP-088 validation result](../project-adapter/independent-runs/2026-07-07-public-sampleproject-runbook-validation/VALIDATION_RESULT.md) (E-01) |
| IAV-002 | The second independent run was private-context and summarised | WP-074 (E-02) |
| E-03 note | The public fixture contains **no real code**; monorepo layouts **not covered** | WP-047 self-validation |

v1.0 final resolved G-13 via **path C**: path B (a documented accepted boundary) applied, path A (a deeper public step-evidenced neutral run) stayed a future improvement — the item the [v1.1 plan](../../roadmap/V1_1_PLAN.md) assigns to this work package.

Verified read-only at `07b2884`: the WP-088 result records four of six runbook steps as "not provided (individually)", and the fixture's own [mock repository tree](../../../examples/neutral-example-project/MOCK_REPOSITORY_TREE.md) states it is a Markdown mock with no real application files. Both limitations are current, not stale.

## Scenario / Fixture

**Scenario:** execute NDF's own published external-validation procedure — the [Independent Adapter Validation Runbook](../project-adapter/INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md) — end to end, with every step individually evidenced, against a generic code-bearing repository that NDF has never seen.

**Why this scenario and not another.** The runbook is the artifact whose per-step evidence G-13 names as missing, so running *that* procedure keeps the new evidence directly comparable with E-01 rather than producing a parallel, non-comparable record. Substituting the input at the point where portability is actually tested (Step 3, applying the adapter phases) converts the run from a self-check into a portability test without inventing a new procedure. One fixture was used: it is the smallest scenario that addresses PSV-001 and the E-03 limits together, so the optional second fixture permitted by the work package was deliberately **not** added.

**Fixture:** `sample-taskqueue` — a generic two-package job-queue repository, 14 files, 183 lines, built for this run and held **outside the NDF repository** (session scratchpad). It is deliberately shaped *against* NDF's expectations:

| Property | Why it is adversarial |
|---|---|
| Real, executable Python and JavaScript | Directly addresses the E-03 "no real code" limit |
| Two packages, two languages | Addresses the E-03 "monorepo not covered" limit |
| No `docs/` directory; docs are three root files with mixed extensions (`.md`, `.txt`) | NDF's own fixture and examples are documentation-shaped |
| Three version sources that disagree (`0.5.0` / `0.4.1` / `0.4.1`) | Forces the conventions' "never guess, mark `unknown`" rule to do real work |
| Three unguarded irreversible operations | Exercises adapter §7 rule 3 (capture, never change) against real code |
| `.env.example` with placeholder values only | Exercises adapter §7 rule 2 (no secret read or copied) |
| No CI configuration, but test targets declared in two places | Forces split evidence in the Health Score "Testing / CI" category |
| No `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`; CLI declares `UNLICENSED`, core declares nothing | Forces `unknown` / `open decision` rather than an invented governance rating |
| A test suite that genuinely fails | Prevents a uniformly positive reading |

**Public neutrality:** placeholders only (`sample-taskqueue`, `example-owner`, `example.local`, `EXAMPLE_SECRET_PLACEHOLDER`). No private project, person, or organisation name; no real domain; no secret value; no private search pattern. No private consumer-project content was used, referenced, or derived from.

**Authoring sequence, stated plainly because it bears on anchoring:** the adapter guide and conventions were read *before* the fixture was authored — unavoidable, since "NDF-naive" is only definable against what NDF expects. NDF's own fixture content (`README.md`, `MOCK_REPOSITORY_TREE.md`) was read only *afterwards*, at Step 2. The fixture and NDF's mock tree independently converged on some motifs (a `reset-db.sh`, an `.env.example`, a lagging changelog); that convergence was not copied.

## Method

The run records, for each step: what was consulted, what command was issued, what came back, and what was decided. Two evidence types are kept separate throughout:

- **DETERMINISTIC** — a command was run and its output is reproducible by anyone at the same revision. Recorded under [Deterministic Checks](#deterministic-checks).
- **SEMANTIC / REVIEW** — a judgment was formed by reading. Recorded under [Semantic Review](#semantic-review). These are opinions with stated bases, not measurements.

No token counts are reported: no instrumentation exists under ADR-0032, so none are estimated.

## Step-by-Step Run

Runbook steps 1–6, all six executed, each individually evidenced — the record WP-088 did not produce.

### Step 1 — Orientation

Read [`PROJECT_ADAPTER_V0_2.md`](../../project-starter/PROJECT_ADAPTER_V0_2.md) (111 lines) and [`PROJECT_ADAPTER_CONVENTIONS.md`](../../project-starter/PROJECT_ADAPTER_CONVENTIONS.md) (124 lines), then resolved every path either document names.

- **Result:** all 9 referenced artifact paths resolve at `07b2884` (DET-01). Purpose, role model, phase table, safety rules and the minimal variant were clear on first reading.
- **Open after Step 1:** which file format Phase 3 actually requires — the conventions say Markdown-canonical, and the spec they point to had not yet been read.

### Step 2 — Fixture review

The runbook directs the reader at `examples/neutral-example-project/`. Read its `README.md` and `MOCK_REPOSITORY_TREE.md`.

- **Result:** the fixture states outright that it is "not runnable software — documented example artifacts only", and the tree is "Markdown mock — no real app files exist". This confirms the E-03 limit as current and is the reason the run proceeds with a code-bearing fixture at Step 3.
- The NDF fixture is adequate for a documentation-shaped walk-through; it cannot evidence adapter behaviour against code.

### Step 3 — Apply adapter phases

Applied the §9 **minimal variant** (Phase 0 → 1 → 2 → 3 → 8 → 10) to `sample-taskqueue`, plus **Phase 7** (Health Score) to exercise the conventions' `unknown` / `n/a` rules against real missing evidence. Per the runbook, each phase answers: *would I now know what to do, what comes out, and where it belongs?*

| Phase | Answer | Basis |
|---|---|---|
| 0 — Intake | **pass with notes** | Template fields clear. Two are unanswerable read-only (`Maintainer Goals`, `Repository URL`); the template is maintainer-filled by design → **EVI-007** |
| 1 — Read-only Review | **pass** | §7 safety rules were directly executable against real code: 3 destructive operations captured and not changed, no secret value read (DET-04, DET-05) |
| 2 — Project Profile | **pass** | Expected content and location unambiguous; `unknown` handling carried four unevidenced fields without invention |
| 3 — Project Manifest | **rework** | Format is **not derivable** from the adapter path → **EVI-001, EVI-002, EVI-003** |
| 4 — Project Brain | not run | Absent from the §9 minimal chain, yet its output is listed in the minimal output structure → **EVI-005** |
| 5–6 — Capability Matrix, Compliance Check | not run | Optional; outside the minimal variant |
| 7 — Health Score | **pass** | All eight conventions categories applied; 1 category `unknown`, 1 `n/a` with reason, 6 scored with justification — the rules held under real missing evidence |
| 8 — Work Package Queue | **pass** | `XY-WP-` prefix instantiated as `STQ-WP-` without ambiguity; §8/§12 guidance produced a documentation/review-first queue rather than features |
| 9 — First Safe WP | not run | Optional |
| 10 — Review & Commit | **pass** | Human-Maintainer-only boundary unambiguous; no commit, push, or staging performed |

Phase 3 is the one phase the documentation could not resolve. The run recorded the choice it was forced to make — Markdown canonical, following the conventions and the output-structure template, because the adapter's Phase 3 row names `PROJECT_MANIFEST.md` — and flagged it rather than presenting it as derived.

### Step 4 — Output review

Checked the conventions' output-path rules and spot-checked the historical WP-047 outputs, overwriting nothing.

- **Result:** all 11 files in `examples/neutral-example-project/adapter-validation-output/` carry the "validation output, not production documentation" marker, and expected/actual outputs are separated into distinct directories (DET-02, DET-03). The conventions are followed by NDF's own shipped outputs.
- The full-variant output structure, however, lists two files no phase produces → **EVI-006**.

### Step 5 — Capture feedback

Completed [`INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md`](../project-adapter/INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md) in full, including the **per-phase results table for all eleven phases** — the table left blank in the WP-088 run. Unknowns marked as unknown; nothing invented. The completed feedback is reproduced in substance by the [Step-by-Step Run](#step-by-step-run), the [Findings](#findings-evi) and the [Semantic Review](#semantic-review) in this record; the working copy is scratchpad-only and is not a repository artifact.

The template's own "Role / Independence" field is answered **not independent** — see [Limitations](#limitations).

### Step 6 — Evaluate result

**PASS WITH NOTES.** The documented public path carried a repository NDF had never seen from intake to a work-package queue, with no invented facts and no safety or neutrality breach. One phase (3) is not resolvable from the documentation alone. No blocker. No stop criterion triggered.

## Evidence

Evidence classes are kept distinct; they are **not** equivalent and are not aggregated into a single score.

| Class | Present in this run? | What it covers |
|---|---|---|
| **Repository-internal evidence** | yes | Every deterministic check below — commands run against the NDF repository at `07b2884` |
| **Public external / generic evidence** | yes | The adapter path exercised against a generic, NDF-naive, code-bearing repository; the fixture is public-neutral and reconstructible |
| **Project-local evidence** | **no** | No private consumer-project content was used, referenced, or derived from. ADR-0032's private-consumer scope question is untouched |
| **Human-Maintainer observation** | **no** | No Human Maintainer participated in this run |
| **Independent third-party observation** | **no** | None. The run is agent-executed. No external reviewer, user, team, feedback, integration, or adoption is claimed or implied |
| **Inference / hypothesis** | marked inline | E.g. "datastore is PostgreSQL" is recorded in the dry run as inferred and `not evidenced`, never as fact |

### Findings (EVI)

Eight findings, produced by using the path rather than reviewing it. All are documentation-consistency findings in the adapter path; none is a security finding; none is a blocker. **This work package records them; it does not fix them** — the files involved are outside its authorised scope.

| ID | Finding | Type | Severity |
|---|---|---|---|
| EVI-001 | Phase 3 format is contradicted across the path: [`PROJECT_ADAPTER_CONVENTIONS.md`](../../project-starter/PROJECT_ADAPTER_CONVENTIONS.md) and [`PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`](../../../framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md) make `PROJECT_MANIFEST.md` canonical Markdown with YAML embedded only, while [`PROJECT_MANIFEST_SPEC.md`](../../project-system/PROJECT_MANIFEST_SPEC.md) prescribes a bare YAML document and contains **zero** occurrences of "Markdown", "canonical/kanonisch", or ".md". Neither document cross-references the other. The spec is the outlier | DETERMINISTIC | medium |
| EVI-002 | 4 of the 6 manifest artifacts NDF ships are standalone YAML (`project-manifest.yaml`, `project-manifest.template.yaml`, `INITIAL_PROJECT_MANIFEST.yaml`); only the adapter-validation output uses the canonical `PROJECT_MANIFEST.md`. An adopter copying the shipped template lands on the non-canonical format | DETERMINISTIC | medium |
| EVI-003 | The spec makes `repository` a mandatory field; the conventions require unevidenced values to be marked `unknown`. Neither states whether a manifest with an unknown mandatory field is valid | SEMANTIC | low |
| EVI-004 | `examples/minimal-ndf-project/project-system/project-manifest.yaml` declares `status: "example"`, which is not among the spec's five permitted values (`idea`/`active`/`paused`/`maintenance`/`archived`), and `ndf_level: 2` while declaring `quality_gates: true` and `health_score: true`, which the spec's ladder places at levels 3 and 4 | DETERMINISTIC | low |
| EVI-005 | The §9 minimal chain (0→1→2→3→8→10) omits Phase 4, but the minimal output structure lists `project-brain/PROJECT_BRAIN.md` as a minimal-variant output | DETERMINISTIC | low |
| EVI-006 | The full-variant output structure lists `docs/ndf/README.md` and `docs/ndf/ADOPTION_NOTES.md` in two places, but no phase in the 0–10 table produces them and the adapter checklist never mentions them | DETERMINISTIC | low |
| EVI-007 | Phase 0 presumes a human maintainer supplies goals and repository identity. An agent-only or solo read-only adoption cannot complete Phase 0 as specified. This is a genuine **NDF-specific assumption**, not a defect — but it is undocumented | SEMANTIC | low |
| EVI-008 | Of the six adapter-path documents this run needed, three are German-only (`PROJECT_ADAPTER_V0_2.md`, `PROJECT_MANIFEST_SPEC.md`, `PROJECT_ADAPTER_INTAKE_TEMPLATE.md`), one is partly bilingual, and two are fully DE/EN. An English-only adopter can follow the conventions and the runbook but not the adapter guide, the manifest spec, or the intake template | DETERMINISTIC | medium |

## Deterministic Checks

Reproducible at `07b2884`. Commands are given under [Reproduce](#reproduce).

| ID | Check | Result |
|---|---|---|
| DET-01 | All 9 artifact paths referenced by the adapter guide and the runbook resolve | **PASS** — 9/9 resolve, 0 broken |
| DET-02 | Every file in `adapter-validation-output/` carries the "validation output" marker | **PASS** — 11/11 |
| DET-03 | Expected and actual adapter outputs are in separate directories | **PASS** — `expected-adapter-output/` (1 file) and `adapter-validation-output/` (11 files) |
| DET-04 | Destructive-operation scan of the fixture (adapter §7 rule 3) | **4 sites found** — `purge_all()`, `purge_failed()`, `reset-db.sh` (`DROP SCHEMA public CASCADE`), CLI `purge` without confirmation; all captured, none modified |
| DET-05 | Secret-surface scan of the fixture (adapter §7 rule 2) | **PASS** — only `.env.example`; both values `EXAMPLE_SECRET_PLACEHOLDER`; no secret value read or carried into any artifact |
| DET-06 | CI configuration present in the fixture | **none** — `.github/`, `.gitlab-ci.yml`, `.circleci`, `Jenkinsfile` all absent |
| DET-07 | Fixture version agreement across sources | **FAIL (by construction)** — `0.5.0` / `0.4.1` / `0.4.1`; recorded as `unknown`, not guessed |
| DET-08 | Fixture core test suite executes | **2/2 pass**, standard library only, nothing installed |
| DET-09 | Fixture CLI test suite executes | **fails** — `packages/cli/src/index.js` calls `main()` at import with no `require.main === module` guard, so the module under test exits the runner; the documented `make test` therefore fails at the CLI stage |
| DET-10 | `PROJECT_MANIFEST_SPEC.md` mentions Markdown / canonical / `.md` | **0 occurrences** — basis for EVI-001 |
| DET-11 | Manifest artifacts shipped by NDF, by format | **4 YAML / 1 Markdown / 1 unrelated** — basis for EVI-002 |
| DET-12 | `docs/ndf/*` referenced by any adapter phase row or the checklist | **0 occurrences** outside the two output-structure listings — basis for EVI-006 |
| DET-13 | DE/EN markers in the six adapter-path documents | 3 German-only, 1 partial, 2 full DE/EN — basis for EVI-008 |
| DET-14 | Public Quality Gate self-test | see [Compatibility](#compatibility) |
| DET-15 | Public Quality Gate, strict mode, on the changed tree | see [Compatibility](#compatibility) |

## Semantic Review

Judgments, with their bases. These are review opinions, not measurements, and do not carry the weight of the deterministic checks.

- **Portability — supported, with one gap.** The adapter's minimal variant carried a repository it was not designed around, in an unfamiliar shape (two packages, two languages, no `docs/`, code-bearing), and produced usable Profile, Manifest, Health Score and Queue artifacts without inventing facts. Phase 3 is the single point where the documentation could not answer the question it raised.
- **Usability — good outside Phase 3.** Roles, safety rules, the phase table and the output-path conventions were applicable on first reading. The `unknown` / `not evidenced` / `n/a` / `open decision` vocabulary did real work: it absorbed a contradictory version state, an inconsistent licence state, and an unscoreable security category without producing false precision. This is the strongest usability result of the run.
- **Safety rules survive contact with real code.** §7 rules 2 and 3 were written for documentation fixtures but proved directly executable against executable code containing genuine irreversible operations. Nothing in them assumed a documentation-only target.
- **Queue quality.** §8 and §12 steered the queue toward documentation and review work rather than features, which is the correct call for a repository with failing tests and no CI. The guidance produced a defensible ordering without project-specific knowledge.
- **NDF-specific assumptions found:** two. EVI-007 (Phase 0 presumes a participating human maintainer) and EVI-008 (the entry path is not fully reachable in English). Neither blocks adoption; both are undocumented. The run did **not** find hidden assumptions that NDF only works on documentation-shaped repositories, on single-package repositories, or on repositories already organised NDF-style — those were the assumptions it was designed to expose, and it did not expose them.

## Evidence Strength

Graded per the [validation-evidence framework](../v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md) vocabulary: **strong · moderate · limited · weak**.

| Dimension | Strength | Reasoning |
|---|---|---|
| **Per-step depth** | **strong** | All six runbook steps and all eleven adapter phases individually recorded, each with its basis. This is the exact record PSV-001 names as missing |
| **Reproducibility** | **strong** | Every deterministic result re-derivable from the commands given; the fixture is reconstructible from the spec and verifiable against a SHA-256 manifest |
| **Portability coverage** | **moderate** | One fixture, one archetype, minimal variant plus Phase 7. Phases 4, 5, 6, 9 and the full variant remain unexercised against code |
| **Adversarial quality** | **moderate–strong** | The fixture was built to break assumptions rather than to pass, and the run returned eight concrete findings including one `rework` phase. A run that found nothing would be weaker evidence |
| **Independence** | **weak — unchanged** | Agent-executed and agent-authored. No independent party. This is **lower** than E-01/E-02, which were genuine independent runs |
| **Adoption / user evidence** | **none** | No user, team, integration, or adoption exists or is claimed |

**Net:** depth, reproducibility and adversarial quality improve materially over the v1.0 baseline; independence does not improve at all.

## G-13 Assessment

G-13 has two limbs. They must be graded separately, because this work package moves one and not the other.

| Limb | Before (v1.0 final) | After this run |
|---|---|---|
| **Depth** — per-step evidence behind the verdict | `not provided` for four of six runbook steps; the per-phase table blank (PSV-001); fixture has no real code and no monorepo coverage (E-03) | All six steps and all eleven phases evidenced; fixture is code-bearing and two-package; 15 deterministic checks; 8 findings. **PSV-001 and both E-03 limits addressed** |
| **Externality** — independence of the observer | Two genuine independent runs, one public, one private-context | **Unchanged.** This run is agent-executed and agent-authored; it adds no independence and, on this limb alone, is weaker evidence than E-01/E-02 |

**Assessment: `MATERIALLY_REDUCED` — not closed.**

The depth limb, which is precisely what path A was defined to address, is substantially closed: the specific named limitation (PSV-001) and both named E-03 limits now have direct, reproducible answers. The externality limb is untouched and cannot be moved from inside this repository — it requires a party that is not the maintainer and not the implementation agent.

**G-13 is therefore not declared closed.** Declaring closure on the strength of one agent-executed fixture would be exactly the kind of overstatement the criterion exists to prevent. The v1.0 path-B accepted boundary remains the honest characterisation of the externality limb; what changes is that the depth objection behind path A no longer stands unanswered.

A future closure would need at least one genuinely independent run — a party other than the maintainer and the agent — against a code-bearing fixture, with the per-step record this run demonstrates is achievable.

## Limitations

Stated plainly; none of these is mitigated by anything in this record.

1. **Not independent.** The implementation agent authored the fixture and executed the run. This is the single largest limitation and it is structural, not an oversight. No independent reviewer, user, or team participated.
2. **Author bias is mitigated, not removed.** The fixture was built adversarially and the adapter path was read before authoring — unavoidable, since "NDF-naive" is only definable against NDF's expectations. A fixture authored by someone who had never read the adapter would be stronger evidence.
3. **One fixture, one archetype.** A generic two-package service repository. Other archetypes — a large monorepo, a documentation-only project, a repository in a non-Latin script, a repository with an existing competing governance framework — remain unexercised.
4. **Minimal variant plus Phase 7 only.** Phases 4, 5, 6, 9 and the complete full variant were not applied to code.
5. **No token counts.** No instrumentation exists under ADR-0032; none were estimated.
6. **The single-maintainer bottleneck is untouched** and remains the structural constraint on independent validation, as recorded since v1.0.
7. **Findings are recorded, not fixed.** EVI-001…008 touch files outside this work package's authorised scope. No adapter, spec, template, or example file was modified.
8. **No project enablement.** No adapter was installed, no project migrated, no configuration written. That work belongs to WP-156.

## Reproduce

At revision `07b2884f0c649e482a53434cd3210023b6c4d576`, from the repository root. All checks are read-only against NDF; the fixture is built outside the repository.

**Deterministic checks against NDF (DET-01, 02, 03, 10, 11, 12, 13):**

```bash
for f in docs/project-starter/PROJECT_ADAPTER_V0_2.md docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md examples/neutral-example-project docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md framework/prompts/project-adapter/PROJECT_ADAPTER_INTAKE_PROMPT.md framework/templates/project-adapter framework/checklists/PROJECT_ADAPTER_CHECKLIST.md docs/project-system docs/toolkit/PROJECT_ADAPTER_HELPER.md; do test -e "$f" && echo "OK $f" || echo "MISSING $f"; done
```

```bash
for f in examples/neutral-example-project/adapter-validation-output/*.md; do grep -qil "validierungsoutput\|validation output" "$f" && echo "MARKER-OK $(basename $f)" || echo "MARKER-MISS $(basename $f)"; done
```

```bash
grep -ic "markdown\|kanonisch\|canonical\|\.md" docs/project-system/PROJECT_MANIFEST_SPEC.md; find examples templates framework -iname "*manifest*" | sort; grep -rn "docs/ndf" docs/project-starter/PROJECT_ADAPTER_V0_2.md framework/templates/project-adapter/ framework/checklists/PROJECT_ADAPTER_CHECKLIST.md
```

**Rebuild the fixture.** Create `sample-taskqueue/` outside the NDF repository with exactly these 14 files:

```text
README.md              thin: install + one usage example; no architecture, no status
CHANGELOG.txt          plain text; newest entry 0.4.1
NOTES-deploy.txt       rough ops notes; states "there is no staging environment yet"
.env.example           TASKQUEUE_DSN + TASKQUEUE_ADMIN_TOKEN, both EXAMPLE_SECRET_PLACEHOLDER
Makefile               install / test / build targets; test runs both packages
packages/core/pyproject.toml                      version = "0.5.0"
packages/core/src/taskqueue_core/__init__.py      re-exports Queue, Job
packages/core/src/taskqueue_core/queue.py         Queue with add/take/retry/list, MAX_ATTEMPTS = 5
packages/core/src/taskqueue_core/admin.py         purge_all() and purge_failed(); both irreversible, unguarded
packages/core/tests/test_queue.py                 2 tests: add/take, retry stops at max
packages/cli/package.json                         version "0.4.1"; "license": "UNLICENSED"; test script "node --test test/"
packages/cli/src/index.js                         add/list/purge; calls main() at import, no require.main guard
packages/cli/test/cli.test.js                     1 test importing ../src/index.js
scripts/reset-db.sh                               psql DROP SCHEMA public CASCADE; no backup
```

No `docs/` directory, no CI configuration, no `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, or `CODE_OF_CONDUCT.md`. Verify with `find . -type f | sort | xargs sha256sum` — 14 files, 183 lines total.

**Fixture checks (DET-04…09):**

```bash
grep -rniE "purge|drop |delete|clear\(\)|truncate|rm -rf|reset" --include=*.py --include=*.js --include=*.sh .
```

```bash
grep '^version' packages/core/pyproject.toml; grep '"version"' packages/cli/package.json; head -1 CHANGELOG.txt
```

Run the core tests with the standard library only (nothing is installed): put `packages/core/src` and `packages/core/tests` on `PYTHONPATH` and call the two test functions directly — both pass. Then run `node --test` in `packages/cli` — it fails; confirm the cause with `node -e "require('./src/index.js')"`, which prints the usage line because `main()` runs at import.

**Then execute** the six steps of the [Independent Adapter Validation Runbook](../project-adapter/INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md), substituting `sample-taskqueue` as the Step 3 target, and record each step as the [Step-by-Step Run](#step-by-step-run) does.

## Compatibility

Per [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), active since `v1.0.0`.

- **Classification: EVIDENCE_ONLY / ADDITIVE.** This work package adds a validation record, work-package notes, a changelog entry, and current-state reconciliation. It changes no interface.
- **Breaking changes: none.** No skill, ADR, prompt, template, standard, specification, adapter, or example was modified. No skill name changed. No public entry point removed.
- **ADR-0032 unchanged and binding.** Docs-only, fail-closed, no scripts added, no network, no secrets, no private data, no autonomous git/release action. The private-consumer scope question remains reserved for a separate, separately authorised ADR; nothing here expands it.
- **Needs ADR: no.**
- **Public Quality Gate:** self-test and strict mode were run locally against the changed tree; results are recorded in the work-package return. The gate remains mandatory and is not bypassed by this record.

## Known Notes

| ID | Note | Status |
|---|---|---|
| EVI-001…003 | Phase 3 manifest format is not derivable from the adapter path | open — recommended for WP-157 (documentation polish); the spec is the outlier |
| EVI-004 | `minimal-ndf-project` manifest contradicts the spec's enumerations | open — recommended for WP-157 |
| EVI-005, EVI-006 | Output structure does not match the phase table, in both the minimal and the full variant | open — recommended for WP-157 |
| EVI-007 | Phase 0 presumes a participating human maintainer | open — an undocumented NDF-specific assumption; relevant to WP-156 |
| EVI-008 | Three of six adapter-path documents are German-only | open — recommended for WP-157 (i18n matrix) |
| G-13 externality | No independent observer; the single-maintainer bottleneck is structural | accepted limitation — unchanged since v1.0 |
| Second fixture | A second archetype was permitted but deliberately not added | closed for this WP — the first fixture addressed the named gaps; more evidence for its own sake was declined |

None of these is a blocker. **This work package fixes none of them** — they are recorded for the work packages that own the files.

## Result

IMPLEMENTED — PENDING NOVA / HUMAN-MAINTAINER ACCEPTANCE

A deeper public-neutral external validation run exists and is reproducible: NDF's published runbook executed end to end, every step and every phase individually evidenced, against a generic code-bearing repository NDF has never seen, returning **PASS WITH NOTES** with eight concrete findings and no blocker.

**G-13: `MATERIALLY_REDUCED` — not closed.** The depth limb that path A names is substantially addressed; the externality limb is unchanged and needs an observer this repository cannot supply.
