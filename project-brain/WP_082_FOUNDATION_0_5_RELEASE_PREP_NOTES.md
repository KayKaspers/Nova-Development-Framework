# Project Brain – WP-082 Foundation 0.5 Release Prep Notes

## Was vorbereitet wurde

- **Release Notes** (bilingual, 12 Sektionspaare + GitHub-Release-Body-Vorschlag): `docs/release/FOUNDATION_0_5_RELEASE_NOTES.md` — External Validation & 1.0 Path Hardening; WP-074 als PASS WITH NOTES mit allen Einschränkungen; v1.0-Draft klar als Messlatte ohne Freigabe; „tag pending".
- **Go/No-Go-Checkliste** (20 Punkte): `FOUNDATION_0_5_GO_NO_GO_CHECKLIST.md` — inkl. der 0.5-spezifischen Punkte 12–14 (keine v1.0-Darstellung, WP-074-Notes als Known Limitations sichtbar, v1.0-Draft-Abgrenzung) und Titel-Prüfung (Punkt 19, Lehre aus 0.2).
- **Tagging-/Release-Guide** (12 Schritte inkl. Rollback + Post-Release-Cleanup-Hinweis): `FOUNDATION_0_5_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` — Tag `v0.5.0-foundation`, Titel „Nova Development Framework v0.5.0 Foundation", Pre-release.
- **Release Criteria:** Release-Prep-Kriterien abgehakt; offen nur finaler Tag/Release.
- **Changelog:** `[Unreleased]` → `[0.5.0-foundation] - 2026-07-07` mit „tag pending" und „Not v1.0"; WP-082-Zeile ergänzt; WP-071–082-Einträge erhalten.
- **README:** Status DE/EN von „scope-locked" auf „für das geplante Pre-Release vorbereitet"; v1.0-Pfad-Link mit Nicht-erreicht-Klarstellung erhalten.
- **Queue:** WP-082 als vorbereitet markiert; WP-075/077/078 optional offen, WP-076-Sonderregel sichtbar, WP-080 deferred.

## Known Limitations (aus WP-081 vollständig übernommen)

WP-074 PASS WITH NOTES (summarisch/neutralisiert; privater Referenzkontext; kein öffentlicher Runbook-Lauf; External Validation im v1.0-Draft nur `partially met`; öffentlicher Fixture-Lauf v1.0-tracked/0.6-Kandidat); optionale WPs 075/077/078 offen; **WP-076: in 0.6 priorisieren oder ehrlich streichen**; WP-080 deferred; i18n-Rest; Security-Prompts DE/EN-Kern; v1.x-Kompatibilitätszusage offen; kein v1.0; Historie unverändert.

## Manuelle nächste Schritte

1. WP-082 committen und pushen (nach GO).
2. Go/No-Go-Checkliste durchgehen (20 Punkte), dann Tag + GitHub Pre-Release gemäß Guide — **Titel sorgfältig prüfen**.
3. Danach Post-Release-Status-Cleanup als eigenes WP (Muster WP-069): Statusheben, read-only-Verifikation, Archiv-Markierungen.
4. In der 0.6-Planung: WP-076-Entscheidung + öffentlicher Fixture-/Runbook-Lauf als Kandidaten.

## Hinweis (Konsistenz)

Wie bei 0.2/0.3/0.4: Nach dem Tagging bleibt „tag pending"/„vorbereitet" kurz überholt — der Post-Release-Cleanup hebt den Status auf „released". Datum 2026-07-07 im Changelog bei späterem Tagging anpassen.

## Empfohlene Entscheidung

GO WITH NOTES — Artefakte vollständig und ehrlich; Notes sind die manuellen Schritte plus die dokumentierten Known Limitations.
