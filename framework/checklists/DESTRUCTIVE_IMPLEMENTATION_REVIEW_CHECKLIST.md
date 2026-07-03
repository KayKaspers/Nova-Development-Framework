# Checklist – Destructive Implementation Review

## DE – Zweck

Diese Checkliste prüft vor dem Commit, ob eine destruktive Implementierung dem freigegebenen Blueprint entspricht: Scope, serverseitige Autorisierung, Bestätigungen, Audit-Privacy und Tests. Entscheidung: GO / GO WITH NOTES / REWORK / STOP.

## EN – Purpose

This checklist verifies before commit that a destructive implementation matches the approved blueprint: scope, server-side authorization, confirmations, audit privacy and tests. Decision: GO / GO WITH NOTES / REWORK / STOP.

## Before Commit

- [ ] Approved destructive blueprint exists
- [ ] Implementation matches blueprint
- [ ] No broadened scope
- [ ] No unrelated refactor
- [ ] No raw host path input
- [ ] No wildcard delete
- [ ] No shell execution with user input
- [ ] All target paths/resources are strictly validated

## Authorization

- [ ] Server-side role check exists
- [ ] Owner-only enforced if required
- [ ] Non-owner test exists
- [ ] Auth bypass not possible through direct API call

## Confirmation

- [ ] UI requires required confirmations
- [ ] Backend validates typed confirmation if applicable
- [ ] Wrong confirmation fails safely
- [ ] Confirmation text is exact

## Audit

- [ ] Audit event exists
- [ ] Audit does not leak secrets
- [ ] Audit does not leak sensitive host paths
- [ ] Audit does not include raw tokens
- [ ] Failure events are audited or intentionally documented

## Tests

- [ ] Focused tests run
- [ ] Negative tests included
- [ ] Audit privacy tested
- [ ] Rate limit tested or documented
- [ ] CI expected to run

## Decision

```text
GO | GO WITH NOTES | REWORK | STOP
```
