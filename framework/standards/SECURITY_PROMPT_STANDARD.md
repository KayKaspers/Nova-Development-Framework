# NDF Standard – Security Prompts

## Status

Required for security work.

## Purpose

Security prompts must reduce risk, not create uncontrolled changes.

## Core Rules

1. Security review and code mitigation are separate work package types.
2. Security score changes happen after evidence.
3. Prompts must forbid secret exposure.
4. Prompts must limit scope.
5. Tests are required for security-code-fix work unless impossible.
6. Claude must not commit or push.
7. Rückmeldung an Nova is mandatory.

## Required Fields

Every security prompt must include:

```text
Work Package Type:
Security Finding:
Risk Level:
Allowed Files:
Forbidden Files:
Secret Handling:
Logging Rules:
Tests Required:
Acceptance Criteria:
Rückmeldung an Nova:
```

## Forbidden by Default

- printing secrets
- copying real `.env` values
- adding test secrets that look real
- changing CI without explicit scope
- broad auth refactors
- unrelated formatting
- disabling security checks to make tests pass
- committing or pushing

## Security Work Package Separation

| Step | Type |
|---|---|
| baseline review | security-baseline |
| risk triage | review-only |
| mitigation | security-code-fix |
| test-only addition | test-only |
| score update | health-score-update |
| release gate | review-only |

## Health Score Rule

Do not raise Security score for review-only work.

Raise Security score only after verified mitigation or control improvement.
