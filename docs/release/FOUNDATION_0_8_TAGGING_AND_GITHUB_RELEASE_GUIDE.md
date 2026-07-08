# Foundation 0.8 Tagging and GitHub Release Guide

## DE – Zweck

Manuelle Anleitung für den **Human Maintainer** zum Taggen und Veröffentlichen von Foundation 0.8. Der Implementation Agent führt diese Schritte nicht aus — Tag und Release sind ausschließlich menschliche Aktionen.

## EN – Purpose

Manual guide for the **Human Maintainer** to tag and publish Foundation 0.8. The Implementation Agent does not execute these steps — tag and release are human-only actions.

## DE – Status

**Vorbereitet (Release Prep, NDF-WP-115).** `v0.8.0-foundation` ist **noch nicht** getaggt oder veröffentlicht.

## EN – Status

**Prepared (release prep, NDF-WP-115).** `v0.8.0-foundation` is **not yet** tagged or released.

## DE – Geplanter Tag / EN – Planned Tag

```text
v0.8.0-foundation
```

## DE – Geplanter Release-Titel / EN – Planned Release Title

```text
Nova Development Framework v0.8.0 Foundation
```

## DE – Release-Typ / EN – Release Type

```text
Pre-release
```

## DE – Voraussetzungen / EN – Prerequisites

- Go/No-Go-Checkliste vollständig mit **GO** abgeschlossen (`FOUNDATION_0_8_GO_NO_GO_CHECKLIST.md`).
- WP-115-Stand ist committet und gepusht.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt.
- `v0.8.0-foundation` existiert noch nicht.

## DE – Manuelle Schritte / EN – Manual Steps

Nur Dokumentation — **nicht durch den Implementation Agent ausführen**:

```powershell
git status
git checkout main
git pull origin main
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
git tag --list v0.8.0-foundation
git tag -a v0.8.0-foundation -m "Nova Development Framework v0.8.0 Foundation"
git push origin v0.8.0-foundation
```

GitHub Pre-Release manuell im UI (**Releases → Draft a new release**, Tag `v0.8.0-foundation`, Target `main`, „Set as a pre-release") oder als vom Human Maintainer entschiedener CLI-Schritt (nur Human-Maintainer-Option, nicht ausführen):

```powershell
gh release create v0.8.0-foundation --title "Nova Development Framework v0.8.0 Foundation" --notes-file docs/release/FOUNDATION_0_8_RELEASE_NOTES.md --prerelease
```

## DE – Nachprüfung / EN – Verification

- [ ] Release erscheint auf GitHub als **Pre-release** mit Tag `v0.8.0-foundation` auf `main`.
- [ ] Release-Titel ist „Nova Development Framework v0.8.0 Foundation".
- [ ] Release Body enthält „This is not a v1.0 release." und die v1.x-Nicht-aktiv-Aussage.
- [ ] Public-Quality-Gate-Action des Release-Commits ist grün.
- [ ] `git tag` zeigt `v0.1.0-foundation` bis `v0.8.0-foundation`.

## DE – Was nicht automatisiert werden darf / EN – What Must Not Be Automated

```text
Do not run release commands from an implementation agent.
Only the Human Maintainer may create, push or publish the release tag.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills; keine GitHub-API-Schreibaktion durch den Implementation Agent.

## DE – Rollback-Hinweis / EN – Rollback Note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht veröffentlicht:** Release löschen, dann Tag löschen und neu setzen:

```powershell
git tag -d v0.8.0-foundation
git push origin :refs/tags/v0.8.0-foundation
```

- **Bereits öffentlich genutzt:** Tag nicht mehr verschieben — stattdessen Korrektur-Release (z. B. `v0.8.1-foundation`). Kein History-Rewrite.

## DE – Post-Release-Follow-up / EN – Post-Release Follow-up

Nach Tag + Release: ein Post-Release-Status-Cleanup-WP (Kandidat **NDF-WP-119**, Muster wie 043/056/069/083/096/106) — Foundation 0.8 auf released/published heben, Tag und GitHub-Release-Metadaten read-only verifizieren, Go/No-Go und diesen Guide als historisch markieren. WP-116/117/118 bleiben davon unberührt (optional reserviert).

## EN – Post-Release Follow-up

After tag + release: a post-release status cleanup WP (candidate **NDF-WP-119**, pattern like 043/056/069/083/096/106) — lift Foundation 0.8 to released/published, verify tag and GitHub release metadata read-only, mark go/no-go and this guide as historical. WP-116/117/118 stay untouched (reserved as optional).
