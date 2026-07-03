# Agent Endpoint Security Pattern

## Grundsatz

Agent-Endpunkte sind privilegierte operative Endpunkte.

## Pflichtkontrollen

- Token-Gate
- Scope-Validierung
- Managed Resource only
- striktes Request Schema
- Rate Limit
- Audit
- keine Secret-Logs
- minimale Response
- Tests

## Verboten

- unauthenticated mutation
- raw command execution
- freie Host-Pfade
- wildcard delete
- broad `/exec`
- Response mit sensiblen Daten

## ADR

Mutierende Agent-Endpunkte brauchen ADR oder Decision Record.
