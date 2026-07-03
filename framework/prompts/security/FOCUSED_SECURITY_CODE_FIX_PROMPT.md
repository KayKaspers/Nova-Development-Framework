# Claude Prompt – Focused Security Code Fix

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Mitigate exactly one approved security finding with minimal, testable changes (fail-closed where appropriate). No unrelated refactors, never output or log secrets, no Health Score update in the same commit, no commit or push by the Implementation Agent.

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

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Zusammenfassung

### Geänderte Dateien

### Security-Lösung

### Verhalten vorher/nachher

### Tests / Prüfung

### Risiken

### Health Score Empfehlung

### Empfehlung
