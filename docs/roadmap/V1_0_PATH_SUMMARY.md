# v1.0 Path Summary

## DE – Kurzfassung

NDF ist **nicht v1.0** — und Foundation 0.5 ändert das nicht. Was Foundation 0.5 ändert: Es gibt jetzt eine öffentliche, messbare Messlatte dafür, was vor einem späteren v1.0 erfüllt sein müsste: [V1_0_READINESS_CRITERIA_DRAFT.md](../release/V1_0_READINESS_CRITERIA_DRAFT.md) (Entwurf, keine Freigabe, kein Zeitplan).

## EN – Summary

NDF is **not v1.0** — and Foundation 0.5 does not change that. What it does change: there is now a public, measurable yardstick for what would have to be met before a later v1.0: [V1_0_READINESS_CRITERIA_DRAFT.md](../release/V1_0_READINESS_CRITERIA_DRAFT.md) (a draft — no approval, no schedule).

## DE – Warum ein v1.0-Pfad nötig ist

„Kein v1.0" war bisher nur eine Abgrenzung. Ohne definierte Kriterien lässt sich weder Fortschritt messen noch eine spätere v1.0-Entscheidung ehrlich treffen — sie wäre Bauchgefühl. Der Kriterien-Entwurf macht die Entscheidung überprüfbar, bevor sie ansteht.

## EN – Why a v1.0 Path Is Needed

"Not v1.0" has so far only been a disclaimer. Without defined criteria, neither progress nor a later v1.0 decision can be handled honestly — it would be gut feeling. The criteria draft makes the decision verifiable before it is due.

## DE – Was Foundation 0.5 beiträgt

1. **External Validation:** Vorbereitung eines unabhängigen Adapter-Validierungslaufs (erledigt, NDF-WP-073) und dessen Durchführung (NDF-WP-074, offen) — gegen den dokumentierten Selbstvalidierungs-Bias. Eine fehlende unabhängige Validierung bleibt in jedem Fall offenes v1.0-Kriterium.
2. **1.0 Path Hardening:** dieser Kriterien-Entwurf (NDF-WP-079) mit 12 Kategorien, ehrlichem Ist-Stand (`met`/`partially met`/`not met`/…) und expliziten v1.0-Nicht-Zielen.

## EN – What Foundation 0.5 Contributes

(1) **External validation:** preparation of an independent adapter validation run (done, NDF-WP-073) and its execution (NDF-WP-074, open) — against the documented self-validation bias; a missing independent validation stays an open v1.0 criterion in any case. (2) **1.0 path hardening:** this criteria draft (NDF-WP-079) with 12 categories, honest current status, and explicit v1.0 non-goals.

## DE – Was vor v1.0 noch offen ist

Stand heute mindestens: eine definierte v1.x-Kompatibilitätszusage; Bestätigung der Konventions-Stabilität über weitere Releases. *Update (NDF-WP-086):* Die ADR-Policy-Entscheidung ist getroffen — Minimal-Policy angenommen (`docs/adr/ADR_POLICY.md`), Kriterium `met with notes`. *Update (NDF-WP-088):* Die öffentliche SampleProject-Runbook-Validierung wurde unabhängig positiv bestätigt (PASS WITH NOTES, keine Blocker/High-Findings) — External Validation damit `met with notes`; Note: Schrittbeleg-Tiefe begrenzt. Kein v1.0-Claim. Vollständige Liste mit Ist-Stand: im Kriterien-Entwurf.

## EN – What Remains Before v1.0

As of today at least: a defined v1.x compatibility promise; confirmation of convention stability across further releases. *Update (NDF-WP-086):* the ADR policy decision is made — minimal policy adopted (`docs/adr/ADR_POLICY.md`), criterion `met with notes`. *Update (NDF-WP-088):* the public SampleProject runbook validation was positively confirmed by an independent reviewer (PASS WITH NOTES, no blockers/high findings) — external validation is now `met with notes`; note: per-step evidence depth remains limited. No v1.0 claim. Full list with current status: in the criteria draft.

## DE – Nächste Schritte

Foundation 0.5 regulär abschließen (WP-074 → optionale WPs → Readiness → Release Prep). Danach entscheidet ein **eigener v1.0-Zyklus** (Scope Lock → Readiness → Prep) mit finaler Freigabe durch den Human Maintainer. Keine Termine — der Pfad ist definiert, nicht terminiert.

*Update: Foundation 0.6 (released) hat External Validation und die ADR/Decision-Structure auf `met with notes` gehoben. **Foundation 0.7 ist scope-locked als v1.0-Pfad-Konsolidierung** ([FOUNDATION_0_7_SCOPE_LOCK.md](FOUNDATION_0_7_SCOPE_LOCK.md)). NDF-WP-099: Checklist-DE/EN-Frage entschieden (optional, kein Blocker). **NDF-WP-100: v1.x Compatibility Policy als [ADR-0031](../adr/ADR-0031-v1x-compatibility-policy.md) angenommen** — Governance-Rahmen für v1.x-Kompatibilität; Kriterium damit `met with notes`. **Die aktive volle v1.x-Zusage tritt erst mit v1.0 in Kraft** — Foundation 0.7 definiert nur den Rahmen, macht NDF nicht v1.0-reif. **NDF-WP-101: Konventions-Stabilität bestätigt** ([Stability Review](../validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md)) — Adapter-Konventionen seit 0.4 über vier Releases unverändert; Kriterium `partially met` → `met with notes` (künftige Änderungen governed über ADR-0031). Kein v1.0-Claim.*

## EN – Next Steps

Complete Foundation 0.5 (WP-074 → optional work → readiness → release prep). A **dedicated v1.0 cycle** (scope lock → readiness → prep) decides afterwards, with final approval by the human maintainer. No dates — the path is defined, not scheduled.

*Update: Foundation 0.6 (released) lifted external validation and the ADR/decision structure to `met with notes`. **Foundation 0.7 is scope-locked as v1.0 path consolidation.** NDF-WP-099 decided the checklist DE/EN question (optional, not a blocker). **NDF-WP-100 accepted the v1.x compatibility policy as [ADR-0031](../adr/ADR-0031-v1x-compatibility-policy.md)** — a governance framework for v1.x compatibility; the criterion is now `met with notes`. **The active full v1.x promise takes effect only at v1.0** — Foundation 0.7 defines only the framework and does not make NDF v1.0-ready. **NDF-WP-101 confirmed convention stability** ([stability review](../validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md)) — adapter conventions unchanged across four releases since 0.4; criterion `partially met` → `met with notes` (future changes governed via ADR-0031). No v1.0 claim.*
