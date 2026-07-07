# Foundation 0.6 Release Notes

Release: `v0.6.0-foundation` — Adoption Confidence & Governance Hardening **Pre-Release**. Vorbereitet für das geplante Foundation Pre-Release / prepared for the planned foundation pre-release — **tag pending**. NDF ist damit bewusst **kein v1.0** und kein v1.0 Release Candidate.

## DE – Überblick

Foundation 0.6 erhöht das Vertrauen externer Nutzer und macht Governance-Entscheidungen verbindlicher: Die in 0.5 sichtbar gemachten offenen Punkte wurden **abgearbeitet oder bewusst entschieden** — öffentliche unabhängige Validierung statt privatem Kontext, eine angenommene ADR-Policy statt drittem Verschieben, und ein nachweisbar wirksamer Public Quality Gate.

## EN – Overview

Foundation 0.6 increases external users' confidence and makes governance decisions more binding: the open items made visible in 0.5 were **worked off or consciously decided** — public independent validation instead of a private context, an adopted ADR policy instead of a third deferral, and a provably effective public quality gate.

## DE – Was ist Foundation 0.6?

Ein **Adoption Confidence & Governance Hardening Release**. Nach External Validation & 1.0 Path Hardening (0.5) schließt 0.6 genau die dort benannten Lücken — je ein Kern-Deliverable pro Leitideen-Hälfte, nicht mehr.

## EN – What is Foundation 0.6?

An **adoption confidence & governance hardening release**. After external validation & 1.0 path hardening (0.5), 0.6 closes exactly the gaps named there — one core deliverable per half of the theme, nothing more.

## DE – Wichtigste Änderungen

- **Minimal ADR Policy angenommen** (Status: Accepted): verbindliche Regeln für Wann/Wo/Wie/Wer von Decision Records; neue ADRs ab ADR-0031 (WP-086)
- **Öffentliche SampleProject-/Runbook-Validierung** unabhängig positiv bestätigt: **PASS WITH NOTES**, keine Blocker (WP-088)
- **Public Quality Gate Maintenance Review** mit CI-Denylist-Wirksamkeitsnachweis: Evidence-Level **strong**, inkl. synthetischem Lokaltest (WP-089)
- WP-090 (separates Nachweis-Artefakt) **not needed**; WP-087 (Validierungs-Nachschärfung) **skipped/not needed**
- Release Readiness Review: **GO WITH NOTES**, keine Blocker (WP-094)

## EN – Highlights

Minimal ADR policy adopted (status Accepted, new ADRs from ADR-0031 — WP-086); public SampleProject / runbook validation independently and positively confirmed: **PASS WITH NOTES**, no blockers (WP-088); public quality gate maintenance review with CI denylist effectiveness at evidence level **strong**, incl. a synthetic local test (WP-089); WP-090 **not needed**, WP-087 **skipped/not needed**; release readiness review: **GO WITH NOTES**, no blockers (WP-094).

## DE – Adoption Confidence

Die 0.5-Known-Limitation — unabhängige Validierung nur über einen privaten Referenzkontext — ist geschlossen: Ein unabhängiger technischer Reviewer hat den **öffentlichen** Validierungspfad (SampleProject-Fixture `examples/neutral-example-project/` + WP-073-Runbook) als verständlich und nutzbar bestätigt. Externe Nutzer können denselben Pfad selbst nachvollziehen.

## EN – Adoption Confidence

The 0.5 known limitation — independent validation only via a private reference context — is closed: an independent technical reviewer confirmed the **public** validation path (SampleProject fixture + WP-073 runbook) as understandable and usable. External users can retrace the same path themselves.

## DE – Governance Hardening

Der ADR-Dauerläufer aus 0.4/0.5 ist entschieden statt erneut verschoben, und der Quality Gate ist erstmals seit v0.2 gewartet und in seiner Wirksamkeit nachgewiesen — Governance-Regeln sind damit verbindlich und belegt statt nur behauptet.

## EN – Governance Hardening

The ADR carry-over from 0.4/0.5 is decided instead of deferred again, and the quality gate is maintained and proven effective for the first time since v0.2 — governance rules are binding and evidenced instead of merely asserted.

## DE – Public SampleProject Runbook Validation

Ergebnis **PASS WITH NOTES** (NDF-WP-088): unabhängig, öffentlich, positiv, keine Blocker/High-Severity-Findings, keine Must-/Should-Fixes; das strenge Downgrade-Ventil wurde nicht benötigt. Dokumentiert ausschließlich neutralisiert unter `docs/validation/project-adapter/independent-runs/2026-07-07-public-sampleproject-runbook-validation/`. Die Note (PSV-001) steht unten bei den bekannten Einschränkungen.

## EN – Public SampleProject Runbook Validation

