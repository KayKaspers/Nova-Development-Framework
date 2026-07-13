# NDF Skill Provenance and Integrity Lock

## 1. Status

```text
Document Status: Implemented, pending Nova review
Implementation Status: Governance only
Tooling Status: Not implemented
Normative Release: Not yet assigned
```

Adopted via `NDF-ADOPT-COREOPS-001B` (docs-only / security-governance) from cross-project feedback candidate `NDF-FC-COREOPS-002`. Governance definition only — **no lock generator, no manifest file, no tool is implemented or executed here.**

## 2. Purpose

Define a technology-independent NDF governance for **imported or locally provided skills**: make skill provenance traceable, bind skill contents to a defined framework version/source, make integrity deviations detectable, prevent silent skill modification, and keep skill import/update under Human-Maintainer control — without introducing any automatic skill execution or a parallel skills system.

## 3. Scope

Covers provenance, an integrity-lock reference model, verification statuses, fail-closed behavior for unverified skills, and update/refresh governance. **Out of scope:** the selective-activation and context-economy rules (already covered — see §4/§5); any executable tooling; any change to skill files, templates, ADRs, or CoreOps sources. This document adds governance only.

## 4. Relationship to Skills-first

The [Skills-first Operating Mode](../validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md) remains authoritative for skill selection, mandatory referencing, and Full/Standard/Short use. Full availability with selective activation is already covered there; this document does **not** duplicate it and adds only provenance/integrity-lock governance on top.

## 5. Relationship to Context Economy

The [Context Economy](NDF_CONTEXT_ECONOMY.md) remains authoritative for selective context/skill loading and token economy. Provenance/lock verification is a security concern and must never be traded away for token savings (consistent with the Skill Security Policy).

## 6. Skill Availability

A skill is **available** when it is locally present and can be read for a suitability check. Availability does **not** imply: automatically activated, automatically trusted, automatically executable, or required for every work package.

## 7. Skill Activation

A skill is **activated** for a concrete work package when it has been checked, read, and its process guidance applied. Activation is separate from technical execution (which stays separately controlled and, per ADR-0032, is not part of the docs-only skill model).

## 8. Skill Provenance

For each skill, provenance records at least:

```text
Skill name
Source framework or repository
Source version or tag
Source commit when available
Import date or import phase
Original relative path
Local relative path
Expected integrity value
Verification method
Human-Maintainer approval state
```

Provenance uses **relative repository paths** only — no absolute local paths, no user names, no OS-specific root paths.

## 9. Integrity Lock Model

A lock is a reference record (technology-independent) that allows a later verification to detect:

- missing skills,
- additional unexpected skills,
- modified skill contents,
- diverging file paths,
- a wrong framework version,
- outdated or unverifiable provenance.

The lock is a **description**, not an executed check; producing or verifying it is a separate, out-of-scope tooling concern under a future explicit decision.

## 10. Required Fields

The lock model contains at least:

```text
schema version
framework identifier
framework release or commit
generated or approved date
skill count
relative path per skill file
cryptographic digest per file
digest algorithm
source reference
approval state
notes
```

## 11. Path and Serialization Rules

- Relative, POSIX-style repository paths only.
- No absolute local paths, no private user names, no OS-specific root paths.
- Stable, deterministic ordering (e.g., sorted by normalized relative path).
- Normalized paths and a single, unambiguous text encoding.
- No timestamps inside the hashed payload where they would prevent reproducible lock results.

## 12. Digest Requirements

- Preferred minimum baseline: **SHA-256**.
- Do not invent custom cryptography.
- Do not prescribe a specific programming language, toolchain, or implementation.
- Same inputs must produce the same integrity values (determinism).

## 13. Verification Status

Defined statuses:

```text
verified
modified
missing
unexpected
source-mismatch
version-mismatch
unverifiable
not-checked
```

A work package may use a skill for **normative or security-sensitive** decisions only when its status is at least `verified`. Exceptions require a documented rationale, Human-Maintainer approval, and risk/scope limitation.

## 14. Fail-closed Behavior

