# Claude Prompt – Security Baseline Review

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Produce a structured security baseline assessment (secrets, auth, authorization, headers, containers, destructive actions, audit, rate limiting, CI) without any functional changes. A security review is not a security fix and not a Health Score update — those are separate work packages. Never output secrets. No commit, no push.

## Rolle

Du bist Claude und prüfst ein Projekt nach dem Nova Development Framework auf eine erste Security-Baseline.

## Work Package Type

security-baseline

## Ziel

Erstelle eine strukturierte Security-Bewertung ohne funktionale Codeänderungen.

## Aufgabe

Prüfe:

1. Secrets und `.env`-Handling
2. Authentifizierung
3. Autorisierung/RBAC
4. Admin-/Owner-Flows
5. Transport/Web Security
6. Security Header
7. Docker-/Container-Hardening
8. Agent-/Admin-Endpunkte
9. Destructive Actions
10. Audit und Logging
11. Rate Limiting
12. Config Defaults
13. CI Security Automation

## Grenzen

- Keine Codeänderungen
- Keine CI-Änderungen
- Keine Docker-Änderungen
- Keine Secrets ausgeben
- Kein Commit
- Kein Push

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Zusammenfassung

### Geänderte Dateien

### Security-Bewertung

### Findings

### Risiken

### Empfohlene Security Work Packages

### Health Score Empfehlung

### Tests / Prüfung

### Empfehlung
