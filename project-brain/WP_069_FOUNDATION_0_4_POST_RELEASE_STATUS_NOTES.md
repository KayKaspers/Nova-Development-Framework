# Project Brain – WP-069 Foundation 0.4 Post-Release Status Notes

## Stand

`v0.4.0-foundation` ist veröffentlicht. Verifiziert per Read-only-Prüfung:

- Tag existiert lokal und remote. **Annotierter** Tag (`git tag -a`), Tag-Objekt-SHA `610b39f`; `v0.4.0-foundation^{commit}` = `cac732d` = der WP-068-Release-Prep-Commit = HEAD. **Der Tag darf nicht verschoben oder neu erstellt werden.**
- GitHub Pre-Release existiert (öffentliche GitHub-API, read-only): Titel korrekt „Nova Development Framework v0.4.0 Foundation", `prerelease: true`, `draft: false`, published 2026-07-04. Titel diesmal korrekt (wie schon bei 0.3, anders als 0.2).

## Release Title

Nova Development Framework v0.4.0 Foundation — read-only bestätigt, keine manuelle Korrektur nötig.

## Bereinigte Statusdokumente

- `CHANGELOG.md`: 0.4.0-foundation von „prepared / tag pending" auf **Released** (2026-07-04).
- `README.md`: Status DE/EN von „für den geplanten Release vorbereitet / prepared for the planned" auf „veröffentlicht / published" (Go/No-Go-Link entfernt, Release-Notes-Link erhalten).
- Release Notes: Kopfzeile auf „veröffentlicht am / published on 2026-07-04 (GitHub Pre-Release)".
- Go/No-Go-Checkliste: als archived/post-release markiert (bleibt Vorlage).
- Tagging-Guide: Post-release note (Titel read-only verifiziert, Tag nicht bewegen).
- Release Criteria: finaler Tag/Release abgehakt, Go/No-Go-Durchgang bestätigt.
- `FOUNDATION_0_4_PLAN.md`: Status „Scope locked" → „Released as v0.4.0-foundation".
- Roadmap-Queue: WP-068 auf done/veröffentlicht, Post-Release-Cleanup in WP-069.
- Historische Dokumente (Readiness Review WP-067, ältere Brain-Notes) bewusst unverändert.

## Keine Release-Aktionen

Kein Tag erstellt/verschoben/gepusht, kein GitHub Release erstellt/geändert, keine schreibende GitHub-API-Aktion. Einzige API-Nutzung: read-only GET zur Verifikation.

## Verbliebene Known Limitations

Optionale WPs 061/062/063/066 offen; deferred 064/065; restliche i18n-Arbeiten; Security-/Gate-Prompts nur DE/EN-Kern; ADR-Nummernkollisionen; kein v1.0.

## Manuelle Follow-ups

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen (weiterhin nicht von hier verifizierbar; Prüfung über GitHub-UI oder CI-Log-Notice).
2. Foundation-0.2-Release-Titel auf GitHub korrigieren (aus WP-043 offen).

## Empfehlung für nächste Phase

Vorschlag (nicht verbindlich): Foundation 0.5 Planning bzw. Post-Release Maintenance — offene optionale WPs 061–063/066, Independent Adapter Run (064), Docs Export/Website Concept (065). Kein 0.5-Scope verbindlich festgelegt.
