# CoreOps Transfer Package 001 – Adoption B

> Work Package: `NDF-ADOPT-COREOPS-001B` — Skill Provenance and Integrity Lock Guidance
> Type: docs-only / security-governance adoption

## 1. Status

```text
Adoption Status: Implemented, pending Nova review
Candidate: NDF-FC-COREOPS-002
NDF Version: not yet assigned
Tooling: not implemented
Human-Maintainer Commit: pending
CoreOps Backlink: pending
```

## 2. Source Intake

Based on the completed intake review `NDF-INTAKE-COREOPS-001` (intake commit `d08e35e`) and its two intake artifacts. Adoption A (`1ebffa6`) is committed and untouched here. Only the generalized provenance/integrity-lock governance is adopted; no source content, no private paths, no project-internal details are copied into NDF governance.

## 3. Candidate

`NDF-FC-COREOPS-002` — Full local skills availability with selective activation, provenance and integrity lock (`partially-covered` → `merge-with-existing-work`).

## 4. Existing Coverage

- **Skills-first / selective activation:** already covered by `SKILLS_FIRST_OPERATING_MODE.md` (mandatory referencing + Full/Standard/Short selection = full availability with selective use).
- **Context economy / selective loading:** already covered by `NDF_CONTEXT_ECONOMY.md`.
- **Skill safety:** governed by `NDF_SKILL_SECURITY_POLICY.md` / ADR-0032 (fail-closed, docs-only, no third-party import); `ndf-skill-supply-chain-risk-reviewer` exists.

## 5. Adopted Gap

NDF had **no** skill **provenance + hash-lock** mechanism — no byte-identical import record and no per-file digest lock artifact for a locally provided skills pack. A read-only scan of `docs/agent-workflows/` confirmed no existing provenance/integrity-lock content. Adoption B adds this governance only (no availability/selective-activation duplication).

## 6. Provenance Model

Per skill: name, source framework/repository, source version/tag, source commit when available, import date/phase, original relative path, local relative path, expected integrity value, verification method, Human-Maintainer approval state. Relative repository paths only — no absolute local paths, no user names, no OS-specific roots.

## 7. Integrity Lock Model

A technology-independent reference record with: schema version, framework identifier, framework release/commit, generated/approved date, skill count, per-file relative path, per-file cryptographic digest, digest algorithm, source reference, approval state, notes. It detects missing, unexpected, modified skills, diverging paths, wrong framework version, and outdated/unverifiable provenance. It is a description — not an executed check.

**Integrity Payload vs Governance Metadata (Nova review note):** the lock separates an integrity payload (schema version, framework identifier, source version/commit, digest algorithm, expected file count, normalized relative paths, per-file digest, deterministic ordering, canonical encoding) from mutable governance metadata (import/generated/approval dates, approval state, reviewer role, migration state, exception state, notes). Per-file digests are computed from the relevant skill-file bytes or explicitly defined canonical content; mutable governance metadata must not influence the expected per-file digests; a future whole-lock digest/signature must explicitly define its canonical payload and every excluded mutable field; changing approval metadata must not silently change the expected content digests.

## 7a. Migration of Existing Projects (Nova review note)

Projects adopted before this governance became effective are not automatically compromised/non-compliant solely because no historical lock exists; they use an explicit migration state (`migration-pending / legacy-unlocked / migration-exception-active / lock-enforced`). A `verified` lock is mandatory before importing/updating/replacing skills, refreshing the pack, declaring enforcement active, or using newly changed skills for normative/security-sensitive work. Temporary exceptions require documented scope/risk, Human-Maintainer approval, a review/expiry condition, and a migration follow-up. Missing historical lock evidence is not proof of manipulation; legacy projects are not silently treated as `verified`; exceptions do not become permanent implicit approvals.

## 8. Verification Statuses

`verified · modified · missing · unexpected · source-mismatch · version-mismatch · unverifiable · not-checked`. A skill may be used for normative/security-sensitive decisions only at status `verified`; exceptions need a documented rationale + Human-Maintainer approval + risk/scope limitation.

