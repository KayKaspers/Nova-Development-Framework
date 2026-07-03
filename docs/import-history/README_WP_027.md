# NDF-WP-027 – Work Package Type Standard Integration

## Ziel

NDF erhält einen verbindlichen Standard für Work-Package-Typen.

## Erkenntnis aus den Referenzprojekten

- Review-Arbeit ist nicht dasselbe wie Code-Arbeit.
- Security-Review ist nicht dasselbe wie Security-Fix.
- Health-Score-Updates sollten nicht im gleichen Commit wie Code-Fixes landen.
- Destructive Actions benötigen Blueprint und Review vor Implementierung.
- Lokale Test-/CI-Diagnose ist ein eigener Arbeitstyp.

## Commit

```text
feat(workflow): integrate work package type standard
```
