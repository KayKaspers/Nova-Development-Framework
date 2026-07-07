# Foundation 0.6 Release Readiness Review

## DE – Zweck

Review-Gate (NDF-WP-094) vor der Release-Vorbereitung von voraussichtlich `v0.6.0-foundation`: Prüfung aller release-blocking Kriterien, der WP-088-/WP-089-Notes, des Quality Gates und der öffentlichen Einstiegspunkte. Ergebnis: **GO WITH NOTES**. Foundation 0.6 ist **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**.

## EN – Purpose

Review gate (NDF-WP-094) before the release preparation of presumably `v0.6.0-foundation`: verification of all release-blocking criteria, the WP-088/WP-089 notes, the quality gate, and the public entry points. Result: **GO WITH NOTES**. Foundation 0.6 is **not released**, **not v1.0**, and **no v1.0 release candidate**.

## DE – Geprüfter Scope

Scope Lock (NDF-WP-085) eingehalten: Adoption Confidence & Governance Hardening, blocking Kern 085/086/088/089/094/095, optionale 087/090–093, deferred Website/i18n/ADR-Migration/v1.0-RC/Rewrite. Kein Scope Creep — kein WP außerhalb des Korridors; das WP-088-Ventil wurde definiert, aber **nicht benötigt**; die ADR-Entscheidungspflicht wurde erfüllt statt umgangen. Keine falschen Haken in den Release Criteria; 0.6 nirgends als released, v1.0 nirgends als erreicht dargestellt (Kontroll-Greps sauber, nur Negationen).

## EN – Reviewed Scope

Scope lock honored: blocking core 085/086/088/089/094/095, optional 087/090–093, deferred items intact; no scope creep; the WP-088 valve was defined but **not needed**; the ADR decision duty was fulfilled, not circumvented. No false checkmarks; 0.6 nowhere claimed as released, v1.0 nowhere claimed as reached.

## DE – Release-blocking Work Packages / EN – Release-blocking Work Packages

| WP | Status | Nachweis / Evidence |
|---|---|---|
| NDF-WP-085 Scope Lock | ✅ done | `FOUNDATION_0_6_SCOPE_LOCK.md` — blocking/optional/deferred getrennt, ADR-Entscheidungspflicht, 8-Bedingungen-Ventil für WP-088, WP-090 conditional, Änderungsregeln, kein v1.0-Claim |
| NDF-WP-086 ADR Policy Decision | ✅ done — **Minimal ADR Policy adopted** | `docs/adr/ADR_POLICY.md` (Status Accepted) + Template + Index-Update; Entscheidung getroffen statt verschoben; Massenmigration ausdrücklich nicht durchgeführt; Nummernkollision als historischer Zustand dokumentiert; neue Regel ab ADR-0031 konsistent |
| NDF-WP-088 Public Validation Run | ✅ done — **PASS WITH NOTES** | `independent-runs/2026-07-07-public-sampleproject-runbook-validation/` (5 Dateien inkl. Runbook Execution Summary) — öffentlicher SampleProject-/Runbook-Kontext, Independent Reviewer neutral dokumentiert, keine Blocker/High-Findings, Ventil nicht benötigt, WP-087 skipped |
| NDF-WP-089 Gate Maintenance Review | ✅ done — **Evidence strong** | `docs/quality/PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md` — strict/self-test grün, New-file-Scan per synthetischem Lokaltest bewiesen, Secret-Integration sauber bewertet (ohne Wert), keine Script-/CI-Änderung nötig, WP-090 not needed |
| NDF-WP-094 Readiness Review | ✅ mit diesem Dokument / with this document | — |
| NDF-WP-095 Release Prep | ⬜ offen / open | nächster Schritt nach GO / next step after GO |

## DE – Quality Gate Ergebnis

`--strict`: **passed** (0 errors, 0 warnings, 3 INFO-Notices — Scan-Modus, lokal keine Denylist; das Secret wirkt in CI). `--self-test`: **passed**. New-file neutrality check aktiv; die in diesem Review erzeugten Dateien wurden vom Gate selbst mitgescannt. Nichts davon muss vor der Release Prep gelöst werden.

## EN – Quality Gate Result

Strict: passed (0/0, 3 INFO notices only); self-test: passed; new-file neutrality check active — the files created by this review were scanned by the gate itself. Nothing requires resolution before release prep.

## DE – Public Neutrality Ergebnis

Kontroll-Prüfungen sauber: keine privaten Projekt-/Personennamen, keine Reviewer-Identitäten, keine Kontakte/Domains/Secret-Werte in getrackten Dateien; beide Validierungsläufe (0.5 privat-neutralisiert, 0.6 öffentlich) durchgehend neutral dokumentiert. Relative Links aller zentralen Einstiegsdokumente vollständig auflösbar (temporärer Link-Check über 10 Dateien, 0 broken, nichts committet).

## EN – Public Neutrality Result

