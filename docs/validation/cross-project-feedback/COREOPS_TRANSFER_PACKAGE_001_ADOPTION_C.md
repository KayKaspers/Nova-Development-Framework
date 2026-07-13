# CoreOps Transfer Package 001 – Adoption C

> Work Package: `NDF-ADOPT-COREOPS-001C` — Governance Status Modeling and Framework Tailoring Patterns
> Type: docs-only / governance-guidance adoption

## 1. Status

```text
Adoption Status: Implemented, pending Nova review
Candidates: NDF-FC-COREOPS-005, 006, 007
NDF Version: not yet assigned
Human-Maintainer Commit: pending
CoreOps Backlink: pending
```

## 2. Source Intake

Based on the completed intake review `NDF-INTAKE-COREOPS-001` (intake commit `d08e35e`). Adoption A (`1ebffa6`) and Adoption B (`e894c6f`) are committed and untouched here. Only generalized, project-neutral governance patterns are adopted; no source content, no private paths, no CoreOps-specific mandatory values are copied into NDF rules.

## 3. Adopted Candidates

- **NDF-FC-COREOPS-005** — Accepted product direction without technical fixation (`new` → `guidance-only`).
- **NDF-FC-COREOPS-006** — Multi-dimensional status models instead of an overloaded single status (`partially-covered` → `guidance-only`, optional).
- **NDF-FC-COREOPS-007** — Framework tailoring before framework adoption (`new` → `guidance-only`).

Not addressed here: 001/003/004 (Adoption A), 002 (Adoption B).

## 4. Existing Coverage

- **005:** decision/ADR records exist, but no direction-vs-technical status distinction.
- **006:** `docs/project-system/CAPABILITY_MATRIX_SPEC.md` defined **one** overloaded status field; no separate roadmap/implementation/support (trust) dimension.
- **007:** `PROJECT_ADAPTER_V0_2.md` adapts NDF to a project; no external-framework candidate→tailoring model existed.

## 5. Adopted Gaps

Three optional, project-neutral governance patterns: a direction-vs-technical decision status family; an optional multi-dimensional capability status model (added additively to the existing single-status spec, which stays valid); and a controlled external-framework tailoring pattern with a conflict hierarchy and framework-overload guards.

## 6. Decision Modeling

New guidance `docs/governance/NDF_DECISION_AND_STATUS_MODELING_GUIDANCE.md` separates Decision Class (`product-direction / governance-direction / architecture-decision / technical-decision / operational-decision`), Lifecycle Status (`proposed / accepted / accepted-with-notes / deferred / rejected / superseded`), and Binding Level (`informative / guidance / binding-governance / normative`). A single overloaded status is avoided where it would merge these dimensions.

## 7. Accepted Product Direction

An accepted product/governance direction records intent without accepting architecture, technology, implementation, dependency, protocol, or a release commitment; technical realization needs its own later architecture/ADR/WP decision under Human-Maintainer approval. The guidance explicitly states `accepted product direction ≠ architecture accepted / technology selected / implementation approved / release commitment`.

## 8. Multi-Dimensional Status Guidance

Optional model with independent dimensions (Roadmap / Implementation / Support / optional Evidence). Separation rules: roadmap ≠ implementation; implementation ≠ supported; vendor/protocol mention ≠ support; **support requires defined evidence**. The existing single-status model remains valid and is the default; multi-dimensional use is optional and used only on real need. Applied additively to `docs/project-system/CAPABILITY_MATRIX_SPEC.md`.

## 9. Framework Tailoring

New guidance `docs/governance/NDF_EXTERNAL_FRAMEWORK_TAILORING_GUIDANCE.md`: an applicability review, mandatory-vs-optional element separation, a project-neutral conflict hierarchy (law → Human-Maintainer authority → security/safety invariants → accepted ADRs/scope locks → normative NDF rules → project-specific governance → tailored external-framework guidance → advisory), tailoring result values, framework-overload guards, optional profiles, no compliance/certification claim by terminology, and a Human-Maintainer gate. Distinct from the NDF-to-project project adapter.

## 10. Optionality Boundary

All three patterns are optional guidance, not universal NDF-core requirements. Simple projects are not burdened with multiple status dimensions or external frameworks; no existing matrix/decision model is retroactively invalidated; no CoreOps-specific value becomes mandatory.

## 11. Files Changed

- `docs/governance/NDF_DECISION_AND_STATUS_MODELING_GUIDANCE.md` (new — candidates 005 + 006 status guidance)
- `docs/governance/NDF_EXTERNAL_FRAMEWORK_TAILORING_GUIDANCE.md` (new — candidate 007)
- `docs/project-system/CAPABILITY_MATRIX_SPEC.md` (additive — optional multi-dimensional status; single-status remains valid)
- `docs/validation/cross-project-feedback/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_C.md` (new — this document)
- `project-brain/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_C_NOTES.md` (new)

**Path note:** the capability matrix spec was updated at its actual path `docs/project-system/CAPABILITY_MATRIX_SPEC.md`; no file was created at `framework/standards/CAPABILITY_MATRIX_SPEC.md`; no file was moved or renamed.

## 12. Compatibility Assessment

Additive and guidance-oriented. Existing single-status matrices and decision records remain valid; no technical decision is derived from a product decision; no external methodology is made fully mandatory; no existing ADR hierarchy is overridden; no compliance/certification claim is created; no new NDF version; no retroactive migration forced. ADR-0031/0032 unaffected and unchanged. Breaking-change potential: **low**.

## 13. Governance Assessment

Governance-positive. The direction-vs-technical separation prevents implicit technical commitment; the optional multi-dimensional status prevents "planned/implemented = supported" misreadings; the tailoring conflict hierarchy keeps law, Human-Maintainer authority, security invariants, and accepted ADRs above tailored external guidance. Human-Maintainer control preserved throughout.

## 14. Validation

See the WP test matrix (preflight, candidate 005/006/007, cross-document consistency, scope, language/neutrality, formatting). All changes additive; only the corrected Allowed Files changed; no forbidden file, ADR, skill, Adoption-A/B, or CoreOps file touched; no file moved/renamed; no network; no git write. Public Quality Gate not run (script execution not permitted by this WP).

## 15. Remaining Candidates

All seven CoreOps Transfer Package 001 candidates are now functionally handled across the three adoption WPs: 001/003/004 (Adoption A), 002 (Adoption B), 005/006/007 (Adoption C). Remaining: the CoreOps backlink (separate traceability WP) after the Human-Maintainer commit.

## 16. Lessons Learned

```text
Lessons Learned:
- Separating decision class, lifecycle and binding level lets a project accept a direction without implying technical/architecture/release acceptance.
- An optional multi-dimensional status model added additively keeps the existing single-status matrix valid while enabling trust/support separation where needed.
- A conflict hierarchy plus framework-overload guards let a project tailor external frameworks without a parallel decision structure or an unearned compliance claim.
NDF Feedback Candidates: none newly created here.
Project-local Follow-ups: none (project-local details stay in the source project).
```

## 17. Next Decision

Nova review of `NDF-ADOPT-COREOPS-001C`; then a Human-Maintainer decision and a separate maintainer commit; afterwards a separate CoreOps-traceability WP to backlink all actually adopted candidates. The NDF version for this adoption is not yet assigned; the CoreOps backlink stays pending until the maintainer commit.
