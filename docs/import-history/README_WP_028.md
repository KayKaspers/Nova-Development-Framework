# NDF-WP-028 – Destructive Action Toolkit Checklist

## Ziel

NDF bekommt ein nutzbares Toolkit für destructive Actions.

## Warum

Referenzprojekt A hat gezeigt, dass gefährliche Funktionen eigene Sicherheitsregeln brauchen.

Beispiele:

- Backup löschen
- Container löschen
- Volume löschen
- Agent-Aktion ausführen
- Server zurücksetzen
- Tenant löschen
- Token widerrufen
- Produktionsdaten löschen

## Kernregel

```text
Keine destructive Action ohne Blueprint, Review, Guard, Tests und Audit.
```

## Commit

```text
feat(toolkit): add destructive action safety toolkit
```
