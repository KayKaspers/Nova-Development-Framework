# Foundation 0.7 Release Readiness Review

## DE – Zweck

Review-Gate (NDF-WP-104) vor der Release-Vorbereitung von voraussichtlich `v0.7.0-foundation`: Prüfung aller release-blocking Kriterien, der WP-099-/WP-100-/WP-101-Ergebnisse, des Quality Gates, der Kompatibilitäts-Governance, der Konventions-Stabilität und der öffentlichen Einstiegspunkte. Ergebnis: **GO WITH NOTES**. Foundation 0.7 ist **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**.

## EN – Purpose

Review gate (NDF-WP-104) before the release preparation of presumably `v0.7.0-foundation`: verification of all release-blocking criteria, the WP-099/WP-100/WP-101 results, the quality gate, compatibility governance, convention stability, and the public entry points. Result: **GO WITH NOTES**. Foundation 0.7 is **not released**, **not v1.0**, and **no v1.0 release candidate**.

## DE – Geprüfter Scope

Scope Lock (NDF-WP-098) eingehalten: Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance, blocking Kern 098/099/100/101/104/105, optionale 102 (mit Upgrade-Ventil)/103/Doku-i18n-Konsolidierung, deferred Website/volle i18n/ADR-Massenmigration/v1.0-RC/Rewrite/App-Features. Kein Scope Creep — kein WP außerhalb des Korridors; das WP-102-Upgrade-Ventil wurde definiert, aber **nicht gezogen**; die Checklist-DE/EN-Entscheidung (WP-099) wurde getroffen statt zum vierten Mal verschoben. Keine falschen Haken in den Release Criteria; 0.7 nirgends als released, v1.0 nirgends als erreicht dargestellt (Kontroll-Greps sauber, nur Negationen/„erst mit v1.0").

## EN – Reviewed Scope

Scope lock (NDF-WP-098) honored: blocking core 098/099/100/101/104/105, optional 102 (with upgrade valve)/103/doc-i18n consolidation, deferred website/full i18n/ADR mass migration/v1.0-RC/rewrite/app features. No scope creep; the WP-102 upgrade valve was defined but **not pulled**; the checklist DE/EN decision (WP-099) was made instead of deferred a fourth time. No false checkmarks; 0.7 nowhere claimed as released, v1.0 nowhere claimed as reached.

## DE – Release-blocking Work Packages / EN – Release-blocking Work Packages

| WP | Status | Nachweis / Evidence |
|---|---|---|
| NDF-WP-098 Scope Lock | ✅ done | `FOUNDATION_0_7_SCOPE_LOCK.md` — blocking/optional/deferred getrennt, WP-102-Upgrade-Ventil, WP-099-Entscheidungskorridor, WP-100 ADR-0031 bevorzugt, Änderungsregeln, kein v1.0-Claim |
| NDF-WP-099 Checklist DE/EN Decision | ✅ done — **Option B (optional mit finaler Begründung)** | `FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md` + `docs/i18n/TRANSLATION_STATUS.md` — eindeutige Entscheidung, kein Auto-Carry mehr, kein Folge-WP; Restlücken bleiben als ehrlicher optionaler i18n-Backlog sichtbar; blockiert 0.7 nicht |
| NDF-WP-100 v1.x Compatibility Policy | ✅ done — **ADR-0031 Accepted** | `docs/adr/ADR-0031-v1x-compatibility-policy.md` (Status Accepted) + Index-Update; Source of Truth, keine separate Policy-Datei; volle v1.x-Zusage aktiviert **erst mit v1.0**; v1.0-Kriterium `met with notes`; nächste freie ADR-Nummer 0032 |
| NDF-WP-101 Convention Stability Review | ✅ done — **Stable with notes** | `PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md` — Adapter-Konventionen seit WP-059 über 0.4→0.7 unverändert; ein low-Drift (`.yaml`→`.md`) korrigiert; keine high/blocker Findings; Adapter-Maturity/Convention-Stability `met with notes` |
| NDF-WP-104 Readiness Review | ✅ mit diesem Dokument / with this document | — |
| NDF-WP-105 Release Prep | ⬜ offen / open | nächster Schritt nach GO / next step after GO |

## DE – Quality Gate Ergebnis

`--strict`: **passed** (0 errors, 0 warnings, 3 INFO-Notices — Scan-Modus, lokal keine Denylist konfiguriert; das Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` wirkt in CI). `--self-test`: **passed**. New-file neutrality check aktiv; die in diesem Review erzeugten Dateien wurden vom Gate selbst mitgescannt. Nichts davon muss vor der Release Prep gelöst werden.

## EN – Quality Gate Result

Strict: passed (0/0, 3 INFO notices only — scan mode, no local denylist; the secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` acts in CI); self-test: passed; new-file neutrality check active — the files created by this review were scanned by the gate itself. Nothing requires resolution before release prep.

## DE – Public Neutrality Ergebnis

Kontroll-Prüfungen sauber: keine privaten Projekt-/Personennamen, keine Reviewer-Identitäten, keine Kontakte/Domains/Secret-Werte in getrackten Dateien; die neutralen Rollenbegriffe (Nova (ChatGPT), Implementation Agent, Human Maintainer, Independent Validator, public SampleProject) bleiben durchgehend gewahrt. Relative Links aller zentralen Einstiegsdokumente vollständig auflösbar (temporärer Link-Check über die 9 Kern-Dateien, 0 broken, nichts committet).

## EN – Public Neutrality Result

Control checks clean: no private names, reviewer identities, contacts, domains, or secret values in tracked files; neutral role terms preserved throughout. Relative links of all central entry documents fully resolvable (temporary link check across the 9 core files, 0 broken, nothing committed).

## DE – Compatibility Governance Ergebnis

Die Governance-Hälfte des Arbeitstitels ist erfüllt: Die v1.x-Kompatibilitätspolicy wurde **entschieden statt vertagt** — ADR-0031 (Status Accepted) definiert fünf Kompatibilitätskategorien (Stable Candidate / Governed / Experimental / Deprecated / Out of Scope) und ist die Single Source of Truth (keine separate Policy-Datei nötig). Zentrale Abgrenzung korrekt gewahrt: „Die volle v1.x-Kompatibilitätszusage tritt erst mit einem späteren v1.0-Release in Kraft." — sie wird nirgends als bereits aktiv dargestellt. Das zuvor als `not met` geführte v1.0-Kriterium steht jetzt ehrlich auf `met with notes`.

## EN – Compatibility Governance Result

The governance half of the working title is fulfilled: the v1.x compatibility policy was **decided instead of deferred** — ADR-0031 (Accepted) defines five compatibility categories and is the single source of truth (no separate policy file needed). The key boundary holds: the full v1.x compatibility promise activates only with a future v1.0 release — nowhere presented as already active. The previously `not met` v1.0 criterion is now honestly `met with notes`.

## DE – Convention Stability Ergebnis

Die Consolidation-Hälfte des Arbeitstitels ist erfüllt: Die Project-Adapter-Konventions-Stabilität wurde als **Stable with notes** bestätigt. Kernbeleg ist die Git-Historie — `PROJECT_ADAPTER_CONVENTIONS.md` ist seit WP-059 (Foundation 0.4) über vier Releases (0.4/0.5/0.6 released, 0.7 gelockt) unverändert. Ein einziger low-Drift (stale `PROJECT_MANIFEST.yaml`-Referenzen → kanonisches `.md`) wurde als redaktionelle Statusklarstellung korrigiert; keine high/blocker Findings. Ehrliche Note (PCS-001): „stable" ist ausdrücklich **nicht** „frozen forever" — künftige Änderungen bleiben über ADR-0031 governed. Kriterium Adapter-Maturity/Convention-Stability von `partially met` auf `met with notes`.

## EN – Convention Stability Result

The consolidation half of the working title is fulfilled: adapter convention stability confirmed as **Stable with notes**. The core evidence is git history — `PROJECT_ADAPTER_CONVENTIONS.md` unchanged since WP-059 (Foundation 0.4) across four releases. One low drift (stale `PROJECT_MANIFEST.yaml` references → canonical `.md`) fixed as an editorial status clarification; no high/blocker findings. Honest note (PCS-001): "stable" is explicitly **not** "frozen forever" — future changes stay governed by ADR-0031. The adapter-maturity/convention-stability criterion moves from `partially met` to `met with notes`.

## DE – v1.0 Path Ergebnis

Alle drei 0.7-Beiträge korrekt und ohne Überhöhung eingearbeitet: **Checklist DE/EN** (WP-099) als Option B ehrlich als optionaler i18n-Backlog eingeordnet — kein v1.0-Blocker; **v1.x-Kompatibilität** (WP-100) `met with notes` mit ADR-0031 als Beleg; **Adapter-Maturity/Convention-Stability** (WP-101) `met with notes` mit der Git-Historie als Beleg. Die `met with notes`-Aussagen sind jeweils mit konkreter Evidenz begründet. Offene v1.0-Kriterien bleiben sichtbar (u. a. Evidenz-Tiefe der externen Validierung, PSV-001). Foundation 0.7 **konsolidiert den v1.0-Pfad — mehr nicht**; nirgends wird v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv dargestellt.

## EN – v1.0 Path Result

All three 0.7 contributions incorporated correctly and without inflation: checklist DE/EN (WP-099) honestly classified as an optional i18n backlog (no v1.0 blocker); v1.x compatibility (WP-100) `met with notes` evidenced by ADR-0031; adapter maturity/convention stability (WP-101) `met with notes` evidenced by git history. Each `met with notes` statement is backed by concrete evidence. Open v1.0 criteria stay visible (notably external-validation evidence depth, PSV-001). Foundation 0.7 **consolidates the v1.0 path — nothing more**; nowhere is v1.0 claimed as reached or a full v1.x promise shown as active.

## DE – Optionale und deferred Work Packages

Keines blockiert:

- **WP-102 External Validation Evidence Depth Pass:** optional, **nicht aktiviert** — das Upgrade-Ventil (nur per Human-Maintainer-Scope-Change) wurde nicht gezogen; adressiert PSV-001, bleibt sonst non-blocking und v1.0-tracked.
- **WP-103 Academy Entry Decision:** optional, **nicht aktiviert** — bleibt bewusst offen als Entscheidungs-WP für einen späteren Zyklus.
- **Doku-/i18n-Konsolidierung:** optional/deferred; volle Doku-Website und volle i18n bleiben deferred.
- **Deferred:** Website, volle i18n, ADR-Massenmigration, v1.0-RC, Rewrite, App-Features, volle externe Zertifizierung — unverändert.

## EN – Optional and Deferred Work Packages

None blocks: WP-102 optional, **not activated** (upgrade valve not pulled; addresses PSV-001, otherwise non-blocking and v1.0-tracked); WP-103 optional, **not activated** (deliberately open decision WP for a later cycle); documentation/i18n consolidation optional/deferred; deferred items (website, full i18n, ADR mass migration, v1.0-RC, rewrite, app features, full external certification) unchanged.

## DE – Bekannte Nicht-Blocker / EN – Known Non-Blockers

| Punkt / Item | Einstufung / Classification |
|---|---|
| WP-099 Checklist DE/EN Option B (optional mit finaler Begründung) | non-blocking → optionaler i18n-Backlog, ehrlich sichtbar; kein Folge-WP, kein Auto-Carry |
| WP-100 volle v1.x-Kompatibilitätszusage aktiviert **erst mit v1.0** | non-blocking → bewusste Governance-Abgrenzung (ADR-0031); **v1.0-tracked** |
| WP-101 „Stable with notes", nicht „frozen forever" (PCS-001) | non-blocking → governed über ADR-0031 |
| PCS-002 low-Drift `.yaml`→`.md` | behoben / fixed |
| PSV-001 externe Validierung — per-Schritt-Belege begrenzt | non-blocking → **v1.0-tracked** (evidence-quality note); optional via WP-102 |
| QGM-003 Gate-ERROR kann bei echtem Treffer den Begriff im CI-Log zeigen | non-blocking → **operational note** (Verstoß sofort beheben) |
| WP-102 / WP-103 optional, nicht aktiviert | non-blocking |
| ADR-Massenmigration / volle Doku-Website / volle i18n / v1.0-RC | deferred |
| Optionaler v0.6-Release-Body-Polish | manual follow-up (kein WP, keine GitHub-Schreibaktion) |
| Foundation 0.7 ist nicht v1.0 | Invariante, überall korrekt |
| Foundation 0.7 ist noch nicht released | korrekt in allen Einstiegspunkten |

## DE – Blocker

**Keine.** Alle release-blocking Kriterien außer WP-104 (dieses Dokument) und WP-105 sind erfüllt und nachgewiesen.

## EN – Blockers

**None.** All release-blocking criteria except WP-104 (this document) and WP-105 are met and evidenced.

## DE – Release-Empfehlung

**GO WITH NOTES.** Foundation 0.7 ist bereit für die Release-Vorbereitung (NDF-WP-105). Die Notes sind ausschließlich non-blocking und bewusst: die volle v1.x-Kompatibilitätszusage aktiviert erst mit v1.0 (ADR-0031); Convention Stability ist „stable with notes", nicht „frozen forever"; PSV-001 bleibt v1.0-tracked; WP-102/WP-103 bleiben optional und wurden nicht aktiviert. Diese Punkte gehören als Known Limitations in die WP-105-Release-Notes.

## EN – Release Recommendation

**GO WITH NOTES.** Foundation 0.7 is ready for release preparation (NDF-WP-105). The notes are exclusively non-blocking and deliberate: the full v1.x compatibility promise activates only at v1.0 (ADR-0031); convention stability is "stable with notes", not "frozen forever"; PSV-001 stays v1.0-tracked; WP-102/WP-103 stay optional and were not activated. These belong in the WP-105 release notes as known limitations.

## DE – Nächste Schritte

1. **NDF-WP-105 – Foundation 0.7 Release Prep:** Release Notes (inkl. der Known Limitations aus diesem Review: v1.x-Zusage erst mit v1.0, Convention Stability with notes, PSV-001, QGM-003, WP-102/103 nicht aktiviert), Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für voraussichtlich `v0.7.0-foundation`, Changelog-Umstellung, README-Status.
2. Danach manuell (Human Maintainer): Go/No-Go, Tag, GitHub Pre-Release; anschließend Post-Release-Cleanup-WP.
3. Für den späteren v1.0-Zyklus vormerken: Evidenz-Tiefe der externen Validierung (PSV-001 / WP-102), Aktivierung der vollen v1.x-Zusage, verbleibende offene v1.0-Kriterien.

## EN – Next Steps

(1) NDF-WP-105 release prep (release notes incl. the known limitations from this review — v1.x promise only at v1.0, convention stability with notes, PSV-001, QGM-003, WP-102/103 not activated — criteria completion, go/no-go checklist, tagging guide for presumably `v0.7.0-foundation`, changelog, README status); (2) then manually: go/no-go, tag, GitHub pre-release, followed by the post-release cleanup work package; (3) note for the later v1.0 cycle: external-validation evidence depth (PSV-001 / WP-102), activation of the full v1.x promise, remaining open v1.0 criteria.
