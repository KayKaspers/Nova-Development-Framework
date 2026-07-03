# ADR-0030: Security Prompt Library Expansion

## Status

Accepted

## Context

SpeakCore and CastCore validated that security work needs stronger prompt boundaries.

Security review, mitigation and scoring must not be mixed casually.

## Decision

NDF will include a dedicated Security Prompt Library.

The library covers:

- Security Baseline Review
- Finding Triage
- Focused Security Code Fix
- Secret Handling
- Fail-closed Config
- CSP Baseline
- Container Hardening
- Agent Endpoint Security
- Audit Privacy
- Threat Modeling
- Security Health Score
- Release Gate

## Consequences

Security work becomes more structured and safer.

Prompts become longer, but less ambiguous.

## Risks

Overhead for small projects.

## Mitigation

Use the prompts selectively based on project risk and NDF level.
