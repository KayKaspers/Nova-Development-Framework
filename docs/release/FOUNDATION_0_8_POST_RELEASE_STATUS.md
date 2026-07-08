# Foundation 0.8 Post-Release Status

## DE – Zweck

Dieses Dokument hält den read-only verifizierten Post-Release-Status von Foundation 0.8 fest (NDF-WP-119) und dokumentiert den Übergang von „release-prepared / tag pending" auf „released / published". Es wurde **keine** Tag-, Release- oder GitHub-Schreibaktion durchgeführt.

## EN – Purpose

This document records the read-only verified post-release status of Foundation 0.8 (NDF-WP-119) and the transition from "release-prepared / tag pending" to "released / published". **No** tag, release, or GitHub write action was performed.

## DE – Status

**Released / published** als `v0.8.0-foundation` Foundation Pre-Release am 2026-07-08. Nicht v1.0, kein v1.0 Release Candidate, keine aktive volle v1.x-Kompatibilitätszusage, kein aktives Claude Skills Pack.

## EN – Status

**Released / published** as the `v0.8.0-foundation` foundation pre-release on 2026-07-08. Not v1.0, no v1.0 release candidate, no active full v1.x compatibility promise, no active Claude Skills Pack.

## DE – Verifizierter Tag

`v0.8.0-foundation` existiert, **annotated tag** (`git cat-file -t` → `tag`), peelt auf den WP-115-Release-Prep-Commit `a39f50b` („docs(release): prepare foundation 0.8 release"). Ältere Foundation-Tags (0.1–0.7) unverändert.

## EN – Verified Tag

`v0.8.0-foundation` exists, **annotated tag**, peeling to the WP-115 release-prep commit `a39f50b`. Older foundation tags (0.1–0.7) unchanged.

## DE – Verifizierter GitHub Release

GitHub Pre-Release „Nova Development Framework v0.8.0 Foundation" existiert und wurde read-only per `gh` verifiziert.

## EN – Verified GitHub Release

The GitHub pre-release "Nova Development Framework v0.8.0 Foundation" exists and was verified read-only via `gh`.

## DE – Release-Metadaten / EN – Release Metadata

```text
tagName:         v0.8.0-foundation
name:            Nova Development Framework v0.8.0 Foundation
isPrerelease:    true
isDraft:         false
targetCommitish: main
publishedAt:     2026-07-08
```

## DE – Tag-Prüfung

Tag-Typ **annotated** (bevorzugt). Ziel-Commit korrekt (`a39f50b`, WP-115). Kein Retag, kein Force-Push, keine Korrektur nötig.

## EN – Tag Verification

Tag type **annotated** (preferred). Target commit correct (`a39f50b`, WP-115). No retag, no force-push, no correction needed.

## DE – Release-Body-Prüfung

Der Release-Body enthält die Pflichtaussagen: „This is not a v1.0 release.", „The full v1.x compatibility promise is not active before a future v1.0 release." und „No active Claude Skills Pack is created; the MVP exists as design only." Bestätigt.

## EN – Release Body Verification

The release body contains the mandatory statements: "This is not a v1.0 release.", "The full v1.x compatibility promise is not active before a future v1.0 release.", and "No active Claude Skills Pack is created; the MVP exists as design only." Confirmed.

## DE – Release-blocking Work Packages

Alle erledigt: WP-108 Scope Lock · WP-109 Context Economy Concept · WP-110 Skill Security Policy / ADR-0032 · WP-111 Skills Pack MVP Design · WP-113 Context Pack Template & Prompt Modes · WP-114 Release Readiness Review (GO WITH NOTES) · WP-115 Release Prep · WP-119 Post-Release Status Cleanup (dieses WP).

## EN – Release-Blocking Work Packages

All complete: WP-108/109/110/111/113/114/115 and WP-119 (this WP).

## DE – Optionale Work Packages

Optional und **nicht aktiviert**: WP-112 (Skills MVP Implementation, nur per Human-Maintainer-Scope-Change), WP-116 (Skill-to-Cursor-Export-Assessment), WP-117 (Workflow-Builder-Evaluation), WP-118 (Docs-Polish-Skill-Evaluation).

## EN – Optional Work Packages

Optional and **not activated**: WP-112/116/117/118.

## DE – Skill-Pack-Status

**Kein aktives Claude Skills Pack.** Das Skills-MVP existiert ausschließlich als Design (WP-111). Dateisystemprüfung: kein `.claude`-Verzeichnis, keine `.claude/skills`, keine `SKILL.md`, keine neuen Skill-Scripts.

## EN – Skill Pack Status

**No active Claude Skills Pack.** The skills MVP exists only as design (WP-111). Filesystem check: no `.claude` directory, no `.claude/skills`, no `SKILL.md`, no new skill scripts.

## DE – v1.0-Abgrenzung

Foundation 0.8 ist **kein v1.0-Schritt** und adressiert kein offenes v1.0-Kriterium direkt; es verbessert die Arbeitsweise (Context Economy, Skill-Governance). Kein Dokument stellt v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv dar (ADR-0031: aktiv erst mit v1.0).

## EN – v1.0 Boundary

Foundation 0.8 is **not a v1.0 step** and addresses no open v1.0 criterion directly; it improves the way of working. No document presents v1.0 as reached or a full v1.x promise as active (ADR-0031: active only at v1.0).

## DE – Bekannte Notes / Limitations

- Foundation 0.8 ist **nicht v1.0** und kein v1.0 Release Candidate.
- Die volle v1.x-Kompatibilitätszusage ist **nicht aktiv** (erst mit einem künftigen v1.0-Release).
- Es existiert **kein aktives Claude Skills Pack**; das MVP ist nur Design.
- **WP-112 bleibt optional und nicht aktiviert.**
- Der Public Quality Gate bleibt Pflichtinvariante; der Human Maintainer kontrolliert Commit, Push, Tag und Release.

## EN – Known Notes / Limitations

Foundation 0.8 is not v1.0 and no v1.0 release candidate; the full v1.x compatibility promise is not active (only at a future v1.0 release); no active Claude Skills Pack exists (MVP is design only); WP-112 remains optional and not activated; the public quality gate remains mandatory; the human maintainer controls commit, push, tag, and release.

## DE – Keine Schreibaktionen durch dieses WP

NDF-WP-119 hat ausschließlich read-only verifiziert und die Statusdokumentation aktualisiert: **kein Tag erstellt/geändert/gepusht, kein GitHub Release erstellt/geändert, keine GitHub-API-Schreibaktion.** Der manuelle Tag und das GitHub Pre-Release wurden vom Human Maintainer durchgeführt.

## EN – No Write Actions by This WP

NDF-WP-119 only verified read-only and updated the status documentation: **no tag created/modified/pushed, no GitHub release created/modified, no GitHub API write action.** The manual tag and GitHub pre-release were performed by the human maintainer.

## DE – Nächster Schritt

Foundation 0.8 ist abgeschlossen. Nächster Kandidat (nur Kandidat, nicht scope-locked): **Foundation 0.9 – Adoption, Validation & Optional Enablement**.

## EN – Next Step

Foundation 0.8 is complete. Next candidate (candidate only, not scope-locked): **Foundation 0.9 – Adoption, Validation & Optional Enablement**.
