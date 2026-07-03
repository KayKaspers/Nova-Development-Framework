# Checklist – Destructive Action Blueprint

## DE – Zweck

Diese Checkliste prüft, ob ein Blueprint für eine destruktive Aktion vollständig ist: Scope, Autorisierung, Bestätigungen, Ausführungsschutz, Audit, Tests und Doku — ohne jede Implementierung.

## EN – Purpose

This checklist verifies that a destructive action blueprint is complete: scope, authorization, confirmations, execution guard, audit, tests and docs — without any implementation.

## Classification

- [ ] Work Package Type is `destructive-blueprint`
- [ ] No implementation is included
- [ ] Resource type is clearly named
- [ ] Irreversibility is stated
- [ ] Risk level is defined

## Scope

- [ ] Allowed resource scope is defined
- [ ] Forbidden targets are defined
- [ ] Managed-resource rule is defined
- [ ] No arbitrary host paths are accepted
- [ ] No wildcard operation is allowed
- [ ] Companion resources are derived deterministically

## Authorization

- [ ] Required role is defined
- [ ] Owner-only requirement checked
- [ ] Server-side authorization required
- [ ] UI-only authorization rejected

## UX / Confirmation

- [ ] Read-only preview required
- [ ] Warning text defined
- [ ] Multiple confirmations defined
- [ ] Typed confirmation defined
- [ ] Submit disabled until requirements met

## Execution Guard

- [ ] Strict request schema
- [ ] Canonical target validation
- [ ] Rate limit defined
- [ ] Dry-run/read-only phase if possible
- [ ] Safe failure behavior

## Audit

- [ ] Audit event required
- [ ] Sensitive audit fields forbidden
- [ ] Success and failure audited
- [ ] Correlation/request ID considered

## Tests

- [ ] Valid target
- [ ] Invalid target
- [ ] Path traversal attempt
- [ ] Unauthorized actor
- [ ] Wrong confirmation
- [ ] Rate limit
- [ ] Audit privacy
- [ ] Companion-resource derivation

## Documentation

- [ ] ADR required
- [ ] Risk register update required
- [ ] User/operator docs required
