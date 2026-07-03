# Security Prompt Library

## Purpose

Security work in NDF must be scoped, reviewable and safe.

This library provides reusable prompt patterns for security-focused work.

## Core Rule

```text
Security review, security mitigation and security scoring are separate work packages.
```

## Prompt Categories

| Category | Work Package Type |
|---|---|
| Security Baseline Review | security-baseline |
| Finding Triage | review-only |
| Focused Security Code Fix | security-code-fix |
| Secret Handling Review | review-only |
| Fail-closed Config Fix | security-code-fix |
| CSP Baseline | security-code-fix or docs-only |
| Container Hardening | review-only or security-code-fix |
| Agent Endpoint Review | review-only |
| Audit Privacy Review | review-only |
| Threat Modeling | review-only |
| Security Health Score Review | health-score-update |
| Security Release Gate | review-only |

## Lessons from Real Projects

### Reference Project A

Validated:

- destructive actions need blueprint-before-implementation
- Owner-only flows require server-side enforcement
- audit must prove without leaking
- agent endpoints require token gates and strict scope

### Reference Project B

Validated:

- security review does not automatically improve Health Score
- finding -> code fix -> test -> score update is the correct sequence
- fail-closed config is a real posture improvement
- local tests and CI evidence matter

## Recommended Sequence

For a new security issue:

```text
Security Baseline Review
-> Finding Triage
-> Focused Security Code Fix
-> Tests
-> Health Score Update
-> Release Gate
```

## Safety Rules

Security prompts must always define:

- allowed files
- forbidden files
- secret handling
- logging restrictions
- test expectation
- Rückmeldung an Nova
- no commit / no push
