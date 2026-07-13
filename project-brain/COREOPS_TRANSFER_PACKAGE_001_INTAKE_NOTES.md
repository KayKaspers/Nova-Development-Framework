# CoreOps Transfer Package 001 – Intake Notes

> Compact project-brain notes for `NDF-INTAKE-COREOPS-001`.
> NDF base: development HEAD `eeb2124` (normative `v1.0.0` = `9dcadc1`).
> Status: implemented – pending Nova review. No adoption performed.

## Summary

Reviewed seven CoreOps cross-project feedback candidates against the current NDF state. No candidate adopted; no NDF rule/skill/template changed; only the intake review doc and these notes created.

## Preflight

- NDF: HEAD `eeb2124`, branch `main`, working tree clean at preflight, `v1.0.0` one commit behind HEAD.
- CoreOps source blocker: **resolved** — transfer package `Approved for NDF Intake`; all seven `Human-Maintainer Gate: approved`; none `transferred-to-ndf`/`adopted-in-ndf`.

## Candidate outcomes (one line each)

| Candidate | Classification | Recommendation | Core NDF evidence / gap |
|---|---|---|---|
| 001 Git read vs write | partially-covered | adopt-with-changes | BLOCK_LIMITS forbids writes; no explicit read-only allowlist in the block (only in Context Economy L4). |
| 002 Skills availability + provenance/lock | partially-covered | merge-with-existing-work | Skills-first/context-economy already cover availability; **provenance/hash-lock absent**. |
| 003 Source handoff | new | adopt-with-changes | No source-preflight (identity/completeness/truncation) before "complete registration". |
| 004 Blocked report w/o commit | partially-covered | adopt-with-changes | STOP exists; no structured no-change blocked-report format. |
| 005 Accepted product direction | new | guidance-only | Decision records are technical; no direction-vs-technical status family. |
| 006 Multi-dimensional status | partially-covered | guidance-only | CAPABILITY_MATRIX_SPEC uses a single status field; no roadmap/impl/support split. |
| 007 Framework tailoring | new | guidance-only | Project adapter = NDF→project; no external-framework candidate→tailoring pattern. |

## Bundles

- **Bundle 1 (001/003/004):** cohere into one additive prompt-safety update → WP A (High).
- **Bundle 2 (002):** only provenance/lock is novel → WP B (Medium), rest merged into existing work.
- **Bundle 3 (005/006/007):** optional governance/status patterns → WP C (Medium); keep 006 optional, not core.

## Recommended adoption WPs (no numeric IDs)

- **WP A – Work-Package Prompt Safety Baseline Update** (001/003/004), docs-only, High.
- **WP B – Skill Provenance and Integrity Lock Guidance** (002), docs-only/security, depends on ADR-0032, Medium.
- **WP C – Governance Status Modeling Patterns** (005/006/007), docs-only/governance, Medium.

## Duplicates / deferrals

None rejected or deferred. Closest overlap: 006 vs single-status capability spec (treated as additive/optional, not duplicate).

## Boundaries honored

Read-only git only; no commit/push/tag/release; no network; no CoreOps files touched; no NDF rule/skill/template modified; only the two allowed files created.

## Next step

Nova review → human-maintainer decision on WP A/B/C. No adoption before that.
