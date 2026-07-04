# First Safe Work Package – SP-WP-001 (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation. **Dieses WP wird hier nur formuliert, nicht ausgeführt.**

## SP-WP-001 – Repository and Documentation Baseline Review

## Work Package Type

review-only

## Ziel

Vollständige, lesende Bestandsaufnahme von SampleProject als Grundlage aller weiteren Arbeit.

## Aufgaben

1. Doku-Bestand sichten (README, docs/, Changelog) und Lücken je Datei auflisten.
2. Port-Widerspruch klären: Welcher Port gilt tatsächlich (Compose-Datei ist die Referenz)?
3. Konfigquellen kartieren: Welche Werte kommen aus `config.ts`, welche aus `.env`, wo doppelt?
4. Status von `scripts/reset-db.sh` klären: in Gebrauch, tot, oder gefährlich verfügbar?
5. Env-Variablen-Kandidatenliste erstellen (Pflicht/Default — soweit lesend erkennbar).
6. Die 4 offenen Fragen aus CURRENT_STATE beantworten oder als „braucht Maintainer-Wissen" markieren.

## Grenzen / Boundaries

- **Keine Codeänderungen. Keine Konfig- oder Deployment-Änderungen. Keine destruktiven Aktionen.**
- Keine Secrets lesen, kopieren oder ausgeben; Fundstellen nur als Risiko nennen.
- Kein Commit, kein Push — Veröffentlichung ausschließlich durch den Human Maintainer (example-owner).

## Tests

Keine (review-only) — begründete Test-Ausnahme.

## Rückmeldung an Nova (ChatGPT)

Strukturierter Report: Zusammenfassung, Doku-Lückenliste, Port-Antwort, Konfig-Karte, reset-db-Status, Env-Kandidatenliste, Risiken, empfohlene nächste WPs, Empfehlung GO / REWORK / SPLIT / STOP.

## Review-Kriterium (Human Maintainer)

Der Report beantwortet die offenen Fragen nachvollziehbar; keine Datei wurde verändert (`git status` sauber); die nächsten WPs (002–004) sind dadurch startklar.
