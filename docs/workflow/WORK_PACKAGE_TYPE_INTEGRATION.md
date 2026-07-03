# Work Package Type Integration

## Purpose

NDF requires every planned work package to declare its type before execution.

This rule was validated through the reference projects.

## Core Rule

```text
Every Work Package must have exactly one primary type.
```

Optional secondary tags may be added, but the primary type decides:

- allowed file changes
- test expectations
- review depth
- commit strategy
- risk handling
- whether Nova approval is required before implementation

## Validated Sources

| Project | Lesson |
|---|---|
| Reference Project A | destructive actions require blueprint, owner-only controls and safety gates |
| Reference Project B | review, code fix, test and Health Score update should be separate steps |

## Required Flow

```text
Classify -> Plan -> Execute -> Rückmeldung an Nova -> Review -> Commit/Push
```

## Work Package Metadata

```yaml
id: "RP-WP-007"
title: "Fail-closed Secret Validation"
type: "security-code-fix"
tags: ["backend", "config", "fail-closed"]
risk: "security"
scope: "backend config validation"
requires_nova_approval: true
requires_tests: true
commit_strategy: "single scoped commit"
```

## Prompt Requirement

Every Claude prompt must include:

```text
Work Package Type: <type>
```

## Commit Requirement

A commit should normally contain only one Work Package type.

Forbidden combinations by default:

- code-fix + Health Score update
- security review + broad refactor
- destructive blueprint + destructive implementation
- CI diagnostic + unrelated cleanup
