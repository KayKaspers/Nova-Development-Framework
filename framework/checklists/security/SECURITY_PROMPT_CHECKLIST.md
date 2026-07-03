# Checklist – Security Prompt

## DE – Zweck

Diese Checkliste prüft Security-Prompts vor dem Versand und Ergebnisse vor dem Commit: Typ, Scope, Secret-Regeln, Tests, getrenntes Health-Score-Update und Rückmeldung an Nova (ChatGPT).

## EN – Purpose

This checklist verifies security prompts before sending and results before commit: type, scope, secret rules, tests, separated Health Score update, and the feedback to Nova (ChatGPT).

## Before Sending Prompt

- [ ] Work Package Type declared
- [ ] Security finding named
- [ ] Risk level defined
- [ ] Allowed files listed
- [ ] Forbidden files listed
- [ ] Secret handling rules included
- [ ] Logging restrictions included
- [ ] Test expectation included
- [ ] No commit / no push rule included
- [ ] Rückmeldung an Nova included

## Before Commit

- [ ] Changed files match allowed scope
- [ ] No secrets exposed
- [ ] No unrelated refactor
- [ ] Tests run or reason documented
- [ ] Risks updated
- [ ] Health Score update separated if needed
- [ ] Commit message scoped

## For Security Code Fix

- [ ] Fail-safe behavior verified
- [ ] Error messages do not reveal secrets
- [ ] Negative tests included
- [ ] Development/test usability considered
- [ ] Production behavior documented
