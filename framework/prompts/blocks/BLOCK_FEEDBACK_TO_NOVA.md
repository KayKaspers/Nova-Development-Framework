# Prompt Block – Rückmeldung an Nova

Am Ende zwingend ausgeben:

## Rückmeldung an Nova

1. Status (z. B. `completed`, `blocked`, `in-progress-limit-reached`)
2. Zusammenfassung
3. Geänderte Dateien
4. Ausgeführte Tests
5. Nicht ausgeführte Tests und warum
6. Offene Punkte
7. Risiken
8. Empfehlungen
9. Nächster sinnvoller Schritt

### Optionale Felder (nur wenn im Work Package relevant)

- **Token-/Limit-Status:** Limit erreicht? Resume erforderlich? abgeschlossene / teilweise / offene Dateien; letzte vollständig abgeschlossene Teilintegration.
- **Skills-first-Nutzung:** je relevantem Skill — geprüft / gelesen / Prozessanweisungen angewendet / technisch ausgeführt: nein / verändert: nein / Zweck; Bestätigung, dass nicht alle Skills geladen wurden.
- **Abweichungen:** oder „Keine bekannte Abweichung."
- **Ausdrückliche Bestätigungen:** z. B. kein Git Write, kein Commit/Push/Tag/Release, nur Allowed Files geändert.
- **Compact Context Summary:** kurze, limitfreundliche Übergabe.

## Blocked-/No-Change-Abschnitt (nur wenn das Work Package blockiert ist)

Dieser Abschnitt gilt **nur** im Blocked-Fall und darf normale Rückmeldungen nicht überladen. Ein Fail-closed-Stopp **vor jeder Änderung** ist selbst ein vollständiges, review-fähiges Ergebnis; er verlangt keinen künstlichen Zwischen-Commit.

```text
Work Package ID
Status: blocked
Blocker
Preflight results
Reason for fail-closed stop
Files changed: none
Git write performed: no
Tests run
Tests not run and why
Exact unblock condition
Recommended next step
Compact Context Summary
```

Regeln im Blocked-Fall: keine leere/unnötige Datei erzeugen; keine reine Statusmutation ohne Freigabe; keinen künstlichen Zwischen-Commit verlangen; den Blocker nicht als `completed` melden.
