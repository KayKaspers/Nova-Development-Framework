# ADR-0028: Work Package Type Standard Integration

## Status

Accepted

## Context

NDF Foundation 0.2 uses real project validation from the reference projects.

Both projects showed that work must be separated by type.

Examples:

- Reference Project B: security review, code mitigation and Health Score update worked best as separate steps.
- Reference Project A: destructive actions require blueprint before implementation.

## Decision

NDF will require all Work Packages and Claude prompts to declare a primary Work Package type.

The type controls:

- allowed changes
- forbidden changes
- review depth
- test expectations
- commit strategy
- safety gates

## Consequences

NDF becomes stricter but safer.

Claude prompts become clearer.

Kay can review changes more easily.

Nova can decide follow-up steps more reliably.

## Risks

Some users may feel the process is heavier.

## Mitigation

NDF should provide lightweight templates and quick reference tables.
