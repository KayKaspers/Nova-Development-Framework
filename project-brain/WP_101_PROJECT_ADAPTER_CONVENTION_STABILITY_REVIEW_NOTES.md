# Project Brain – WP-101 Project Adapter Convention Stability Review Notes

## Summary

Release-blocking Convention Stability Review durchgeführt: **Stable with notes.** Die Adapter-Konventionen sind seit WP-059 (Foundation 0.4) über vier Releases (0.4/0.5/0.6 released, 0.7 gelockt) unverändert und in sich konsistent. Ein low-Drift gefunden und korrigiert. Das v1.0-Kriterium „Adapter-Konventionen stabil" steigt von `partially met` auf `met with notes`. Kein v1.0-Claim.

## Inputs reviewed

Git-Historie der Konventionsdokumente (Kernbeleg), Conventions-Doku, Adapter v0.2, Validierungsläufe (WP-047/074/088), Backlog, ADR-0031, v1.0-Draft, 0.7-Scope-Lock/Criteria.

## Artifact inventory

`PROJECT_ADAPTER_CONVENTIONS.md` (WP-059, seither unverändert = 4 Releases), `PROJECT_ADAPTER_V0_2.md` (stabil seit WP-059, ein low-Drift korrigiert), `SAMPLEPROJECT_ADAPTER_VALIDATION.md`, zwei independent-runs (PASS WITH NOTES), Backlog (kein offener Konventionspunkt), SampleProject-Fixture (Pfad stabil), ADR-0031 (Governed).

## Stability dimensions

12 Dimensionen bewertet: 9× stable, 3× stable with notes (independent validation evidence depth, versioning/compatibility, v1.0 readiness relevance). Keine unstable/not-enough-evidence.

## Drift / contradiction check

Eine Konventionsquelle, keine konkurrierenden; kein Widerspruch zwischen ADR-0031 und Konventionen oder zwischen v1.0-Readiness und Adapterstand. **Ein low-Drift (PCS-002):** stale `PROJECT_MANIFEST.yaml` in Phasen-Tabelle + Ergebnisstruktur von Adapter v0.2, während Header/Conventions `.md` (Markdown kanonisch) festlegen → als redaktionelle Statusklarstellung auf `.md` angeglichen. Keine high/blocker-Widersprüche.

## Overall assessment

**Stable with notes** — ausreichend stabil für 0.7 und den v1.0-Pfad; volle v1.x-Kompatibilität bleibt governed über ADR-0031, aktiviert erst mit v1.0. Nicht „für immer eingefroren".

## Findings / notes

PCS-001 (info): stabil, aber volle v1.x-Zusage erst mit v1.0. PCS-002 (low, behoben): 2 stale `.yaml`-Referenzen → `.md`. PSV-001 (info, aus WP-088): Evidenz-Tiefe begrenzt, optional via WP-102. Keine high/blocker.

## Impact on Foundation 0.7

WP-101 erfüllt — **alle inhaltlichen blocking WPs sind damit done** (098/099/100/101). **WP-102/WP-103 nicht aktiviert** — kein release-blocking Grund; bleiben optional. Offen: WP-104 (Readiness) → WP-105 (Release Prep).

## Impact on v1.0 path

Kriterium „Adapter-Konventionen stabil" `partially met` → **`met with notes`**; Kategorie 3 (Project Adapter Maturity) ebenfalls auf `met with notes`. Path Summary DE+EN aktualisiert. Kein v1.0-Claim.

## Files changed

Neu: Review-Dokument, diese Note. Geändert: `PROJECT_ADAPTER_V0_2.md` (2 stale `.yaml`→`.md`), v1.0-Draft (2 Zeilen), Path Summary, 0.7-Criteria/Queue/Scope-Lock/Plan (WP-101 done), CHANGELOG, NEXT_PHASE_0_7. README unverändert.

## What was not done

Keine neuen Adapter-Features, keine Konventions-Neustrukturierung, keine neue Adapter-Version, kein v1.0-Claim, keine aktive v1.x-Garantie, keine WP-102/103-Aktivierung, keine Release Prep.

## Risks

Gering: „Stable with notes" könnte als „eingefroren" gelesen werden → im Review explizit verneint (künftige Änderungen governed über ADR-0031). PSV-001-Evidenz-Tiefe bleibt optionaler v1.0-tracked Punkt.

## Next step

**NDF-WP-104 – Foundation 0.7 Release Readiness Review.**

## Compact Context Summary

Foundation 0.7 (scope-locked, v1.0 Path Consolidation & Compatibility Governance); 0.6 released. Alle vier inhaltlichen blocking WPs done: 099 (Checklist Option B), 100 (ADR-0031 v1.x Compatibility Policy, met with notes), **101 (Convention Stability: Stable with notes — Konventionen seit 0.4 über 4 Releases unverändert; low-Drift `.yaml`→`.md` korrigiert; Kriterium + Adapter-Maturity `met with notes`)**. WP-102/103 optional, nicht aktiviert. Offen: WP-104 (Readiness) → WP-105 (Release Prep). Nächste freie ADR-Nummer: 0032. Kein v1.0, kein Release.
