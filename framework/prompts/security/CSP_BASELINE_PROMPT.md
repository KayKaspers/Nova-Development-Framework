# Claude Prompt – CSP Header Baseline

## Rolle

Du bist Claude und setzt oder dokumentierst eine erste Content-Security-Policy nach NDF.

## Work Package Type

security-code-fix

## Ziel

Reduziere das Risiko fehlender CSP-Header mit einer praktikablen Baseline.

## Aufgabe

1. Prüfe, wo Security Header sinnvoll gesetzt werden.
2. Prüfe bestehende Header.
3. Wähle eine konservative CSP.
4. Implementiere minimal oder dokumentiere Reverse-Proxy-Lösung.
5. Berücksichtige Self-hosting, WebSockets, Fonts, Images und Frontend-Framework.
6. Ergänze Tests/Checks wenn sinnvoll.

## CSP-Richtung

```text
default-src 'self';
base-uri 'self';
object-src 'none';
frame-ancestors 'none';
img-src 'self' data: blob:;
font-src 'self' data:;
style-src 'self' 'unsafe-inline';
script-src 'self';
connect-src 'self' ws: wss:;
```

## Grenzen

- Keine externen Domains ohne Bedarf
- Keine großen Refactors
- Keine CI-Änderungen
- Kein Commit
- Kein Push

## Rückmeldung an Nova

### Zusammenfassung

### Geänderte Dateien

### CSP-Lösung

### Gewählte CSP

### Auswirkungen

### Tests / Prüfung

### Risiken

### Health Score Empfehlung

### Empfehlung