Control checks clean: no private names, reviewer identities, contacts, domains, or secret values; both validation runs documented neutrally throughout. Relative links of all central entry documents fully resolvable (temporary link check across 10 files, 0 broken).

## DE – Adoption Confidence Ergebnis

Die erste Leitideen-Hälfte ist erfüllt: Die öffentliche SampleProject-/Runbook-Validierung wurde durch einen unabhängigen technischen Reviewer **positiv bestätigt** (PASS WITH NOTES, keine Blocker/High-Findings, keine Must-/Should-Fixes) — damit ist die 0.5-Known-Limitation (privater statt öffentlicher Kontext) geschlossen. Ehrliche Einordnung der Note (PSV-001): Die per-Schritt-Belege des Runbook-Laufs liegen nicht vollständig vor — non-blocking, aber Pflicht-Known-Limitation für die WP-095-Release-Notes; v1.0-tracked als evidence-quality note.

## EN – Adoption Confidence Result

The first half of the theme is fulfilled: the public SampleProject / runbook validation was **positively confirmed** by an independent technical reviewer (PASS WITH NOTES, no blockers/high findings, no must/should fixes) — closing the 0.5 known limitation. Honest classification of the note (PSV-001): per-step runbook evidence is not fully provided — non-blocking, but a mandatory known limitation for the WP-095 release notes; v1.0-tracked as an evidence-quality note.

## DE – Governance Hardening Ergebnis

Die zweite Leitideen-Hälfte ist erfüllt: Die ADR-Policy wurde **entschieden statt zum dritten Mal verschoben** — Minimal ADR Policy adopted (Wann-ADR/Wann-Note, Ablage nur `docs/adr/`, Nummerierung über beide Ordner ab ADR-0031, Statuswerte, Rollen, Supersede-Regel, ausdrücklich keine Massenmigration). Der Dauerläufer aus 0.4/0.5 ist geschlossen; die Alt-Nummernkollision bleibt dokumentierter historischer Zustand.

## EN – Governance Hardening Result

The second half is fulfilled: the ADR policy was **decided instead of deferred a third time** — minimal ADR policy adopted (when-ADR/when-note, location `docs/adr/` only, cross-folder numbering from ADR-0031, status values, roles, supersede rule, explicitly no mass migration). The 0.4/0.5 carry-over is closed; the legacy numbering collision stays a documented historical state.

## DE – Public Quality Gate Maintenance Ergebnis

Erstes Gate-Wartungsreview seit v0.2 erfolgreich: alle 10 Script-Prüfpunkte grün, CI-Verdrahtung sauber (Self-Test-Schritt + Strict-Schritt mit Secret via `env`, Fallback dokumentiert), **CI-Denylist-Wirksamkeit mit Evidence-Level strong** — inkl. kontrolliertem synthetischem Lokaltest (erwarteter FAIL mit New-file-Erkennung, sauberes Cleanup, wieder grün). **WP-090 not needed.** Note (QGM-003, low/non-blocking): Bei einem echten Treffer druckt der Gate den gefundenen Begriff im ERROR — in CI-Logs sichtbar; der Begriff wäre dann aber ohnehin bereits in der Repo-Datei öffentlich. Operative Erwartung: Verstoß sofort beheben.

## EN – Public Quality Gate Maintenance Result

First gate maintenance review since v0.2 succeeded: all 10 script checks green, CI wiring clean, **CI denylist effectiveness at evidence level strong** including a controlled synthetic local test. **WP-090 not needed.** Note (QGM-003, low/non-blocking): on a real hit the gate prints the matched term in the ERROR — visible in CI logs; at that point the term is already public in the repo file itself. Operational expectation: fix any real violation immediately.

## DE – v1.0 Path Ergebnis

Alle drei 0.6-Beiträge korrekt und ohne Überhöhung eingearbeitet: **ADR/Decision Structure** `met with notes` (Policy adopted, Migration deferred, Bewährung offen); **External Validation** `met with notes` (öffentlicher Lauf bestätigt; Note = Nachweis-Tiefe); **Public Quality Gate & Neutralität** `met` inkl. des jetzt geschlossenen CI-Wirksamkeits-Prüfpunkts. Offene v1.0-Kriterien bleiben sichtbar (v1.x-Kompatibilitätszusage, Konventions-Stabilität über weitere Releases). Foundation 0.6 **reduziert v1.0-Unsicherheit — mehr nicht**; nirgends wird v1.0 als erreicht dargestellt.

## EN – v1.0 Path Result

All three 0.6 contributions incorporated correctly and without inflation: ADR/decision structure `met with notes`; external validation `met with notes`; public quality gate & neutrality `met` including the now-closed CI effectiveness spot-check. Open v1.0 criteria stay visible (v1.x compatibility promise, convention stability). Foundation 0.6 **reduces v1.0 uncertainty — nothing more**.

## DE – Optionale, übersprungene und deferred Work Packages

Keines blockiert:

