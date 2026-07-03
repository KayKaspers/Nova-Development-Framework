# Destructive Action Patterns

## Definition

Destructive Actions sind Aktionen, die Ressourcen unwiderruflich löschen, überschreiben, widerrufen, zurücksetzen oder deprovisionieren.

## Pflichtablauf

```text
Blueprint -> Nova Review -> Read-only Preview -> Guarded Execution -> Audit -> Tests -> Maintainer Commit
```

## Pflichtinhalte im Blueprint

- Zielressource
- erlaubter Scope
- verbotene Targets
- Validierungsregeln
- Rollen-/Rechteprüfung
- Confirmation Flow
- Rate Limit
- Audit Privacy
- Tests
- Rollback-Grenzen
- ADR-Bedarf

## Verbotene Muster

- freier Host-Pfad
- Wildcard-Delete
- Shell-Delete mit User Input
- Delete nach unvalidiertem Dateinamen
- Companion-Datei aus User Input
- Audit von Secrets/Pfaden/Inhalten
