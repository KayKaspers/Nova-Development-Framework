# Project Brain – WP-043 Foundation 0.2 Post-Release Status Notes

## Stand

`v0.2.0-foundation` ist veröffentlicht: Tag existiert lokal und remote (zeigt auf den WP-041-Commit `d8d08a1`), GitHub **Pre-Release** wurde am 2026-07-03 angelegt (per Read-only-Abfrage der öffentlichen GitHub-API verifiziert). **Der Tag darf nicht neu erstellt oder verschoben werden.**

## Bereinigte Statusangaben

- `CHANGELOG.md`: 0.2.0-foundation von „prepared / tag pending" auf **Released** (2026-07-03).
- `README.md`: Status DE/EN von „release in Vorbereitung" auf „veröffentlicht / published" (Links auf Release Notes erhalten).
- `FOUNDATION_0_2_PLAN.md`: Status „In development" → „Released as v0.2.0-foundation (pre-release)".
- Release Notes: Veröffentlichungsdatum ergänzt; Go/No-Go-Checkliste als archived/post-release markiert (bleibt Vorlage); Tagging-Guide mit Post-release note („do not recreate or move the tag"); Release Criteria: erledigte manuelle Schritte abgehakt.
- Roadmap-Progress-Dateien (Release Prep + Readiness) auf done/released aktualisiert.
- Historische Dokumente (Readiness Review WP-040, ältere Brain-Notes) bewusst unverändert — sie beschreiben den damaligen Stand.

## Gefundener manueller Korrekturbedarf

Der GitHub-Release-**Titel** lautet versehentlich `NDF_PUBLIC_NEUTRALITY_DENYLIST` (offenbar Copy-Paste beim Anlegen) statt „Nova Development Framework v0.2.0 Foundation". Der Release-**Body** ist korrekt und enthält keine privaten Begriffe — es wurde nur der öffentliche Secret-*Name* eingefügt, kein Inhalt. **Manuell auf GitHub den Release-Titel editieren** (kein Git-Eingriff nötig).

## Offene Folgearbeiten

1. Release-Titel auf GitHub korrigieren (siehe oben).
2. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/verifizieren.
3. Post-Release: Foundation 0.3 Planning bzw. Maintenance — Adapter-Praxistest, ADR Consolidation, i18n-Voll-Pass.

## Nächster empfohlener Schritt

WP-043 committen/pushen, Release-Titel korrigieren, dann Foundation 0.3 Planning mit Nova (ChatGPT) starten.
