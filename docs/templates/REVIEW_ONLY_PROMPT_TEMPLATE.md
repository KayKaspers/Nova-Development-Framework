# REVIEW_ONLY_PROMPT Template

> Purpose: a Nova/maintainer review prompt (Review-only profile, B1–B2) that works from an Evidence Pack and starts no new implementation.
> Part of the [Token Efficiency & Context Budget Baseline](../guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md) (NDF-WP-152). Additive, docs-only.

```text
Keep this file short.
Do not duplicate completed history.
Reference stable NDF rules instead of repeating them.
Escalate context budget when scope, safety, release, ADR, privacy or compatibility risk increases.
```

## Template

```text
WP-ID / Titel:
Prompt profile: Review-only (B1–B2)   # starts no new implementation

Review-Auftrag:
Abnahmekriterien:

## Evidence Pack
Relevant files:
Relevant diffs:
Checks run:
Acceptance criteria:
Known risks:
Open questions:

Erwartetes Review-Ergebnis: GO / GO WITH NOTES / REWORK / STOP / BLOCKED
```

## Notes

- Review-only never edits code or starts implementation; it evaluates the Evidence Pack against the acceptance criteria.
- If evidence is missing or contradictory → request it or escalate the budget; do not guess.
- Governance/release/security reviews stay Full where the fail-closed rules require it.
- No secrets, no private data, no private project names or domains.
