# CoreOps Transfer Package 001 – NDF Intake Review

> Work Package: `NDF-INTAKE-COREOPS-001`
> Type: cross-project feedback intake review (docs-only, read-only analysis)
> NDF base: development HEAD `eeb2124` (normative release tag `v1.0.0` on `9dcadc1`)
> Status: **implemented – pending Nova review**
> This document records an intake **review and recommendation only**. It does **not** adopt, implement, or merge any candidate into the NDF. No NDF rule, skill, or template is modified by this work package.

## 1. Purpose

Review the seven cross-project feedback candidates bundled in CoreOps Transfer Package 001 against the current NDF development state, classify each candidate, document concrete existing NDF coverage, identify gaps, and recommend possible later adoption work packages. No adoption is performed here.

## 2. Source and Authorization

- **Source project:** CoreOps (an independent, self-hosted operations control plane; source repository external to NDF).
- **Transfer Package Status (source):** Approved for NDF Intake.
- **Source Human-Maintainer gates:** all seven candidates carry `Human-Maintainer Gate: approved` and `Status: approved-for-transfer`.
- **Adoption status (source):** Not transferred; no candidate is `transferred-to-ndf` or `adopted-in-ndf`.
- **Previous CoreOps source blocker:** resolved (finalize-intake-approval-gates commit present in the source repository).

## 3. NDF Preflight

```text
Repository:      D:/Projects/Nova-Development-Framework
Branch:          main
HEAD:            eeb2124
Working tree:    clean at preflight
Normative tag:   v1.0.0 -> 9dcadc1 (one commit behind development HEAD)
Tags at HEAD:    none
```

Development HEAD is unchanged from the previously blocked run (`eeb2124`). The intake is performed against this current local NDF state; the normative `v1.0.0` baseline (`9dcadc1`) is noted as one commit behind HEAD.

## 4. Classification and Recommendation Vocabulary

Each candidate receives exactly one intake classification (`new`, `partially-covered`, `already-covered`, `conflicting`, `needs-split`, `insufficient-evidence`) and exactly one recommendation (`adopt`, `adopt-with-changes`, `merge-with-existing-work`, `guidance-only`, `template-only`, `skill-update-candidate`, `defer`, `duplicate`, `reject`, `split`).

`already-covered`/`duplicate` require concrete existing NDF evidence; `new`/`partially-covered` require a concrete gap description.

---

## 5. Candidate Assessments

### NDF-FC-COREOPS-001 – Git Read versus Git Write in Work-Package-Prompts

- **Source Lesson:** LL-001
- **CoreOps Bundle:** Bundle 1 (Work-Package Safety and Source Handling)
- **Intake Classification:** `partially-covered`
- **Recommendation:** `adopt-with-changes`
- **Existing NDF Coverage:** The forbidden write side already exists, and the read-only concept exists but only in a non-prompt-block location.
- **Exact NDF Evidence:**
  - `framework/prompts/blocks/BLOCK_LIMITS.md` forbids `Kein Commit / Kein Push / Kein Reset / Kein Rebase / Kein Force Push` (write operations) but contains **no** explicit "allowed read-only git" list.
  - `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md` (Layer 4 – Evidence Context) explicitly permits "read-only git status/log" as evidence.
  - `docs/validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md` compression matrix lists "Self-Check (`git status`/`diff`)" as a recurring allowed step.
- **Gap:** There is no explicit positive read-only-git allowlist inside the reusable prompt block that work-package prompts import (`BLOCK_LIMITS.md`). The read-only permission is only implicit in the Context Economy concept doc and the skills matrix, so a prompt that imports only the limits block still lacks an explicit read/write distinction.
- **Generalizability:** High — applies to every NDF work package where the implementation agent must verify scope read-only but must not write.
- **Suggested NDF Target Area:** `framework/prompts/blocks/BLOCK_LIMITS.md` (or a dedicated git block); optionally `framework/standards/git-standard.md`.
- **Core or Optional:** Guidance-level clarification of an existing invariant; not a new core rule.
- **Potential Files:** `BLOCK_LIMITS.md`, `git-standard.md`.
- **Skill Impact:** `ndf-work-package-runner` already carries the self-check; a read-only allowlist would align its wording.
- **Template Impact:** None required.
- **Breaking-Change Potential:** Low (additive clarification).
- **Migration/Adoption Impact:** None; existing prompts remain valid.
- **Suggested Adoption Work Package:** WP A (Work-Package Prompt Safety Baseline Update).
- **Dependencies:** None.
- **Notes:** Aligns the prompt block with the already-documented Context Economy Layer 4 permission.

