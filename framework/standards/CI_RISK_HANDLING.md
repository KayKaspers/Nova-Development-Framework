# NDF Standard – CI Risk Handling

## Kategorien

- Codefehler
- Testfehler
- Generated Artifact Drift
- Dependency/Pull Failure
- Docker/Runner Problem
- Path/Config Mismatch
- Flaky Test

## Regel für generierte Dateien

Commitpflichtige generierte Dateien müssen deterministisch sein.

## Diagnose

Immer zuerst Job, Step, Diff und Reproduzierbarkeit prüfen.
