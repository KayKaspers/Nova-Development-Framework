# Project Brain – WP-115 Foundation 0.8 Release Prep Notes

## Summary

Foundation-0.8-Release im Full Prompt Mode vollständig vorbereitet (ohne Ausführung): Release Notes, Go/No-Go-Checkliste und Tagging-/GitHub-Release-Guide erstellt; Criteria/Roadmap/Plan/Brain/Context-Pack auf „release-prepared / tag pending" gehoben. **Kein Tag, kein Release, kein Commit.** Kein aktives Skill Pack. Kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

Foundation-0.8 Context Pack, Readiness Review (WP-114), Scope Lock/Plan/Queue/Criteria; Context Economy (WP-109), Prompt Modes + Context Pack Template (WP-113), Skill Security Policy + ADR-0032 (WP-110), Skills MVP Design (WP-111); ADR-0031/0032 + ADR-README; NEXT_PHASE_0_8; WP-114-Brain-Notiz; README, CHANGELOG, V1_0_PATH_SUMMARY. Gate strict/self-test grün, Working Tree sauber (WP-114 `a08268b`), `v0.8.0-foundation` existiert nicht.

## Release Prep result

**GO WITH NOTES** — Release Prep vollständig; tatsächlicher Tag + GitHub Pre-Release bleiben manueller Human-Maintainer-Schritt.

## Release Notes

`FOUNDATION_0_8_RELEASE_NOTES.md` (DE/EN): Status (release-prepared/tag pending), Release-Typ Pre-release, Zusammenfassung, Was-neu (WP-109/110/111/113/114), release-blocking + optionale WPs, Sicherheitsgrenzen (ADR-0032 fail closed), Skill-Pack-Status (kein aktives Pack, MVP nur Design), Context Economy, ADRs (0031/0032 accepted, nächste 0033), Known Notes/Limitations, Nicht-Ziele, Upgrade-Notizen, nächste Schritte; GitHub-Release-Body-Vorschlag mit „This is not a v1.0 release." + v1.x-nicht-aktiv-Aussage.

## Go/No-Go Checklist

`FOUNDATION_0_8_GO_NO_GO_CHECKLIST.md` (DE/EN): Vor-dem-Release-Checks (Working Tree, Branch, Gate strict/self-test, Tag existiert noch nicht), release-blocking Kriterien (108–115), Sicherheits-/Neutralitätskriterien, Skill-Pack-Kriterien (WP-112 optional, kein aktives Pack, keine `.claude/skills`/`SKILL.md`/neuen Scripts), v1.0-Abgrenzung, manuelle Human-Maintainer-Entscheidung (Titel geprüft, Pre-release, kein Agent-Tag/-Release), Ergebnisfeld GO/GO WITH NOTES/NO-GO.

## Tagging and GitHub Release Guide

`FOUNDATION_0_8_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` (DE/EN): geplanter Tag `v0.8.0-foundation`, Titel „Nova Development Framework v0.8.0 Foundation", Pre-release; Voraussetzungen; manuelle Schritte (nur Doku, nicht ausgeführt); optionaler `gh release create`-Schritt nur als Human-Maintainer-Option; Pflichtwarnung „Do not run release commands from an implementation agent"; Nachprüfung; Rollback; Post-Release-Follow-up (Kandidat NDF-WP-119, WP-116/117/118 unberührt).

## Release Criteria updates

WP-115 als vorbereitet abgehakt; finaler Tag/Release + manuelles Go/No-Go bleiben offen; Klarstellung „release-prepared / tag pending, nicht released bis manueller Human-Maintainer-Release". Kein Release-/v1.0-Claim.

## Roadmap / Plan / Brain updates

Queue: WP-115 erledigt, Post-Release-Cleanup-Kandidat NDF-WP-119 genannt. Plan-Status: 115 erledigt/release-prepared. NEXT_PHASE_0_8: nächster Schritt manueller Human-Maintainer-Release → WP-119. Alle WPs außer manuellem Tag/Release erledigt.

## Context Pack updates

`CONTEXT_PACK_FOUNDATION_0_8.md`: Phasenstatus release-prepared/tag pending; WP-115 als letztes done; WP-115 in Queue done; Compact Context History um WP-114/115 ergänzt; Next Prompt Recommendation = manueller Release, dann Full Prompt für WP-119.

## README / CHANGELOG / v1.0 path

README (DE/EN): Foundation 0.8 „vorbereitet für `v0.8.0-foundation`" (release-prepared/tag pending, nicht released), Links auf Release Notes/Go-No-Go. CHANGELOG: WP-115-Zeile unter „Foundation 0.8 Scope Locked" (weiterhin Unreleased). V1_0_PATH_SUMMARY (DE+EN): 0.8 release-prepared/tag pending, kein v1.0-Schritt, keine aktive v1.x-Zusage.

## Known notes / limitations

Bis zum manuellen Release bestehen: 0.8 nicht released; nicht v1.0; volle v1.x-Zusage nicht aktiv; WP-112 optional/nicht aktiviert; kein aktives Skill Pack (MVP nur Design); Skill-Implementierung nur per Human-Maintainer-Scope-Change; Gate Pflicht; Human Maintainer kontrolliert Commit/Push/Tag/Release.

## What was not done

Kein Commit, kein Push, kein Tag, kein Release, keine GitHub-API-Schreibaktion; keine Skills/`.claude/skills`/`SKILL.md`/Scripts; keine WP-112/116/117/118-Aktivierung; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt. Tag-Prüfung: `v0.8.0-foundation` existiert nicht.

## Risks

Gering: „release-prepared/tag pending" muss beim Post-Release-Cleanup (WP-119) auf „released/published" gehoben werden. Tag/Release bleibt manuelle Human-Maintainer-Aktion; die Warnung „nur Human Maintainer" ist im Tagging-Guide prominent. Der GitHub-Release-Body muss beide Pflichtaussagen enthalten.

## Recommendation

**GO WITH NOTES** — Release Prep abgeschlossen; danach manuelles Go/No-Go + Tag + GitHub Pre-Release durch den Human Maintainer, dann Post-Release-Cleanup (WP-119).

## Compact Context Summary

Foundation 0.8 (`v0.8.0-foundation`) Release Prep **abgeschlossen** (WP-115): Release Notes + Go/No-Go-Checkliste + Tagging-Guide erstellt; Criteria/Roadmap/Plan/Brain/Context-Pack/README/CHANGELOG/V1_0_PATH auf „release-prepared / tag pending". Alle release-blocking WPs (108/109/110/111/113/114/115) erledigt; offen nur der manuelle Tag + GitHub Pre-Release durch den Human Maintainer. WP-112/116/117/118 optional, nicht aktiviert; kein aktives Skill Pack (MVP nur Design). ADR-0031+0032 Accepted, nächste 0033. Gate strict/self-test grün; `v0.8.0-foundation` existiert noch nicht. Danach Post-Release-Cleanup-Kandidat NDF-WP-119. Kein Release, kein v1.0, keine aktive volle v1.x-Zusage.
