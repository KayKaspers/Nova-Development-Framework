# Capability Matrix – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

| Capability | Status | Evidence | Risk | Recommended WP |
|---|---|---|---|---|
| Documentation | partial | README/Deployment/Changelog vorhanden, aber lückenhaft und widersprüchlich (SP-F-001/002) | Onboarding und Betrieb hängen am Maintainer | SP-WP-001, SP-WP-004 |
| Deployment | partial | docker-compose vorhanden, Start per `up -d`; Port unklar, kein Rollback | Fehlkonfiguration, Update-Risiko | SP-WP-004 |
| Security | missing | keine Rollen, geteilter Admin, Secrets ungeklärt (SP-F-008/009) | hoch | SP-WP-003 |
| Authentication | partial | Username/Passwort + Session (Brief) — Details not evidenced | schwache Kontrolle, keine 2FA | SP-WP-003 |
| Authorization / roles | missing | „eingeloggt = darf alles" | jeder kann löschen | SP-WP-003, Folge-WP Rollen |
| Audit logging | missing | „Ist: keins" | keine Nachvollziehbarkeit | Konzept nach SP-WP-003 |
| Backup / restore | missing | Backup „TODO", Rollback „hoffen" | Datenverlust bei Update | SP-WP-004 (Regel dokumentieren), später ops-WP |
| Destructive actions | missing (ungeschützt) | Sofort-Löschung, `reset-db.sh` (SP-F-011/012) | irreversibler Verlust | SP-WP-005 (**Blueprint only**) |
| CI / tests | partial | Workflow existiert, rot + ignoriert; Alt-Tests, Abdeckung unknown | Regressionen unbemerkt | ci-diagnostic nach Baseline |
| Release management | missing | kein Prozess, Changelog ungepflegt | unklare Live-Stände (Changelog-Lücke) | SP-WP-004 + späteres release-prep-WP |
| i18n | partial | DE/EN gemischt, unentschieden | inkonsistente Doku | Maintainer-Entscheidung, dann docs-WP |
| Project governance | missing | keine Roadmap/Queue/Kriterien | Scope Creep | durch Adapter-Baseline gestartet |
| Health score | missing → initialized | vor Adapter keiner; initial mit diesem Lauf | Fortschritt war unmessbar | `HEALTH_SCORE.md` pflegen (health-score-update) |
| Work-package workflow | missing → initialized | Wunschliste statt Queue; Queue jetzt initial | unkontrollierte Arbeit | `INITIAL_WORK_PACKAGE_QUEUE.md` nutzen |