## 9. Fail-closed Boundary

Unknown, modified, or provenance-unverified skills fail closed for normative/security-sensitive use. **Local availability is not trust.** Digest baseline SHA-256; deterministic ordering; normalized relative paths; same inputs → same integrity values. No custom cryptography; no prescribed language/toolchain.

## 10. Human-Maintainer Control

The Human Maintainer controls skill import, update, replacement, and lock refresh. No silent overwrite; no automatic lock refresh without review; no accepting changed hashes merely because a file is present; no mixing skill updates with unrelated work packages. Each update is its own traceable commit under Human-Maintainer approval.

## 11. Files Changed

- `docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md` (new — governance, 20 sections)
- `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (additive — reference to the provenance/lock governance; no duplication)
- `docs/validation/cross-project-feedback/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_B.md` (new — this document)
- `project-brain/COREOPS_TRANSFER_PACKAGE_001_ADOPTION_B_NOTES.md` (new)

## 12. Compatibility Assessment

Additive and backward-compatible. Skills-first and Context Economy unchanged; existing projects not retroactively faulty; missing historical locks are a migration topic; no automatic skill execution; no prescribed language/toolchain; no new NDF version. ADR-0031/0032 unaffected and unchanged. Breaking-change potential: **low to medium** (new optional governance; no change to existing mandatory behavior).

## 13. Security Assessment

Security-positive. Provenance + integrity lock make silent skill manipulation detectable; fail-closed prevents trusting unverified skills; the Human-Maintainer update gate prevents silent overwrite/auto-refresh. No secrets, no private data, no network, no autonomous git/release actions, no third-party import.

## 14. Tooling Boundary

**Governance only.** No lock generator, no manifest file, no verification tool is implemented or executed. Any tooling stays out of scope and behind a future explicit ADR/scope decision (scripts remain forbidden under ADR-0032). No hash tool was run; no lock/manifest was generated.

**Manual verification path (Nova review note):** the status `verified` may initially be established through a documented manual verification process whose evidence identifies the verified source, expected version/commit, reviewed relative paths, compared integrity values, verification method, result, Human-Maintainer approval, and verification date/phase. This adoption defines the governance requirement and the manual evidence process only. Automated verification, automated enforcement, a lock generator, and a validator are **not implemented and not claimed** (`Tooling: not implemented`). The four layers are distinct: governance requirement · manual evidence process · future tooling support · automated enforcement — only the first two are covered here.

## 15. Validation

See the WP test matrix (preflight, existing coverage, provenance model, integrity lock, security, scope, public neutrality, formatting). All changes additive; only the four Allowed Files changed; no forbidden file, skill, template, lock/manifest, or CoreOps file touched; no network; no git write. Public Quality Gate not run (script execution not permitted by this WP).

## 16. Remaining Candidates

- **001 / 003 / 004** — adopted in Adoption A (`1ebffa6`), not modified here.
- **005 / 006 / 007** — Governance Status Modeling Patterns → Adoption C (not started).

## 17. Lessons Learned

```text
Lessons Learned:
- Availability/selective-activation was already covered; only provenance + integrity-lock was a real gap — adopting only the gap avoids a parallel skills system.
- A technology-independent lock model (fields + SHA-256 baseline + deterministic serialization) keeps the governance implementation-agnostic and CI-agnostic.
- Fail-closed on unverified/modified skills makes "locally available" explicitly not equal to "trusted".
NDF Feedback Candidates: none newly created here.
Project-local Follow-ups: none (project-local details stay in the source project).
```

## 18. Next Decision

Nova review of `NDF-ADOPT-COREOPS-001B`; then a Human-Maintainer decision and a separate maintainer commit; only afterwards NDF Adoption C. The NDF version for this adoption is not yet assigned; tooling is not implemented; the CoreOps backlink stays pending until the maintainer commit.
