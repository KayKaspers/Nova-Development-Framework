# Claude Prompt – Fail-closed Config Validation

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Implement minimal fail-closed validation for production-critical configuration: production refuses to start with unsafe defaults, development and test stay usable, error messages never contain secret values, focused tests included. No commit or push by the Implementation Agent.

## Rolle

Du bist Claude und implementierst eine minimale Fail-Closed-Validierung für produktionskritische Konfiguration.

## Work Package Type

security-code-fix

## Ziel

Ein Projekt darf in Production nicht mit unsicheren Defaults starten.

## Aufgabe

1. Identifiziere produktionskritische Secrets.
2. Prüfe Environment-Unterscheidung.
3. Erlaube Development/Test pragmatisch.
4. Blockiere Production mit unsicheren Defaults.
5. Fehlermeldung ohne Secret-Werte.
6. Ergänze Tests.
7. Dokumentiere Risiken.

## Akzeptanzkriterien

- Production fail-closed
- Development/Test bleiben nutzbar
- Keine Secrets im Log
- Tests grün
- Risiko aktualisiert

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Zusammenfassung

### Geänderte Dateien

### Fail-Closed-Lösung

### Development/Test Verhalten

### Production Verhalten

### Tests

### Risiken

### Health Score Empfehlung

### Empfehlung
