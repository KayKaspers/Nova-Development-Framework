# NDF-WP-133 – Foundation 0.9 Post-Release Reconciliation Cleanup (Notes)

## Ziel

Foundation 0.9 nach dem manuellen Release des Human Maintainers auf den Status **released / published — reconciliation documented** heben, den vorhandenen Tag und das GitHub-Pre-Release **read-only** verifizieren und die Sondersituation transparent dokumentieren, dass der Tag-Cut bereits bei WP-126 erfolgte, während WP-127/WP-128 erst danach committet wurden. Kein Tag-Move, kein History-Rewrite, kein Korrektur-Release.

## Input Summary

- Vorgänger: WP-127 (Readiness Review, GO WITH NOTES) und WP-128 (Release Prep) — beide committet (`b268503`).
- Tag `v0.9.0-foundation` und GitHub Pre-Release existierten bereits vor dem Commit von WP-127/128.
- Muster analog zu den Post-Release-Cleanups 043/056/069/083/096/106/119.

## Release-Bestätigung (read-only verifiziert)

- Tag: `v0.9.0-foundation`, **annotated** (`git cat-file -t` → `tag`).
- Tag-Ziel: Commit `e735041` (WP-126) — `git rev-list -n1 v0.9.0-foundation`.
- GitHub Release: „Nova Development Framework v0.9.0 Foundation", **Pre-release** (isPrerelease=true, isDraft=false), Target `main`, published 2026-07-10.
- Public Quality Gate v0.2: grün (`--strict` + `--self-test`).

## Reconciliation-Hinweis

Der Tag-Cut erfolgte am Commit von WP-126 (`e735041`), bevor WP-127 (Readiness Review) und WP-128 (Release Prep) committet waren. WP-127/128 wurden anschließend als `b268503` committet und werden hier **post-release** dokumentiert. Der Release bleibt gültig; die Prep-/Readiness-Artefakte sind inhaltlich vollständig und wurden lediglich nach dem Tag persistiert.

## Tag-Cut-Hinweis

Der veröffentlichte Tag zeigt bewusst auf `e735041` (WP-126) und wird **nicht** auf `b268503` verschoben. Öffentlich genutzte Tags werden gemäß Tagging-Guide-Rollback-Regel nicht verschoben.

## Entscheidung

- **Kein Tag-Move.**
- **Kein History-Rewrite.**
- **Kein neuer Tag.**
- **Kein Korrektur-Release.**
- **Kein Editieren des GitHub Release.**
- Status-Dokumente werden auf released/published gehoben; Go/No-Go-Checkliste und Tagging-Guide werden als historisch markiert.

## Geänderte Dateien

- `docs/release/FOUNDATION_0_9_RELEASE_CRITERIA.md` — Status auf released/published; WP-128/133 als erledigt.
- `docs/release/FOUNDATION_0_9_RELEASE_NOTES.md` — Status auf released/published mit Tag/Commit/Datum.
- `docs/release/FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md` — als historischer Prep-/Governance-Check markiert.
- `docs/release/FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` — als historischer Referenz-Guide markiert.
- `docs/roadmap/FOUNDATION_0_9_PLAN.md` — Statuszeile released/published + Reconciliation-Notiz.
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md` — Banner + WP-128-Zeile + neue WP-133-Zeile.
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md` — Current status + Next WP (WP-125).
- `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md` — Status, Last/Next WP, History, Next Prompt Recommendation.
- `CHANGELOG.md` — `[0.9.0-foundation] - 2026-07-10` veröffentlicht + Reconciliation-Notiz + WP-133-Zeile.
- `project-brain/WP_133_FOUNDATION_0_9_POST_RELEASE_RECONCILIATION_CLEANUP_NOTES.md` — diese Notiz.

## Statuswechsel

Von `release-prepared / pending manual release` auf **`released / published — reconciliation documented`** als `v0.9.0-foundation` (2026-07-10).

## Known Notes

- Foundation 0.9 ist **nicht v1.0**, kein v1.0 Release Candidate; volle v1.x-Kompatibilitätszusage nicht aktiv (ADR-0031).
- **Kein aktives Claude Skills Pack**; Skills bleiben Design/Decision (ADR-0032 bindend, fail-closed).
- WP-125 optional/conditional (nächster empfohlener Blueprint); WP-129/130/131/132 optional, nicht aktiviert.
- v1.0-Pfad gestärkt, aber nicht geschlossen (WP-126).

## Public-Neutrality-Prüfung

Public Quality Gate v0.2 `--strict` + `--self-test` grün; new-file neutrality check aktiv; keine privaten Bezüge, Domains, Suchmuster oder Reviewer-Identitäten. Der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` wird nur genannt; Inhalt niemals ausgegeben.

## ADR-/Governance-Prüfung

ADR-0031 (v1.x Compatibility Policy) und ADR-0032 (Skill Security Policy) bleiben Accepted und unverändert. Nächste freie ADR-Nummer: 0033. Keine autonomen Git-/Release-Aktionen durch Agenten (ADR-0032).

## Skill-Nichtaktivierung

Kein `.claude/skills`, kein `SKILL.md`, keine Scripts angelegt oder aktiviert. WP-125/129/130/131/132 bleiben nicht aktiviert.

## Nächste empfohlene Phase

**NDF-WP-125 – Skills MVP Implementation Blueprint** (docs-only / Blueprint-only, Full Prompt Mode, empfohlenes Modell Claude Opus 4.8; vom Human Maintainer priorisiert). WP-129 erst danach entscheidbar und nicht aktiviert.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

Foundation 0.9 ist als `v0.9.0-foundation` (Pre-Release, 2026-07-10) veröffentlicht und read-only verifiziert; der Status wurde auf released/published — reconciliation documented gehoben. Der Tag-Cut bei WP-126 (`e735041`) ist transparent dokumentiert; WP-127/128 wurden nach dem Tag committet (`b268503`); kein Tag-Move, kein History-Rewrite, kein Korrektur-Release. Nächster empfohlener Schritt: WP-125 (Blueprint-only). Ergebnis: GO WITH NOTES.