- **WP-087** skipped/not needed (Lauf direkt mit WP-073-Unterlagen) · **WP-090** not needed (Nachweis in WP-089 erbracht) — beide sauber begründet dokumentiert.
- **WP-091 Checklist DE/EN, WP-092 Academy Entry, WP-093 v1.x Compatibility Policy Draft:** optional offen → Known-Limitation-Kandidaten. Hinweis für die 0.7-Planung: WP-091 (Checklist DE/EN) ist seit 0.4 zum dritten Mal optional offen — analog zur früheren ADR-Regel sollte 0.7 eine Priorisieren-oder-Streichen-Entscheidung erwägen; WP-093 bleibt der natürliche erste ADR-0031-Kandidat.
- **Deferred:** Website, volle i18n, ADR-Massenmigration, v1.0-RC, Rewrite, App-Features — unverändert.

## EN – Optional, Skipped and Deferred Work Packages

None blocks: WP-087 skipped, WP-090 not needed (both documented with rationale); WP-091/092/093 optional open → known-limitation candidates (note for 0.7 planning: WP-091 is optional-open for the third time since 0.4 — 0.7 should consider a prioritize-or-drop decision analogous to the former ADR rule; WP-093 stays the natural first ADR-0031 candidate); deferred items unchanged.

## DE – Bekannte Nicht-Blocker / EN – Known Non-Blockers

| Punkt / Item | Einstufung / Classification |
|---|---|
| WP-088 PASS WITH NOTES statt PASS (per-Schritt-Belege begrenzt, PSV-001) | non-blocking → Known Limitation in Release Notes; **v1.0-tracked** (evidence-quality note) |
| WP-089 QGM-003: Gate-ERROR kann bei echtem Treffer den Begriff im CI-Log zeigen | non-blocking → **operational note** in Release Notes (Verstoß sofort beheben) |
| ADR-Massenmigration bleibt deferred; Alt-Nummernkollision bleibt historischer Zustand | deferred / dokumentiert → Known Limitation |
| WP-091 Checklist DE/EN optional offen (drittes Mal) | non-blocking → Known Limitation + 0.7-Hinweis (priorisieren oder streichen erwägen) |
| WP-092 Academy Entry optional offen | non-blocking → Known Limitation |
| WP-093 v1.x Compatibility Policy Draft optional offen | non-blocking → Known Limitation; **v1.0-tracked** (bewusste Lücke) |
| Volle Doku-Website / volle i18n / v1.0-RC / Rewrite | deferred |
| Foundation 0.6 ist nicht v1.0 | Invariante, überall korrekt |
| Foundation 0.6 ist noch nicht released | korrekt in allen Einstiegspunkten |

## DE – Blocker

**Keine.** Alle release-blocking Kriterien außer WP-094 (dieses Dokument) und WP-095 sind erfüllt und nachgewiesen.

## EN – Blockers

**None.** All release-blocking criteria except WP-094 (this document) and WP-095 are met and evidenced.

## DE – Release-Empfehlung

**GO WITH NOTES.** Foundation 0.6 ist bereit für die Release-Vorbereitung (NDF-WP-095). Die Notes sind ausschließlich non-blocking: PSV-001 und QGM-003 (Pflicht-Known-Limitations für die Release Notes), die offenen optionalen WPs 091–093 und die deferred Punkte. Der WP-091-Hinweis (drittes optional-offen) gehört als Empfehlung in die 0.7-Planung.

## EN – Release Recommendation

**GO WITH NOTES.** Foundation 0.6 is ready for release preparation (NDF-WP-095). The notes are exclusively non-blocking: PSV-001 and QGM-003 (mandatory known limitations for the release notes), the open optional WPs 091–093, and the deferred items. The WP-091 note (third time optional-open) belongs in 0.7 planning as a recommendation.

## DE – Nächste Schritte

1. **NDF-WP-095 – Foundation 0.6 Release Prep:** Release Notes (inkl. PSV-001, QGM-003 und aller Known Limitations aus diesem Review), Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für voraussichtlich `v0.6.0-foundation`, Changelog-Umstellung, README-Status.
2. Danach manuell (Human Maintainer): Go/No-Go, Tag, GitHub Pre-Release; anschließend Post-Release-Cleanup-WP.
3. In der 0.7-Planung: WP-091-Entscheidung erwägen; WP-093 als ADR-0031-Kandidat; verbleibende v1.0-Kriterien (v1.x-Zusage, Konventions-Stabilität).

## EN – Next Steps

(1) NDF-WP-095 release prep (release notes incl. PSV-001, QGM-003 and all known limitations from this review, criteria completion, go/no-go checklist, tagging guide for presumably `v0.6.0-foundation`, changelog, README status); (2) then manually: go/no-go, tag, GitHub pre-release, followed by the post-release cleanup work package; (3) in 0.7 planning: consider the WP-091 decision, WP-093 as the ADR-0031 candidate, and the remaining v1.0 criteria.
