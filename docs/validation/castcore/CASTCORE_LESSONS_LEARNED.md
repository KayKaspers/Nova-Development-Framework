# CastCore Lessons Learned

## L-001 – Committed generated files must be deterministic

Tagesabhängige Felder in commitpflichtigen Artefakten erzeugen CI-Flakiness.

## L-002 – Review-only verbessert Sichtbarkeit, nicht automatisch Security

Security Score steigt erst nach echter Mitigation.

## L-003 – Code-Fix und Health Score Update trennen

Code zuerst, Tests/CI danach, Score separat.

## L-004 – Lokale Docker-Probleme sind echte Projekt-Risiken

DNS, Image Pulls und Container-Pfade müssen sauber diagnostiziert werden.

## L-005 – Container-Pfade prüfen

Wenn `backend/tests/...` nicht existiert, im Container mit `find` den echten Pfad suchen.

## L-006 – Fail-closed Production Config ist ein starker Security-Hebel

Development darf bequem bleiben, Production muss streng abbrechen.

## L-007 – Moderate Scores schaffen Vertrauen

Security 60 -> 66 war sinnvoll; keine künstliche Überbewertung.
