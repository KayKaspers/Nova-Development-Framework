# LEAN_WP_PROMPT Template

> Purpose: a compact work-package prompt (Lean profile, B1) that references stable NDF rules instead of repeating them.
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
Prompt profile: Lean (B1)   # escalate on any fail-closed trigger

1. Ziel:
2. Scope:
3. Relevante Quellen:
4. Verbindliche Invarianten (nur WP-spezifisch):
5. Konkrete Aufgabe:
6. Abnahmekriterien:
7. Non-Goals:
8. Rückmeldeformat: Short Report + Compact Context Summary (Referenz)

Referenzierte Standardregeln (nicht wiederholen):
  Rollenmodell · Git-Grenzen · Secret-Grenzen · Public-Neutrality · Self-Check · Skills-first
Sichtbar bleiben:
  WP-ID · Ziel · Scope · Allowed/Forbidden Files · WP-Sonderregeln · Fail-Closed-Trigger · Human-Maintainer-Gate · erwartete Commit-Message
```

## Notes

- Use Lean only when no elevated complexity or criticality applies. For release, ADR, security policy, v1.x-compatibility, breaking-change, migration, privacy/permission, unclear scope, contradictory sources → escalate to Standard/Full.
- Select only the skills required (B1: 1–3). Do not force all 38 skills.
- No secrets, no private data, no private project names or domains.
