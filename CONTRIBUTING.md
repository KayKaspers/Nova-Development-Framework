# Contributing to Nova Development Framework

## Purpose

This document describes how contributions to NDF should be made.

## Core Rule

NDF is human-led and AI-assisted.

AI may help create content, but contributors are responsible for reviewing, approving and committing changes.

## Workflow

1. Define the goal.
2. Check whether the change fits the NDF Blueprint.
3. Create or update documentation.
4. Add or update ADRs if the change is architectural.
5. Check affected standards or templates.
6. Review changes locally.
7. Commit with a Conventional Commit message.
8. Push to GitHub.

## Commit Messages

Use Conventional Commits:

```text
feat(scope): short description
docs(scope): short description
fix(scope): short description
chore(scope): short description
```

## Documentation Rules

- Write clearly.
- Prefer beginner-friendly explanations.
- Explain why, not only what.
- Link related concepts if possible.
- Update Project Brain if knowledge changes.

## AI Usage

AI-generated work must be reviewed.

AI must not autonomously:

- push
- force push
- reset
- rebase
- delete branches
- delete tags
- publish releases

## ADR Requirement

Create an ADR when a change affects:

- architecture
- governance
- repository structure
- security model
- release process
- AI workflow
- project lifecycle

## Review Checklist

Before committing:

- [ ] Changes are intentional.
- [ ] No secrets are included.
- [ ] Documentation is updated.
- [ ] Relevant ADRs are updated or created.
- [ ] Commit message follows NDF style.
