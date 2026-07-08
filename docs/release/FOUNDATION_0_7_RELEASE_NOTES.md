# Foundation 0.7 Release Notes

Release: `v0.7.0-foundation` — **v1.0 Path Consolidation & Compatibility Governance** Foundation **Pre-Release**, veröffentlicht am / published on 2026-07-08 (GitHub Pre-Release „Nova Development Framework v0.7.0 Foundation", Target `main`). NDF ist bewusst **kein v1.0** und kein v1.0 Release Candidate; die volle v1.x-Kompatibilitätszusage ist vor einem künftigen v1.0-Release **nicht aktiv**. / Published as the `v0.7.0-foundation` foundation pre-release on 2026-07-08. Not v1.0, no v1.0 release candidate; the full v1.x compatibility promise is not active before a future v1.0 release.

## DE – Überblick

Foundation 0.7 konsolidiert den v1.0-Pfad und entscheidet die Kompatibilitäts-Governance. Die in 0.6 sichtbar gebliebenen Punkte wurden **entschieden statt weiter verschoben**: die v1.x-Kompatibilitätszusage als angenommene ADR, die Konventions-Stabilität als bestätigtes Review und die seit 0.4 mitgeschleppte Checklist-DE/EN-Frage als verbindliche Entscheidung. Foundation 0.7 behauptet dabei keine v1.0-Reife.

## EN – Overview

Foundation 0.7 consolidates the v1.0 path and decides compatibility governance. The items still visible in 0.6 were **decided instead of deferred again**: the v1.x compatibility promise as an accepted ADR, convention stability as a confirmed review, and the checklist DE/EN question carried since 0.4 as a binding decision. Foundation 0.7 claims no v1.0 maturity.

## DE – Was ist Foundation 0.7?

Ein **v1.0 Path Consolidation & Compatibility Governance Release**. Nach Adoption Confidence & Governance Hardening (0.6) schließt 0.7 die dort benannten offenen v1.0-Punkte so weit, wie ehrlich möglich — je ein Kern-Deliverable pro Titel-Hälfte (Governance → ADR-0031, Consolidation → Convention Stability), plus die überfällige Checklist-Entscheidung.

## EN – What is Foundation 0.7?

A **v1.0 path consolidation & compatibility governance release**. After adoption confidence & governance hardening (0.6), 0.7 closes the open v1.0 items named there as honestly as possible — one core deliverable per title half (governance → ADR-0031, consolidation → convention stability), plus the overdue checklist decision.

## DE – Wichtigste Änderungen

- **v1.x Compatibility Policy als ADR-0031 angenommen** (Status: Accepted): Governance-Rahmen mit Kompatibilitätskategorien; volle v1.x-Zusage aktiviert **erst mit v1.0** (WP-100)
- **Project Adapter Convention Stability Review: Stable with notes** — Adapter-Konventionen seit WP-059 über 0.4→0.7 unverändert; ein low-Drift korrigiert (WP-101)
- **Checklist DE/EN entschieden: Option B** (optional mit finaler Begründung, kein Auto-Carry, kein Folge-WP) (WP-099)
- **WP-102** (External Validation Evidence Depth) und **WP-103** (Academy Entry) **nicht aktiviert** — bleiben optional
- Release Readiness Review: **GO WITH NOTES**, keine Blocker (WP-104)

## EN – Highlights

v1.x compatibility policy accepted as ADR-0031 (status Accepted; full v1.x promise activates only at v1.0 — WP-100); Project Adapter convention stability review: **Stable with notes** (conventions unchanged since WP-059 across 0.4→0.7; one low drift fixed — WP-101); checklist DE/EN decided: **Option B** (optional with final rationale, no auto-carry, no follow-up work package — WP-099); **WP-102** and **WP-103 not activated** — stay optional; release readiness review: **GO WITH NOTES**, no blockers (WP-104).

## DE – Compatibility Governance

Die Governance-Hälfte des Arbeitstitels ist erfüllt: Die v1.x-Kompatibilitätszusage wurde **entschieden statt vertagt**. Sie ist als Decision Record geführt (ADR-0031, Accepted) und definiert, welche Bestandteile welche Kompatibilitätserwartung tragen — ohne vor v1.0 ein volles Versprechen zu geben.

## EN – Compatibility Governance

The governance half is fulfilled: the v1.x compatibility promise was **decided instead of deferred**. It lives as a decision record (ADR-0031, Accepted) and defines which parts carry which compatibility expectation — without giving a full promise before v1.0.

## DE – v1.x Compatibility Policy / ADR-0031

**ADR-0031 (Status: Accepted)** ist die Single Source of Truth für die v1.x-Kompatibilitäts-Governance — es ist **keine separate Policy-Datei** nötig. Es definiert fünf Kompatibilitätskategorien (Stable Candidate, Governed, Experimental, Deprecated, Out of Scope) und die zugehörigen Breaking-/Deprecation-Regeln. Zentrale Abgrenzung: **Die volle v1.x-Kompatibilitätszusage tritt erst mit einem späteren v1.0-Release in Kraft** — vor v1.0 ist sie nicht aktiv. Das zuvor als `not met` geführte v1.0-Kriterium steht damit ehrlich auf `met with notes`. Nächste freie ADR-Nummer: ADR-0032. Details: `docs/adr/ADR-0031-v1x-compatibility-policy.md`

## EN – v1.x Compatibility Policy / ADR-0031

**ADR-0031 (status Accepted)** is the single source of truth for v1.x compatibility governance — **no separate policy file** is needed. It defines five compatibility categories (Stable Candidate, Governed, Experimental, Deprecated, Out of Scope) and the associated breaking/deprecation rules. Key boundary: **the full v1.x compatibility promise activates only with a future v1.0 release** — it is not active before v1.0. The previously `not met` v1.0 criterion is now honestly `met with notes`. Next free ADR number: ADR-0032.

## DE – Project Adapter Convention Stability

Die Consolidation-Hälfte des Arbeitstitels ist erfüllt: Die Project-Adapter-Konventions-Stabilität wurde als **Stable with notes** bestätigt (WP-101). Kernbeleg ist die Git-Historie — `PROJECT_ADAPTER_CONVENTIONS.md` ist seit WP-059 (Foundation 0.4) über vier Releases unverändert. Ein einziger low-Drift wurde korrigiert: stale `PROJECT_MANIFEST.yaml`-Referenzen wurden an das kanonische `PROJECT_MANIFEST.md` angeglichen. Keine high/blocker Findings. **„Stable" heißt ausdrücklich nicht „frozen forever"** — künftige Änderungen bleiben über ADR-0031 governed. Kriterium Adapter-Maturity/Convention-Stability jetzt `met with notes`. Details: `docs/validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md`

## EN – Project Adapter Convention Stability

The consolidation half is fulfilled: adapter convention stability confirmed as **Stable with notes** (WP-101). The core evidence is git history — `PROJECT_ADAPTER_CONVENTIONS.md` unchanged since WP-059 (Foundation 0.4) across four releases. One low drift was fixed: stale `PROJECT_MANIFEST.yaml` references aligned to the canonical `PROJECT_MANIFEST.md`. No high/blocker findings. **"Stable" explicitly does not mean "frozen forever"** — future changes stay governed by ADR-0031. The adapter-maturity/convention-stability criterion is now `met with notes`.

## DE – Checklist DE/EN Entscheidung

Die seit Foundation 0.4 mehrfach optional offene Frage ist verbindlich entschieden (WP-099): **Option B — optional mit finaler Begründung.** Die Checklist-DE/EN-Arbeit bleibt optional, aber **kein Auto-Carry mehr** und **kein Folge-WP**; die Restlücken bleiben ehrlich als optionaler i18n-Backlog im Translation-Status sichtbar. Damit ist der Dauerläufer sauber geschlossen. Details: `docs/roadmap/FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md`

## EN – Checklist DE/EN Decision

The question kept optional since Foundation 0.4 is now bindingly decided (WP-099): **Option B — optional with final rationale.** The checklist DE/EN work stays optional, but **no more auto-carry** and **no follow-up work package**; the remaining gaps stay honestly visible as an optional i18n backlog in the translation status. The carry-over is cleanly closed.

## DE – v1.0 Path

Foundation 0.7 **reduziert v1.0-Unsicherheit und konsolidiert den Pfad — mehr nicht**: v1.x-Kompatibilität jetzt `met with notes` (ADR-0031), Adapter-Maturity/Convention-Stability jetzt `met with notes` (WP-101), Checklist DE/EN ehrlich als optionaler i18n-Backlog eingeordnet. Offene v1.0-Kriterien bleiben sichtbar — u. a. die Evidenz-Tiefe der externen Validierung (PSV-001). Kein 0.7-Dokument stellt v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv dar. Messlatte: `docs/release/V1_0_READINESS_CRITERIA_DRAFT.md` · Einstieg: `docs/roadmap/V1_0_PATH_SUMMARY.md`

## EN – v1.0 Path

Foundation 0.7 **reduces v1.0 uncertainty and consolidates the path — nothing more**: v1.x compatibility now `met with notes` (ADR-0031), adapter maturity/convention stability now `met with notes` (WP-101), checklist DE/EN honestly classified as an optional i18n backlog. Open v1.0 criteria stay visible — notably external-validation evidence depth (PSV-001). No 0.7 document presents v1.0 as reached or a full v1.x promise as active.

## DE – Scope Lock und Release-Blocking Scope

Foundation 0.7 wurde früh eingefroren (`docs/roadmap/FOUNDATION_0_7_SCOPE_LOCK.md`). Release-blocking: WP-098, WP-099, WP-100, WP-101, WP-104, WP-105. Optional / nicht aktiviert: WP-102 (mit Upgrade-Ventil — nicht gezogen), WP-103. Deferred: vollständige Doku-Website, vollständige i18n, ADR-Massenmigration, v1.0-RC, großer Rewrite, neue App-Features, vollständige externe Zertifizierung. Kein Scope Creep; das WP-102-Upgrade-Ventil und der WP-099-Entscheidungskorridor wurden regulär abgearbeitet.

## EN – Scope Lock and Release-Blocking Scope

Foundation 0.7 was frozen early. Release-blocking: 098/099/100/101/104/105; optional / not activated: WP-102 (with upgrade valve — not pulled), WP-103; deferred: full documentation website, full i18n, ADR mass migration, v1.0-RC, large rewrite, new application features, full external certification. No scope creep; the WP-102 upgrade valve and WP-099 decision corridor were handled regularly.

## DE – Bekannte Einschränkungen und Operational Notes

- **v1.x-Kompatibilität (bewusste Governance-Abgrenzung):** ADR-0031 ist Accepted, aber die **volle v1.x-Kompatibilitätszusage aktiviert erst mit einem späteren v1.0-Release** — vor v1.0 nicht aktiv. v1.0-tracked.
- **Convention Stability (PCS-001):** „Stable with notes", **nicht „frozen forever"** — künftige Änderungen bleiben über ADR-0031 governed.
- **PSV-001 (Known Limitation):** Die externe SampleProject-Validierung war positiv und unabhängig, aber **detaillierte per-Schritt-Belege liegen nicht vollständig vor** — v1.0-tracked als evidence-quality note; optional adressierbar über WP-102 (nicht aktiviert).
- **QGM-003 (Operational Note):** Bei einem **echten** Public-Quality-Gate-Verstoß kann der gefundene Begriff im ERROR-/CI-Log erscheinen (nötig für Behebbarkeit; der Begriff wäre dann ohnehin bereits in der Repo-Datei öffentlich). Operative Erwartung: **echte Verstöße sofort beheben.**
- **WP-102** (External Validation Evidence Depth) und **WP-103** (Academy Entry) wurden **nicht aktiviert** — bleiben optional.
- ADR-Massenmigration, vollständige Doku-Website, vollständige i18n, v1.0 Release Candidate, großer Rewrite, neue App-Features und vollständige externe Zertifizierung bleiben deferred.
- NDF ist ein Foundation-Release, **kein v1.0**.
- Die Git-Historie bleibt unverändert.

## EN – Known Limitations and Operational Notes

**v1.x compatibility (deliberate governance boundary):** ADR-0031 is Accepted, but the **full v1.x compatibility promise activates only with a future v1.0 release** — not active before v1.0; v1.0-tracked. **Convention stability (PCS-001):** "Stable with notes", **not "frozen forever"** — future changes stay governed by ADR-0031. **PSV-001 (known limitation):** the external SampleProject validation was positive and independent, but **detailed per-step evidence is not fully provided** — v1.0-tracked as an evidence-quality note; optionally addressable via WP-102 (not activated). **QGM-003 (operational note):** for a **real** public-quality-gate violation, the matched term can appear in ERROR / CI log output (needed for fixability; the term would already be public in the repo file at that point) — fix real violations immediately. **WP-102** and **WP-103 not activated** — stay optional. ADR mass migration, full documentation website, full i18n, v1.0 release candidate, large rewrite, new application features, and full external certification stay deferred. NDF is a foundation release, **not v1.0**. The git history stays unchanged.

## DE – Upgrade von Foundation 0.6

Foundation 0.6 bleibt veröffentlicht (Tag `v0.6.0-foundation`). Foundation 0.7 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.6 nutzt, erhält zusätzlich die angenommene v1.x-Compatibility-Policy (ADR-0031), das Convention-Stability-Review und die verbindliche Checklist-DE/EN-Entscheidung.

## EN – Upgrade from Foundation 0.6

Foundation 0.6 stays published. Foundation 0.7 is additive: no migration steps, no replaced artifacts — users of 0.6 additionally get the accepted v1.x compatibility policy (ADR-0031), the convention stability review, and the binding checklist DE/EN decision.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; keine aktive volle v1.x-Kompatibilitätszusage vor v1.0; keine ADR-Massenmigration; keine vollständige Repo-Übersetzung; keine vollständige Academy; keine Website/Export-Pipeline/CLI; kein History-Rewrite; keine privaten Projektbeispiele oder Reviewer-Daten; keine Release-Automation; **kein Skill-Pack und kein Context-Economy-Dokument in diesem Release.**

## EN – Non-Goals

No v1.0 and no v1.0 release candidate; no active full v1.x compatibility promise before v1.0; no ADR mass migration; no full repository translation; no complete academy; no website/export pipeline/CLI; no history rewrite; no private project examples or reviewer data; no release automation; **no skills pack and no context-economy document in this release.**

## DE – Möglicher nächster Evolutionsschritt

Future Candidate nach Foundation 0.7 (nur Hinweis, **kein Scope, kein Release-Kriterium, kein blocking WP**): **NDF Agent Enablement & Context Economy**, inklusive eines kleinen public-neutralen Claude Skills Pack. Ob und wann das aufgenommen wird, entscheidet ein späterer eigener Planungszyklus.

## EN – Possible Next Evolution Step

Future candidate after Foundation 0.7 (hint only, **not scope, not a release criterion, not a blocking work package**): **NDF Agent Enablement & Context Economy**, including a small public-neutral Claude Skills Pack. Whether and when this is taken up is decided by a later dedicated planning cycle.

## DE – Empfohlene nächste Schritte

1. Manuell (Human Maintainer): Go/No-Go-Checkliste, Tag `v0.7.0-foundation`, GitHub Pre-Release, danach Post-Release-Cleanup.
2. Für den späteren v1.0-Zyklus vormerken: Evidenz-Tiefe der externen Validierung (PSV-001 / WP-102), Aktivierung der vollen v1.x-Zusage, verbleibende offene v1.0-Kriterien.
3. Optional: Future-Candidate „Agent Enablement & Context Economy" in einem eigenen Planungs-WP bewerten.

## EN – Recommended Next Steps

(1) Manually: go/no-go checklist, tag `v0.7.0-foundation`, GitHub pre-release, then post-release cleanup. (2) Note for the later v1.0 cycle: external-validation evidence depth (PSV-001 / WP-102), activation of the full v1.x promise, remaining open v1.0 criteria. (3) Optionally: evaluate the "Agent Enablement & Context Economy" future candidate in a dedicated planning work package.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.7.0 Foundation is a v1.0 path consolidation and
compatibility governance pre-release.

Highlights:
- v1.x Compatibility Policy accepted as ADR-0031 (governance framework;
  full v1.x promise activates only at v1.0)
- Project Adapter Convention Stability reviewed: Stable with notes
  (conventions unchanged across 0.4 to 0.7; one low drift fixed)
- Checklist DE/EN decided: Option B (optional with final rationale, no auto-carry)
- WP-102 and WP-103 optional and not activated
- Foundation 0.7 Release Readiness Review completed with no blockers (GO WITH NOTES)

Known notes:
- The full v1.x compatibility promise is not active before a future v1.0 release.
- Convention stability is "stable with notes", not frozen forever.
- External validation per-step evidence remains limited (PSV-001).
- For real Public Quality Gate violations, the matched term can appear in ERROR / CI
  log output; fix real violations immediately (QGM-003).

Future candidate after Foundation 0.7: NDF Agent Enablement & Context Economy,
including a small public-neutral Claude Skills Pack.

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_7_RELEASE_NOTES.md

---

DE: v1.0-Pfad-Konsolidierung und Kompatibilitäts-Governance-Pre-Release. Kein v1.0;
die volle v1.x-Kompatibilitätszusage ist vor einem künftigen v1.0-Release nicht aktiv.
Vollständige zweisprachige Release Notes im Repository unter
docs/release/FOUNDATION_0_7_RELEASE_NOTES.md.
```
