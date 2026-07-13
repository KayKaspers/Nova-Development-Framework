# NDF Decision and Status Modeling Guidance

> Sprachstatus / Language status: EN mit deutscher Kurz-Einleitung. / English with a short German introduction.
>
> DE: Optionale, projektneutrale Governance-Guidance zur Trennung von Entscheidungsart, Lebenszyklus und Bindungsgrad sowie zu optionalen mehrdimensionalen Statusmodellen. Keine universelle NDF-Core-Pflicht.

## 1. Status

```text
Document Status: Implemented, pending Nova review
Guidance Type: Optional project-governance guidance
Normative Release: Not yet assigned
```

Adopted via `NDF-ADOPT-COREOPS-001C` from cross-project feedback candidates `NDF-FC-COREOPS-005` (accepted product direction) and the status-model half of `NDF-FC-COREOPS-006` (multi-dimensional status). Optional guidance — not a mandatory requirement for every NDF project.

## 2. Purpose

Help projects separate **what** a decision is (class), **where it stands** (lifecycle), and **how binding** it is (binding level); allow an accepted product/governance direction without accepting technical fixation; and provide an optional multi-dimensional status model for capabilities that legitimately hold several independent states — without burdening simple projects.

## 3. Scope

Optional governance guidance only. **Out of scope:** any mandatory change to the single-status capability matrix (which remains valid; see `../project-system/CAPABILITY_MATRIX_SPEC.md`), any change to accepted ADRs, security invariants, skills, or CoreOps sources. No new NDF version.

## 4. Decision Class

A decision carries exactly one primary class, e.g.:

```text
product-direction
governance-direction
architecture-decision
technical-decision
operational-decision
```

Projects may tailor these terms; the point is not to conflate a product/governance direction with a technical decision.

## 5. Lifecycle Status

A decision's lifecycle is tracked separately, e.g.:

```text
proposed
accepted
accepted-with-notes
deferred
rejected
superseded
```

## 6. Binding Level

The binding degree is a separate dimension, e.g.:

```text
informative
guidance
binding-governance
normative
```

A single overloaded status value should be avoided where it would merge decision class, lifecycle, and binding level.

## 7. Accepted Product Direction

An accepted product or governance direction may establish **what a project intends to achieve** without accepting a technical architecture, implementation, dependency, or protocol. It records intent and guardrails early while deferring technical acceptance.

## 8. Technical Decision Boundary

`accepted product direction` does **not** imply, and must not be read as:

```text
architecture accepted
technology selected
implementation approved
release commitment
```

Technical realization requires its own later architecture, ADR, or work-package decision. Human-Maintainer approval remains required.

## 9. Single-Status Models

A simple single-status model remains fully valid and is the default. A project should keep a single status when no independent status dimensions are needed, no misreading arises, and no separate support/evidence status is required.

## 10. Multi-Dimensional Status Models

A multi-dimensional model is **optional** guidance, useful when a capability can hold several independent states at once. Use it when roadmap, implementation, and support progress independently, when maturity/evidence is assessed separately, or when a single status would produce false conclusions.

## 11. Example Dimensions

```text
Roadmap Status
Implementation Status
Support Status
Evidence or Validation Status
```

Example:

```text
Roadmap Status: target-observe
Implementation Status: not-implemented
Support Status: not-supported
Evidence Status: not-assessed
```

## 12. Evidence and Support Status

Separation rules:

```text
Roadmap inclusion does not imply implementation.
Implementation does not imply supported status.
Vendor or protocol mention does not imply support.
Support requires defined evidence.
```

## 13. Tailoring Guidance

Projects tailor these dimensions to real need. Keep a single status when sufficient; adopt multiple dimensions only when they prevent misreadings. Do not force every capability matrix into multiple dimensions.

## 14. Human-Maintainer Gate

Decision acceptance, status changes, and any move from direction to technical commitment stay under Human-Maintainer control. This guidance does not replace a Human-Maintainer decision.

## 15. Compatibility

Additive and optional. Existing single-status matrices and decision records remain valid; no retroactive migration is forced; no CoreOps-specific values become mandatory NDF values; no new NDF version is claimed. ADR-0031/0032 unaffected. Breaking-change potential: low.

## 16. Examples

- A project accepts a "self-hostable operations direction" (`product-direction`, `accepted`, `guidance`) while leaving the concrete stack a later `architecture-decision`.
- A capability lists `Roadmap Status: planned`, `Implementation Status: not-implemented`, `Support Status: not-supported` to avoid a reader inferring support from a roadmap entry.

## 17. Anti-Patterns

- Reading an accepted product direction as an accepted architecture/technology/release.
- One overloaded status value hiding that something is planned but unsupported.
- Forcing multi-dimensional status on a small project that does not need it.
- Deriving support from roadmap or implementation status alone.

## 18. Open Questions

- Whether a shared optional template for multi-dimensional status is added later (not created here).
- How a project maps these dimensions onto its existing decision index (project-specific).
- Whether specific binding-level names become a recommended (still optional) vocabulary.
