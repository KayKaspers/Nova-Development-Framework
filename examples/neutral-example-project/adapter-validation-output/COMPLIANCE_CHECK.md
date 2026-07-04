# Compliance Check – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

Regel: `fail` ist kein Blocker für die NDF-Adoption — es wird zur Work-Package-Quelle.

| Prüfpunkt | Status | Evidence | Gap | Recommended next action |
|---|---|---|---|---|
| Work Package Typisierung | fail → initialized | vor Adapter: Wunschliste; jetzt initiale Queue mit Typen | Queue muss gelebt werden | SP-WP-001 starten, Typen-Standard verlinken |
| Project Brain | fail → initialized | vorher keiner; `PROJECT_BRAIN.md` erstellt | Pflege-Routine fehlt | nach jedem WP aktualisieren (SP-WP-002 formalisiert) |
| Health Score | fail → initialized | vorher keiner; initial evidenzbasiert | Update-Regel fehlt | nur via health-score-update-WPs ändern |
| Security Baseline | fail | keine systematische Prüfung je erfolgt | Findings SP-F-008/009/010 | SP-WP-003 (security-baseline) |
| Destructive Blueprint vor Implementation | fail | Löschung/Reset existieren ohne jeden Schutz | kein Blueprint vorhanden | SP-WP-005 (destructive-blueprint), Implementierung erst nach Freigabe |
| Documentation-first | fail | Features vor Doku („zuletzt genanntes Feature gewinnt") | README/Deployment-Lücken | SP-WP-001/004 |
| Human Maintainer Review | partial | Maintainer prüft faktisch alles selbst, aber ohne definierten Gate | kein Review-Gate | Arbeitsweise aus PROJECT_BRAIN übernehmen |
| No Implementation Agent commit/push | n/a → pass (Regel gesetzt) | bisher kein Agent im Einsatz; Regel jetzt im PROJECT_BRAIN verankert | — | beibehalten |
| DE/EN-Transparenz | partial | Anforderungen benennen die Unklarheit ehrlich | keine Entscheidung | Maintainer-Entscheidung dokumentieren |
| Release Criteria | fail | „einfach deployen" | keine Kriterien, kein Backup | Backup-Regel in SP-WP-004, Kriterien als späteres WP |

## Wichtigste Lücken

1. Security Baseline komplett offen (inkl. Secrets, Rollen, Audit).
2. Destruktive Funktionen ohne Blueprint-Prozess.
3. Doku widersprüchlich — blockiert Onboarding am stärksten (Antwort auf CURRENT_STATE-Frage 4).
