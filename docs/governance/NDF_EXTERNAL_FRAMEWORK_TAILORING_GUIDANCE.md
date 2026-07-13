# NDF External Framework Tailoring Guidance

> Sprachstatus / Language status: EN mit deutscher Kurz-Einleitung. / English with a short German introduction.
>
> DE: Optionale, projektneutrale Guidance zum kontrollierten Tailoring externer Frameworks/Methoden/Standards vor ihrer Übernahme — Schutz vor Framework-Overload, keine Compliance-/Zertifizierungsbehauptung, keine universelle Pflicht.

## 1. Status

```text
Document Status: Implemented, pending Nova review
Guidance Type: Optional framework-tailoring guidance
Normative Release: Not yet assigned
```

Adopted via `NDF-ADOPT-COREOPS-001C` from cross-project feedback candidate `NDF-FC-COREOPS-007` (framework tailoring before framework adoption). Optional guidance — distinct from the NDF-to-project project adapter.

## 2. Purpose

Provide a controlled way to evaluate and tailor external frameworks, methodologies, or standards **before** adopting them as project governance, to prevent framework overload and premature full adoption, and to keep NDF core lean.

## 3. Scope

Optional governance guidance only. **Out of scope:** the NDF-to-project project adapter (`../project-starter/PROJECT_ADAPTER_V0_2.md` handles adapting NDF to a project — a different concern), any change to accepted ADRs/security invariants/skills/CoreOps sources, any compliance/certification assessment. No new NDF version.

## 4. External Framework Definition

An external framework/method/standard is any externally authored governance, process, methodology, or compliance model a project might adopt. Naming such a framework does **not** make it project governance.

## 5. Applicability Review

Before adopting, review at least:

```text
goal and problem statement
actual applicability
mandatory versus optional elements
conflicts with law, security, NDF and accepted ADRs
adoption, tailoring or exclusion of individual elements
role and responsibility impact
documentation and process cost
required evidence
breaking-change or migration effect
review and update need
```

## 6. Mandatory versus Optional Elements

Separate a framework's mandatory core from its optional elements. Adopt only what solves a real problem; exclude or defer the rest explicitly.

## 7. Conflict Hierarchy

A project-neutral precedence order (adjust only if existing normative NDF documents already define a binding different hierarchy):

```text
Applicable law and regulation
Human-Maintainer authority
Security and safety invariants
Accepted ADRs and scope locks
Normative NDF rules
Project-specific accepted governance
Tailored external-framework guidance
Roadmap or advisory guidance
```

## 8. Tailoring Decision

Record a tailoring result, e.g.:

```text
adopted
adopted-with-tailoring
guidance-only
optional-profile
deferred
rejected
not-applicable
```

These are guidance values, not a mandatory global status list.

## 9. Roles and Responsibilities

Tailoring must not silently create a second parallel decision structure or duplicate roles. Map any new role/responsibility onto existing NDF roles (Nova planning/review, implementation agent, Human Maintainer) rather than inventing overlapping authorities.

## 10. Process and Documentation Cost

Weigh the documentation/process cost of each adopted element. Prefer the lightest form that solves the problem; avoid meetings, artifacts, or terminology with no real benefit.

## 11. Security and Compliance Claims

Adopting a framework's terminology does **not** create a compliance or certification claim. No compliance/certification status is asserted merely by naming or tailoring an external framework; any real claim needs its own evidenced process outside this guidance.

## 12. Optional Profiles

Where projects have different needs, prefer optional profiles/guidance over universal mandates. A tailored subset can be offered as an `optional-profile` rather than forced on every project.

## 13. ADR and Governance Review

If tailoring touches architecture or accepted decisions, route it through an ADR/governance review rather than adopting silently.

## 14. Human-Maintainer Gate

Framework adoption, tailoring decisions, and any conflict resolution stay under Human-Maintainer control. This guidance does not replace a Human-Maintainer decision.

## 15. Periodic Review

Tailored external-framework guidance should carry a review/update condition, since external frameworks and project needs change over time.

## 16. Anti-Patterns

- Full adoption of a framework by name alone.
- Introducing roles/meetings/terminology with no benefit.
- Duplicate terminology or a second parallel decision structure.
- A compliance/certification claim created only by terminology.
- Forcing one framework's full requirements on every project.

## 17. Compatibility

Additive and optional; existing governance remains valid; no ADR hierarchy is overridden; no compliance/certification claim is created; no retroactive migration is forced; no new NDF version is claimed. ADR-0031/0032 unaffected. Breaking-change potential: low.

## 18. Examples

- A project evaluates an external operations/compliance framework, adopts two elements `adopted-with-tailoring`, marks the rest `deferred`/`not-applicable`, and records the conflict hierarchy so security invariants and accepted ADRs still win.
- A project offers a tailored subset as an `optional-profile` for teams that need it, keeping the default lean.

## 19. Open Questions

- Whether a shared tailoring-decision checklist template is added later (not created here).
- How tailoring results integrate with a project's decision index (project-specific).
- Whether specific tailoring-result values become a recommended (still optional) vocabulary.
