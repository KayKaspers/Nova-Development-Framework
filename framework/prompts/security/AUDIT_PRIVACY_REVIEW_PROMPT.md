# Claude Prompt – Audit Privacy Review

## Rolle

Du bist Claude und prüfst Audit-Events auf Privacy und Security.

## Work Package Type

review-only

## Ziel

Stelle sicher, dass Audit beweiskräftig ist, aber keine sensiblen Daten leakt.

## Prüfe

- event type
- actor fields
- resource class
- result
- reason code
- timestamp/correlation
- verbotene Felder
- Tests gegen Secret-/Path-Leaks

## Verboten im Audit

- raw tokens
- API keys
- passwords
- secrets
- file contents
- full host paths
- sensitive filenames
- raw request bodies

## Rückmeldung an Nova

### Ergebnis

### Sichere Felder

### Gefährliche Felder

### Testempfehlung

### Empfehlung
