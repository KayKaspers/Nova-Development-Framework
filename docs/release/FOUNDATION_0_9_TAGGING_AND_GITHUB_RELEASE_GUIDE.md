# Foundation 0.9 Tagging and GitHub Release Guide

## DE – Zweck

Manuelle Anleitung für den **Human Maintainer** zum Taggen und Veröffentlichen von Foundation 0.9. Der Implementation Agent führt diese Schritte nicht aus — Tag und Release sind ausschließlich menschliche Aktionen.

## EN – Purpose

Manual guide for the **Human Maintainer** to tag and publish Foundation 0.9. The Implementation Agent does not execute these steps — tag and release are human-only actions.

## DE – Status

**Historischer Referenz-Guide (post-release).** `v0.9.0-foundation` wurde am 2026-07-10 getaggt (annotated, → Commit `e735041`) und als GitHub Pre-Release veröffentlicht; per `gh` read-only verifiziert. Tag **nicht** neu erstellen oder verschieben. Diese Anleitung bleibt als Referenz für künftige Releases erhalten. Foundation 0.9 ist nicht v1.0 und kein v1.0 Release Candidate.

## EN – Status

**Historical reference guide (post-release).** `v0.9.0-foundation` was tagged (annotated, → commit `e735041`) and published as a GitHub pre-release on 2026-07-10; verified read-only via `gh`. Do **not** recreate or move the tag. Retained for reference for future releases. Foundation 0.9 is not v1.0 and no v1.0 release candidate.

## DE – Geplanter Tag / EN – Planned Tag

```text
v0.9.0-foundation   (annotated Tag)
```

## DE – Geplanter Release-Titel / EN – Planned Release Title

```text
Nova Development Framework v0.9.0 Foundation
```

## DE – Release-Typ / EN – Release Type

```text
Pre-release
```

## DE – Voraussetzungen / EN – Prerequisites

- Go/No-Go-Checkliste vollständig mit **GO** abgeschlossen (`FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md`).
- WP-127- und WP-128-Stand sind committet und gepusht.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt.
- `v0.9.0-foundation` existiert noch nicht.

## DE – Manuelle Schritte / EN – Manual Steps

Nur Dokumentation — **nicht durch den Implementation Agent ausführen**:

```bash
git status
git checkout main
git pull origin main
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
git tag --list v0.9.0-foundation
git tag -a v0.9.0-foundation -m "Nova Development Framework v0.9.0 Foundation"
git push origin v0.9.0-foundation
```

GitHub Pre-Release manuell im UI (**Releases → Draft a new release**, Tag `v0.9.0-foundation`, Target `main`, „Set as a pre-release") oder als vom Human Maintainer entschiedener CLI-Schritt (nur Human-Maintainer-Option, nicht ausführen):

```bash
gh release create v0.9.0-foundation --title "Nova Development Framework v0.9.0 Foundation" --notes-file docs/release/FOUNDATION_0_9_RELEASE_NOTES.md --prerelease
```

## DE – Nachprüfung / EN – Verification

- [ ] Release erscheint auf GitHub als **Pre-release** mit Tag `v0.9.0-foundation` auf `main`.
- [ ] Release-Titel ist „Nova Development Framework v0.9.0 Foundation".
- [ ] Tag ist **annotated** (`git cat-file -t v0.9.0-foundation` → `tag`).
- [ ] Release Body enthält „This is not a v1.0 release.", die v1.x-Nicht-aktiv-Aussage und „No active Claude Skills Pack".
- [ ] Public-Quality-Gate-Action des Release-Commits ist grün.
- [ ] `git tag` zeigt `v0.1.0-foundation` bis `v0.9.0-foundation`.

## DE – Was nicht automatisiert werden darf / EN – What Must Not Be Automated

```text
Do not run release commands from an implementation agent.
Only the Human Maintainer may create, push or publish the release tag.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills; keine GitHub-API-Schreibaktion durch den Implementation Agent (ADR-0032 bleibt bindend).

## DE – Rollback-Hinweis / EN – Rollback Note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht veröffentlicht:** Release löschen, dann Tag löschen und neu setzen:

```bash
git tag -d v0.9.0-foundation
git push origin :refs/tags/v0.9.0-foundation
```

- **Bereits öffentlich genutzt:** Tag nicht mehr verschieben — stattdessen Korrektur-Release (z. B. `v0.9.1-foundation`). Kein History-Rewrite.

## DE – Post-Release-Follow-up / EN – Post-Release Follow-up

Nach Tag + Release: **NDF-WP-133 – Foundation 0.9 Post-Release Status Cleanup** (Muster wie 043/056/069/083/096/106/119) — Foundation 0.9 auf released/published heben, Tag und GitHub-Release-Metadaten read-only verifizieren, Go/No-Go und diesen Guide als historisch markieren. WP-125/129/130/131/132 bleiben davon unberührt (optional).

## EN – Post-Release Follow-up

After tag + release: **NDF-WP-133 – Foundation 0.9 Post-Release Status Cleanup** — lift Foundation 0.9 to released/published, verify tag and GitHub release metadata read-only, mark go/no-go and this guide as historical. WP-125/129/130/131/132 stay untouched (optional).
