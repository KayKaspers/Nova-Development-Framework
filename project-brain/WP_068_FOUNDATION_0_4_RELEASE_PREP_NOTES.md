# Project Brain – WP-068 Foundation 0.4 Release Prep Notes

## Was wurde vorbereitet?

- Release Notes (bilingual, 12 Sektionspaare + GitHub-Release-Body-Vorschlag): `docs/release/FOUNDATION_0_4_RELEASE_NOTES.md`
- Go/No-Go-Checkliste (18 Punkte, inkl. Release-Titel-Prüfung): `docs/release/FOUNDATION_0_4_GO_NO_GO_CHECKLIST.md`
- Tagging-/GitHub-Release-Guide (11 Schritte, inkl. Rollback + Titel-Warnung): `docs/release/FOUNDATION_0_4_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
- Release Criteria aktualisiert (Release-Prep-Kriterien abgehakt, finaler Tag offen)
- Changelog: `[Unreleased]` → `[0.4.0-foundation] - 2026-07-04` mit „tag pending"-Status; WP-068-Eintrag
- README-Status DE/EN: „in Planung" → „für den geplanten Release vorbereitet" mit Links

## Known Limitations (aus WP-067, in Release Notes übernommen)

Optionale WPs 061/062/063/066 offen; deferred 064/065; restliche i18n-Arbeiten; Security-/Gate-Prompts nur DE/EN-Kern; CI-Secret-Scharfschaltung; unveränderte Git-Historie; ADR-Nummernkollisionen; kein v1.0.

## Offene manuelle Schritte

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen (weiterhin nicht von hier verifizierbar — Prüfung über GitHub-UI oder CI-Log-Notice).
2. WP-068 committen und pushen (nach GO).
3. Go/No-Go-Checkliste durchgehen, dann Tag `v0.4.0-foundation` + GitHub Pre-Release (nur Human Maintainer, gemäß Guide) — **Release-Titel sorgfältig prüfen** (Lehre aus dem 0.2-Titel-Fehler).
4. Foundation-0.2-Release-Titel auf GitHub korrigieren.

## Hinweis (Konsistenz)

Wie bei 0.2/0.3: Nach dem Tagging/Release bleibt „tag pending"/„vorbereitet" in Changelog/README kurz überholt — ein Post-Release-Cleanup analog WP-043/WP-056 hebt den Status auf „released".

## Nächste Aktion

Nova-Review → GO → Commit → Maintainer führt Go/No-Go und Tagging aus. Danach Foundation-0.4 Post-Release-Status-Cleanup.
