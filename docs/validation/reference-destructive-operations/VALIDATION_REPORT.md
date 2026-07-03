# Reference Project A Validation Report

## Fokus

Referenzprojekt A ist die NDF-Referenz für gefährliche Aktionen und Sicherheitsmuster.

## Validierter Fall

Einzelnes managed Backup löschen:

- exakt eine validierte managed Backup-`.tar.gz`
- exakt abgeleitete `.metadata.json`
- token-gated Agent-Endpunkt
- OWNER-only Web-Flow
- Warnanzeige
- 3 Pflichtbestätigungen
- getippter Text `DELETE BACKUP`
- Rate-Limit 5/h
- Audit ohne Dateiname, Prüfsumme, Inhalt oder Host-Pfad
- ADR, Doku und Tests

## NDF-Erkenntnis

Delete ist kein normales CRUD. Delete ist ein kontrolliertes operational event.

## Validierte Patterns

| Pattern | Status |
|---|---|
| Blueprint vor destructive action | validiert |
| Read-only vor Write/Delete | validiert |
| OWNER-only Flow | validiert |
| Mehrfachbestätigung | validiert |
| Typed Confirmation | validiert |
| Rate Limit | validiert |
| Audit Privacy | validiert |
| Managed Scope Validation | validiert |
| Agent Token Gate | validiert |
| ADR-Pflicht | validiert |

## NDF-Konsequenz

NDF braucht einen verbindlichen Destructive Action Standard.
