# Project Brain – WP-104 Foundation 0.7 Release Readiness Notes

## Summary

Release-Readiness-Gate für Foundation 0.7 durchgeführt: **GO WITH NOTES.** Alle release-blocking Kriterien außer WP-104 (dieses Review) und WP-105 sind erfüllt und nachgewiesen. Foundation 0.7 ist bereit für die Release-Vorbereitung (WP-105), aber bewusst mit non-blocking Notes. Kein Release, kein v1.0, keine aktive volle v1.x-Zusage.

## Inputs reviewed

Scope Lock, Plan, Work-Package-Queue, 0.7-Release-Criteria, NEXT_PHASE_0_7, README, CHANGELOG; die vier Evidenz-Dokumente WP-099 (Checklist-Decision + TRANSLATION_STATUS), WP-100 (ADR-0031 + Index), WP-101 (Convention Stability Review + Adapter v0.2 + v1.0-Draft + Path Summary); Quality Gate (strict/self-test); Kontroll-Greps und temporärer Link-Check.

## Release-blocking WPs

098 Scope Lock ✅ · 099 Checklist DE/EN (Option B) ✅ · 100 v1.x Compatibility Policy (ADR-0031 Accepted) ✅ · 101 Convention Stability (Stable with notes) ✅ · 104 Readiness Review ✅ (dieses Dokument, GO WITH NOTES) · 105 Release Prep ⬜ offen.

## WP-099 result

Option B — Checklist DE/EN bleibt optional mit finaler Begründung. Eindeutige Entscheidung, kein Auto-Carry, kein Folge-WP; Restlücken ehrlich als optionaler i18n-Backlog sichtbar. Kein 0.7-Blocker. Der seit 0.4 mitgeschleppte Dauerläufer ist damit sauber geschlossen.

## WP-100 result

ADR-0031 v1.x Compatibility Policy (Status Accepted) als Source of Truth; keine separate Policy-Datei. Fünf Kompatibilitätskategorien; volle v1.x-Zusage aktiviert **erst mit v1.0** — nirgends als aktiv dargestellt. v1.0-Kriterium `not met` → `met with notes`. Nächste freie ADR-Nummer 0032.

## WP-101 result

Convention Stability: Stable with notes. Kernbeleg Git-Historie — `PROJECT_ADAPTER_CONVENTIONS.md` seit WP-059 über 0.4→0.7 unverändert. Ein low-Drift (`.yaml`→`.md`, PCS-002) behoben; keine high/blocker Findings. „stable" ≠ „frozen forever" (PCS-001), künftige Änderungen governed über ADR-0031. Adapter-Maturity/Convention-Stability `met with notes`.

## Optional/deferred WPs

WP-102 External Validation Evidence Depth Pass: optional, **nicht aktiviert** (Upgrade-Ventil nicht gezogen); adressiert PSV-001, sonst non-blocking/v1.0-tracked. WP-103 Academy Entry Decision: optional, **nicht aktiviert**. Doku-/i18n-Konsolidierung optional/deferred. Deferred: Website, volle i18n, ADR-Massenmigration, v1.0-RC, Rewrite, App-Features, volle externe Zertifizierung.

## Known non-blockers

WP-099 Option B (i18n-Backlog); WP-100 volle v1.x-Zusage erst mit v1.0 (v1.0-tracked); WP-101 stable with notes/nicht frozen (PCS-001); PCS-002 behoben; PSV-001 Evidenz-Tiefe (v1.0-tracked, optional via WP-102); QGM-003 Gate-ERROR im CI-Log (operational note); WP-102/103 nicht aktiviert; ADR-Massenmigration/Website/volle i18n/v1.0-RC deferred; optionaler v0.6-Release-Body-Polish (manual follow-up). 0.7 nicht v1.0, nicht released.

## Quality Gate

`--strict`: passed (0 errors, 0 warnings, 3 INFO-Notices — Scan-Modus, lokal keine Denylist; Secret wirkt in CI). `--self-test`: passed. New-file neutrality check aktiv; die in diesem Review erzeugten Dateien wurden mitgescannt. Kontroll-Greps sauber (keine Foundation-0.7-Release- oder v1.0-Behauptung; nur Negationen/„erst mit v1.0"). Temporärer Link-Check über 9 Kern-Dateien: 0 broken, nichts committet.

## Release recommendation

**GO WITH NOTES** — bereit für WP-105 Release Prep; Notes ausschließlich non-blocking und bewusst.

## Next step

**NDF-WP-105 – Foundation 0.7 Release Prep** (Release Notes inkl. Known Limitations, Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für voraussichtlich `v0.7.0-foundation`).

## Compact Context Summary

Foundation 0.7 (scope-locked, v1.0 Path Consolidation & Compatibility Governance); 0.6 released (`v0.6.0-foundation`, 2026-07-07). WP-104 Readiness Review: **GO WITH NOTES** — alle blocking WPs außer 104/105 erfüllt und nachgewiesen (098/099 Option B/100 ADR-0031 met with notes/101 Stable with notes). WP-102/103 optional, nicht aktiviert. Notes non-blocking: volle v1.x-Zusage erst mit v1.0, Convention Stability „stable with notes" ≠ frozen, PSV-001 v1.0-tracked, QGM-003 operational note. Gate strict/self-test grün (0/0/3 notices). Nächste freie ADR-Nummer 0032. Nächster Schritt WP-105 Release Prep. Kein v1.0, kein Release.
