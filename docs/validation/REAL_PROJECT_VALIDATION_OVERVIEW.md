# Real Project Validation Overview

## Zweck

NDF soll nicht nur aus Regeln bestehen, sondern in echten Projekten funktionieren.

Dieses Paket dokumentiert die ersten zwei Referenzvalidierungen:

- SpeakCore
- CastCore

## Zentrale Erkenntnis

NDF funktioniert am besten als kontrollierter Ausführungsrahmen:

```text
Planung -> kleines Work Package -> Claude Umsetzung -> Rückmeldung an Nova -> Kay Review -> Commit/Push
```

## SpeakCore als Referenz

SpeakCore validiert NDF für besonders riskante Funktionen:

- destructive actions
- Backup-Delete
- OWNER-only Flows
- Audit ohne sensible Daten
- Agent-Endpunkte
- Rate Limits
- ADR-Pflicht
- Blueprint-vor-Ausführung

## CastCore als Referenz

CastCore validiert NDF für technische Projektreife:

- Docker-first
- CI-Gates
- docs-status Stabilität
- Health Score
- Security Baseline Review
- fail-closed Production Config
- lokale Test-/Docker-Probleme

## NDF-Verbesserungen aus beiden Projekten

1. Work Package Typen müssen formalisiert werden.
2. Destructive Actions brauchen eigene Standards.
3. Security-Findings brauchen einen festen Ablauf.
4. Health Score darf nur begründet steigen.
5. Tests vor Commit sind Pflicht bei Codeänderungen.
6. Audit muss beweiskräftig sein, aber nichts Sensibles leaken.
7. Agent-Endpunkte sind privilegierte Security Boundaries.
8. Docker-/CI-Probleme müssen als eigene Risiko-Kategorie behandelt werden.
