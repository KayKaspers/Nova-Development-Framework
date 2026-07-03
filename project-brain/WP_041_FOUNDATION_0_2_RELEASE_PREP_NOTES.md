# Project Brain – WP-041 Foundation 0.2 Release Prep Notes

## Was wurde erstellt?

- Release Notes (bilingual, alle 12 Sektionspaare): `docs/release/FOUNDATION_0_2_RELEASE_NOTES.md`
- Release Criteria aktualisiert (echter 0.2-Stand, Checkboxen, manuelle Schritte, GO/NO-GO-Felder): `docs/release/FOUNDATION_0_2_RELEASE_CRITERIA.md`
- Go/No-Go-Checkliste (14 Punkte): `docs/release/FOUNDATION_0_2_GO_NO_GO_CHECKLIST.md`
- Tagging-/GitHub-Release-Guide (10 Schritte, inkl. Rollback): `docs/release/FOUNDATION_0_2_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
- Changelog: `[Unreleased]` → `[0.2.0-foundation] - 2026-07-03` mit „tag pending"-Hinweis; WP-041-Eintrag ergänzt
- README-Status verweist jetzt auf die Release Notes (DE+EN)

## Wichtiger Vorfall (behoben)

Der WP-040-Readiness-Report enthielt die Neutralitäts-Grep-Befehle **wörtlich** — inklusive der privaten Namen. Der Kontroll-Grep traf damit nach dem Commit sein eigenes Prüfprotokoll (in WP-040 unbemerkt, weil die Datei beim Final-Check noch untracked war und `git grep` nur getrackte Dateien durchsucht). In WP-041 neutralisiert. **Lehre:** Prüf-Dokumentation darf die privaten Muster nie wörtlich enthalten; die Go/No-Go-Checkliste beschreibt die Greps deshalb abstrakt über den Denylist-Mechanismus (bewusste Abweichung von der WP-041-Vorgabe, die wörtliche Snippets verlangte).

## Offene manuelle Schritte

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen.
2. WP-041 committen und pushen (nach GO).
3. Go/No-Go-Checkliste durchgehen, dann Tag + Pre-Release gemäß Guide (nur Human Maintainer).

## Nächste Aktion

Nova-Review dieses WPs → GO → Commit → Maintainer führt Go/No-Go und Tagging aus.
