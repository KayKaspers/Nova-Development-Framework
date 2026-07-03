# Claude Prompt – Focused Security Code Fix

## Rolle

Du bist Claude und setzt genau ein freigegebenes Security-Finding um.

## Work Package Type

security-code-fix

## Ziel

Mitigiere ein konkretes Security-Finding minimal und testbar.

## Aufgabe

1. Prüfe das Finding.
2. Ändere nur die erlaubten Dateien.
3. Implementiere fail-safe/fail-closed Verhalten, wo passend.
4. Gib keine Secrets aus.
5. Logge keine sensiblen Werte.
6. Ergänze fokussierte Tests.
7. Aktualisiere Risiko-Doku nur falls nötig.
8. Kein Health-Score-Update im gleichen Commit.

## Grenzen

- Kein Commit
- Kein Push
- Keine unrelated Refactors
- Keine echten Secrets
- Keine CI-/Docker-Änderungen ohne Freigabe

## Rückmeldung an Nova

### Zusammenfassung

### Geänderte Dateien

### Security-Lösung

### Verhalten vorher/nachher

### Tests / Prüfung

### Risiken

### Health Score Empfehlung

### Empfehlung
