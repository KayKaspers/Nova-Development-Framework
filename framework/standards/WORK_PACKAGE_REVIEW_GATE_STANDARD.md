# NDF Standard – Work Package Review Gate

> Sprachstatus / Language status: EN mit deutscher Einleitung. / English with German introduction.

DE: Das Review Gate stellt sicher, dass kein Work Package ohne Scope- und Sicherheitsprüfung committet wird. Die Review-Fragen und typ-spezifischen Gates unten sind englisch; die Entscheidungswerte sind GO / GO WITH NOTES / REWORK / SPLIT / STOP.

## Purpose

The Review Gate ensures that no Work Package is committed without scope and safety checks.

## Required Review Questions

1. Does the change match the declared Work Package type?
2. Are only allowed files changed?
3. Are forbidden areas untouched?
4. Were tests run if required?
5. Is the Rückmeldung complete?
6. Are risks documented?
7. Is a follow-up needed?
8. Is Health Score affected?
9. Is Project Brain affected?
10. Is the commit message scoped?

## Type-Specific Gates

### Docs-only

- no code files changed
- docs are coherent
- no misleading status claims

### Code-fix

- focused tests run
- no unrelated refactor
- no hidden config change

### Security-code-fix

- no secrets exposed
- failure mode safe
- error messages safe
- risk updated
- tests cover security behavior

### Destructive implementation

- blueprint exists
- authorization tested
- confirmation tested
- audit privacy tested
- rate limit considered
- ADR exists

### Health-score-update

- evidence exists
- deltas explained
- open risks visible
- no code files changed

## Decision Values

```text
GO
GO WITH NOTES
REWORK
SPLIT
STOP
```
