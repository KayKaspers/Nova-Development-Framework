# Academy Lesson – Destructive Actions

## Ziel

Verstehen, warum Delete-, Reset- und Deprovision-Funktionen in NDF anders behandelt werden.

## Problem

Eine normale Funktion kann man korrigieren. Eine destructive Action kann Daten löschen.

Deshalb gilt:

```text
Destructive Actions sind Sicherheitsfunktionen.
```

## Beispiele

- Backup löschen
- Volume löschen
- Tenant löschen
- Token widerrufen
- Server zurücksetzen

## NDF-Ablauf

```text
Blueprint -> Review -> Implementierung -> Tests -> Commit -> CI
```

## SpeakCore-Beispiel

SpeakCore hat einen Einzel-Backup-Delete mit diesen Controls umgesetzt:

- OWNER-only
- 3 Pflichtbestätigungen
- typed `DELETE BACKUP`
- Rate Limit
- token-gated Agent Endpoint
- Audit ohne sensible Daten

## Merksatz

```text
Erst zeigen, dann prüfen, dann löschen.
```
