# Foundation 0.4 Release Readiness Review (NDF-WP-067)

## DE – Zweck

Ehrliche Prüfung, ob Foundation 0.4 („Adoption Hardening & Public Usability") bereit für die Release-Vorbereitung von `v0.4.0-foundation` ist (NDF-WP-068). Review-only: keine Release Notes, kein Tag, kein GitHub Release durch dieses Work Package. Foundation 0.4 ist damit **nicht** released — geprüft wird nur, ob die Release Prep starten kann.

## EN – Purpose

Honest check whether Foundation 0.4 (the "adoption hardening & public usability" release) is ready for the release preparation of `v0.4.0-foundation` (NDF-WP-068). Review-only: no release notes, no tag, no GitHub release from this work package. Foundation 0.4 is **not** released by this — the review only decides whether release prep may start.

## DE – Geprüfter Scope

Scope-Lock-Einhaltung (Plan, Scope Lock, Queue, Kriterien, Project Brain), Nachweise aller release-blocking WPs, Ehrlichkeit der Release Criteria, Public Quality Gate v0.2 (strict + self-test + Scan-Modus), zehn zentrale öffentliche Einstiegspunkte, relative Links (36 geprüft), Optional-/Deferred-WPs und bekannte Risiken.

Ergebnis der Scope-Prüfung: Foundation 0.4 ist unverändert als Adoption Hardening & Public Usability definiert; der Scope Lock wurde eingehalten (kein Scope Creep — kein neues blocking WP hinzugekommen; WP-064/065 weiterhin deferred, WP-061/062/063/066 weiterhin optional); die Kriterien enthalten keine falschen Haken (nur objektiv Erfülltes ist abgehakt, WP-067/068 offen, Optionale/Deferred klar nicht-blockierend, Invarianten und Go/No-Go-Felder vorhanden); keine v1.0-Behauptung; Foundation 0.4 nirgends als released dargestellt.

## EN – Reviewed Scope

Scope lock compliance, evidence for all release-blocking work packages, honesty of the release criteria, public quality gate v0.2, ten central public entry points, relative links (36 checked), optional/deferred work packages and known risks. Result: adoption-hardening definition intact, scope lock respected (no scope creep), no false checkmarks, no v1.0 claims, 0.4 not shown as released.

## DE – Release-blocking Work Packages

| WP | Status | Nachweis |
|---|---|---|
| NDF-WP-058 Scope Lock | ✅ abgeschlossen | `docs/roadmap/FOUNDATION_0_4_SCOPE_LOCK.md` — blocking/optional/deferred getrennt, Änderungsregeln und WP-060-Downgrade-Ventil definiert |
| NDF-WP-059 Adapter Conventions Polish | ✅ abgeschlossen | `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` — Manifest-, Output-Pfad- und Health-Score-Konvention; Templates/Checkliste/Prompts konsistent; WP-047-Backlog 1–5 als addressed markiert; WP-047-Ergebnis bleibt historisch PASS WITH NOTES |
| NDF-WP-060 Prompt DE/EN Priority Pass | ✅ abgeschlossen | 5 Adoptions-Erstkontakt-Prompts vollständig bilingual (Marker „DE/EN priority pass complete"), 7 Security-/Gate-Prompts DE/EN-Kern; `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md` |
| NDF-WP-067 Readiness Review | ✅ mit diesem Dokument | Entscheidung unten |
| NDF-WP-068 Release Prep | ⬜ offen | nächster Schritt nach GO |

## EN – Release-blocking Work Packages

058, 059 and 060 are complete with verifiable evidence; 067 completes with this document; 068 is the next step.

## DE – Quality Gate Ergebnis / EN – Quality Gate Result

`--strict`: **passed** (0 Fehler, 0 Warnungen, 3 erwartete Notices: Scan-Modus „tracked + new/untracked", fehlende lokale Denylist, Strukturregeln-Hinweis). `--self-test`: **passed**. Der Gate meldet den tracked+new-file-Scan nachvollziehbar; keine Hinweise, die vor der Release Prep gelöst werden müssten.

## DE – Public Neutrality Ergebnis / EN – Public Neutrality Result

Die Standard-Neutralitätsprüfungen (private project/person checks) sind repo-weit sauber; der Public Quality Gate v0.2 prüft neue/untracked Dateien mit (new-file neutrality check). Die konkreten privaten Begriffe stehen bewusst nirgends im Repository, auch nicht in Prüf- oder Release-Dokumenten.

## DE – Adapter Conventions Ergebnis / EN – Adapter Conventions Result

Manifest- (`PROJECT_MANIFEST.md` kanonisch), Output-Pfad- (Validierung vs. produktionsnah, expected ≠ actual) und Health-Score-Konvention (Foundation-0.4-Kategorien mit `unknown`/`n/a`-Regeln) sind geklärt und in Guide, Helper, Checkliste und Templates konsistent verankert. Keine offenen release-blocking Adapter-Findings; die WP-047-Validierungshistorie bleibt unverfälscht.

## DE – Prompt DE/EN Priority Pass Ergebnis / EN – Prompt DE/EN Priority Pass Result

Die fünf Adoptions-Erstkontakt-Prompts (Adapter Intake/Baseline/Create, WP Classification, Boundary Review) sind vollständig DE/EN nutzbar; Rückmeldung an Nova (ChatGPT), Human-Maintainer-Grenzen und Entscheidungslogik (GO/REWORK/SPLIT/STOP) sind erhalten. Die Security-/Gate-Prompts sind ehrlich als DE/EN-Kern dokumentiert; die restliche Prompt Library wird nicht fälschlich als vollständig übersetzt dargestellt.

## DE – Bekannte Nicht-Blocker / EN – Known Non-Blockers

| Punkt | Einstufung |
|---|---|
| WP-061 Checklist DE/EN, WP-062 Academy Entry, WP-063 ADR Policy, WP-066 Gate Maintenance nicht umgesetzt | non-blocking (optional; Reststand transparent, muss in 0.4-Release-Notes als Known Limitation) |
| WP-064 Independent Adapter Validation Run | deferred (nur wenn Unbeteiligte verfügbar) |
| WP-065 Docs Export / Website Concept | deferred (0.5) |
| Vollübersetzung der übrigen Prompt Library | non-blocking (→ 0.5, in `docs/i18n/TRANSLATION_STATUS.md`) |
| Security-/Gate-Prompts nur DE/EN-Kern | non-blocking (ehrlich dokumentiert) |
| GitHub Secret custom denylist muss gesetzt/gepflegt sein | manual follow-up (macht den new-file check in CI scharf) |
| Foundation-0.2-GitHub-Release-Titel-Korrektur | manual follow-up |
| README nennt Foundation 0.4 noch „in Planung" — wird in WP-068 auf Release-Vorbereitung gehoben | non-blocking (Teil der Release Prep, wie bei 0.3/WP-055) |
| Historische Brain-Notes mit alten Statusformulierungen | non-blocking (beschreiben Vergangenheit) |
| Git-Historie bleibt unverändert (History-Rewrite ausgeschlossen) | non-blocking (akzeptiert) |

## DE – Blocker / EN – Blockers

**Keine. / None.**

## DE – Release-Empfehlung / EN – Release Recommendation

```text
GO WITH NOTES
```

Foundation 0.4 ist bereit für die Release-Vorbereitung (NDF-WP-068). Die Notes sind ausschließlich die dokumentierten Nicht-Blocker oben — insbesondere: die offenen optionalen WPs (061/062/063/066) und die i18n-Rückstände müssen in den 0.4-Release-Notes ehrlich als Known Limitations erscheinen, und die beiden manuellen GitHub-Schritte (Secret, 0.2-Titel) sollten spätestens mit dem 0.4-Release erledigt werden. / Ready for release prep; the notes are the documented non-blockers above, which must appear honestly as known limitations in the 0.4 release notes.

## DE – Nächste Schritte / EN – Next Steps

1. **NDF-WP-068 – Foundation 0.4 Release Prep:** Release Notes (inkl. Known Limitations aus den Nicht-Blockern), Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide, Changelog-Umstellung, README-Status.
2. Manuell: GitHub Secret prüfen/setzen; Foundation-0.2-Release-Titel korrigieren.
3. Nach 0.4: optionale WPs 061–063/066, Independent Adapter Run (064), Docs Export/Website Concept (065).
