# Foundation 0.2 Release Criteria

> Aktualisiert in WP-041. Ersetzt die ursprünglichen Planungs-Kriterien von 2026-06-29; der tatsächliche 0.2-Scope ist während der Entwicklung gewachsen (Neutralisierung, Quality Gate, i18n). / Updated in WP-041, replacing the original planning criteria; the actual 0.2 scope grew during development.

## Release-Typ

```text
Foundation Stabilization Release (Pre-Release v0.2.0-foundation)
```

## Pflichtkriterien / Required criteria

- [x] Foundation 0.1 ist released/frozen (Tag `v0.1.0-foundation` existiert).
- [x] Foundation 0.2 Scope abgeschlossen (WP-027 bis WP-041 im Changelog nachvollziehbar).
- [x] Public Neutralization done (WP-030: keine privaten Projektnamen im Repository).
- [x] Maintainer Neutralization done (WP-031: keine privaten Personen-/Owner-Namen).
- [x] Public Repository Quality Gate done (WP-032: Script + CI-Workflow, lokal grün).
- [x] Repository Structure Review done (WP-033: Links, ADR-Struktur, History-Trennung).
- [x] Project Adapter v0.2 available (WP-034/035: Guide, Templates, Checkliste, Prompts).
- [x] README DE/EN done (WP-036: vollständig bilingual).
- [x] Nova (ChatGPT) role clarified (WP-037: Rollendokument + Einstiegspunkte).
- [x] Workflow Docs DE/EN improved (WP-038: Kern-Dokumente bilingual).
- [x] Prompt & Checklist DE/EN improved (WP-039: 12 Kern-Prompts, 7 Checklisten).
- [x] Release Readiness Review done (WP-040: GO WITH NOTES, keine Blocker).
- [x] Release Notes vorbereitet (`FOUNDATION_0_2_RELEASE_NOTES.md`).
- [x] Go/No-Go-Checkliste vorbereitet (`FOUNDATION_0_2_GO_NO_GO_CHECKLIST.md`).
- [x] Tagging-/Release-Guide vorbereitet (`FOUNDATION_0_2_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`).

## Bekannte Nicht-Blocker / Known non-blockers

- [ ] Restliche i18n-Arbeiten (übrige Prompts/Checklisten, `GITHUB_DESKTOP_WORKFLOW.md`, Academy) — transparent in `docs/i18n/TRANSLATION_STATUS.md`.
- [ ] ADR-Nummernkollisionen — dokumentierter, eingefrorener Altbestand (`adr/README.md`).
- [ ] Adapter-Praxistest an externem Projekt — nach 0.2.
- [ ] Git-Historie enthält alte Begriffe — History-Rewrite bewusst ausgeschlossen.

## Manuelle Pre-Release-Schritte / Manual pre-release tasks

- [ ] GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen (Maintainer; Inhalt kommagetrennt, Begriffe niemals ins Repo schreiben).
- [x] WP-041-Stand committen und pushen (Human Maintainer).
- [ ] Go/No-Go-Checkliste vollständig durchgehen.
- [x] Tag `v0.2.0-foundation` erstellen und pushen (nur Human Maintainer, siehe Tagging-Guide).
- [x] GitHub Release als **Pre-Release** anlegen (veröffentlicht 2026-07-03; Titel-Korrektur siehe WP-043-Notes).

## Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```
