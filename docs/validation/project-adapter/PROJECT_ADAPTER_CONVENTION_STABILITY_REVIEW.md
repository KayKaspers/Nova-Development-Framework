# Project Adapter Convention Stability Review

## DE – Zweck

Release-blocking Foundation-0.7-Review (NDF-WP-101): Prüft, ob die Project-Adapter-Konventionen über die Foundation-Releases 0.3–0.7 stabil und nachvollziehbar geblieben sind, um den v1.0-Pfad zu stärken. Ergebnis: **Stable with notes.** Kein v1.0-Claim; volle v1.x-Kompatibilität bleibt gemäß ADR-0031 an einen späteren v1.0-Release gebunden.

## EN – Purpose

Release-blocking Foundation 0.7 review (NDF-WP-101): assesses whether the project adapter conventions stayed stable and traceable across Foundation releases 0.3–0.7 to strengthen the v1.0 path. Result: **Stable with notes.** No v1.0 claim; full v1.x compatibility stays bound to a later v1.0 release under ADR-0031.

## DE – Ausgangslage

Der v1.0 Readiness Criteria Draft führt „Adapter-Konventionen stabil über ≥ 2 Releases" als blocking-Kriterium `partially met`. Foundation 0.7 (Scope Lock, WP-098) macht diese Review release-blocking. ADR-0031 (WP-100) ordnet die Project Adapter Conventions als **Governed** ein.

## EN – Background

The v1.0 readiness draft lists "adapter conventions stable across ≥ 2 releases" as a blocking criterion at `partially met`. Foundation 0.7 makes this review release-blocking. ADR-0031 classifies the project adapter conventions as **Governed**.

## DE – Geprüfte Artefakte / EN – Reviewed Artifacts

| Artefakt / Path | Zweck | Stabilitäts-Evidenz | Risiko |
|---|---|---|---|
| `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` | verbindliche Konventionen (Manifest, Output-Pfade, Health Score) | erstellt in WP-059 (0.4), **seither unverändert** — stabil über 0.4→0.7 (4 Releases) | none |
| `docs/project-starter/PROJECT_ADAPTER_V0_2.md` | Adapter-Anleitung (Phasen 0–10) | seit WP-059 stabil; **ein low-Drift bei zwei stale `.yaml`-Referenzen — in dieser Review korrigiert** (PCS-002) | low (behoben) |
| `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md` | Validierungsnachweis (WP-047 PASS WITH NOTES) | historisch unverändert; nur additive 0.5/0.6-Update-Vermerke | none |
| `docs/validation/project-adapter/independent-runs/` (2026-07-06, 2026-07-07) | unabhängige Validierungsläufe | zwei Läufe (WP-074 privat, WP-088 öffentlich), beide PASS WITH NOTES | info |
| `docs/validation/project-adapter/PROJECT_ADAPTER_V0_2_IMPROVEMENT_BACKLOG.md` | Backlog | kein offener Konventionspunkt mehr (Punkte 1–5 addressed, 6 completed) | none |
| `examples/neutral-example-project/` | SampleProject-Fixture | Pfad stabil, als Doku-Fixture konsistent referenziert | none |
| `docs/adr/ADR-0031-v1x-compatibility-policy.md` | Governance-Rahmen | führt Adapter Conventions als **Governed** | none |

## DE – Stabilitätsdimensionen / EN – Stability Dimensions

| Dimension | Status | Evidenz / Notiz |
|---|---|---|
| 1. Naming stability | stable | Konventionen seit WP-059 unverändert |
| 2. Directory/file layout | stable | Output-Pfad-Konvention (Fixture-Output / zentrale Nachweise / produktiv) konsistent |
| 3. Required vs optional outputs | stable | Phasen-Tabelle + Ergebnisstruktur; nach `.yaml`→`.md`-Korrektur konsistent |
| 4. Role model consistency | stable | Nova (ChatGPT) → Implementation Agent → Human Maintainer durchgängig |
| 5. Public neutrality expectations | stable | Neutralitäts-/Private-Begriffe-Regel identisch mit Gate-Invariante |
| 6. Quality Gate expectations | stable | Gate v0.2, in WP-089 mit Evidence strong bestätigt |
| 7. SampleProject fixture consistency | stable | `examples/neutral-example-project/` stabil |
| 8. Independent validation/runbook | stable with notes | Runbook (WP-073) stabil; Evidenz-Tiefe begrenzt (PSV-001, WP-088) |
| 9. Backlog/finding handling | stable | kein offener Konventions-Backlog |
| 10. Versioning/compatibility relationship | stable with notes | via ADR-0031 als Governed geregelt; volle v1.x-Zusage erst mit v1.0 |
| 11. DE/EN usability | stable | Conventions vollständig bilingual |
| 12. v1.0 readiness relevance | stable with notes | trägt eine Hebung `partially met` → `met with notes` |

## DE – Drift- und Widerspruchsprüfung

