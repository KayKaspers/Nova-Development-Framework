# Checklist – Work Package Type

## DE – Zweck

Diese Checkliste prüft vor dem Prompt und vor dem Commit, ob das Work Package korrekt typisiert ist und im Scope geblieben ist. Die Schnellreferenz unten ordnet Aufgaben den Typen zu.

## EN – Purpose

This checklist verifies before the prompt and before commit that the work package is correctly typed and stayed in scope. The quick reference below maps tasks to types.

## Before Prompt

- [ ] Work Package ID defined
- [ ] Primary type selected
- [ ] Scope defined
- [ ] Allowed files listed
- [ ] Forbidden files listed
- [ ] Tests expectation defined
- [ ] Risk level defined
- [ ] Rückmeldung structure included

## Before Commit

- [ ] Changed files match type
- [ ] No unrelated changes
- [ ] Tests run or reason documented
- [ ] Risks documented
- [ ] Follow-up captured
- [ ] Commit message matches type

## Quick Reference

| If you are doing this | Use this type |
|---|---|
| assessing current state | review-only |
| writing documentation | docs-only |
| fixing one bug | code-fix |
| fixing a security finding | security-code-fix |
| reviewing security | security-baseline |
| updating score | health-score-update |
| diagnosing CI | ci-diagnostic |
| planning delete/reset | destructive-blueprint |
| implementing approved delete/reset | destructive-implementation |
