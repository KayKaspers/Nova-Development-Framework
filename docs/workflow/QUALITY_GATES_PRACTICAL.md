# Praktische Quality Gates / Practical Quality Gates

## DE

### Was ist ein Quality Gate?

Ein Quality Gate ist ein fester Prüfpunkt im Workflow: Erst wenn die Prüfungen bestanden sind, geht die Arbeit in den nächsten Schritt. Quality Gates laufen vor der Umsetzung, nach der Umsetzung, vor dem Commit und nach dem Push.

### Vor der Umsetzung

- Ziel ist klar
- Aufgabe ist klein und typisiert
- Grenzen sind definiert
- Rückmeldung an Nova (ChatGPT-Review-Rolle) ist gefordert

### Nach der Umsetzung

- Dateien geprüft
- keine unerwarteten Änderungen
- Tests oder Prüfhinweise vorhanden
- Dokumentation berücksichtigt
- Rückmeldung an Nova vollständig

### Vor dem Commit

- Änderungen geprüft (z. B. in GitHub Desktop)
- keine Secrets
- Public Quality Gate grün: `python scripts/check_public_quality.py --strict` ([PUBLIC_QUALITY_GATE.md](../repository/PUBLIC_QUALITY_GATE.md))
- Neutralitäts-Greps leer (keine privaten Projekt-/Personenbezüge)
- Commit-Message im NDF-Stil
- Aufgabe abgeschlossen oder sauber dokumentiert

### Nach dem Push

- CI-Lauf (Public Quality Gate) geprüft
- Nova bekommt Rückmeldung
- Project Brain wird bei Bedarf aktualisiert
- nächster Schritt wird geplant

### Entscheidung

Am Review-Gate wird entschieden: **GO / GO WITH NOTES / REWORK / SPLIT / STOP** ([WORK_PACKAGE_REVIEW_GATE_STANDARD.md](../../framework/standards/WORK_PACKAGE_REVIEW_GATE_STANDARD.md)).

## EN

### What is a quality gate?

A quality gate is a fixed checkpoint in the workflow: work only moves to the next step once the checks pass. Quality gates run before execution, after execution, before commit, and after push.

### Before execution

- goal is clear
- task is small and typed
- limits are defined
- feedback to Nova (ChatGPT review role) is required

### After execution

- files reviewed
- no unexpected changes
- tests or verification notes present
- documentation considered
- feedback to Nova complete

### Before commit

- changes reviewed (e.g. in GitHub Desktop)
- no secrets
- public quality gate green: `python scripts/check_public_quality.py --strict` ([PUBLIC_QUALITY_GATE.md](../repository/PUBLIC_QUALITY_GATE.md))
- neutrality greps empty (no private project/person references)
- commit message in NDF style
- task finished or cleanly documented

### After push

- CI run (public quality gate) checked
- Nova receives the feedback
- Project Brain updated if needed
- next step planned

### Decision

At the review gate the decision is made: **GO / GO WITH NOTES / REWORK / SPLIT / STOP** ([WORK_PACKAGE_REVIEW_GATE_STANDARD.md](../../framework/standards/WORK_PACKAGE_REVIEW_GATE_STANDARD.md)).
