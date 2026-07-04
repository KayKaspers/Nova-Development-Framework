# Findings – SampleProject Read-only Review (Adapter Phase 1)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

Spalte „0.3-blocking": Ein Finding blockiert Foundation 0.3 nur, wenn es zeigt, dass der **Project Adapter selbst** nicht ausreichend funktioniert — Fixture-Findings sind erwartetes Fundmaterial.

| ID | Titel | Quelle | Schwere | Kategorie | Evidenz | Auswirkung | Empfohlene Aktion | 0.3-blocking |
|---|---|---|---|---|---|---|---|---|
| SP-F-001 | README-Installation bricht ab | sample-docs/README_INCOMPLETE.md | medium | Documentation | „TODO: .env erklären", Kommentar zu fehlenden Schritten | Onboarding unmöglich ohne Maintainer | SP-WP-001/004 | no |
| SP-F-002 | Port-Widerspruch 3000 vs. 8080 | README vs. DEPLOYMENT_NOTES | medium | Documentation | zwei Dokumente nennen verschiedene Ports | Fehlkonfiguration, Verwirrung | SP-WP-004 | no |
| SP-F-003 | CI rot und ignoriert | CURRENT_STATE, MOCK_TREE (.github/workflows/ci.yml) | medium | CI/Tests | „läuft rot, wird ignoriert" | keine Regressionssicherheit | eigenes ci-diagnostic-WP nach Baseline | no |
| SP-F-004 | Kein Project Brain | CURRENT_STATE | medium | Governance | „Fehlt"-Liste | Wissen nur im Kopf des Maintainers | SP-WP-002 | no |
| SP-F-005 | Kein Health Score / Reifegrad | CURRENT_STATE | low | Governance | „Fehlt"-Liste | Fortschritt nicht messbar | durch diesen Adapter-Lauf initialisiert | no |
| SP-F-006 | Keine Work-Package-Struktur | CURRENT_STATE, ROADMAP | medium | Governance | Wunschliste statt Queue | Scope Creep (RISKS #1) | SP-WP-Queue (dieser Lauf) | no |
| SP-F-007 | Roadmap nur im Kopf | ROADMAP | medium | Governance | „keine schriftliche Roadmap" | Prioritäten-Chaos | Queue + Maintainer-Review | no |
| SP-F-008 | Geteilter Admin, keine Rollen | SECURITY_NOTES, CURRENT_STATE | **high** | Security | „eingeloggt = darf alles", geteilter Account | keine Zurechenbarkeit, jeder kann löschen | SP-WP-003 (Baseline), danach Rollen-WP | no |
| SP-F-009 | Secret-Handling ungeklärt | SECURITY_NOTES | **high** | Security | `.env` per Chat geteilt, Pflicht-Variablen unbekannt | Leak-Risiko, unsichere Prod-Starts | SP-WP-003, später fail-closed security-code-fix | no |
| SP-F-010 | Kein Audit-Logging | SECURITY_NOTES | medium | Security | „Ist: keins" | keine Nachvollziehbarkeit | Konzept nach SP-WP-003 | no |
| SP-F-011 | Ungeschützte Notiz-Löschung | SECURITY_NOTES, CURRENT_STATE | **high** | Destructive | sofort, ohne Bestätigung/Backup/Audit/Rolle | irreversibler Datenverlust möglich | SP-WP-005 (**destructive-blueprint**, keine Implementierung) | no |
| SP-F-012 | `reset-db.sh` ungeschützt | MOCK_REPOSITORY_TREE | **high** | Destructive | „ungeschütztes Reset-Skript" | kompletter Datenverlust per Aufruf | im Blueprint SP-WP-005 miterfassen; Status klären | no |
| SP-F-013 | Kein Release-Prozess/Backup | CURRENT_STATE, DEPLOYMENT_NOTES | **high** | Operations | „einfach deployen", Backup „TODO", Rollback „hoffen" | Update kann Daten kosten | Backup-vor-Update-Regel in SP-WP-004 dokumentieren | no |
| SP-F-014 | Konfigquellen doppelt/widersprüchlich | CURRENT_STATE, MOCK_TREE (config.ts vs .env.example) | medium | Maintainability | „teils hart codiert, teils .env, teils beides" | unvorhersehbares Verhalten | Review in SP-WP-001, Fix als späteres code-fix-WP | no |
| SP-F-015 | i18n unentschieden | REQUIREMENTS | low | i18n | „gemischt und unentschieden" | Doku wächst inkonsistent | Maintainer-Entscheidung, dann Doku-WP | no |
| SP-F-016 | Ein-Personen-Wissen | RISKS #7 | medium | Governance | Deployment nur im Kopf des Maintainers | Ausfallrisiko | SP-WP-002 + SP-WP-004 | no |

## Zusammenfassung

16 Findings: 5× high (Security/Destructive/Operations), 8× medium, 3× low. **Kein Finding ist 0.3-blocking** — alle stammen aus dem Fixture und wurden vom Adapter-Prozess wie vorgesehen gefunden; genau das war der Zweck. Beobachtungen über den Adapter selbst stehen im `ADAPTER_VALIDATION_REVIEW_REPORT.md` und im Improvement Backlog.
