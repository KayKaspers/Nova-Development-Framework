# Foundation 0.7 – Tagging & GitHub Release Guide

Anleitung für den **Human Maintainer**. Der Implementation Agent führt diese Schritte nicht aus — Tag und Release sind ausschließlich menschliche Aktionen. / Guide for the human maintainer; tag and release are human-only actions.

> **Status: vorbereitet (Release Prep, NDF-WP-105).** `v0.7.0-foundation` ist **noch nicht** getaggt oder veröffentlicht. / Prepared; `v0.7.0-foundation` not yet tagged or released.

## 1. Voraussetzungen / Prerequisites

- Go/No-Go-Checkliste vollständig mit **GO** abgeschlossen (`FOUNDATION_0_7_GO_NO_GO_CHECKLIST.md`, 26 Punkte).
- WP-105-Stand ist committet und gepusht.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (Wirksamkeit seit WP-089 belegt).

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

Erwartung: Der WP-105-Commit ist der aktuelle Stand von `origin/main`.

## 4. Prüfen, ob der Tag bereits existiert / Check whether the tag already exists

```powershell
git tag --list v0.7.0-foundation
git ls-remote --tags origin v0.7.0-foundation
```

Wenn der Tag bereits existiert: **nicht verschieben, nicht neu erstellen.**

## 5. Tag erstellen / Create the tag

```powershell
git tag -a v0.7.0-foundation -m "Nova Development Framework v0.7.0 Foundation"
```

## 6. Tag pushen / Push the tag

```powershell
git push origin v0.7.0-foundation
```

## 7. GitHub Pre-Release erstellen / Create the GitHub pre-release

Auf GitHub: **Releases → Draft a new release**

```text
Tag:    v0.7.0-foundation
Target: main
Type:   Pre-release  (Häkchen "Set as a pre-release")
```

## 8. Release Title

```text
Nova Development Framework v0.7.0 Foundation
```

**Sorgfältig prüfen:** kein Secret-Name, kein Platzhalter, kein falscher Text als Titel (Lehre aus dem 0.2-Release).

## 9. Release Body

Aus `docs/release/FOUNDATION_0_7_RELEASE_NOTES.md` ableiten — der fertige Vorschlag steht dort im Abschnitt „GitHub Release Body (Vorschlag / suggested)". Keine privaten Begriffe einfügen. **Der Body muss klar enthalten:**

- „This is not a v1.0 release."
- „The full v1.x compatibility promise is not active before a future v1.0 release."

## 10. Nachprüfung / Verification

- [ ] Release erscheint auf GitHub als **Pre-release** mit Tag `v0.7.0-foundation` auf `main`.
- [ ] Release-Titel ist korrekt.
- [ ] Release Body enthält „This is not a v1.0 release" und die v1.x-Nicht-aktiv-Aussage.
- [ ] Public-Quality-Gate-Action des Release-Commits ist grün.
- [ ] README, Release Notes und Changelog sind über die GitHub-Oberfläche korrekt lesbar.
- [ ] `git tag` zeigt `v0.1.0-foundation` bis `v0.7.0-foundation`.

## 11. Rollback-Hinweis / Rollback note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht veröffentlicht:** Release löschen, dann Tag löschen und neu setzen:

```powershell
git tag -d v0.7.0-foundation
git push origin :refs/tags/v0.7.0-foundation
```

- **Bereits öffentlich genutzt:** Tag nicht mehr verschieben — stattdessen Korrektur-Release (z. B. `v0.7.1-foundation`). Kein History-Rewrite.

## 12. Post-Release-Cleanup / Post-release cleanup

Nach Tag + Release: Post-Release-Status-Cleanup als eigenes WP (Muster WP-043/056/069/083/096) — Changelog/README/Release-Notes von „tag pending/vorbereitet" auf „released" heben, Tag und Release read-only verifizieren, Go/No-Go und diesen Guide als historisch markieren.
