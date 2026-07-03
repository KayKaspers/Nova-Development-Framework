# Backup and Delete Patterns

## NDF-Regel

Backup-Delete ist eine destructive action und braucht Blueprint vor Umsetzung.

## Mindestanforderungen

- OWNER-only
- managed Backup-Scope
- exakt validierter Target-Name
- keine freien Pfade
- keine Wildcards
- exakt abgeleitete Metadaten-Datei
- 3 Bestätigungen bei irreversiblen Löschungen
- Typed Confirmation, z. B. `DELETE BACKUP`
- Rate Limit
- Audit Privacy
- Tests

## Audit darf nicht enthalten

- Host-Pfad
- Dateiinhalt
- sensible Dateinamen
- Prüfsummen, wenn sie Inventory verraten
- Secrets/Tokens
