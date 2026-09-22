# WP-155 — External Validation Improvement (Notes)

## Work Package

`NDF-WP-155 – External Validation Improvement` — G-13 path A: a deeper public, step-evidenced, neutral validation run. Profile: Validation / evidence improvement, Prompt Mode Full, budget B2 target / B3 maximum. Support skills: `ndf-work-package-runner`, `ndf-validation-evidence-reviewer`, `ndf-public-neutrality-guard`.

## Baseline

Revision `07b2884f0c649e482a53434cd3210023b6c4d576`, branch `main`, working tree clean, index empty. v1.0.0 final released, v1.x promise active (ADR-0031); v1.1 planning only.

## Scenario Used

NDF's published [Independent Adapter Validation Runbook](../docs/validation/project-adapter/INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md) executed end to end — all six steps individually evidenced — with the adapter's minimal variant (plus Phase 7) applied to `sample-taskqueue`: a generic two-package job-queue repository, 14 files, 183 lines, real Python and JavaScript, built for this run and kept **outside** the NDF repository (scratchpad only; reconstructible from the spec in the validation record).

The fixture was built adversarially — no `docs/`, mixed doc extensions, three disagreeing version sources, three unguarded irreversible operations, no CI, no licence consistency, a genuinely failing test suite. One fixture only: the optional second fixture was deliberately declined once the first addressed the named gaps.

## Key Findings

Eight findings (EVI-001…008), all documentation-consistency issues in the adapter path; none is a security finding, none is a blocker. **Recorded, not fixed** — every affected file is outside this WP's authorised scope.

- **EVI-001/002/003 — Phase 3 is not derivable from the documentation.** The conventions and the output-structure template make `PROJECT_MANIFEST.md` canonical Markdown; the manifest spec they point to prescribes bare YAML and contains zero mentions of Markdown. 4 of 6 shipped manifest artifacts are standalone YAML. No rule covers a mandatory field the source cannot supply. This was the single phase the run rated `rework`.
- **EVI-004** — `examples/minimal-ndf-project` manifest uses `status: "example"` (not in the spec's five values) and `ndf_level: 2` while declaring gates and health score (spec ladder: levels 3 and 4).
- **EVI-005/006** — the minimal phase chain omits Phase 4 but the minimal output structure lists its output; the full output structure lists `docs/ndf/*` that no phase produces.
- **EVI-007** — Phase 0 presumes a participating human maintainer. A genuine, undocumented NDF-specific assumption.
- **EVI-008** — three of the six adapter-path documents an adopter needs are German-only.

What the run did **not** find matters as much: no hidden assumption that NDF only works on documentation-shaped, single-package, or already-NDF-organised repositories. The §7 safety rules and the `unknown` / `not evidenced` / `n/a` vocabulary held under real code and real missing evidence.

## G-13 Outcome

**`MATERIALLY_REDUCED` — not closed.** G-13 has two limbs and this WP moves exactly one:

- **Depth** — substantially closed. PSV-001 (four of six runbook steps "not provided") and both E-03 limits (no real code, monorepo not covered) now have direct, reproducible answers: six steps and eleven phases evidenced, 15 deterministic checks.
- **Externality** — unchanged. The run is agent-executed and agent-authored. On independence alone it is weaker than the two genuine independent runs already on record.

Closure is not claimed and would be dishonest on one agent-executed fixture. A future closure needs at least one genuinely independent run against a code-bearing fixture, with the per-step record this run shows is achievable.

## Compatibility

EVIDENCE_ONLY / ADDITIVE. No breaking change. No skill, ADR, prompt, template, standard, spec, adapter, or example modified. ADR-0031/0032 unchanged and binding; the ADR-0032 private-consumer scope question stays reserved for a separate, separately authorised ADR (candidate ADR-0033). Needs ADR: no.

## Limitations

Not independent (agent authored the fixture and ran the check — the largest limitation, structural). Author bias mitigated, not removed. One fixture, one archetype. Minimal variant plus Phase 7 only; Phases 4/5/6/9 and the full variant unexercised against code. No token counts (no instrumentation under ADR-0032). Single-maintainer bottleneck untouched. No project enablement performed.

## Validation Summary

Public Quality Gate self-test **passed**; strict mode **passed** (0 errors, 0 warnings, 4 notices). All 13 relative links and 7 anchors in the validation record resolve. `git diff --check` clean. Index empty. No skill, ADR, or framework execution-contract file changed. No private identifiers. No network use. No stage, commit, push, fetch, tag, or release.

## Next WP if Accepted

`NDF-WP-156 – Project Enablement Validation`. **WP-156 must not start before Nova review and Human-Maintainer acceptance of WP-155.** EVI-007 is relevant input for WP-156; EVI-001…006 and EVI-008 are recommended for WP-157 (public documentation polish).

## Forbidden Premature Work

No WP-156 start; no adapter, spec, template, or example fix for EVI-001…008 in this WP; no ADR change and no ADR-0033; no skill change; no expansion of the ADR-0032 consumer scope; no provider mechanics; no runtime; no v1.1 scope lock or release prep; no git write action of any kind.

## Compact Context Summary

WP-155 executed NDF's own public external-validation runbook end to end against a generic, code-bearing, NDF-naive fixture held outside the repository, recording every one of the six runbook steps and all eleven adapter phases individually — the record G-13 named as missing. Verdict **PASS WITH NOTES**, no blocker, eight findings (EVI-001…008), one phase rated `rework` because the manifest format is contradicted between the adapter conventions and the manifest spec. Fifteen deterministic checks are separated from the semantic review throughout; evidence classes (repository-internal, public generic, project-local, Human-Maintainer, independent, inference) are kept distinct and not aggregated. No project-local, Human-Maintainer, or independent evidence was used or invented. **G-13 → `MATERIALLY_REDUCED`, not closed:** depth substantially addressed, externality unchanged and unreachable from inside this repository. Compatibility EVIDENCE_ONLY / ADDITIVE; gate green; artifacts are the validation record `docs/validation/v1-1/EXTERNAL_VALIDATION_IMPROVEMENT.md` and these notes. Pending Nova review and Human-Maintainer acceptance; WP-156 is next and not started.
