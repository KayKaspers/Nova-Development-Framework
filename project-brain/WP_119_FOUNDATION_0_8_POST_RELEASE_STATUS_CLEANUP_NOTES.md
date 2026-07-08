# Project Brain – WP-119 Foundation 0.8 Post-Release Status Cleanup Notes

## Summary

Foundation 0.8 read-only als veröffentlicht verifiziert und alle Statusdokumente von „release-prepared / tag pending" auf „released / published" gehoben. Tag `v0.8.0-foundation` (annotated) und GitHub Pre-Release existieren und sind korrekt. **Kein Tag/Release erstellt oder geändert.** Kein aktives Skill Pack. Kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

Read-only: `git cat-file -t`/`git rev-list`/`git show` für v0.8.0-foundation; `gh release view` (JSON + body), `gh release list`. Dokumente: Foundation-0.8 Context Pack, Release Notes/Go-No-Go/Tagging-Guide/Criteria/Readiness Review, Plan/Queue/V1_0_PATH, NEXT_PHASE, README, CHANGELOG, ADR-0031/0032/README.

## Tag verification

`v0.8.0-foundation` existiert, **annotated tag** (`git cat-file -t` → `tag`), peelt auf den WP-115-Commit `a39f50b` („docs(release): prepare foundation 0.8 release"). Ältere Foundation-Tags (0.1–0.7) unverändert. Diesmal annotated (frühere Lightweight-Nebennote entfällt).

## GitHub Release verification

`gh release view v0.8.0-foundation`: `tagName=v0.8.0-foundation`, `name="Nova Development Framework v0.8.0 Foundation"`, `isPrerelease=true`, `isDraft=false`, `targetCommitish=main`, `publishedAt=2026-07-08T18:38:42Z`. `gh release list` zeigt konsistent 0.1–0.8 als Pre-release.

## Release body verification

Der Release-Body (die vollständigen Release Notes) enthält alle Pflichtaussagen: „This is not a v1.0 release.", „The full v1.x compatibility promise is not active before a future v1.0 release." und „No active Claude Skills Pack is created; the MVP exists as design only." Bestätigt.

## Post-release status

`docs/release/FOUNDATION_0_8_POST_RELEASE_STATUS.md` (DE/EN) erstellt: verifizierter Tag/Release, Metadaten, Body-Prüfung, release-blocking + optionale WPs, Skill-Pack-Status, v1.0-Abgrenzung, Known Notes, „keine Schreibaktionen durch dieses WP".

## Release criteria updates

Status-Header DE/EN auf released/published (WP-119); Ziel-Block auf „veröffentlicht 2026-07-08"; finaler Tag/Release + Post-Release-Cleanup abgehakt; Klarstellung „released, nicht v1.0, v1.x nicht aktiv, kein aktives Skill Pack".

## Roadmap / Plan / Brain / Context Pack updates

Queue: WP-115 „Release veröffentlicht", WP-119-Zeile ergänzt (released/published); Top-Banner auf released. Plan-Status-Header auf released. NEXT_PHASE: Foundation 0.8 released, keine offenen Follow-ups, nächster Kandidat Foundation 0.9 Planning. Context Pack: Phasenstatus released/published, WP-119 als letztes done, Compact Context History + Next Prompt Recommendation aktualisiert.

## README / CHANGELOG / v1.0 path updates

README (DE/EN): Foundation 0.8 „veröffentlicht als `v0.8.0-foundation`" + Post-Release-Status-Link (0.7 bleibt veröffentlicht). CHANGELOG: `[Unreleased] – Scope Locked` → `[0.8.0-foundation] – 2026-07-08` (Published), WP-119-Zeile ergänzt. V1_0_PATH_SUMMARY (DE+EN): 0.8 released, kein v1.0-Schritt, keine aktive v1.x-Zusage.

## Skill Pack status

Dateisystemprüfung: kein `.claude`-Verzeichnis, keine `.claude/skills`, keine `SKILL.md`, keine neuen Skill-Scripts. Skills-MVP nur Design. Kein aktives Skill Pack.

## v1.0 boundary

Foundation 0.8 kein v1.0-Schritt; adressiert kein offenes v1.0-Kriterium direkt; kein Dokument stellt v1.0 als erreicht oder volle v1.x-Zusage als aktiv dar (ADR-0031: aktiv erst mit v1.0).

## Known notes / limitations

Nicht v1.0; volle v1.x-Zusage nicht aktiv; kein aktives Skill Pack (MVP nur Design); WP-112 optional/nicht aktiviert; Gate Pflicht; Human Maintainer kontrolliert Commit/Push/Tag/Release. Alle non-blocking.

## What was not done

Kein Tag/Release erstellt, geändert oder verschoben; keine GitHub-API-Schreibaktion; kein Commit/Push durch den Implementation Agent; keine History-Rewrite-/CI-/Script-Änderung; keine Skills/`.claude/skills`/`SKILL.md`/Scripts; keine WP-112/116/117/118-Aktivierung; kein v1.0-Claim.

## Risks

Gering und dokumentiert: keine offenen 0.8-blocking Follow-ups. Optional/kosmetisch: WP-112 (Skills MVP Implementation) nur per Human-Maintainer-Scope-Change. Foundation 0.9 bleibt Kandidat (nicht scope-locked).

## Recommendation

**GO WITH NOTES** — Post-Release-Cleanup sauber; Foundation 0.8 ist veröffentlicht, v1.x-Kompatibilität bleibt future-v1.0-bound, kein aktives Skill Pack, WP-112 optional. Notes ausschließlich non-blocking.

## Compact Context Summary

Foundation 0.8 **released / published** als `v0.8.0-foundation` (2026-07-08, GitHub Pre-Release; Titel „Nova Development Framework v0.8.0 Foundation", isPrerelease=true, Target main, **annotated** Tag → Commit `a39f50b`; Body enthält alle Pflichtaussagen). WP-119 hob alle 0.8-Statusdokumente von release-prepared/tag-pending auf released/published; read-only verifiziert (git + gh). Kein aktives Skill Pack (MVP nur Design); WP-112/116/117/118 optional/nicht aktiviert. Alle release-blocking WPs (108/109/110/111/113/114/115/119) done. ADR-0031+0032 Accepted, nächste 0033. Gate strict/self-test grün. Nächster Kandidat: Foundation 0.9 Planning (Adoption, Validation & Optional Enablement — kein Scope). Kein v1.0, keine aktive volle v1.x-Zusage.
