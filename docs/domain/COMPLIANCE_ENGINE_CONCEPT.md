# NDF Compliance Engine Concept

## Ziel

Die Compliance Engine prüft, ob ein Projekt nach NDF-Standards geführt wird.

## Bewertungsbereiche

- Project Brain
- README
- Roadmap
- ADRs
- Standards
- Tests
- Security
- Documentation
- Release Process
- Prompt Workflow

## Statuswerte

- Pass
- Warning
- Fail
- Not Applicable

## Beispiel

| Bereich | Status | Hinweis |
|---|---|---|
| Project Brain | Pass | vorhanden |
| ADRs | Warning | wenige Entscheidungen dokumentiert |
| Security | Pass | keine Secrets gefunden |
| Tests | Fail | keine Teststrategie dokumentiert |

## Ergebnis

Die Compliance Engine erzeugt:

- Compliance Score
- Risiken
- empfohlene Work Packages
