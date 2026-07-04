# Project Brain – WP-056 Foundation 0.3 Post-Release Status Notes

## Stand

`v0.3.0-foundation` ist veröffentlicht. Verifiziert per Read-only-Prüfung:

- Tag existiert lokal und remote. Es ist ein **annotierter** Tag (`git tag -a`), daher weicht der Tag-Objekt-SHA vom Commit-SHA ab; `v0.3.0-foundation^{commit}` = `e970ce5` = der WP-055-Release-Prep-Commit. **Der Tag darf nicht verschoben oder neu erstellt werden.**
- GitHub Pre-Release existiert (öffentliche GitHub-API, read-only): Titel korrekt „Nova Development Framework v0.3.0 Foundation", `prerelease: true`, published 2026-07-04. Diesmal ist der Titel korrekt (anders als beim 0.2-Release).

## Bereinigte Statusangaben

- `CHANGELOG.md`: 0.3.0-foundation von „prepared / tag pending" auf **Released** (2026-07-04).
- `README.md`: Status DE/EN von „für den geplanten Release vorbereitet / prepared for the planned" auf „veröffentlicht / published" (Go/No-Go-Link entfernt, Release-Notes-Link erhalten).
- Release Notes: Kopfzeile auf „veröffentlicht am / published on 2026-07-04".
- Go/No-Go-Checkliste: als archived/post-release markiert (bleibt Vorlage).
- Tagging-Guide: Post-release note „do not recreate or move the tag".
- Release Criteria: finaler Tag/Release abgehakt, Go/No-Go-Durchgang bestätigt.
- `FOUNDATION_0_3_PLAN.md`: Status „Scope locked" → „Released as v0.3.0-foundation".
- Roadmap-Queue + Release-Prep-Progress auf done/released.
- Historische Dokumente (Readiness Review WP-054, ältere Brain-Notes WP-041/043/044/055) bewusst unverändert — beschreiben den damaligen Stand.

## Keine Release-Aktionen

Kein Tag erstellt/verschoben/gepusht, kein GitHub Release erstellt/geändert, keine schreibende GitHub-API-Aktion. Einzige API-Nutzung: read-only GET auf den Releases-Endpunkt zur Verifikation.

## Bekannte offene Punkte (manuell / später)

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen (macht den new-file check in CI scharf).
2. Foundation-0.2-Release-Titel auf GitHub korrigieren (aus WP-043 offen).
3. Optionale i18n-WPs 048–051, Adapter Conventions Polish, unabhängiger Adapter-Testlauf, WP-053 (deferred).

## Nächster empfohlener Schritt

Foundation 0.4 Planning bzw. Post-Release Maintenance.
