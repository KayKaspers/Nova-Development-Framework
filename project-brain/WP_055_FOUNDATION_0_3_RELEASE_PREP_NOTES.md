# Project Brain – WP-055 Foundation 0.3 Release Prep Notes

## Was wurde erstellt?

- Release Notes (bilingual, alle 13 Sektionspaare): `docs/release/FOUNDATION_0_3_RELEASE_NOTES.md`
- Go/No-Go-Checkliste (17 Punkte): `docs/release/FOUNDATION_0_3_GO_NO_GO_CHECKLIST.md`
- Tagging-/GitHub-Release-Guide (11 Schritte, inkl. Rollback): `docs/release/FOUNDATION_0_3_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
- Release Criteria aktualisiert (Release-Prep-Kriterien abgehakt, finaler Tag offen): `docs/release/FOUNDATION_0_3_RELEASE_CRITERIA.md`
- Changelog: neue Sektion `[0.3.0-foundation] - 2026-07-04` mit „tag pending"-Status; WP-055-Eintrag
- README-Status DE/EN: „in Planung" → „für den geplanten Release vorbereitet" mit Links auf Release Notes + Go/No-Go

## Known Limitations (aus WP-054, in Release Notes übernommen)

Optionale i18n-WPs 048–050, ADR-Policy 051, Adapter-Conventions-Backlog, unabhängiger Adapter-Testlauf (later), WP-053 deferred, CI-Secret-Scharfschaltung, unveränderte Git-Historie, kein v1.0.

## Offene manuelle Schritte

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen.
2. WP-055 committen und pushen (nach GO).
3. Go/No-Go-Checkliste durchgehen, dann Tag `v0.3.0-foundation` + GitHub Pre-Release (nur Human Maintainer, gemäß Guide).
4. Foundation-0.2-Release-Titel auf GitHub korrigieren.

## Hinweis (Konsistenz)

Wie bei Foundation 0.2 (WP-041/043): Nach dem Tagging/Release bleibt „tag pending"/„vorbereitet" in Changelog/README kurz überholt — ein Post-Release-Cleanup analog WP-043 hebt den Status auf „released". Prüf-Dokumente enthalten bewusst keine wörtlichen privaten Suchmuster (Lehre aus WP-040/041).

## Nächste Aktion

Nova-Review → GO → Commit → Maintainer führt Go/No-Go und Tagging aus. Danach Foundation-0.3 Post-Release-Status-Cleanup (analog WP-043).
