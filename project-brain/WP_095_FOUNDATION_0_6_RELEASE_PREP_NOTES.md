# Project Brain – WP-095 Foundation 0.6 Release Prep Notes

## Was vorbereitet wurde

- **Release Notes** (bilingual, 14 Sektionspaare + GitHub-Release-Body-Vorschlag): `docs/release/FOUNDATION_0_6_RELEASE_NOTES.md` — Adoption Confidence & Governance Hardening; ADR Policy adopted (ab ADR-0031, Migration deferred); WP-088 PASS WITH NOTES; WP-089 Evidence strong; WP-090 not needed, WP-087 skipped; „tag pending", „kein v1.0".
- **Go/No-Go-Checkliste** (22 Punkte): `FOUNDATION_0_6_GO_NO_GO_CHECKLIST.md` — inkl. der 0.6-spezifischen Punkte 13–16 (PSV-001 als Known Limitation, QGM-003 als Operational Note, WP-090 not needed, ADR adopted + Migration deferred) und Titel-Prüfung (Punkt 21).
- **Tagging-/Release-Guide** (12 Schritte inkl. Rollback + Post-Release-Cleanup): `FOUNDATION_0_6_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` — Tag `v0.6.0-foundation`, Titel „Nova Development Framework v0.6.0 Foundation", Pre-release; Nachprüfung verlangt ausdrücklich „This is not a v1.0 release" im Body.
- **Release Criteria:** Release-Prep-Kriterien abgehakt; offen nur finaler Tag/Release + Invarianten.
- **Changelog:** Unreleased-Sektion → `[0.6.0-foundation] - 2026-07-07` mit „tag pending" und „Not v1.0"; WP-084–095-Einträge erhalten; WP-095-Zeile ergänzt.
- **README:** Status DE/EN von „scope-locked" auf „für das geplante Pre-Release vorbereitet"; ADR-Policy- und v1.0-Pfad-Links erhalten; 0.5 unverändert released.
- **Queue:** WP-095 als vorbereitet; 087 skipped, 090 not needed, 091–093 optional, deferred unverändert.

## Known Limitations / Operational Notes (aus WP-094 vollständig übernommen)

**PSV-001** (Known Limitation, v1.0-tracked): öffentliche Validierung positiv/unabhängig, per-Schritt-Belege nicht vollständig. **QGM-003** (Operational Note): Gate-ERROR kann bei echtem Treffer den Begriff im CI-Log zeigen — sofort beheben. Dazu: ADR-Migration deferred + Alt-Kollision historisch; WP-091 optional offen (**0.7: Priorisieren-oder-Streichen erwägen — drittes Mal**); WP-092 offen; WP-093 offen (ADR-0031-Kandidat); Website/i18n/v1.0-RC/Rewrite/App-Features deferred; kein v1.0; Historie unverändert.

## Manuelle nächste Schritte

1. WP-095 committen und pushen (nach GO).
2. Go/No-Go durchgehen (22 Punkte), dann Tag + GitHub Pre-Release gemäß Guide — **Titel prüfen**, Body mit „not a v1.0 release".
3. Danach Post-Release-Status-Cleanup als eigenes WP (Muster WP-083).
4. Foundation-0.7-Planung: WP-091-Entscheidung, WP-093/ADR-0031, verbleibende v1.0-Kriterien.

## Hinweis (Konsistenz)

Wie bei 0.2–0.5: Nach dem Tagging bleibt „tag pending"/„vorbereitet" kurz überholt — der Post-Release-Cleanup hebt den Status auf „released". Datum 2026-07-07 bei späterem Tagging anpassen.

## Empfohlene Entscheidung

GO WITH NOTES — Artefakte vollständig, ehrlich und neutral; Notes sind die manuellen Schritte plus PSV-001/QGM-003 und die dokumentierten Known Limitations.