### NDF-FC-COREOPS-002 – Full Local Skills Availability with Selective Activation (+ Provenance/Lock)

- **Source Lesson:** LL-002, LL-003
- **CoreOps Bundle:** Bundle 2 (Skills Availability and Context Economy)
- **Intake Classification:** `partially-covered`
- **Recommendation:** `merge-with-existing-work`
- **Existing NDF Coverage:** The availability + selective-activation half is already well covered.
- **Exact NDF Evidence:**
  - `docs/validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md` defines skills-first with mandatory referencing plus Full/Standard/Short selection — i.e., full availability with selective use.
  - `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md` defines selective context/skill loading.
  - `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` and `docs/adr/ADR-0032-skill-security-policy.md` govern skill safety (fail-closed, docs-only, no third-party import).
  - A `ndf-skill-supply-chain-risk-reviewer` skill exists.
- **Gap:** NDF has **no** skill **provenance + hash-lock** mechanism — no byte-identical import record and no per-file SHA-256 lock artifact for a locally provided skills pack. A repository-wide search for `SHA-256 / lock file / byte-identical / provenance` returned only unrelated backup/audit matches, none for skills.
- **Generalizability:** High — relevant to any NDF project importing a full local skills pack that must remain integrity-verifiable.
- **Suggested NDF Target Area:** ADR-0032 environment / `ndf-skill-supply-chain-risk-reviewer` documentation; a provenance + lock reference pattern.
- **Core or Optional:** The selective-activation half is already core; the provenance/lock half would be an optional security-supply-chain pattern.
- **Potential Files:** `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (reference), skill-supply-chain reviewer docs.
- **Skill Impact:** `skill-update-candidate` for `ndf-skill-supply-chain-risk-reviewer` (add provenance/lock guidance).
- **Template Impact:** Possible optional provenance/lock reference template.
- **Breaking-Change Potential:** Low (additive, security-positive).
- **Migration/Adoption Impact:** None for existing skills; new guidance for future imports.
- **Suggested Adoption Work Package:** WP B (Skill Provenance and Integrity Lock Guidance).
- **Dependencies:** ADR-0032.
- **Notes:** Only the provenance/lock component is novel; the availability/selective-activation component should be marked merged into existing skills-first/context-economy work.

### NDF-FC-COREOPS-003 – Source-Handoff for Chat/External Documents

- **Source Lesson:** LL-004
- **CoreOps Bundle:** Bundle 1
- **Intake Classification:** `new`
- **Recommendation:** `adopt-with-changes`
- **Existing NDF Coverage:** Registration/analysis flows exist, but no source-verification preflight.
- **Exact NDF Evidence:** `ndf-existing-project-analysis-runner` and project-starter/registration flows exist, but a repository search for `source handoff / source preflight / truncation check` returned no matches; no explicit verification-before-registration procedure is defined.
- **Gap:** No standard "source preflight" (identity, section completeness, truncation detection, unchanged-source status) is required before an agent claims a "complete registration" of a large externally/chat-provided document.
- **Generalizability:** High — applies to any project registering large external source documents into a repository.
- **Suggested NDF Target Area:** Work-package prompt guidance for `docs-only` registration work packages; possibly `ndf-existing-project-analysis-runner` environment.
- **Core or Optional:** Optional guidance/reference pattern.
- **Potential Files:** work-package prompt guidance / registration standard.
- **Skill Impact:** Possible guidance addition to `ndf-existing-project-analysis-runner`.
- **Template Impact:** Possible source-preflight checklist.
- **Breaking-Change Potential:** Low (additive prechecks).
- **Migration/Adoption Impact:** None.
- **Suggested Adoption Work Package:** WP A (Work-Package Prompt Safety Baseline Update).
- **Dependencies:** None.
- **Notes:** The candidate generalizes only the procedure; no source content is transferred.

### NDF-FC-COREOPS-004 – Blocked Report without Artificial Intermediate Commit

- **Source Lesson:** LL-005
- **CoreOps Bundle:** Bundle 1
- **Intake Classification:** `partially-covered`
- **Recommendation:** `adopt-with-changes`
- **Existing NDF Coverage:** The `STOP` outcome and human-only commit are covered; the structured no-change report format is not.
- **Exact NDF Evidence:**
  - `framework/standards/WORK_PACKAGE_REVIEW_GATE_STANDARD.md` and `framework/standards/WORK_PACKAGE_LIFECYCLE.md` define `STOP` as a decision value and human-controlled commit.
  - `framework/prompts/blocks/BLOCK_FEEDBACK_TO_NOVA.md` defines the report structure but assumes changes were made (it lists "Geänderte Dateien / Ausgeführte Tests").
- **Gap:** No explicit "Blocked Report" format establishing that a fail-closed stop **without any file change** is itself a complete, review-ready result (reason, affected preflight check, unblock condition, no intermediate commit needed).
- **Generalizability:** High — applies to every fail-closed NDF workflow with a human-maintainer commit gate.
- **Suggested NDF Target Area:** `BLOCK_FEEDBACK_TO_NOVA.md` and/or `WORK_PACKAGE_LIFECYCLE.md` (fail-closed section).
- **Core or Optional:** Guidance-level standard format.
- **Potential Files:** `BLOCK_FEEDBACK_TO_NOVA.md`, `WORK_PACKAGE_LIFECYCLE.md`.
- **Skill Impact:** `ndf-work-package-runner` / `ndf-compact-context-summary-runner` could carry the blocked-report variant.
- **Template Impact:** Optional blocked-report template.
- **Breaking-Change Potential:** Low.
- **Migration/Adoption Impact:** None.
- **Suggested Adoption Work Package:** WP A (Work-Package Prompt Safety Baseline Update).
- **Dependencies:** None.
- **Notes:** This intake run is itself a live example (blocked, then resumed without an intermediate commit).

### NDF-FC-COREOPS-005 – Accepted Product Direction without Technical Commitment

- **Source Lesson:** LL-011
- **CoreOps Bundle:** Bundle 3 (Governance and Status Modeling)
- **Intake Classification:** `new`
- **Recommendation:** `guidance-only`
- **Existing NDF Coverage:** NDF has ADR/decision records for technical decisions but no direction-vs-technical status distinction.
- **Exact NDF Evidence:** `framework/templates/governance/DECISION_RECORD_TEMPLATE.md` is a standard decision/options/consequences record; the ADR set (`adr/`) captures technical/architecture decisions. No status value expresses "strategic direction accepted without technical/architecture commitment."
- **Gap:** No optional status family that lets a project register a strategic product direction early while explicitly deferring technical/architecture/certification acceptance.
- **Generalizability:** Medium–High — useful for any project formalizing strategic guardrails before final architecture.
- **Suggested NDF Target Area:** Decision-index / governance guidance (optional status-value family).
- **Core or Optional:** Optional guidance pattern; not a core mandatory field.
- **Potential Files:** decision-index/governance guidance doc.
- **Skill Impact:** Possibly `ndf-adr-governance-review` guidance (advisory only).
- **Template Impact:** Optional decision-index status-family note.
- **Breaking-Change Potential:** Low–Medium (new optional status family; no change to existing mandatory fields).
- **Migration/Adoption Impact:** None for existing decisions.
- **Suggested Adoption Work Package:** WP C (Governance Status Modeling Patterns).
- **Dependencies:** ADR governance boundaries (ADR-0031/0032 unaffected).
- **Notes:** Must remain optional to avoid over-constraining projects that only use ADRs.

### NDF-FC-COREOPS-006 – Multi-Dimensional Status Models

- **Source Lesson:** LL-008
- **CoreOps Bundle:** Bundle 3
- **Intake Classification:** `partially-covered` (tension with current single-status spec)
- **Recommendation:** `guidance-only`
- **Existing NDF Coverage:** NDF has a capability matrix, but with a single overloaded status dimension.
- **Exact NDF Evidence:** `docs/project-system/CAPABILITY_MATRIX_SPEC.md` defines **one** status field with values `not_planned / planned / in_progress / implemented / verified / deprecated`. `framework/project-system/templates/CAPABILITY_MATRIX_TEMPLATE.md` uses a single `Status` column. There is no separate roadmap/implementation/support (trust) dimension.
- **Gap:** The current single field conflates planning, build progress, and trust/support. The candidate proposes three independent dimensions (roadmap, implementation, support) to prevent "planned = supported" or "implemented = supported" misreadings.
- **Generalizability:** High — applies to any capability/feature/integration matrix.
- **Suggested NDF Target Area:** `CAPABILITY_MATRIX_SPEC.md` as an **optional** multi-dimensional variant (not a replacement).
- **Core or Optional:** Recommend **optional guidance / template variant**, explicitly not core-mandatory (the source candidate itself flagged this open question).
- **Potential Files:** `CAPABILITY_MATRIX_SPEC.md`, `CAPABILITY_MATRIX_TEMPLATE.md`.
- **Skill Impact:** None mandatory.
- **Template Impact:** Optional multi-dimensional capability-matrix template variant.
- **Breaking-Change Potential:** Low if additive/optional; would become breaking only if it replaced the existing single-status spec (not recommended).
- **Migration/Adoption Impact:** None for projects keeping the single-status matrix.
- **Suggested Adoption Work Package:** WP C (Governance Status Modeling Patterns).
- **Dependencies:** None.
- **Notes:** Keep the existing single-status matrix valid; add the multi-dimensional model as an optional pattern for projects that need trust/support separation.

### NDF-FC-COREOPS-007 – Framework Tailoring before Framework Adoption

- **Source Lesson:** LL-013
- **CoreOps Bundle:** Bundle 3
- **Intake Classification:** `new`
- **Recommendation:** `guidance-only`
- **Existing NDF Coverage:** NDF has a project adapter, but it adapts NDF to a project — not external-framework adoption.
- **Exact NDF Evidence:** `docs/project-starter/PROJECT_ADAPTER_V0_2.md` covers adapter phases and required NDF artifacts (adapting NDF to an existing project). No "external framework candidate → tailoring decision" two-phase model exists; a repository search for external methodology frameworks (e.g., ITIL/PRINCE2) found no adoption/tailoring pattern.
- **Gap:** No reference pattern for handling multiple external governance/compliance frameworks via an explicit "candidate, not accepted" phase plus a separate tailoring decision, to avoid framework overload and premature full adoption.
- **Generalizability:** Medium–High — relevant to any project evaluating multiple external governance/compliance frameworks.
- **Suggested NDF Target Area:** Governance documentation / ADR-preparation guidance.
- **Core or Optional:** Optional guidance pattern.
- **Potential Files:** governance / ADR-preparation guidance doc.
- **Skill Impact:** Possibly `ndf-adr-governance-review` advisory guidance.
- **Template Impact:** Optional framework-candidate → tailoring-decision checklist.
- **Breaking-Change Potential:** Low.
- **Migration/Adoption Impact:** None.
- **Suggested Adoption Work Package:** WP C (Governance Status Modeling Patterns).
- **Dependencies:** None.
- **Notes:** Distinct from the NDF-to-project project adapter; this concerns external-framework adoption governance.

---

## 6. Bundle Assessment

### Bundle 1 – Work-Package Safety and Source Handling (001, 003, 004)

All three are `new` or `partially-covered` clarifications of work-package prompt safety. They cohere as a single additive update to prompt blocks/standards: an explicit read-only-git allowlist (001), a source-preflight verification procedure (003), and a blocked-report-without-commit format (004). Low breaking-change risk. Recommend a single adoption work package (WP A).

### Bundle 2 – Skills Availability and Context Economy (002)

The availability + selective-activation half is `already-covered` by `SKILLS_FIRST_OPERATING_MODE.md`, `NDF_CONTEXT_ECONOMY.md`, and `NDF_SKILL_SECURITY_POLICY.md`/ADR-0032. Only the **provenance + hash-lock** component is novel and worth adopting, as security-supply-chain guidance in the ADR-0032 / skill-supply-chain-reviewer environment (WP B). Recommend `merge-with-existing-work` with a focused provenance/lock addition.

### Bundle 3 – Governance and Status Modeling (005, 006, 007)

Three governance/status patterns with no direct NDF equivalent: a direction-vs-technical status family (005), an optional multi-dimensional capability status model (006), and an external-framework candidate→tailoring pattern (007). All should be **optional guidance/template**, not core-mandatory. For 006 specifically: keep the existing single-status capability matrix valid and add the multi-dimensional model as an optional variant. Recommend a single governance-patterns adoption work package (WP C).

## 7. Duplicate Findings

No candidate is an exact duplicate of an existing NDF rule. The closest overlap is candidate 006 with the existing single-status `CAPABILITY_MATRIX_SPEC.md`; this is treated as an additive/optional extension, not a duplicate. Candidate 002's availability/selective-activation half overlaps existing skills-first/context-economy work and is handled via `merge-with-existing-work` rather than as a duplicate.

## 8. Recommended Adoption Work Packages (no numeric IDs assigned)

### WP A – Work-Package Prompt Safety Baseline Update
- **Type:** docs-only / standards-update
- **Scope:** Add an explicit read-only-git allowlist, a source-preflight verification procedure, and a blocked-report-without-commit format to the reusable prompt blocks/standards.
- **Included candidates:** 001, 003, 004.
- **Target areas:** `framework/prompts/blocks/BLOCK_LIMITS.md`, `framework/prompts/blocks/BLOCK_FEEDBACK_TO_NOVA.md`, `framework/standards/WORK_PACKAGE_LIFECYCLE.md`, `framework/standards/git-standard.md`.
- **Dependencies:** None.
- **Priority:** High.

### WP B – Skill Provenance and Integrity Lock Guidance
- **Type:** docs-only / security-governance
- **Scope:** Add a provenance + per-file hash-lock reference pattern for locally imported skill packs; mark the availability/selective-activation part as already covered.
- **Included candidates:** 002 (provenance/lock component only).
- **Target areas:** `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (reference), `ndf-skill-supply-chain-risk-reviewer` skill docs.
- **Dependencies:** ADR-0032.
- **Priority:** Medium.

