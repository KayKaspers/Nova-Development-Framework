# GitHub Desktop Workflow

## Vor Arbeitsbeginn

1. Repository öffnen.
2. Auf `Fetch origin` klicken.
3. Falls `Pull origin` erscheint, zuerst pullen.
4. Erst danach Dateien ändern.

## Nach einer Änderung

1. GitHub Desktop öffnen.
2. Links unter `Changes` alle Änderungen prüfen.
3. Ungewollte Änderungen abwählen.
4. Summary eintragen.
5. Commit to main klicken.
6. Push origin klicken.

## Commit-Nachrichten

NDF verwendet Conventional Commits.

Beispiele:

```text
feat(workflow): add practical workflow
docs(readme): update project overview
fix(ci): stabilize build check
chore(repo): cleanup generated files
```

## Niemals blind committen

Vor jedem Commit prüfen:

- Sind nur gewünschte Dateien geändert?
- Sind keine Secrets enthalten?
- Ist die Commit-Nachricht verständlich?
- Wurde die Aufgabe abgeschlossen?
