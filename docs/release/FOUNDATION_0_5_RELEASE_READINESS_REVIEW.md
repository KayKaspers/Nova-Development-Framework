# Foundation 0.5 Release Readiness Review

## DE – Zweck

Review-Gate (NDF-WP-081) vor der Release-Vorbereitung von `v0.5.0-foundation`: Prüfung aller release-blocking Kriterien, der WP-074-Notes, des Quality Gates und der öffentlichen Einstiegspunkte. Ergebnis: **GO WITH NOTES**. Foundation 0.5 ist **nicht released** und **nicht v1.0**.

## EN – Purpose

Review gate (NDF-WP-081) before the `v0.5.0-foundation` release preparation: verification of all release-blocking criteria, the WP-074 notes, the quality gate, and the public entry points. Result: **GO WITH NOTES**. Foundation 0.5 is **not released** and **not v1.0**.

## DE – Geprüfter Scope

Scope Lock (NDF-WP-072) eingehalten: External Validation & 1.0 Path Hardening, kleiner blocking Kern (072/073/074/079/081/082), 075–078 optional, 080 deferred. Kein Scope Creep — kein WP außerhalb des Korridors gestartet; das WP-074-Downgrade-Ventil wurde definiert, aber **nicht benötigt**. Keine falschen Haken in den Release Criteria gefunden; 0.5 nirgends als released, v1.0 nirgends als erreicht dargestellt (Kontroll-Greps sauber, nur Negationen).

## EN – Reviewed Scope

Scope lock honored: small blocking core, optional 075–078, deferred 080, no scope creep; the WP-074 downgrade valve was defined but **not needed**. No false checkmarks in the release criteria; 0.5 nowhere claimed as released, v1.0 nowhere claimed as reached (control greps clean, negations only).

## DE – Release-blocking Work Packages / EN – Release-blocking Work Packages

| WP | Status | Nachweis / Evidence |
|---|---|---|
| NDF-WP-072 Scope Lock | ✅ done | `FOUNDATION_0_5_SCOPE_LOCK.md` — blocking/optional/deferred getrennt, 8-Bedingungen-Ventil, Änderungsregeln, kein v1.0-Claim |
| NDF-WP-073 Validation Preparation | ✅ done | alle 6 Unterlagen vorhanden (Preparation, Runbook, Brief, Feedback-/Outreach-Template, Ergebnisort) — sofort ausführbarer Plan; WP-074 nicht vorweggenommen |
| NDF-WP-074 Validation Run | ✅ done — **PASS WITH NOTES** | `independent-runs/2026-07-06-private-reference-validation/` — echter unabhängiger Review, neutralisiert dokumentiert, keine Blocker/High-Findings, `not provided`-Felder ehrlich, Ventil nicht benötigt |
| NDF-WP-079 v1.0 Criteria Draft | ✅ done | `V1_0_READINESS_CRITERIA_DRAFT.md` (12 Kategorien, prüfbare Tabellen, ehrliche Statuswerte) + `V1_0_PATH_SUMMARY.md`; External Validation korrekt nur `partially met`; kein v1.0-Claim |
| NDF-WP-081 Readiness Review | ✅ mit diesem Dokument / with this document | — |
| NDF-WP-082 Release Prep | ⬜ offen / open | nächster Schritt nach GO / next step after GO |

## DE – Quality Gate Ergebnis

`--strict`: **passed** (0 errors, 0 warnings, 3 notices — nur INFO: Scan-Modus, keine lokale Denylist konfiguriert; das Secret wirkt in CI). `--self-test`: **passed**. New-file neutrality check aktiv (tracked + untracked). Nichts davon muss vor der Release Prep gelöst werden.

## EN – Quality Gate Result

`--strict`: **passed** (0 errors, 0 warnings, 3 INFO notices only); `--self-test`: **passed**; new-file neutrality check active. Nothing requires resolution before release prep.

## DE – Public Neutrality Ergebnis