### WP C – Governance Status Modeling Patterns
- **Type:** docs-only / governance
- **Scope:** Add optional patterns — a direction-vs-technical decision status family, an optional multi-dimensional capability status model, and an external-framework candidate→tailoring pattern.
- **Included candidates:** 005, 006, 007.
- **Target areas:** decision-index/governance guidance, `docs/project-system/CAPABILITY_MATRIX_SPEC.md` (optional variant), ADR-preparation guidance.
- **Dependencies:** None (ADR-0031/0032 unaffected).
- **Priority:** Medium.

## 9. Deferred, Duplicate or Rejected Candidates

None deferred, duplicated, or rejected. All seven candidates are recommended for later adoption in some form (adopt-with-changes, merge-with-existing-work, or guidance-only). Candidate 002's availability half is folded into existing work rather than rejected.

## 10. Validation

- NDF preflight verified read-only; HEAD `eeb2124`; working tree clean at preflight.
- CoreOps source blocker verified resolved (approved package status + seven approved human-maintainer gates; no candidate transferred/adopted).
- Each `already-covered`/`partially-covered` classification cites concrete NDF file evidence.
- Each `new`/`partially-covered` classification states a concrete gap.
- No numeric NDF work-package IDs invented.
- No candidate adopted; no CoreOps status set to `transferred-to-ndf`.
- Only the two Allowed Files created; no NDF rule, skill, or template modified.

## 11. Skills-first Usage

This intake review followed skills-first discipline conceptually (targeted context loading per Context Economy layers; read-only evidence only). No skill was executed or modified. The `ndf-skill-supply-chain-risk-reviewer` and `ndf-adr-governance-review` skills were identified as relevant future targets but not invoked.

## 12. Explicit Confirmations

- No NDF rule changed.
- No skill changed.
- No template changed.
- No candidate adopted.
- No adoption work package implemented.
- No CoreOps file changed.
- No network access.
- No Git write, commit, push, tag, or release.
- Only the two Allowed Files created.

## 13. Next Step

Nova review of this completed intake review, followed by a human-maintainer decision on the recommended adoption work packages (WP A, WP B, WP C). No adoption begins before that decision.
