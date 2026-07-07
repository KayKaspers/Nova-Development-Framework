# WP-096 – Foundation 0.6 Post-Release Status Cleanup Notes

## Summary

`v0.6.0-foundation` wurde read-only verifiziert (erstmals per GitHub CLI — `gh` ist jetzt installiert) und alle Statusdokumente wurden von „prepared/tag pending" auf „published/released" gehoben. Foundation 0.6 ist damit vollständig abgeschlossen: Planung, Scope Lock, ADR-Entscheidung, öffentliche Validierung, Gate-Wartung, Readiness, Release Prep, manuelles Release, Cleanup. **Kein v1.0.**

## Verified Release Facts

```text
Tag:                v0.6.0-foundation
Tag object:         9e5c7e8 (annotated tag, 2026-07-07)
Target commit:      78db384 (WP-095 release prep commit)
HEAD commit:        78db384 (identisch — Tag zeigt auf den erwarteten Stand)
Origin tag present: yes (git ls-remote verified)
Release title:      Nova Development Framework v0.6.0 Foundation
isPrerelease:       true
isDraft:            false
publishedAt:        2026-07-07T09:45:34Z
targetCommitish:    main
Verification mode:  read-only (git + gh release view)
```

## Tag Verification

Annotierter Tag, lokal und remote identisch (`9e5c7e8` → Commit `78db384`); alle älteren Foundation-Tags unverändert (v0.1 `0551370`, v0.2 `d8d08a1`, v0.3 `e970ce5`, v0.4 `cac732d`, v0.5 `9aa5660`). Kein Tag verschoben.

## GitHub Release Verification

Per `gh release view` (read-only): Titel korrekt, Pre-release, kein Draft, Target main. **Body-Prüfung:** enthält die Pflichtaussage „This is not a v1.0 release." ✅ — der Body ist allerdings **minimal** (nur diese eine Zeile; kein Verweis auf die Release Notes, keine Highlights). Kein STOP-Grund (Titel korrekt, keine privaten Daten, keine Secrets, Kernaussage vorhanden), aber als optionaler Follow-up notiert (siehe unten).

## Quality Gate

strict: passed (0 errors, 0 warnings); self-test: passed — vor und nach dem Cleanup.

## Files Updated

`CHANGELOG.md` (0.6 → Published + WP-096-Zeile) · `README.md` (DE/EN → veröffentlicht; Go/No-Go-Link entfernt, Release-Notes-/ADR-/v1.0-Pfad-Links erhalten; 0.5 unverändert) · `FOUNDATION_0_6_RELEASE_NOTES.md` (Kopf → published mit Release-Fakten; Known Limitations unverändert) · `FOUNDATION_0_6_RELEASE_CRITERIA.md` (Go/No-Go durchgegangen + finaler Tag/Release abgehakt mit Verifikationsdetails) · `FOUNDATION_0_6_GO_NO_GO_CHECKLIST.md` + `FOUNDATION_0_6_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` (archived/historical-Banner) · `FOUNDATION_0_6_WORK_PACKAGES.md` (WP-095 done, Release Execution completed, Cleanup in WP-096) · `FOUNDATION_0_6_PLAN.md` (Status DE/EN → Released) · `NEXT_PHASE_FOUNDATION_0_6.md` · diese Note.

## Status Changes

Alle „prepared/tag pending/für das geplante"-Formulierungen in aktuellen Einstiegspunkten auf „published/veröffentlicht" gehoben; historische Formulierungen nur noch in den archivierten Prozessdokumenten (als solche markiert).

## Known Limitations Retained

Unverändert sichtbar in den Release Notes: PSV-001 (per-Schritt-Belege begrenzt, v1.0-tracked), QGM-003 (Gate-Log-Echo, operational note), ADR-Migration deferred + Alt-Kollision historisch, WP-091/092/093 optional offen, Website/i18n/v1.0-RC/Rewrite deferred, **kein v1.0**.

## What Was Not Changed

Kein Tag/Release erstellt oder geändert (nur read-only GETs); historische Dokumente (Readiness Review, ältere WP-Notes, 0.1–0.5-Dokumente) unangetastet; kein `NEXT_PHASE_FOUNDATION_0_7.md`-Stub (im Repo-Muster entstehen NEXT_PHASE-Dokumente erst mit dem Planning-WP — die 0.7-Kandidaten stehen stattdessen hier und in NEXT_PHASE_0_6); keine Script-/CI-Änderungen.

## Risks / Follow-ups

1. **Optionaler Follow-up (manuell, kosmetisch):** Der GitHub-Release-Body ist minimal — der Maintainer kann ihn per Release-Edit um den Body-Vorschlag aus den Release Notes ergänzen (Highlights + Notes-Verweis). Non-blocking; die Pflichtaussage ist vorhanden.
2. Foundation 0.6 hat darüber hinaus **keine offenen manuellen Follow-ups** (Secret seit WP-070 verifiziert, Titel korrekt).

## Next Phase Recommendation

**Foundation 0.7 Planning** (oder v1.0 Path Planning) durch Nova (ChatGPT) — Kandidaten aus WP-094/095:

1. WP-091 Checklist DE/EN: **priorisieren oder streichen** (drittes Mal optional offen — Regel analog zur früheren ADR-Entscheidung)
2. WP-093 v1.x Compatibility Policy Draft — natürlicher **ADR-0031**-Kandidat (v1.0-tracked)
3. Verbleibende v1.0-Kriterien: v1.x-Zusage, Konventions-Stabilität über weitere Releases, volles External-Validation-`met` (Detail-Feedback-Template)
4. Optional: Academy Entry (WP-092-Nachfolger), Doku-/i18n-Konsolidierung

Kein 0.7-Scope festgelegt; kein v1.0.
