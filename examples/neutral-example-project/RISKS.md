# SampleProject – Risks

> Fiktive Risikoliste aus Maintainer-Sicht. Input für Compliance Check und Health Score.

| # | Risiko | Beschreibung | Auswirkung |
|---|---|---|---|
| 1 | Scope Creep | Features entstehen nach Zuruf; nichts begrenzt Größe oder Reihenfolge | Projekt wächst unkontrolliert, nichts wird fertig |
| 2 | Unscharfe Rollen | geteilter Admin-Account, keine serverseitige Rollenprüfung | jeder kann alles — auch löschen |
| 3 | Unvollständige Security | Secret-Handling ungeklärt, kein Audit, keine fail-closed-Prüfung | vermeidbare Vorfälle, keine Nachvollziehbarkeit |
| 4 | Fehlende Tests | unbekannte Testabdeckung, CI rot und ignoriert | Regressionen werden erst im Betrieb bemerkt |
| 5 | Fehlende Release-Kriterien | „einfach deployen", kein Backup davor | Update kann Daten kosten, kein Rollback-Weg |
| 6 | Unklare i18n-Anforderungen | DE intern, EN „irgendwann", nichts entschieden | Doku wächst gemischt und inkonsistent weiter |
| 7 | Ein-Personen-Wissen | Deployment und Konfiguration nur im Kopf des Maintainers | Ausfallrisiko, Onboarding unmöglich |

## Erwartung an den Adapter

Diese Risiken sollen sich in Compliance Check, Health Score und der initialen Work Package Queue wiederfinden — priorisiert, nicht nur aufgelistet.
