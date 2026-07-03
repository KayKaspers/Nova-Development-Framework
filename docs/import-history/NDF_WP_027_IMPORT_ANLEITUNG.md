# Import-Anleitung – NDF-WP-027 Work Package Type Standard Integration

## Zielrepository

`Nova-Development-Framework`

## Zweck

Dieses Paket integriert die aus den Referenzprojekten validierten Work-Package-Typen fest in NDF.

Nach dem Import gilt:

- Kein Work Package ohne Typ.
- Kein Claude-Prompt ohne Work-Package-Typ.
- Kein Commit ohne klaren Scope.
- Review, Docs, Code-Fix, Security-Fix, Health-Score-Update und destructive Actions werden getrennt geführt.

## Import-Schritte

1. ZIP entpacken.
2. Inhalt in das NDF-Repository kopieren.
3. Änderungen prüfen.
4. Commit erstellen:

```text
feat(workflow): integrate work package type standard
```

5. Push origin.

## Erwartete Bereiche

```text
docs/workflow/
framework/standards/
framework/templates/work-packages/
framework/checklists/
framework/prompts/core/
framework/prompts/review/
framework/prompts/security/
docs/academy/
docs/adr/
project-brain/
docs/roadmap/
```

Foundation 0.1 bleibt eingefroren. Dieses Paket gehört zu Foundation 0.2.
