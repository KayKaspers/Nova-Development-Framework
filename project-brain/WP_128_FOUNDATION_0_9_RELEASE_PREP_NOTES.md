# Project Brain – WP-128 Foundation 0.9 Release Prep Notes

## Ziel

Foundation 0.9 – Adoption, Validation & Optional Enablement dokumentarisch für den späteren manuellen Release vorbereiten (Full Prompt Mode): Release Notes, Go/No-Go-Checkliste, Tagging-/GitHub-Pre-Release-Guide, Criteria-/Roadmap-/Brain-/Context-Pack-/CHANGELOG-Updates. **Keine Veröffentlichung, kein Tag, kein Commit.**

## Input Summary

WP-127 Readiness Review: GO WITH NOTES (18-Punkte-Check, 16 Met / 2 Met with notes, keine Blocker). Alle release-blocking WPs vor WP-128 (121/122/123/124/126/127) done. ADR-0031/0032 unverändert, nächste ADR-Nummer 0033. Kein aktives Skill Pack; WP-125 optional/conditional (nicht aktiviert), WP-129 optional/nicht aktiviert. Gate strict/self-test grün; `v0.9.0-foundation` existiert nicht. **Vorprüfungs-Befund:** Working Tree enthielt die unkommitteten WP-127-Änderungen (Readiness Review + Status-Updates aus dem unmittelbar vorherigen WP dieses Workflows) — dokumentiert, nichts überschrieben/bereinigt; WP-128 baut darauf auf. Empfehlung: zwei getrennte Commits (erst WP-127, dann WP-128).

## Änderungen

Neu: `docs/release/FOUNDATION_0_9_RELEASE_NOTES.md` (DE/EN, inkl. GitHub-Release-Body-Vorschlag mit allen Pflichtaussagen), `docs/release/FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md` (Scope Lock, WP-Completion, Criteria, Known Notes, ADR-0031/0032, Skill Security, Neutralität, Changelog, Context Pack, Tagging-/Release-Readiness, Human-Maintainer-Handoff, WP-133-Readiness), `docs/release/FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` (annotated Tag `v0.9.0-foundation`, Titel „Nova Development Framework v0.9.0 Foundation", Pre-release, Befehle nur als Doku, Rollback, WP-133-Follow-up), diese Notiz. Geändert: Release Criteria (WP-128 abgehakt, „release-prepared / pending manual release"), Queue (WP-128 done, WP-133 als Post-Release-Schritt), Plan-Statuszeile, NEXT_PHASE (nächster Schritt manueller Release → WP-133), Context Pack (Phasenstatus, Last/Next WP, Queue, History, Next Prompt Recommendation), CHANGELOG (WP-128-Zeile).

## Release Prep Ergebnis

**GO WITH NOTES** — Release Prep vollständig; Foundation 0.9 ist **release-prepared / pending manual release**. Tag + GitHub Pre-Release bleiben manuelle Human-Maintainer-Schritte.

## Known Notes

Vollständig übernommen in Release Notes + Go/No-Go: nicht v1.0; kein v1.0 RC; volle v1.x-Zusage nicht aktiv; ADR-0031/0032 accepted/unverändert; kein aktives Skill Pack, keine `.claude/skills`/`SKILL.md`/Scripts; WP-125 optional/conditional; WP-129 optional/nicht aktiviert; WP-130/131/132 optional; Short-Prompt-Ersteinsatz offen; externe Validierungs-Evidenz-Tiefe v1.0-tracked; WP-133 erst post-release; Commit/Push/Tag/Release Human-Maintainer-only.

## Go/No-Go Ergebnis

Checkliste vorbereitet; erwartetes Ergebnis bei sauberem Durchlauf: `GO WITH NOTES – ready for manual release by Human Maintainer`. Finale Entscheidung liegt beim Human Maintainer.

## Nächste Human-Maintainer-Schritte

1. WP-127-Diff prüfen und committen (`docs(release): add foundation 0.9 readiness review`). 2. WP-128-Diff prüfen und committen (`docs(release): prepare foundation 0.9 release`). 3. Finale Go/No-Go-Checkliste durchgehen. 4. Annotated Tag `v0.9.0-foundation` erstellen und pushen. 5. GitHub Pre-Release „Nova Development Framework v0.9.0 Foundation" erstellen. 6. WP-133 Post-Release Cleanup starten.

## Nächste NDF-Schritte nach manuellem Release

**NDF-WP-133 – Foundation 0.9 Post-Release Status Cleanup:** Tag + GitHub Release read-only verifizieren, Statusdokumente auf released/published heben, Go/No-Go + Tagging-Guide als historisch markieren. Danach Foundation-1.0- oder Folgephasen-Planung als Kandidat (nicht vorgegriffen).

## Rückmeldung an Nova-kompatible Zusammenfassung

WP-128 Release Prep abgeschlossen mit GO WITH NOTES; Foundation 0.9 release-prepared / pending manual release; alle Known Notes übernommen; keine Blocker; WP-125/129 nicht aktiviert; keine Veröffentlichung durch den Implementation Agent; nächster Schritt manueller Human-Maintainer-Release, dann WP-133.

## Compact Context Summary

Foundation 0.9 (`v0.9.0-foundation`) Release Prep **abgeschlossen** (WP-128, 2026-07-10): Release Notes + Go/No-Go-Checkliste + Tagging-Guide erstellt; Criteria/Queue/Plan/NEXT_PHASE/Context-Pack/CHANGELOG auf „release-prepared / pending manual release". Alle release-blocking WPs (121/122/123/124/126/127/128) erledigt; offen nur der manuelle annotated Tag + GitHub Pre-Release durch den Human Maintainer (Working Tree enthält WP-127+WP-128 unkommittet — zwei getrennte Commits empfohlen). Danach WP-133 Post-Release Cleanup. WP-125/129/130/131/132 optional, nicht aktiviert; kein aktives Skill Pack; ADR-0031/0032 unverändert, nächste 0033. Kein Release, kein v1.0, keine aktive volle v1.x-Zusage.
