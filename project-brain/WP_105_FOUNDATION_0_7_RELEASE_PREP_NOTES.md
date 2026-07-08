# Project Brain – WP-105 Foundation 0.7 Release Prep Notes

## Summary

Release Prep für Foundation 0.7 (`v0.7.0-foundation`) vorbereitet: Release Notes, 26-Punkte-Go/No-Go-Checkliste und Tagging-/GitHub-Release-Guide erstellt; Release Criteria, CHANGELOG, README, WP-Queue und Plan auf „prepared / tag pending" gehoben. **Kein Release ausgeführt** — Tag und GitHub Pre-Release bleiben manuelle Human-Maintainer-Aktionen. Kein v1.0, keine aktive volle v1.x-Zusage. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

Readiness Review (WP-104, GO WITH NOTES) + Brain-Notiz; Release Criteria, Scope Lock, WP-Queue, Plan, NEXT_PHASE_0_7; ADR-0031, Convention Stability Review, v1.0-Draft, Path Summary; README, CHANGELOG; als Vorlage die 0.6-Release-Artefakte (Notes/Go-No-Go/Tagging-Guide).

## Release Notes

`docs/release/FOUNDATION_0_7_RELEASE_NOTES.md` (DE/EN): v1.0 Path Consolidation & Compatibility Governance; ADR-0031 Accepted als Source of Truth (volle v1.x-Zusage erst mit v1.0); Convention Stability „Stable with notes" (nicht frozen, low-Drift `.yaml`→`.md` behoben); Checklist DE/EN Option B; WP-102/103 nicht aktiviert; PSV-001 (Known Limitation, v1.0-tracked) + QGM-003 (Operational Note); Public Quality Gate/Neutralität als Pflichtinvarianten; genau ein Future-Candidate-Hinweis (Agent Enablement & Context Economy inkl. kleinem public-neutralen Claude Skills Pack — kein Scope); GitHub-Release-Body-Vorschlag mit „This is not a v1.0 release." + v1.x-Nicht-aktiv-Aussage.

## Go/No-Go Checklist

`docs/release/FOUNDATION_0_7_GO_NO_GO_CHECKLIST.md`: 26 Punkte — Working Tree/Branch/Commit, Gate strict/self-test, new-file check, Secret, Release Notes/Criteria/CHANGELOG/README, keine v1.0-/released-Darstellung, ADR-0031 Accepted, v1.x nicht aktiv, Convention Stability with notes, Option B, WP-102/103 nicht aktiviert, PSV-001, QGM-003, Neutralität, Tag/Release nur durch Human Maintainer, Release-Titel geprüft, finale GO/NO-GO-Zeile.

## Tagging Guide

`docs/release/FOUNDATION_0_7_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`: Voraussetzungen, lokale Prüfungen, main aktualisieren, Tag-Existenz prüfen (nicht verschieben), Tag `v0.7.0-foundation` erstellen/pushen, GitHub Pre-Release, Titel „Nova Development Framework v0.7.0 Foundation", Body aus Release Notes, Nachprüfung, Rollback, Post-Release-Cleanup-Hinweis. Alle Befehle nur dokumentiert, nicht ausgeführt.

## Release Criteria

WP-105 (Release Notes/Go-No-Go/Tagging-Guide) abgehakt. Offen: finaler Tag + GitHub Pre-Release (Human Maintainer). Kein v1.0-Claim, keine aktive volle v1.x-Zusage.

## CHANGELOG / README

CHANGELOG: `[Unreleased] – Scope Locked` → `[0.7.0-foundation] – 2026-07-08`, Status „Prepared for Foundation pre-release — tag pending. Not v1.0. Full v1.x compatibility promise activates only with a future v1.0 release." WP-097–105-Einträge erhalten; WP-105-Zeile ergänzt (inkl. Future-Candidate-Hinweis als nicht-Scope). README: Foundation 0.7 „vorbereitet für das geplante `v0.7.0-foundation`" (nicht released), Foundation 0.6 bleibt „veröffentlicht"; Links auf Release Notes/Go-No-Go ergänzt.

## Known Limitations / Operational Notes

Volle v1.x-Zusage erst mit v1.0 (v1.0-tracked); Convention Stability „stable with notes" ≠ frozen (PCS-001); PSV-001 (Evidenz-Tiefe, v1.0-tracked, optional via WP-102); QGM-003 (Gate-ERROR im CI-Log, sofort beheben); WP-102/103 nicht aktiviert; ADR-Massenmigration/Website/volle i18n/v1.0-RC/Rewrite/App-Features/volle externe Zertifizierung deferred. 0.7 nicht v1.0, noch nicht released.

## Future Candidate

Genau ein kurzer Hinweis aufgenommen (Release Notes, WP-Queue, Plan, NEXT_PHASE): **NDF Agent Enablement & Context Economy** inkl. kleinem public-neutralen Claude Skills Pack — nur möglicher nächster Evolutionsschritt nach 0.7. **Kein Scope, kein Release-Kriterium, kein blocking WP; kein Skill-Pack/Context-Economy-Dokument in diesem WP erstellt.**

## Manual next steps

Human Maintainer: Go/No-Go-Checkliste → Tag `v0.7.0-foundation` → GitHub Pre-Release („Nova Development Framework v0.7.0 Foundation", Pre-release) → danach Post-Release-Status-Cleanup-WP (Muster 043/056/069/083/096).

## What was not done

Kein Commit/Push/Tag/Release durch den Implementation Agent; keine GitHub-API-Schreibaktion; keine CI-/Script-Änderung; keine optionalen WPs (102/103) miterledigt; kein Skill-Pack; kein Context-Economy-Dokument; kein v1.0-Claim; keine aktive volle v1.x-Zusage.

## Risks

Gering und dokumentiert: Der Future-Candidate-Hinweis könnte als Scope missverstanden werden → überall ausdrücklich als „kein Scope / kein blocking WP" markiert. „tag pending"-Status muss beim Post-Release-Cleanup auf „released" gehoben werden. Tagging bleibt manuelle Human-Maintainer-Aktion.

## Recommendation

**GO WITH NOTES** — Release Prep kann committed und gepusht werden; danach Human-Maintainer Go/No-Go + Tagging. Notes sind ausschließlich non-blocking.

## Compact Context Summary

Foundation 0.7 (`v0.7.0-foundation`) Release Prep **vorbereitet** (WP-105): Release Notes + 26-Punkte-Go/No-Go + Tagging-Guide erstellt; Criteria/CHANGELOG/README/Queue/Plan auf „prepared / tag pending". Alle blocking WPs außer finalem Tag erfüllt (098/099 Option B/100 ADR-0031 met-with-notes/101 Stable-with-notes/104 GO WITH NOTES/105 prepared). WP-102/103 optional, nicht aktiviert. Known Limitations: volle v1.x-Zusage erst mit v1.0, Convention Stability ≠ frozen, PSV-001 v1.0-tracked, QGM-003 operational note. Ein Future-Candidate-Hinweis (Agent Enablement & Context Economy + kleiner public-neutraler Claude Skills Pack — kein Scope). Gate strict/self-test grün. Nächster Schritt: manuelles Go/No-Go + Tagging durch Human Maintainer, dann Post-Release-Cleanup. Kein v1.0, noch nicht released. Nächste freie ADR-Nummer 0032.
