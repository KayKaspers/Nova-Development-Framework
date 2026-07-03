# ADR-0027: Real Project Validation with SpeakCore and CastCore

## Status

Accepted

## Context

NDF Foundation 0.2 needs validation through real projects.

SpeakCore and CastCore provide complementary validation cases:

- SpeakCore for destructive actions, owner-only flows, backups, audit privacy and agent endpoint security.
- CastCore for Docker, CI, docs tooling, security baseline, Health Score and focused technical hardening.

## Decision

NDF will use SpeakCore and CastCore as initial real-project validation references.

## Consequences

NDF gains standards for:

- Work Package Types
- Destructive Actions
- Owner-only Actions
- Backup Delete
- Audit Privacy
- Agent Endpoint Security
- Health Score Updates
- Local Testing
- CI Risk Handling

## Risks

Project-specific patterns may be overgeneralized.

## Mitigation

Use NDF levels/profiles. Apply heavy controls only when risk type requires them.
