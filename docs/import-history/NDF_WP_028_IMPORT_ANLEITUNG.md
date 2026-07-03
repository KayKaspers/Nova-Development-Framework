# Import-Anleitung – NDF-WP-028 Destructive Action Toolkit Checklist

## Zielrepository

`Nova-Development-Framework`

## Zweck

Dieses Paket ergänzt NDF um ein konkretes Toolkit für gefährliche und irreversible Aktionen.

Es baut direkt auf den Erkenntnissen aus Referenzprojekt A auf:

- Blueprint vor Ausführung
- Read-only vor Delete
- Owner-only Flow
- typed confirmation
- Rate Limit
- Audit ohne sensible Daten
- strikt validierter Managed Scope
- ADR/Risiko-Doku
- Tests vor Commit

## Import-Schritte

1. ZIP entpacken.
2. Inhalt in das NDF-Repository kopieren.
3. Änderungen prüfen.
4. Commit erstellen:

```text
feat(toolkit): add destructive action safety toolkit
```

5. Push origin.

## Erwartete Bereiche

```text
docs/toolkit/destructive-actions/
framework/checklists/
framework/templates/security/
framework/prompts/security/
docs/academy/
docs/adr/
project-brain/
docs/roadmap/
```

Foundation 0.1 bleibt eingefroren. Dieses Paket gehört zu Foundation 0.2.
