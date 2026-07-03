# Project Brain – WP-037 Nova Role & Workflow i18n Notes

## Was wurde gemacht?

- **Nova als ChatGPT-Rolle geklärt:** Neues bilinguales Rollendokument `docs/workflow/NOVA_CHATGPT_ROLE.md` (Was ist Nova, was macht Nova (nicht), Verhältnis zu Implementation Agent und Human Maintainer, Grenzen, Beispielablauf).
- **README:** Rollenmodell in DE und EN präzisiert — „Nova (ChatGPT) — die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle" plus Workflow-Kette `Nova (ChatGPT) → Implementation Agent → Human Maintainer` und Link auf das Rollendokument.
- **Workflow-Dokumente:** `ROLES_AND_RESPONSIBILITIES.md` vollständig bilingual (inkl. Umbenennung „Claude – Implementation Assistant" → „Implementation Agent (z. B. Claude)"); `NDF_PRACTICAL_WORKFLOW.md` mit Sprachstatus, Nova-(ChatGPT)-Klarstellung und bilingualem Grundablauf-Kern; `WORK_PACKAGE_STANDARD.md` mit Sprachstatus und Nova-Erklärung bei „Rückmeldung an Nova".
- **Prompts:** Prompt-Index und Prompt-Library-Overview mit Rollenhinweis; beide Adapter-Prompts erklären Nova im Rückmeldungs-Abschnitt.
- **Academy/Beispiele:** „Nova (ChatGPT)" an den Einstiegsstellen (Band-1-README, Rollen-Kapitel, Checkliste, Expansion-Plan, Minimal-Beispiel README + Workflow).

## Kernentscheidung

Nova bleibt ein Rollenname (kein Produktversprechen): Dokumente sagen „Nova steht aktuell für ChatGPT in der Planungs-/Review-Funktion" — so bleibt der Workflow stabil, falls sich das Werkzeug ändert.

## Offene Folgearbeiten

1. Workflow-Docs vollständig DE/EN (GIT_SAFETY, QUALITY_GATES, WORK_PACKAGE_TYPE_INTEGRATION u. a.)
2. Adapter-Praxistest (aus WP-034 offen)
3. ADR Consolidation (aus WP-033 offen)
