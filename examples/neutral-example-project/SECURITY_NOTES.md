# SampleProject – Security Notes

> Fiktiver Sicherheitsstand. Keine echten Secrets, Tokens oder Hostnamen — nur Platzhalter wie `EXAMPLE_SECRET_PLACEHOLDER` und `example.local`.

## Authentifizierung (angenommen)

- Username/Passwort mit Session-Cookie.
- Ein geteilter Admin-Account für das ganze Team (bekanntes Anti-Pattern, soll weg).
- Keine 2FA, keine Passwort-Regeln.

## Rollenmodell (grob)

- Ist: eingeloggt = darf alles.
- Soll: mindestens `member` und `owner`; Owner-only für riskante Aktionen — serverseitig geprüft, nicht nur in der UI.

## Secret Handling (offen)

- `.env`-Datei mit Werten wie `SESSION_SECRET=EXAMPLE_SECRET_PLACEHOLDER` — wird derzeit per Team-Chat weitergegeben (dokumentierte schlechte Praxis, keine echten Werte).
- Ungeklärt: Pflicht-Variablen, Defaults, fail-closed-Verhalten in Produktion.
- Gewünscht: dokumentierte Variablenliste + Produktions-Start verweigert unsichere Defaults.

## Audit Logging (unvollständig)

- Ist: keins.
- Soll: Ereignis, Akteur(-Rolle), Ressourcen-Klasse, Ergebnis — ohne sensible Inhalte („Belege ohne Leaks").

## Destructive-Action-Planungsfall (harmlos, bewusst gewählt)

**Use-Case: Löschen einer Beispielnotiz.**

- Ist: Ein Klick löscht die Notiz sofort — keine Bestätigung, kein Backup/Papierkorb, kein Audit-Eintrag, keine Rollenprüfung.
- Erwartung an NDF: Dieser Fall wird im Adapter **nur erfasst und klassifiziert** (Kandidat für `destructive-blueprint` → nach Freigabe `destructive-implementation`). Keine Implementierung im Fixture.
- Warum harmlos: Es geht um fiktive Notizen in einem fiktiven Projekt — ideal, um den NDF-Prozess für destruktive Aktionen gefahrlos zu demonstrieren.

## Benötigte Sicherheitsreviews (aus Sicht des Maintainers)

1. Security-Baseline-Review (Gesamtbild, Findings-Liste).
2. Secret-Handling-Review (Variablen, fail-closed).
3. Destructive-Action-Blueprint für die Notiz-Löschung.
4. Audit-Logging-Konzept.

## Explizit nicht enthalten

- keine echten Secrets, Tokens, API-Keys
- keine echten Hostnamen oder Domains (nur `example.local`)
- keine echten Personen oder Accounts
