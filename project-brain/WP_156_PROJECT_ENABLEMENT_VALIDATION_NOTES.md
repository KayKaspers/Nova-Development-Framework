# WP-156 — Project Enablement Validation (Notes)

## Work Package

`NDF-WP-156 – Project Enablement Validation` — validate that NDF's public adapter path can enable an existing project without private leakage, automatic migration, Skill installation, or authority ambiguity. Profile: Project Enablement Validation, Prompt Mode Full, budget B2 target / B3 maximum, B4 not authorised. Support skills referenced (not invoked as tools): `ndf-work-package-runner`, `ndf-existing-project-analysis-runner`, `ndf-project-adapter-quality-reviewer`.

## Baseline

Revision `243225d3ad4ef2c55a830d7454d27b60c145f7e7`, branch `main`, working tree clean, index empty at preflight, `origin/main` at the same commit. v1.0.0 final released, v1.x promise active (ADR-0031); v1.1 planning only.

## Scenario Used

An **Enablement Dry-Run**: a procedural walk-through of Project Adapter Phase 0 (Intake) and Phase 1 (Read-only Review) mechanics, reasoning against the same generic, two-package, code-bearing archetype WP-155 already validated at the phase level — cited by its already-public properties, not re-executed or re-installed. No real project was engaged; no adapter output was generated into any repository. This deliberately stays inside the Project-Enablement Boundary (no migration, no adapter installation, no consumer Skill install, no runtime/MCP/network).

## Key Findings

Five findings (PEV-001…005), all documentation-consistency or documentation-gap issues; none is a security finding, none is a blocker. **Recorded, not fixed** — every affected file (adapter guide/conventions/intake template, the two support skills, the token-efficiency baseline) is outside this WP's authorised scope.

