# ADR-0027: Real Project Validation with the reference projects

## Status

Accepted

## Context

NDF Foundation 0.2 needs validation through real projects.

The reference projects provide complementary validation cases:

- Reference Project A for destructive actions, owner-only flows, backups, audit privacy and agent endpoint security.
- Reference Project B for Docker, CI, docs tooling, security baseline, Health Score and focused technical hardening.

## Decision

NDF will use the reference projects as initial real-project validation references.

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
