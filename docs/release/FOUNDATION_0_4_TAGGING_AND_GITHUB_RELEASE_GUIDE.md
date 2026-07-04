# Foundation 0.4 – Tagging & GitHub Release Guide

Anleitung für den **Human Maintainer**. Der Implementation Agent führt diese Schritte nicht aus — Tag und Release sind ausschließlich menschliche Aktionen. / Guide for the human maintainer; tag and release are human-only actions.

## 1. Voraussetzungen / Prerequisites

- Go/No-Go-Checkliste vollständig mit **GO** abgeschlossen (`FOUNDATION_0_4_GO_NO_GO_CHECKLIST.md`).
- WP-068-Stand ist committet und gepusht.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (empfohlen, macht den new-file neutrality check in CI scharf).

## 2. Lokale Prüfungen / Local checks

```powershell
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
git status
```

Erwartung: Gate passed, self-test passed, Working Tree sauber.

## 3. main aktualisieren / Update main

```powershell
git checkout main
git pull origin main
git log --oneline -3
```

Erwartung: Der WP-068-Commit ist der aktuelle Stand von `origin/main`.

## 4. Prüfen, ob der Tag bereits existiert / Check whether the tag already exists

```powershell
git tag --list v0.4.0-foundation
git ls-remote --tags origin v0.4.0-foundation
```

Wenn der Tag bereits existiert: **nicht verschieben, nicht neu erstellen.**

## 5. Tag erstellen / Create the tag

```powershell
git tag -a v0.4.0-foundation -m "Nova Development Framework v0.4.0 Foundation"
```

## 6. Tag pushen / Push the tag

```powershell
git push origin v0.4.0-foundation
```

## 7. GitHub Pre-Release erstellen / Create the GitHub pre-release

Auf GitHub: **Releases → Draft a new release**

```text
Tag:    v0.4.0-foundation
Target: main
Type:   Pre-release  (Häkchen "Set as a pre-release")
```

## 8. Release Title

```text
Nova Development Framework v0.4.0 Foundation
```

**Sorgfältig prüfen:** kein Secret-Name, kein Platzhalter, kein falscher Text als Titel (Lehre aus dem 0.2-Release, dessen Titel versehentlich falsch war).

## 9. Release Body

Aus `docs/release/FOUNDATION_0_4_RELEASE_NOTES.md` ableiten — der fertige Vorschlag steht dort im Abschnitt „GitHub Release Body (Vorschlag / suggested)". Keine privaten Begriffe einfügen.

## 10. Nachprüfung / Verification

- [ ] Release erscheint auf GitHub als **Pre-release** mit Tag `v0.4.0-foundation` auf `main`.
- [ ] Release-Titel ist korrekt.
- [ ] Public-Quality-Gate-Action des Release-Commits ist grün.
- [ ] README, Release Notes und Changelog sind über die GitHub-Oberfläche korrekt lesbar.
- [ ] `git tag` zeigt `v0.1.0-foundation`, `v0.2.0-foundation`, `v0.3.0-foundation`, `v0.4.0-foundation`.

## 11. Rollback-Hinweis / Rollback note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht veröffentlicht:** Release löschen, dann Tag löschen und neu setzen:

```powershell
git tag -d v0.4.0-foundation
git push origin :refs/tags/v0.4.0-foundation
```

- **Bereits öffentlich genutzt:** Tag nicht mehr verschieben — stattdessen Korrektur-Release (z. B. `v0.4.1-foundation`). Kein History-Rewrite.
