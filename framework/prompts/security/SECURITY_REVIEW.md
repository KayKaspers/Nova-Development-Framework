---
id: ndf-sec-review-001
title: Security Review
version: 0.1
category: security
role: Claude Security Reviewer
supported_models: [Claude, ChatGPT]
risk_level: high
requires_human_review: true
---

# NDF Prompt – Security Review

## Ziel

Führe eine strukturierte Sicherheitsprüfung durch.

## Aufgabe

1. Suche nach Secrets.
2. Prüfe gefährliche Defaults.
3. Prüfe Authentifizierung, falls vorhanden.
4. Prüfe Berechtigungen.
5. Prüfe Docker/CI-Risiken.
6. Erstelle priorisierte Empfehlungen.

## Grenzen

- Keine riskanten Änderungen ohne Freigabe.
- Kein Commit.
- Kein Push.

## Rückmeldung an Nova

Nutze den Standardblock Rückmeldung an Nova.
