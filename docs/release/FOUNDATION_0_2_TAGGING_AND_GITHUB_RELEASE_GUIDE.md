# Foundation 0.2 – Tagging & GitHub Release Guide

> **Post-release note:** `v0.2.0-foundation` has been published (2026-07-03); do not recreate or move the tag. Diese Anleitung bleibt als Referenz für künftige Releases erhalten. / This guide remains as a reference for future releases.

Anleitung für den **Human Maintainer**. Der Implementation Agent führt diese Schritte nicht aus — Tag und Release sind ausschließlich menschliche Aktionen.

## 1. Voraussetzungen

- Go/No-Go-Checkliste vollständig mit **GO** abgeschlossen (`FOUNDATION_0_2_GO_NO_GO_CHECKLIST.md`).
- WP-041-Stand ist committet und gepusht.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (empfohlen).

## 2. Lokale Prüfungen

```powershell
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
git status
```

Erwartung: Gate passed, self-test passed, Working Tree sauber.

## 3. Commit muss auf `main` sein

```powershell
git checkout main
git pull origin main
git log --oneline -3
```

Erwartung: Der Release-Prep-Commit (WP-041) ist der aktuelle Stand von `origin/main`.

## 4. Tag erstellen

```powershell
git tag v0.2.0-foundation
```

Optional mit Annotation:

```powershell
git tag -a v0.2.0-foundation -m "Nova Development Framework v0.2.0 Foundation"
```

## 5. Tag pushen

```powershell
git push origin v0.2.0-foundation
```

## 6. GitHub Release erstellen (Pre-Release)

Auf GitHub: **Releases → Draft a new release**

```text
Tag:    v0.2.0-foundation
Target: main
Type:   Pre-release  (Häkchen "Set as a pre-release")
```

## 7. Release Title

```text
Nova Development Framework v0.2.0 Foundation
```

## 8. Release Body

Aus `docs/release/FOUNDATION_0_2_RELEASE_NOTES.md` ableiten — empfohlen: die Abschnitte *Overview*, *What is new?*, *Known Limitations* und *Recommended Next Steps* (EN zuerst, DE optional darunter). Keine privaten Begriffe einfügen.

## 9. Nachprüfung

- [ ] Release erscheint auf GitHub als **Pre-release** mit Tag `v0.2.0-foundation` auf `main`.
- [ ] Public-Quality-Gate-Action des Release-Commits ist grün.
- [ ] README, Release Notes und Changelog sind über die GitHub-Oberfläche korrekt lesbar.
- [ ] `git tag` lokal und auf GitHub zeigen `v0.1.0-foundation` und `v0.2.0-foundation`.

## 10. Rollback-Hinweis

Falls nach dem Tag ein Fehler auffällt:

- **Release-Text falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht veröffentlicht:** Release löschen, dann Tag löschen und neu setzen:

```powershell
git tag -d v0.2.0-foundation
git push origin :refs/tags/v0.2.0-foundation
```

- **Bereits öffentlich genutzt:** Tag nicht mehr verschieben — stattdessen Korrektur-Release (z. B. `v0.2.1-foundation`) vorbereiten. Kein History-Rewrite.