Result **PASS WITH NOTES** (NDF-WP-088): independent, public, positive, no blockers/high-severity findings, no must/should fixes; the strict downgrade valve was not needed. Documented exclusively in neutralized form. The note (PSV-001) appears under known limitations below.

## DE – Public Quality Gate Maintenance

Erstes Wartungsreview seit v0.2 (NDF-WP-089): alle Script-Prüfpunkte grün, CI-Verdrahtung sauber (Self-Test + Strict mit Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` via `env`, Wert wird nie geloggt), **CI-Denylist-Wirksamkeit mit Evidence-Level strong** — belegt durch einen kontrollierten synthetischen Lokaltest (erwarteter FAIL inkl. New-file-Erkennung, sauberes Cleanup). Ein separates Nachweis-Artefakt (WP-090) ist deshalb nicht nötig. Details: `docs/quality/PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md`

## EN – Public Quality Gate Maintenance

First maintenance review since v0.2 (NDF-WP-089): all script checks green, clean CI wiring (self-test + strict with the secret passed via `env`, value never logged), **CI denylist effectiveness at evidence level strong** — proven by a controlled synthetic local test. A separate proof artifact (WP-090) is therefore not needed.

## DE – ADR Policy

**Minimal ADR Policy adopted** (NDF-WP-086, Status: Accepted — `docs/adr/ADR_POLICY.md` + Template + Index): Wann braucht NDF eine ADR vs. wann reicht eine WP-Note; neue ADRs entstehen nur in `docs/adr/` mit ordnerübergreifender Nummerierung (**nächste: ADR-0031** — nach dem dokumentierten Altbestand); Statuswerte, Rollen (finale Entscheidung: Human Maintainer), Supersede statt Umschreiben. **ADR-Massenmigration bleibt ausdrücklich deferred**; die alte Nummernkollision bleibt dokumentierter historischer Zustand.

## EN – ADR Policy

**Minimal ADR policy adopted** (NDF-WP-086, status Accepted): when NDF needs an ADR vs. a work-package note; new ADRs only in `docs/adr/` with cross-folder numbering (**next: ADR-0031**); status values, roles (final decision: human maintainer), supersede instead of rewrite. **ADR mass migration stays explicitly deferred**; the legacy numbering collision remains a documented historical state.

## DE – v1.0 Path

Foundation 0.6 **reduziert v1.0-Unsicherheit — mehr nicht**: ADR/Decision Structure jetzt `met with notes`, External Validation jetzt `met with notes`, Public Quality Gate & Neutralität `met` inkl. CI-Wirksamkeitsnachweis. Offen bleiben u. a. die v1.x-Kompatibilitätszusage (WP-093, natürlicher ADR-0031-Kandidat) und die Konventions-Stabilität über weitere Releases. Messlatte: `docs/release/V1_0_READINESS_CRITERIA_DRAFT.md` · Einstieg: `docs/roadmap/V1_0_PATH_SUMMARY.md`

## EN – v1.0 Path

Foundation 0.6 **reduces v1.0 uncertainty — nothing more**: ADR/decision structure now `met with notes`, external validation now `met with notes`, public quality gate & neutrality `met` incl. the CI effectiveness proof. Still open: the v1.x compatibility promise (WP-093, natural ADR-0031 candidate) and convention stability across further releases.

## DE – Scope Lock und Release-Blocking Scope

Foundation 0.6 wurde früh eingefroren (`docs/roadmap/FOUNDATION_0_6_SCOPE_LOCK.md`). Release-blocking: WP-085, WP-086, WP-088, WP-089, WP-094, WP-095. Skipped: WP-087. Not needed: WP-090. Optional: WP-091, WP-092, WP-093. Deferred: Website, volle i18n, ADR-Massenmigration, v1.0-RC, Rewrite, App-Features. Kein Scope Creep; beide Härtungsregeln (ADR-Entscheidungspflicht, WP-088-Ventil) wurden regulär erfüllt statt gezogen.

## EN – Scope Lock and Release-Blocking Scope

Foundation 0.6 was frozen early. Release-blocking: 085/086/088/089/094/095; skipped: 087; not needed: 090; optional: 091–093; deferred items unchanged. No scope creep; both hardening rules (ADR decision duty, WP-088 valve) were fulfilled regularly rather than invoked.

## DE – Bekannte Einschränkungen und Operational Notes

- **PSV-001 (Known Limitation):** Die öffentliche SampleProject-Validierung war positiv und unabhängig, aber **detaillierte Schritt-für-Schritt-Belege des Runbook-Laufs liegen in der neutralisierten Rückmeldung nicht vollständig vor** — deshalb PASS WITH NOTES statt PASS; v1.0-tracked als evidence-quality note.
- **QGM-003 (Operational Note):** Bei einem **echten** Gate-Verstoß kann der gefundene Begriff im ERROR-/CI-Log erscheinen (nötig für Behebbarkeit; der Begriff wäre dann ohnehin bereits in der Repo-Datei öffentlich). Operative Erwartung: **echte Verstöße sofort beheben.**
- ADR-Massenmigration bleibt deferred; die ältere ADR-Nummernkollision bleibt dokumentierter historischer Zustand.
- WP-091 (Checklist DE/EN) bleibt optional offen — **Foundation 0.7 sollte eine Priorisieren-oder-Streichen-Entscheidung erwägen** (drittes Mal optional offen).
- WP-092 (Academy Entry) bleibt optional offen.
- WP-093 (v1.x Compatibility Policy Draft) bleibt optional offen — natürlicher künftiger ADR-0031-Kandidat.
- Vollständige Doku-Website, vollständige i18n-Abdeckung, v1.0 Release Candidate, großer Rewrite und neue App-Features bleiben deferred.
- NDF ist ein Foundation-Release, **kein v1.0**.
- Die Git-Historie bleibt unverändert.

## EN – Known Limitations and Operational Notes

**PSV-001 (known limitation):** the public SampleProject validation was positive and independent, but **detailed per-step runbook evidence was not fully provided** in the neutralized feedback — hence PASS WITH NOTES, not PASS; v1.0-tracked as an evidence-quality note. **QGM-003 (operational note):** for a **real** gate violation, the matched term can appear in ERROR / CI log output (needed for fixability; the term would already be public in the repo file at that point) — operational expectation: **fix real violations immediately.** ADR mass migration stays deferred; the older ADR numbering collision remains documented history. WP-091 stays optional open — **Foundation 0.7 should consider a prioritize-or-drop decision** (third time optional-open). WP-092 stays optional open. WP-093 stays optional open — a natural future ADR-0031 candidate. Full documentation website, full i18n, v1.0 release candidate, large rewrite, and new application features stay deferred. NDF is a foundation release, **not v1.0**. The git history stays unchanged.

## DE – Upgrade von Foundation 0.5

Foundation 0.5 bleibt released (Tag `v0.5.0-foundation`). Foundation 0.6 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.5 nutzt, erhält zusätzlich die ADR-Policy, den öffentlichen Validierungsnachweis und den Gate-Wartungsnachweis.

## EN – Upgrade from Foundation 0.5

Foundation 0.5 stays released. Foundation 0.6 is additive: no migration steps, no replaced artifacts — users of 0.5 additionally get the ADR policy, the public validation evidence, and the gate maintenance evidence.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; keine ADR-Massenmigration; keine vollständige Repo-Übersetzung; keine vollständige Academy; keine Website/Export-Pipeline/CLI; kein History-Rewrite; keine privaten Projektbeispiele oder Reviewer-Daten; keine Release-Automation.

## EN – Non-Goals

No v1.0 and no v1.0 release candidate; no ADR mass migration; no full repository translation; no complete academy; no website/export pipeline/CLI; no history rewrite; no private project examples or reviewer data; no release automation.

## DE – Empfohlene nächste Schritte

1. Manuell (Human Maintainer): Go/No-Go-Checkliste, Tag `v0.6.0-foundation`, GitHub Pre-Release, danach Post-Release-Cleanup.
2. Foundation-0.7-Planung: WP-091-Entscheidung (priorisieren oder streichen), WP-093 als ADR-0031-Kandidat, verbleibende v1.0-Kriterien (v1.x-Zusage, Konventions-Stabilität).
3. Optional qualitativ: Bei einem künftigen Validierungslauf das Feedback-Template im Detailformat einsammeln → volles PASS / v1.0-`met` ohne Note erreichbar.

## EN – Recommended Next Steps

(1) Manually: go/no-go checklist, tag `v0.6.0-foundation`, GitHub pre-release, then post-release cleanup. (2) Foundation 0.7 planning: the WP-091 decision, WP-093 as the ADR-0031 candidate, the remaining v1.0 criteria. (3) Optionally: collect the detailed feedback template in a future validation run — enabling a full PASS / unqualified v1.0 `met`.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.6.0 Foundation is an adoption confidence and governance hardening pre-release.

Highlights:
- Minimal ADR Policy adopted (new ADRs from ADR-0031; no mass migration)
- Public SampleProject Runbook Validation documented with PASS WITH NOTES
- Public Quality Gate Maintenance Review completed with strong evidence
- WP-090 not needed; WP-087 skipped
- Foundation 0.6 Release Readiness Review completed with no blockers

Known notes:
- Public validation per-step evidence remains limited in the neutralized feedback.
- For real Public Quality Gate violations, the matched term can appear in ERROR / CI log
  output; fix real violations immediately.

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_6_RELEASE_NOTES.md

---

DE: Adoption-Confidence- und Governance-Hardening-Pre-Release. Kein v1.0. Vollständige
zweisprachige Release Notes im Repository unter docs/release/FOUNDATION_0_6_RELEASE_NOTES.md.
```
