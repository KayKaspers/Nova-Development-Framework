# Owner-only Flow Pattern

## Wann verwenden?

- Backup löschen
- Tenant löschen
- Production Reset
- Secrets rotieren
- Agent Token widerrufen
- irreversible Serveraktionen

## Pflichtkontrollen

| Kontrolle | Pflicht |
|---|---|
| serverseitige OWNER-Prüfung | ja |
| Warnanzeige | ja |
| Read-only Preview | ja |
| Mehrfachbestätigung | ja |
| Typed Confirmation | bei irreversibel |
| Rate Limit | ja |
| Audit | ja |
| Tests | ja |

## Regel

Owner-only ersetzt keine Tests. Owner-only braucht mehr Tests.