Kontroll-Prüfungen sauber: keine privaten Projekt-/Personennamen, keine Reviewer-Identität, keine Kontakte/Domains/Secret-Werte in getrackten Dateien; der private Referenzkontext aus WP-074 ist durchgehend neutralisiert („independent technical reviewer", „private reference context"). Relative Links der zentralen Einstiegsdokumente vollständig auflösbar (temporärer Link-Check, 0 broken, nichts committet).

## EN – Public Neutrality Result

Control checks clean: no private project/person names, no reviewer identity, no contacts/domains/secret values; the WP-074 private reference context is neutralized throughout. Relative links of the central entry documents fully resolvable (temporary link check, 0 broken, nothing committed).

## DE – External Validation Ergebnis

Die External-Validation-Hälfte ist erfüllt: Vorbereitung vollständig (WP-073), Lauf durchgeführt und ausgewertet (WP-074, PASS WITH NOTES). Ehrliche Einordnung der Notes: Die Rückmeldung war **echt unabhängig, positiv und blockerfrei** — das erfüllt den Kern des Kriteriums (externe Sicht außerhalb der Rollenkette). Sie war aber **summarisch/neutralisiert** und **kein vollständiger Runbook-Lauf gegen das öffentliche SampleProject-Fixture**. Beide Punkte sind non-blocking für 0.5, gehören aber als Known Limitations in die 0.5-Release-Notes und bleiben v1.0-tracked (öffentlicher Fixture-Lauf = Kandidat für Foundation 0.6).

## EN – External Validation Result

The external-validation half is fulfilled: preparation complete (WP-073), run performed and evaluated (WP-074, PASS WITH NOTES). Honest classification: the feedback was **genuinely independent, positive, and blocker-free** — fulfilling the core of the criterion — but **summarized/neutralized** and **not a full runbook walk against the public SampleProject fixture**. Both points are non-blocking for 0.5, belong in the 0.5 release notes as known limitations, and stay v1.0-tracked (public fixture run = Foundation 0.6 candidate).

## DE – v1.0 Path Hardening Ergebnis

