# Initial Work Package Queue – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

Präfix `SP-WP` = **S**ample**P**roject Work Package (projekteigenes Präfix gemäß Template-Regel; hier deckungsgleich mit dem Template-Beispiel, weil das Projekt tatsächlich „SampleProject" heißt — für echte Projekte eigenes Präfix wählen).

| ID | Titel | Typ | Priorität | Ziel | Risiko | Abhängigkeiten | Review-Kriterium |
|---|---|---|---|---|---|---|---|
| SP-WP-001 | Repository and Documentation Baseline Review | review-only | P1 | vollständige Bestandsaufnahme: Doku-Lücken, Port-Klärung, Konfigquellen, Status `reset-db.sh` | keins (read-only) | — | Report beantwortet die 4 offenen Fragen aus CURRENT_STATE |
| SP-WP-002 | Project Brain Bootstrap | docs-only | P1 | PROJECT_BRAIN in den Alltag überführen: Pflege-Regel, erste Einträge aus SP-WP-001 | keins | SP-WP-001 | Brain aktuell + Pflege-Regel dokumentiert |
| SP-WP-003 | Security Baseline Review | security-baseline | P1 | systematische Security-Bewertung (Rollen, Secrets, Audit, Endpunkte) — Findings, keine Fixes | keins (review) | SP-WP-001 | priorisierte Findings-Liste mit WP-Vorschlägen |
| SP-WP-004 | Deployment Documentation Cleanup | docs-only | P1 | README + Deployment konsolidieren: ein Port, Env-Variablen-Liste, Backup-vor-Update-Regel, Rollback-Weg | gering (nur Doku) | SP-WP-001 | Neuer Nutzer kann von Null installieren |
| SP-WP-005 | Destructive Action Blueprint for Example Note Delete | destructive-blueprint | P2 | sicheren Lösch-Flow planen (Preview, Bestätigung, Rolle, Audit, Backup); `reset-db.sh` miterfassen | keins (nur Planung) | SP-WP-003 | Blueprint besteht Blueprint-Review-Gate; **keine Implementierung** |

## Regeln

- Reihenfolge: 001 → (002 ‖ 004) → 003 → 005. Nichts Destruktives vor freigegebenem Blueprint.
- Jedes WP endet mit Rückmeldung an Nova (ChatGPT); Commit/Push nur durch den Human Maintainer (example-owner).
- Neue WPs entstehen aus SP-WP-001/003-Findings — klein und typisiert.
