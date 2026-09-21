# FIX_PROMPT Template

> Purpose: one targeted correction (Fix profile, B0–B1) that does not widen scope.
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
Prompt profile: Fix (B0–B1)   # must not widen scope

Symptom:
Ziel (Soll-Zustand):
Betroffene Datei(en):
Zu wahrende Invariante:
Non-Goals (kein Scope-Ausbau):
Rückmeldeformat: Short Report + Compact Context Summary
```

## Notes

- Fix stays within the named files and the single symptom. A larger root cause or refactor → escalate to a normal WP (Standard/Full), do not expand the Fix.
- If the fix touches release, ADR, security, migration, privacy, or v1.x-compatibility → escalate the budget (fail-closed).
- No secrets, no private data, no private project names or domains.
