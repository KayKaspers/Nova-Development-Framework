# Audit Privacy Pattern

## Prinzip

```text
Evidence without leakage
```

## Audit soll zeigen

- wer
- welche Aktionsklasse
- Ergebnis
- Zeitpunkt
- Resource-Kategorie
- Request-/Correlation-ID

## Audit soll nicht zeigen

- Secrets
- Tokens
- Inhalte
- Host-Pfade
- sensible Dateinamen
- rohe Request-Bodies
- Checksum-Inventory, wenn sensibel

## NDF-Regel

Jedes Security- oder Destructive-WP muss Audit Privacy explizit beschreiben.
