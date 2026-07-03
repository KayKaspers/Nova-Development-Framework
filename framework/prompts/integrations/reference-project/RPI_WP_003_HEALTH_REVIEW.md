---
id: reference-project-rpi-wp-003-health-review
title: Reference Project Health Review
version: 0.1
category: integrations/reference-project
role: Claude Reviewer
supported_models: [Claude, ChatGPT]
risk_level: low
requires_human_review: true
---

# Claude Prompt – Reference Project Health Review

## Ziel

Bewerte Reference Project B anhand des NDF Health Score.

## Aufgabe

1. Prüfe Architektur.
2. Prüfe Dokumentation.
3. Prüfe Tests.
4. Prüfe CI/CD.
5. Prüfe Docker/Deployment.
6. Prüfe Security-Basis.
7. Prüfe Project Brain.
8. Prüfe Release Readiness.
9. Aktualisiere `project-system/HEALTH_SCORE.md`.

## Grenzen

- Keine Codeänderungen.
- Kein Commit.
- Kein Push.

## Rückmeldung an Nova

Nutze das Standardformat.
