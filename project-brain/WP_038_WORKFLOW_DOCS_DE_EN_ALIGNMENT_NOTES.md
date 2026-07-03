# Project Brain – WP-038 Workflow Docs DE/EN Alignment Notes

## Was wurde gemacht?

- **Vollständig bilingual (DE/EN-Blöcke):** `NDF_PRACTICAL_WORKFLOW.md`, `WORK_PACKAGE_STANDARD.md`, `GIT_SAFETY_STANDARD.md`, `QUALITY_GATES_PRACTICAL.md` — dazu waren `NOVA_CHATGPT_ROLE.md` und `ROLES_AND_RESPONSIBILITIES.md` bereits bilingual (WP-037).
- **Kern gespiegelt:** `WORK_PACKAGE_TYPE_INTEGRATION.md` mit DE-Kurzfassung (Typ-Pflicht, review-only/docs-only/code-fix/security-code-fix, destructive-blueprint vs. -implementation, Health Score separat) + Sprachstatus; EN-Detailteil unverändert.
- **Standards mit deutscher Einleitung:** `WORK_PACKAGE_LIFECYCLE.md`, `WORK_PACKAGE_REVIEW_GATE_STANDARD.md`, `WORK_PACKAGE_TYPES.md` (jeweils Sprachstatus + DE-Einstiegserklärung, englische Fachbegriffe bleiben).
- Inhaltlich beim Spiegeln nachgeschärft: Git Safety enthält jetzt explizit „keine automatischen Commits durch den Implementation Agent", `git status` vor/nach Änderungen, kleine scoped Commits, Force-Push nur nach Freigabe, keine Secrets; Quality Gates verweisen jetzt auf den Public Quality Gate, die Neutralitäts-Greps und das Review-Gate (GO/GO WITH NOTES/REWORK/SPLIT/STOP).
- Interne Links ergänzt: Nova-Rollendokument, WP-Types, WP-Lifecycle, Review-Gate, Public-Quality-Gate-Doku.

## Sprachstatus

`docs/workflow/` = **bilingual** (nur `GITHUB_DESKTOP_WORKFLOW.md` noch de-only; Detailteile von TYPE_INTEGRATION und der drei Standards bleiben EN mit DE-Einleitung).

## Offene i18n-Folgearbeiten

1. `GITHUB_DESKTOP_WORKFLOW.md` EN-Spiegelung (klein)
2. Prompts/Checklisten EN (nächste Matrix-Priorität)
3. `docs/project-starter/` EN

## Nächste empfohlene WPs

1. Prompts + Checklisten DE/EN
2. Adapter-Praxistest (aus WP-034 offen)
3. ADR Consolidation (aus WP-033 offen)
