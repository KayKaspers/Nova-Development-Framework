# Foundation 0.5 Release Notes

Release: `v0.5.0-foundation` — External Validation & 1.0 Path Hardening **Pre-Release**, veröffentlicht am / published on 2026-07-07 (GitHub Pre-Release „Nova Development Framework v0.5.0 Foundation"). NDF ist damit bewusst **kein v1.0** — der v1.0 Readiness Criteria Draft ist eine Messlatte, keine Freigabe.

## DE – Überblick

Foundation 0.5 härtet den NDF-Adoptionspfad an seinen zwei strukturellen Schwachstellen: Der Project Adapter wurde erstmals **von außerhalb der eigenen Rollenkette** validiert (gegen den dokumentierten Selbstvalidierungs-Bias), und der Weg Richtung v1.0 ist erstmals **messbar** — als ehrlicher Kriterien-Entwurf mit Ist-Stand statt Wunschliste.

## EN – Overview

Foundation 0.5 hardens the NDF adoption path at its two structural weak spots: the project adapter was validated **from outside its own role chain** for the first time (against the documented self-validation bias), and the path toward v1.0 is **measurable** for the first time — as an honest criteria draft with current status instead of a wish list.

## DE – Was ist Foundation 0.5?

Ein **External Validation & 1.0 Path Hardening Release**. Nach Adoptionsbeweis (0.3) und Adoption Hardening (0.4) schließt 0.5 die beiden Lücken, die kein internes WP schließen konnte: unabhängige Sicht und v1.0-Messlatte — nicht mehr.

## EN – What is Foundation 0.5?

An **external validation & 1.0 path hardening release**. After the adoption proof (0.3) and adoption hardening (0.4), 0.5 closes the two gaps no internal work package could close: an independent perspective and a v1.0 yardstick — nothing more.

## DE – Wichtigste Änderungen

- Independent Adapter Validation vollständig vorbereitet: Runbook, Validator Brief, Feedback- und Outreach-Template, Ergebnisort (WP-073)
- Unabhängige Validierung durchgeführt und neutralisiert dokumentiert: **PASS WITH NOTES**, keine Blocker (WP-074)
- v1.0 Readiness Criteria Draft: 12 Kategorien, prüfbare Kriterien, ehrlicher Ist-Stand (WP-079)
- v1.0 Path Summary als öffentlicher Einstieg in den v1.0-Pfad (WP-079)
- Foundation 0.5 Scope Lock mit präzisem WP-074-Downgrade-Ventil — das Ventil wurde **nicht benötigt** (WP-072)
- Release Readiness Review: **GO WITH NOTES**, keine Blocker (WP-081)

## EN – Highlights

Independent adapter validation fully prepared (runbook, validator brief, feedback + outreach templates, result location — WP-073); independent validation performed and documented in neutralized form: **PASS WITH NOTES**, no blockers (WP-074); v1.0 readiness criteria draft with 12 categories, verifiable criteria, honest current status (WP-079); v1.0 path summary (WP-079); scope lock with a precise WP-074 downgrade valve that was **not needed** (WP-072); release readiness review: **GO WITH NOTES**, no blockers (WP-081).

## DE – External Validation

Die größte dokumentierte Schwäche des bisherigen Adoptionsbeweises war der Selbstvalidierungs-Bias: Adapter gebaut und validiert von derselben Rollenkette (Nova (ChatGPT) → Implementation Agent → Human Maintainer). Foundation 0.5 bricht das auf — mit vollständigen, sofort nutzbaren Validierungsunterlagen (`docs/validation/project-adapter/`) und einem durchgeführten unabhängigen Review.

## EN – External Validation

The biggest documented weakness of the adoption proof so far was the self-validation bias: adapter built and validated by the same role chain. Foundation 0.5 breaks that up — with complete, immediately usable validation materials and a performed independent review.

## DE – Independent Adapter Validation

Ein unabhängiger technischer Reviewer (nicht an der Adapter-/NDF-Implementierung beteiligt) gab positive Rückmeldung in einem **privaten Referenzkontext**: Struktur, Doku-Richtung und die sicherheitsorientierten NDF-Muster sind verständlich; **keine Blocker, keine High-Severity-Findings**. Ergebnis: **PASS WITH NOTES** — dokumentiert ausschließlich neutralisiert unter `docs/validation/project-adapter/independent-runs/2026-07-06-private-reference-validation/`. Das öffentliche Repository enthält keine privaten Projektnamen, keine Reviewer-Identität, keine Kontakte, Domains oder Secrets. Die Notes stehen unten ehrlich als bekannte Einschränkungen.

## EN – Independent Adapter Validation

An independent technical reviewer (not involved in the adapter/NDF implementation) gave positive feedback in a **private reference context**: structure, documentation direction, and the safety-oriented NDF patterns are understandable; **no blockers, no high-severity findings**. Verdict: **PASS WITH NOTES** — documented exclusively in neutralized form. The public repository contains no private project names, reviewer identity, contacts, domains, or secrets. The notes appear honestly below as known limitations.

## DE – v1.0 Path Hardening

„Kein v1.0" ist jetzt messbar statt nur Abgrenzung: `docs/release/V1_0_READINESS_CRITERIA_DRAFT.md` definiert 12 Kategorien mit prüfbaren Kriterien (Nachweis-Spalten, blocking/tracked-Trennung) und ehrlichem Ist-Stand — inklusive klarer `not met`-Einträge (ADR-Policy, v1.x-Kompatibilitätszusage) und expliziter v1.0-Nicht-Ziele. Kompakter Einstieg: `docs/roadmap/V1_0_PATH_SUMMARY.md`. **Der Draft ist keine v1.0-Freigabe und kein Release Candidate** — v1.0 braucht später einen eigenen Zyklus (Scope Lock → Readiness → Prep → Maintainer-Freigabe).

## EN – v1.0 Path Hardening

"Not v1.0" is now measurable instead of a mere disclaimer: the criteria draft defines 12 categories with verifiable criteria and an honest current status — including clear `not met` entries and explicit v1.0 non-goals. **The draft is no v1.0 approval and no release candidate** — v1.0 needs its own later cycle.

## DE – Scope Lock und Release-Blocking Scope

Foundation 0.5 wurde früh eingefroren (`docs/roadmap/FOUNDATION_0_5_SCOPE_LOCK.md`). Release-blocking: WP-072, WP-073, WP-074, WP-079, WP-081, WP-082. Optional: WP-075, WP-076, WP-077, WP-078. Deferred: WP-080. Kein Scope Creep; das 8-Bedingungen-Downgrade-Ventil für WP-074 wurde definiert, aber nicht gebraucht.

## EN – Scope Lock and Release-Blocking Scope

Foundation 0.5 was frozen early. Release-blocking: WP-072/073/074/079/081/082. Optional: WP-075–078. Deferred: WP-080. No scope creep; the 8-condition downgrade valve for WP-074 was defined but not needed.

## DE – Public Quality Gate

Der Public Quality Gate v0.2 bleibt aktiv und war über alle 0.5-WPs grün: strict + self-test, new-file neutrality check (scannt auch neue/untracked Dateien), custom denylist über das GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` in CI. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## EN – Public Quality Gate

The public quality gate v0.2 stays active and was green across all 0.5 work packages: strict + self-test, new-file neutrality check, custom denylist via the GitHub secret in CI.

## DE – Bekannte Einschränkungen

- **WP-074 ist PASS WITH NOTES, nicht PASS:** Die unabhängige Rückmeldung war positiv und blockerfrei, aber **summarisch und neutralisiert** — die Runbook-Schritte sind nicht einzeln belegt.
- **Privater Referenzkontext:** Die Validierung erfolgte über einen neutralisierten privaten Referenzkontext, nicht als vollständiger öffentlicher SampleProject-Runbook-Lauf.
- **External Validation im v1.0-Draft bleibt deshalb nur `partially met`;** ein öffentlicher Fixture-/Runbook-Lauf bleibt v1.0-tracked und ist Kandidat für Foundation 0.6.
- Optionale WPs offen: Checklist DE/EN (WP-075), Academy Entry (WP-077), Quality Gate Maintenance (WP-078).
- **WP-076 (ADR Policy) muss in Foundation 0.6 verbindlich priorisiert oder ehrlich gestrichen werden** — ein drittes stilles Verschieben ist laut Scope Lock unzulässig.
- WP-080 (Docs Export / Website Concept) bleibt deferred.
- Restliche i18n-Arbeit offen; Security-/Gate-Prompts teils nur DE/EN-Kern — Stand: `docs/i18n/TRANSLATION_STATUS.md`.
- Die v1.x-Kompatibilitätszusage ist offen und bleibt v1.0-relevant (bewusste Lücke für den v1.0 Scope Lock).
- NDF ist ein Foundation-Release, **kein v1.0**.
- Die Git-Historie bleibt unverändert.

## EN – Known Limitations

WP-074 is PASS WITH NOTES, not PASS (positive and blocker-free, but **summarized and neutralized** — runbook steps not individually evidenced); the validation used a **private reference context**, not a full public SampleProject runbook walk; external validation in the v1.0 draft therefore stays `partially met`, and a public fixture/runbook run remains v1.0-tracked (Foundation 0.6 candidate). Optional work packages open: checklist DE/EN (WP-075), academy entry (WP-077), gate maintenance (WP-078). **WP-076 (ADR policy) must be prioritized bindingly in Foundation 0.6 or dropped honestly** — a third silent carry-over is not allowed. WP-080 stays deferred. Remaining i18n work open; security/gate prompts partly DE/EN core only. The v1.x compatibility promise is open and stays v1.0-relevant. NDF is a foundation release, **not v1.0**. The git history stays unchanged.

## DE – Upgrade von Foundation 0.4

Foundation 0.4 bleibt released (Tag `v0.4.0-foundation`). Foundation 0.5 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.4 nutzt, erhält zusätzlich die Validierungsunterlagen, den unabhängigen Validierungsnachweis und die v1.0-Messlatte.

## EN – Upgrade from Foundation 0.4

Foundation 0.4 stays released. Foundation 0.5 is additive: no migration steps, no replaced artifacts — users of 0.4 additionally get the validation materials, the independent validation evidence, and the v1.0 yardstick.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; keine vollständige Repo-Übersetzung; keine vollständige Academy; keine Website/Export-Pipeline/CLI; kein History-Rewrite; keine privaten Projektbeispiele oder Reviewer-Daten; keine ADR-Massenmigration; keine Release-Automation.

## EN – Non-Goals

No v1.0 and no v1.0 release candidate; no full repository translation; no complete academy; no website/export pipeline/CLI; no history rewrite; no private project examples or reviewer data; no bulk ADR migration; no release automation.

## DE – Empfohlene nächste Schritte

1. Manuell (Human Maintainer): Go/No-Go-Checkliste, Tag `v0.5.0-foundation`, GitHub Pre-Release, danach Post-Release-Cleanup.
2. Foundation-0.6-Planung: WP-076-Entscheidung (priorisieren oder streichen) und öffentlicher Fixture-/Runbook-Lauf als Kandidaten.
3. Offene v1.0-Kriterien über 0.6-WPs schließen (ADR-Policy, v1.x-Kompatibilitätszusage, volles External-Validation-`met`).

## EN – Recommended Next Steps

(1) Manually: go/no-go checklist, tag `v0.5.0-foundation`, GitHub pre-release, then post-release cleanup. (2) Foundation 0.6 planning: the WP-076 decision and the public fixture/runbook run as candidates. (3) Close the open v1.0 criteria via 0.6 work packages.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.5.0 Foundation is an external validation and v1.0 path hardening pre-release.

Highlights:
- Independent Adapter Validation Preparation (runbook, validator brief, templates)
- Neutralized independent validation result with PASS WITH NOTES and no blockers
- v1.0 Readiness Criteria Draft (12 categories, honest status)
- v1.0 Path Summary
- Foundation 0.5 Release Readiness Review with no blockers
- Public Quality Gate v0.2 remains active

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_5_RELEASE_NOTES.md

---

DE: External-Validation- und v1.0-Path-Hardening-Pre-Release. Vollständige zweisprachige
Release Notes im Repository unter docs/release/FOUNDATION_0_5_RELEASE_NOTES.md.
```
