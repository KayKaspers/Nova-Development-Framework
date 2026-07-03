# ADR-0029: Destructive Action Toolkit

## Status

Accepted

## Context

Reference Project A validated a safe pattern for destructive actions, especially managed backup deletion.

NDF needs a reusable toolkit so future projects do not re-invent dangerous delete flows inconsistently.

## Decision

NDF will include a destructive action toolkit with:

- blueprint checklist
- implementation review checklist
- owner-only checklist
- audit privacy checklist
- backup delete checklist
- agent endpoint destructive checklist
- templates
- prompts
- Academy lesson

## Consequences

Destructive features require more upfront structure.

This increases safety and reviewability.

## Risks

The process may feel heavy for small projects.

## Mitigation

Only apply the full toolkit when the action is destructive, irreversible or security-sensitive.
