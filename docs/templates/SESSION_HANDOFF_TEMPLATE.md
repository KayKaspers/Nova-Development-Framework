# SESSION_HANDOFF Template

> Purpose: resume an interrupted session without the whole old chat. Builds on the Compact Context Summary and adds *Do not reload* and *Forbidden work*.
> Part of the [Token Efficiency & Context Budget Baseline](../guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md) (NDF-WP-152). Additive, docs-only. Handoff is not an implementation mode.

```text
Keep this file short.
Do not duplicate completed history.
Reference stable NDF rules instead of repeating them.
Escalate context budget when scope, safety, release, ADR, privacy or compatibility risk increases.
```

## Template

```text
Project:
NDF version:
Branch / revision:
Active WP:
Scope:
Completed:
Open:
Decisions:
Blockers:
Relevant files:
Do not reload:
Next action:
Recommended prompt profile:
Forbidden work:
Compact Context Summary:
```

## Handoff types

- Implementation continuation
- Review
- Fix
- Human-maintainer decision
- Nova handoff

## Notes

- One screen maximum (~30 lines). It replaces chat history, not the safety/gate/human-review checks.
- `Recommended prompt profile`: Lean / Handoff / Review-only / Fix / Standard / Full — escalate on any fail-closed trigger.
- No secrets, no private data, no private project names or domains.