Die zweite Titel-Hälfte ist erfüllt: messbarer Kriterien-Entwurf (12 Kategorien, blocking/tracked-Trennung, Nachweis-Spalten, ehrliche `not met`-Einträge inkl. der bewussten Lücke „v1.x-Kompatibilitätszusage") plus Path Summary. Das WP-074-Ergebnis wurde korrekt eingearbeitet (`partially met`, nicht überhöht). Kein v1.0-Claim, kein Release Candidate, keine Termine — mehrfach absichert an allen Einstiegspunkten.

## EN – v1.0 Path Hardening Result

The second half is fulfilled: a measurable criteria draft (12 categories, blocking/tracked separation, evidence columns, honest `not met` entries including the deliberate "v1.x compatibility promise" gap) plus the path summary. The WP-074 result was incorporated correctly (`partially met`, not inflated). No v1.0 claim, no release candidate, no dates.

## DE – Optionale und deferred Work Packages

Keines muss vor der Release Prep erledigt werden:

- **WP-075 Checklist DE/EN, WP-077 Academy Entry, WP-078 Gate Maintenance:** optional, transparent dokumentiert → Known-Limitation-Kandidaten für die Release Notes. Bei WP-078 bleibt der empfohlene Prüfpunkt (CI-Denylist-Wirksamkeit mit gesetztem Secret) offen — non-blocking, solange der Gate grün ist.
- **WP-076 ADR Policy:** optional, aber mit **Sonderregel aus dem Scope Lock**: Da WP-076 in 0.5 unerledigt bleibt, gilt verbindlich — **in Foundation 0.6 priorisieren oder ehrlich streichen**; ein drittes stilles Verschieben ist unzulässig. Diese Feststellung ist Teil dieses Reviews und muss in Release Notes und 0.6-Planung erscheinen.
- **WP-080 Docs Export / Website Concept:** bleibt deferred (kein 0.5-Kernziel hängt daran).

## EN – Optional and Deferred Work Packages

None must be done before release prep: WP-075/077/078 stay optional (known-limitation candidates; the WP-078 CI-denylist effectiveness check stays open, non-blocking while the gate is green). **WP-076 ADR policy:** since it remains undone in 0.5, the scope-lock special rule now binds — **prioritize in Foundation 0.6 or drop honestly**; a third silent carry-over is not allowed. This finding is part of this review and must appear in the release notes and 0.6 planning. WP-080 stays deferred.

## DE – Bekannte Nicht-Blocker / EN – Known Non-Blockers

| Punkt / Item | Einstufung / Classification |
|---|---|
| WP-074 PASS WITH NOTES statt PASS (summarisch/neutralisiert) | non-blocking → Known Limitation in Release Notes |
| WP-074 nutzte privaten Referenzkontext, kein öffentlicher Fixture-/Runbook-Lauf | non-blocking → Known Limitation; **v1.0-tracked**, Foundation-0.6-Kandidat |
| External Validation im v1.0-Draft nur `partially met` | v1.0-tracked (korrekt so) |
| WP-075 Checklist DE/EN offen | non-blocking → Known Limitation |
| WP-076 ADR Policy offen | non-blocking → Known Limitation **+ verbindliche 0.6-Regel: priorisieren oder streichen** |
| WP-077 Academy Entry offen | non-blocking → Known Limitation |
| WP-078 Gate Maintenance offen (inkl. CI-Denylist-Wirksamkeitsnachweis) | non-blocking → Known Limitation |
| WP-080 Docs Export / Website Concept | deferred |
| Restliche i18n-Arbeit; Security-/Gate-Prompts teils nur DE/EN-Kern | non-blocking → Known Limitation (Stand: `docs/i18n/TRANSLATION_STATUS.md`) |
| v1.x-Kompatibilitätszusage offen | v1.0-tracked (bewusste Lücke, gehört in den v1.0 Scope Lock) |
| Foundation 0.5 ist nicht v1.0 | Invariante, überall korrekt ausgewiesen |
| Git-Historie bleibt unverändert | Invariante |

## DE – Blocker

**Keine.** Alle release-blocking Kriterien außer WP-081 (dieses Dokument) und WP-082 sind erfüllt und nachgewiesen.

## EN – Blockers

**None.** All release-blocking criteria except WP-081 (this document) and WP-082 are met and evidenced.

## DE – Release-Empfehlung

**GO WITH NOTES.** Foundation 0.5 ist bereit für die Release-Vorbereitung (NDF-WP-082). Die Notes sind ausschließlich non-blocking: die WP-074-Einschränkungen (summarisch, privater Referenzkontext) und die offenen optionalen WPs — alle müssen als Known Limitations in den 0.5-Release-Notes erscheinen, und die WP-076-Regel (0.6: priorisieren oder streichen) muss in die 0.6-Planung.

## EN – Release Recommendation

**GO WITH NOTES.** Foundation 0.5 is ready for release preparation (NDF-WP-082). The notes are exclusively non-blocking: the WP-074 limitations and the open optional work packages — all must appear as known limitations in the 0.5 release notes, and the WP-076 rule (0.6: prioritize or drop) must enter the 0.6 planning.

## DE – Nächste Schritte

1. **NDF-WP-082 – Foundation 0.5 Release Prep:** Release Notes (inkl. der Known Limitations aus diesem Review), Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für `v0.5.0-foundation`, Changelog-Umstellung, README-Status.
2. Danach manuell (Human Maintainer): Go/No-Go, Tag, GitHub Pre-Release.
3. In der 0.6-Planung: WP-076-Entscheidung (priorisieren oder streichen) und öffentlicher Fixture-/Runbook-Lauf als Kandidaten.

## EN – Next Steps

(1) NDF-WP-082 release prep (release notes incl. the known limitations from this review, criteria completion, go/no-go checklist, tagging guide, changelog, README status); (2) then manually: go/no-go, tag, GitHub pre-release by the human maintainer; (3) in 0.6 planning: the WP-076 decision and the public fixture/runbook run as candidates.