- **Eine Konventionsquelle:** `PROJECT_ADAPTER_CONVENTIONS.md`, keine konkurrierenden Quellen; konsistent über 23 Dateien referenziert.
- **Kein Widerspruch** zwischen ADR-0031 (Governed) und den Konventionsdokumenten.
- **Kein Widerspruch** zwischen v1.0-Readiness und aktuellem Adapterstand.
- **Ein low-Drift gefunden und behoben (PCS-002):** Die Phasen-Tabelle und die Ergebnisstruktur in `PROJECT_ADAPTER_V0_2.md` trugen noch `PROJECT_MANIFEST.yaml`, während Header und Konventionen `PROJECT_MANIFEST.md` (Markdown kanonisch) festlegen. Als redaktionelle Statusklarstellung auf `.md` angeglichen — keine inhaltliche Konventionsänderung.
- **Keine high/blocker-Widersprüche.**

## EN – Drift and Contradiction Check

Single convention source, no competing sources, consistent across 23 files; no contradiction between ADR-0031 (Governed) and the convention docs, nor between v1.0 readiness and the current adapter state. One low drift found and fixed (PCS-002): two stale `PROJECT_MANIFEST.yaml` references in the adapter v0.2 phase table/result structure were aligned to the canonical `.md` — an editorial clarification, not a convention change. No high/blocker contradictions.

## DE – Gesamturteil / EN – Overall Assessment

**Stable with notes.** Die Project-Adapter-Konventionen sind über 0.4→0.7 (vier Releases, davon 0.4/0.5/0.6 released) unverändert und in sich konsistent — ausreichend stabil für Foundation 0.7 und den v1.0-Pfad. Volle v1.x-Kompatibilität bleibt gemäß ADR-0031 governed und aktiviert erst mit einem späteren v1.0-Release. Die Konventionen sind **nicht** „für immer eingefroren"; künftige Änderungen laufen über die ADR-0031-Regeln (Breaking-Change-/Deprecation-Vermerk).

## DE – Bekannte Einschränkungen / EN – Known Limitations

- **PCS-001 (info):** Konventionen stabil, aber die aktive volle v1.x-Kompatibilitätszusage bleibt an einen späteren v1.0-Release gebunden (ADR-0031) — nicht in Foundation 0.7 aktiv.
- **PCS-002 (low, behoben):** Zwei stale `.yaml`-Manifest-Referenzen in `PROJECT_ADAPTER_V0_2.md` auf `.md` korrigiert; keine offene Aktion.
- **PSV-001 (aus WP-088, non-blocking):** per-Schritt-Evidenz-Tiefe der öffentlichen Validierung begrenzt, außer WP-102 wird ausdrücklich hochgestuft.

## DE – Findings / EN – Findings

| ID | Severity | Area | Finding | Recommendation | 0.7 impact | v1.0 impact |
|---|---|---|---|---|---|---|
| PCS-001 | info | Versioning | Konventionen stabil; volle v1.x-Zusage erst mit v1.0 (ADR-0031) | so belassen; kein v1.0-Claim | non-blocking | tracked |
| PCS-002 | low | Manifest naming | 2 stale `.yaml`-Referenzen vs. kanonisches `.md` | in dieser Review korrigiert | none (behoben) | none |
| PSV-001 | info | Validation evidence | öffentliche Validierung PASS WITH NOTES, Evidenz-Tiefe begrenzt | optional via WP-102 (mit Ventil) | non-blocking | tracked |

Keine high/blocker Findings. Kein REWORK/STOP-Grund.

## DE – Auswirkungen auf Foundation 0.7

WP-101 ist **erfüllt** — letzter inhaltlicher release-blocking Baustein. Blocking Kern: 098/099/100/101 (done) · 104 · 105. **WP-102 und WP-103 müssen nicht aktiviert werden** — die Review offenbart keinen release-blocking Evidenz-Depth- oder Adoption-Grund; sie bleiben optional. Nächster Schritt: WP-104.

## EN – Impact on Foundation 0.7

WP-101 is **fulfilled** — the last content-level release-blocking piece. Blocking core: 098/099/100/101 (done) · 104 · 105. **WP-102 and WP-103 need not be activated** — the review reveals no release-blocking evidence-depth or adoption reason; they stay optional. Next step: WP-104.

## DE – Auswirkungen auf den v1.0-Pfad

Das Kriterium „Adapter-Konventionen stabil über ≥ 2 Releases" steigt ehrlich von `partially met` auf **`met with notes`** — vier Releases unveränderter, konsistenter Konventionen. Note: künftige Änderungen governed über ADR-0031; volle v1.x-Zusage erst mit v1.0. Kein v1.0-Claim.

## EN – Impact on the v1.0 Path

The "adapter conventions stable across ≥ 2 releases" criterion honestly moves from `partially met` to **`met with notes`** — four releases of unchanged, consistent conventions. Note: future changes governed via ADR-0031; full v1.x promise only at v1.0. No v1.0 claim.

## DE – Nicht-Ziele / EN – Non-Goals

Keine neuen Adapter-Features, keine große Konventions-Neustrukturierung, keine neue Adapter-Version, kein v1.0-Claim, keine aktive v1.x-Garantie, keine Release Prep, kein „für immer eingefroren".

## DE – Nächster Schritt / EN – Next Step

**NDF-WP-104 – Foundation 0.7 Release Readiness Review.**
