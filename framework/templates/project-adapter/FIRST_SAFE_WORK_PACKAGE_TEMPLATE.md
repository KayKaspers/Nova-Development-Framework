# First Safe Work Package (Template)

Das erste umzusetzende Work Package nach der Adapter-Baseline. Muss klein und ungefährlich sein. Konventionen: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`.

## <XY>-WP-001 – <Titel / title>

## Work Package Type

`review-only` oder `docs-only` (nichts anderes für das erste WP)

## DE – Ziel / EN – Goal

<!-- Eine klar begrenzte, sichere Aufgabe — z. B. Doku-Bestandsaufnahme, Klärung eines Widerspruchs. -->

## Aufgaben / Tasks

<!-- konkrete, lesende bzw. rein dokumentierende Schritte -->

## Grenzen / Boundaries

- **Keine Codeänderungen. Keine Konfig-/Deployment-Änderungen. Keine destruktiven Aktionen.**
- Keine Secrets lesen, kopieren oder ausgeben; Fundstellen nur als Risiko nennen.
- Kein Commit, kein Push — Veröffentlichung ausschließlich durch den Human Maintainer.
- Keine privaten Namen/Domains/Secrets in erzeugte Dateien (Public Quality Gate v0.2).

## Tests

Bei `review-only`: keine (begründete Test-Ausnahme). Bei `docs-only`: keine Codeänderung, daher keine Funktionstests.

## Rückmeldung an Nova (ChatGPT)

Strukturierter Report (Zusammenfassung, Ergebnis, offene Fragen, Risiken, empfohlene nächste WPs, Empfehlung GO / REWORK / SPLIT / STOP). Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle.

## Review-Kriterium (Human Maintainer)

Der Report ist nachvollziehbar; keine Datei wurde funktional verändert (`git status` sauber); die nächsten WPs sind dadurch startklar.
