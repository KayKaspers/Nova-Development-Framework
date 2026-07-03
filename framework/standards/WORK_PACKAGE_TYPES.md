# NDF Standard – Work Package Types

## Status

Required.

## Core Rule

```text
No Work Package without a declared type.
```

## Primary Types

| Type | Purpose | Code Allowed | Test Expected |
|---|---|---:|---:|
| `review-only` | inspect and report | no | no |
| `docs-only` | documentation update | no | optional |
| `code-fix` | targeted code correction | yes | yes |
| `feature` | small feature addition | yes | yes |
| `test-only` | add or adjust tests | test code only | yes |
| `security-baseline` | security review and findings | no by default | no |
| `security-code-fix` | mitigate one security finding | yes | yes |
| `health-score-update` | update project score after evidence | no | no |
| `ci-diagnostic` | diagnose CI/local build failure | maybe | case-by-case |
| `release-prep` | release documentation/checklist | no by default | no |
| `destructive-blueprint` | plan high-risk destructive action | no | no |
| `destructive-implementation` | implement approved destructive action | yes | yes |
| `project-adapter` | adapt NDF to a project | docs/config | optional |

## Type Rules

### review-only

Allowed: reading files, writing review documents, listing findings, recommending work packages.  
Forbidden: code changes, config changes, CI changes.

### docs-only

Allowed: documentation files, changelog entries, project-brain updates.  
Forbidden: functional code changes or hidden behavior changes.

### code-fix

Allowed: minimal scoped code changes, focused tests, small docs note if necessary.  
Required: test or documented reason why no test exists.  
Forbidden: unrelated refactor or Health Score update in the same commit by default.

### security-baseline

Allowed: security review document, risk list, recommendations.  
Forbidden: code fixes unless explicitly converted into a security-code-fix work package.

### security-code-fix

Allowed: one approved mitigation, focused tests, minimal risk/project-brain update.  
Required: no secret leakage, security-specific Rückmeldung, test evidence.

### health-score-update

Allowed: Health Score file and optional project-brain note.  
Required: previous score, new score, deltas, evidence, remaining risks.  
Forbidden: code changes.

### ci-diagnostic

Allowed: investigation, small fix if root cause is proven, documentation of environment issue.  
Forbidden: broad refactor and speculative changes.

### destructive-blueprint

Allowed: blueprint, risk analysis, ADR draft, test plan.  
Forbidden: implementation.

### destructive-implementation

Allowed only after approved blueprint.  
Required: strict validation, read-only preview, authorization, confirmation flow, rate limit, audit privacy, tests and ADR/decision record.

## Prompt Rule

Every prompt must state:

```text
Work Package Type:
Allowed Files:
Forbidden Files:
Tests Required:
Rückmeldung an Nova:
```

## Commit Rule

One commit should represent one coherent Work Package.
