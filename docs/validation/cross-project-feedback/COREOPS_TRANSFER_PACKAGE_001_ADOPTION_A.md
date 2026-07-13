# CoreOps Transfer Package 001 – Adoption A

> Work Package: `NDF-ADOPT-COREOPS-001A` — Work-Package Prompt Safety Baseline Update
> Type: docs-only / standards-adoption

## 1. Status

```text
Adoption Status: Implemented, pending Nova review
Candidates: 001, 003, 004
NDF Version: not yet assigned
Human-Maintainer Commit: pending
CoreOps Backlink: pending
```

## 2. Source Intake

Adoption is based on the completed intake review `NDF-INTAKE-COREOPS-001` (intake commit `d08e35e`) and its two intake artifacts under `docs/validation/cross-project-feedback/` and `project-brain/`. The source is an external, independent project (Transfer Package 001, approved for NDF intake); no source content is transferred — only the generalized safety patterns of the three adopted candidates. No private paths or project-internal details are copied into public NDF rules.

## 3. Adopted Candidates

- **NDF-FC-COREOPS-001** – Git Read versus Git Write in work-package prompts (`partially-covered` → `adopt-with-changes`).
- **NDF-FC-COREOPS-003** – Source-Handoff for chat/external documents (`new` → `adopt-with-changes`).
- **NDF-FC-COREOPS-004** – Blocked Report without artificial intermediate commit (`partially-covered` → `adopt-with-changes`).

Not addressed here (deferred to later adoption WPs): 002 (Adoption B), 005/006/007 (Adoption C).

## 4. Scope

Additive, backward-compatible NDF safety clarifications in four reusable/normative documents plus this adoption evidence and a project-brain note. No new NDF version, no release, no skill/template change, no CoreOps change.

## 5. Existing NDF Coverage

- **001:** `BLOCK_LIMITS.md` already forbade write operations (`Kein Commit/Push/Reset/Rebase/Force Push`); read-only git was permitted only implicitly in `NDF_CONTEXT_ECONOMY.md` (Layer 4) and the skills-first self-check — no explicit read-only allowlist inside the imported prompt block.
- **003:** registration/analysis flows exist, but no explicit source-verification preflight before claiming a complete registration.
- **004:** `WORK_PACKAGE_LIFECYCLE.md` covered the `STOP` outcome and human-controlled commit; `BLOCK_FEEDBACK_TO_NOVA.md` assumed changes were made — no structured no-change blocked-report format.

## 6. Adopted Changes

- `framework/prompts/blocks/BLOCK_LIMITS.md`: added a Git Read vs Git Write section — read-only allowlist pattern, "no write from read" rule, network boundary, human-maintainer-only, and a prompt rule for separating allowed/forbidden git commands.
- `standards/git-standard.md`: added a Git read/write taxonomy, safe read-only examples, state-changing/network-mutating operations, human-maintainer control, and a note on the WP-specific allowlist.
- `framework/standards/WORK_PACKAGE_LIFECYCLE.md`: added a source-handoff preflight, a fail-closed transition to `blocked`, a structured blocked report, a no-change rule, a no-artificial-commit rule, a human-maintainer gate, and a resume/new-WP step.
- `framework/prompts/blocks/BLOCK_FEEDBACK_TO_NOVA.md`: added a status field and optional token/limit, skills-first, deviations, explicit-confirmations and Compact Context Summary fields, plus an optional structured Blocked/No-Change section (only when blocked).

## 7. Git Read/Write Model

Read-only git (status/diff/log/show/rev-parse/branch --show-current/remote get-url/tag --points-at HEAD) may be allowed for preflight/evidence/review; write/state-changing/network-mutating operations (add/commit/push/pull/fetch/checkout/switch/reset/clean/tag create-delete/merge/rebase/stash/config/submodule/lfs) require explicit WP authorization and stay human-maintainer-controlled. Read-only implies no network; write is never derived from read. A WP prompt states allowed read-only commands, forbidden write commands, the network boundary, and human-maintainer-only operations separately.

## 8. Source-Handoff Model

Before any change, WPs relying on chat/uploaded/external/other-repo/exported/handed-over sources run a preflight (availability, identity, expected artifact, completeness, truncation risk, version/provenance when relevant, scope-section readability). Missing/ambiguous/partial/truncated/mismatched/unreadable sources cause a fail-closed stop — no file change, no invented content, no memory-as-source, status `blocked` with the exact missing source and unblock condition. A present source is not an automatic trust grant (deeper provenance/hash/neutrality/security/license checks belong to their designated WP).

## 9. Blocked/No-Change Model

A fail-closed stop before any change is a complete, review-ready result with a structured blocked report (WP ID, status blocked, blocker, preflight results, reason, files changed none, git write no, tests run/not-run, exact unblock condition, next step, Compact Context Summary). A blocked WP with no changes needs no artificial intermediate commit; the agent creates no empty file, performs no unauthorized status mutation, demands no artificial commit, and does not report the blocker as completed. The human maintainer may make a separate commit only for actually authorized changes, with the intended status already correct in the documents before staging.

## 10. Files Changed

- `framework/prompts/blocks/BLOCK_LIMITS.md` (additive: Git read/write section)
- `standards/git-standard.md` (additive: git read/write taxonomy, human-maintainer control)
- `framework/standards/WORK_PACKAGE_LIFECYCLE.md` (additive: source-handoff, fail-closed, blocked report, no-change/no-artificial-commit, resume)
- `framework/prompts/blocks/BLOCK_FEEDBACK_TO_NOVA.md` (additive: status/optional fields, blocked/no-change section)
- `docs/validation/cross-project-feedback/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_A.md` (new, this document)
- `project-brain/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_A_NOTES.md` (new)

## 11. Compatibility Assessment

Additive and backward-compatible. Existing forbidden write operations remain forbidden; prompt blocks remain compact and reusable; no git-write operation is implicitly allowed; no read-only git enables network access; no human-maintainer control is reduced; old work packages remain valid; no new NDF version is claimed. Breaking-change potential: **low** (as expected in the source intake).

## 12. Security Assessment

Security-positive. The read-only allowlist prevents accidental write authorization; the source-handoff preflight adds a fail-closed gate against incomplete/spoofed sources; the blocked/no-change rule prevents artificial mutations. ADR-0032 (skill security) and ADR-0031 (v1.x compatibility) are unaffected and unchanged. No secrets, no private data, no network, no autonomous git/release actions.

## 13. Validation

See the WP test matrix (preflight, candidate 001/003/004, cross-document consistency, scope, public neutrality, formatting). All adopted changes are additive; only the six Allowed Files were changed; no forbidden file, skill, template, or CoreOps file was touched; no network; no git write.

## 14. Remaining Candidates

- **002** – Skill Provenance and Integrity Lock Guidance → Adoption B (not started).
- **005 / 006 / 007** – Governance Status Modeling Patterns → Adoption C (not started).

## 15. Lessons Learned

```text
Lessons Learned:
- An explicit read-only-git allowlist inside the imported prompt block closes the read/write ambiguity that a limits-only prompt otherwise leaves open.
- A source-handoff preflight makes "complete registration" claims verifiable and fail-closed.
- A structured no-change blocked report removes the incentive for artificial intermediate commits.
NDF Feedback Candidates: none newly created here.
Project-local Follow-ups: none (project-local details stay in the source project).
```

## 16. Next Decision

Nova review of `NDF-ADOPT-COREOPS-001A`; then a human-maintainer decision and a separate maintainer commit; only afterwards NDF Adoption B. The NDF version for this adoption is not yet assigned; the CoreOps backlink stays pending until the maintainer commit.