- **PEV-001** — no NDF document states the proposed `NDF-B0`…`NDF-B4`/`NDF-Lean` terminology-namespacing convention for consumer-project collisions; a repository-wide search returned zero matches before this record.
- **PEV-002** — EVI-007 (Phase 0's human-maintainer dependency, from WP-155) is still undocumented in the adapter guide/intake template themselves; this WP names and evidences the PREPARED/AUTHORIZED split but does not add it to the source documents (out of scope).
- **PEV-003** — `ndf-existing-project-analysis-runner`'s SKILL.md doesn't state which Phase 0 intake fields its output can vs. cannot cover.
- **PEV-004** — the first project feedback intake is framework-general; only 1 of 7 candidates bears on project enablement, and that candidate's own adoption is still pending Human-Maintainer commit.
- **PEV-005** — the Phase 0 Intake Template doesn't itself mark which fields are agent-preparable vs. human-only.

## Enablement Verdict

**Portable in its PREPARED half; correctly gated in its AUTHORIZED half.** Six of nine Phase 0 intake fields (Project Type, Tech Stack, Known Risks, and partially Project Name/Deployment Model/Repository URL) are read-only derivable by an implementation agent or by `ndf-existing-project-analysis-runner`; three (Maintainer Goals, Public/Private Status, Safety Notes) encode intent/policy and are human-only by construction. The minimal enablement artifact set is five items: Project Brief/Intake, Existing Project Analysis, an adapter-variant decision, an explicit scope boundary, and a next-authorised-action statement — everything else (CURRENT_STATE, terminology map, SESSION_HANDOFF, feedback note) is optional/situational. No hidden NDF knowledge, no private-project leakage, and no forced Skill installation were found necessary anywhere in the path.

## EVI-007 Outcome

**`CLARIFIED`.** Not `RESOLVED` (no source document changed; PEV-002 stands), not `OPEN` (the question has a direct, evidence-grounded answer), not `PARTIALLY_CLARIFIED` (the boundary is fully and consistently characterised). Phase 0 cannot be completed by an agent alone — an intentional governance boundary, not a defect — but an agent can PREPARE a non-authoritative draft covering most fields; only the Human Maintainer can AUTHORIZE the phase to advance. This PREPARED/AUTHORIZED distinction is named and tested field-by-field for the first time in this record.

## Feedback Intake Outcome

Source: the existing, already-public, already-neutralised cross-project feedback intake under `docs/validation/cross-project-feedback/` (the "first real project feedback intake" the v1.1 plan names). Used only in abstract form; no further private detail added; the underlying source record itself is unmodified by this WP. Of its seven candidates, one (source-handoff/registration preflight) bears on enablement; triaged as usability friction / documentation gap, not a blocker, not authority — its own adoption draft is independently still pending and not acted on here. No feedback was fabricated; where the source record is silent on enablement mechanics, this record says so.

## Compatibility

EVIDENCE_ONLY / ADDITIVE. No breaking change. No skill, ADR, prompt, template, standard, spec, adapter, or example modified. ADR-0031/0032 unchanged and binding; ADR-0032's private-consumer scope question stays reserved for a separate, separately authorised ADR (candidate ADR-0033). Needs ADR: no.

## Limitations

No real project engaged (archetype cited by its public properties, not re-executed). Enablement-boundary self-restraint tested only within this run. Feedback signal for enablement specifically is thin (1 of 7 candidates, itself not yet adopted). No independent observer (same structural limitation as G-13; G-13 itself untouched). Terminology-collision testing is conceptual, not exercised against a live conflict. PEV-001…005 recorded, not fixed — every target file is outside this WP's authorised scope. Single-maintainer bottleneck untouched. No token counts (no instrumentation under ADR-0032).

## Validation Summary

Public Quality Gate self-test and strict mode run locally against the changed tree; results recorded in the work-package return. `git diff --check` clean. Index empty throughout (no staging performed). No skill, ADR, or framework/adapter file changed. No private identifiers. No network use. No stage, commit, push, fetch, tag, or release.

## Next WP if Accepted

`NDF-WP-157 – Public Documentation Polish` — next planned, **not started**; requires its own complete execution prompt. Nova review of WP-156 has passed; **WP-157 must not start before Human-Maintainer acceptance (commit) of WP-156 is complete and verified.** PEV-001, PEV-002, PEV-003, PEV-005 (and the carried-forward EVI-001…006/EVI-008) are recommended inputs for WP-157.

## Forbidden Premature Work

No WP-157 start; no fix of PEV-001…005 or EVI-001…006/EVI-008 in this WP; no ADR change and no ADR-0033; no skill change; no adapter/spec/template/example change; no expansion of the ADR-0032 consumer scope; no real project migration or adapter installation; no consumer Skill install; no provider mechanics; no runtime; no v1.1 scope lock or release prep; no git write action of any kind.

## Compact Context Summary

WP-156 validated NDF's project-enablement path — not by re-running the adapter (WP-155 already did that at the phase level) but by testing the enablement layer itself: intake field-by-field authority, the existing-project-analysis skill's coverage, the Human-Maintainer authority model, a proposed terminology-collision convention, the adapter-variant decision rule, the minimal artifact set, session/handoff readiness, and the first real project feedback intake. It found the public path portable in its PREPARED half (agent-derivable: Project Type, Tech Stack, Known Risks, partial Project Name/Deployment/Repository URL) and correctly gated in its AUTHORIZED half (human-only: Maintainer Goals, Public/Private Status, Safety Notes) — a distinction named and evidenced for the first time here. **EVI-007 → `CLARIFIED`**: an intentional governance boundary, not a defect. Five new findings (PEV-001…005), all documentation gaps, none a blocker, recorded for WP-157. The first project feedback intake was used only in its already-public, already-neutralised form; only one of its seven candidates bears on enablement, and that candidate's own adoption remains independently pending. No real project was engaged, no adapter output generated, no Skill installed anywhere. Compatibility EVIDENCE_ONLY / ADDITIVE; gate green; artifacts are the validation record `docs/validation/v1-1/PROJECT_ENABLEMENT_VALIDATION.md` and these notes. Nova review passed; Human-Maintainer acceptance effective through the commit carrying this state. WP-157 is next planned and not started.