Unknown, modified, or provenance-unverified skills **fail closed** for normative or security-sensitive use: they are not treated as trusted merely because they are locally available. Local availability is not trust. In doubt: forbid and escalate to the Human Maintainer (consistent with the Skill Security Policy's fail-closed principle).

## 15. Update and Lock Refresh

A skill update requires:

1. a documented source,
2. a comparison to the previous version,
3. a security and scope review,
4. new integrity values,
5. Human-Maintainer approval,
6. its own traceable commit,
7. a compatibility check of existing projects when relevant.

Not permitted: silent overwrite; automatic lock refresh without review; accepting changed hashes merely because a file is locally present; mixing skill updates with functionally unrelated work packages.

## 16. Human-Maintainer Gate

The Human Maintainer controls skill import, update, replacement, and lock refresh. No provenance/lock mechanism replaces a Human-Maintainer decision; it only makes deviations visible for that decision.

## 17. Exceptions

Any deviation from `verified`-only use for normative/security-sensitive decisions requires: a documented rationale, explicit Human-Maintainer approval, and an explicit risk/scope limitation. Exceptions are never implicit.

## 18. Compatibility

Additive and backward-compatible. Skills-first and Context Economy remain unchanged; existing projects are not retroactively declared faulty; missing historical locks are a migration topic, not a defect; no automatic skill execution is introduced; no specific language/toolchain is prescribed; no new NDF version is claimed. Breaking-change potential: low to medium (new optional governance, no change to existing mandatory behavior). ADR-0031/0032 remain unaffected and unchanged.

## 19. Integrity Payload and Governance Metadata

The lock record is split into an **integrity payload** (what per-file skill digests are computed over) and **governance metadata** (mutable review/approval data).

**Integrity Payload (at least):**

```text
schema version
framework identifier
source version or commit
digest algorithm
expected file count
normalized relative file paths
per-file digest
deterministic ordering
canonical encoding rules
```

**Governance Metadata (at least):**

```text
import date
generated date
approval date
approval state
reviewer role
migration state
exception state
notes
```

**Binding rules:**

- Per-file digests are calculated from the relevant skill-file bytes or from explicitly defined canonical skill content.
- Mutable governance metadata must **not** influence the expected per-file skill digests.
- If a whole-lock digest or signature is introduced later, its canonical payload and every excluded mutable metadata field must be explicitly defined.
- Changing approval metadata must **not** silently change the expected skill-content digests.

## 20. Migration of Existing Projects

Projects adopted before the provenance and integrity-lock governance became effective are **not** automatically considered compromised or non-compliant solely because no historical lock exists. They must be recorded using an explicit migration state such as:

```text
migration-pending
legacy-unlocked
migration-exception-active
lock-enforced
```

A `verified` lock becomes **mandatory before**:

- importing new skills,
- updating or replacing existing skills,
- refreshing the local skills pack,
- declaring lock enforcement active,
- or using newly changed skills for normative or security-sensitive work.

A temporary migration exception requires: documented scope, documented risk, Human-Maintainer approval, a review or expiry condition, and a defined migration follow-up.

**Additional limits:**

- Missing historical lock evidence is **not** proof of manipulation.
- Legacy projects must **not** be silently treated as `verified`.
- Migration exceptions must **not** become permanent implicit approvals.

## 21. Manual Verification and Tooling Boundary

The status `verified` may initially be established through a documented **manual verification process**. Manual verification evidence must identify:

```text
verified source
expected version or commit
reviewed relative paths
compared integrity values
verification method
result
Human-Maintainer approval
verification date or phase
```

This governance document defines **required behavior and evidence**. It does **not** claim that automated verification, automated enforcement, a lock generator, or a validator already exists.

Distinguish clearly:

```text
Governance requirement
Manual evidence process
Future tooling support
Automated enforcement
```

Only the governance requirement and the manual evidence process are covered by this adoption. Tooling support and automated enforcement remain **not implemented**.

## 22. Adoption Guidance

Projects importing a full local skills pack should record provenance per skill and, where integrity matters, maintain a lock per the model above. Verification (initially manual, see §21), lock generation, and refresh remain manual/Human-Maintainer-gated until a future explicit ADR/scope decision defines any tooling. Prefer referencing this governance over duplicating it.

## 23. Open Implementation Questions

- Which exact lock file location/format a project uses (out of scope here; tooling decision).
- Whether a future ADR narrowly permits a verification tool (currently forbidden as script per ADR-0032).
- How lock refresh integrates with CI (out of scope; Human-Maintainer-gated for now).
- Whether a shared reference template for the lock model is added later (optional, not created here).
