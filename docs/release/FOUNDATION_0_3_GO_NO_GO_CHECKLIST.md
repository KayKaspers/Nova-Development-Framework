# Foundation 0.3 Go/No-Go Checklist

> **Status: abgeschlossen / archived (post-release).** Der Release `v0.3.0-foundation` wurde am 2026-07-04 veröffentlicht. Diese Checkliste bleibt als Vorlage für künftige Releases erhalten.

> DE: Finale Prüfung vor Tag und GitHub Release `v0.3.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release. / EN: Final check before tag and GitHub release `v0.3.0-foundation`. Performed by the human maintainer; the Implementation Agent creates neither tag nor release.

## 1. Working Tree

```powershell
git status
git branch --show-current
```

- [ ] Working Tree sauber; Branch ist `main`.

## 2. Latest Commit

```powershell
git log -1 --oneline
```

- [ ] Der letzte Commit enthält den WP-055-Release-Prep-Stand.

## 3. Public Quality Gate (strict)

```powershell
python scripts/check_public_quality.py --strict
```

Alternativ / alternatively: `py scripts/check_public_quality.py --strict`

- [ ] Ergebnis: `Public quality gate passed.` (0 errors, 0 warnings)

## 4. Self-Test

```powershell
python scripts/check_public_quality.py --self-test
```

- [ ] Ergebnis: `self-test passed`

## 5. New-file Neutrality Check

- [ ] Die Gate-Ausgabe meldet Scan-Modus „tracked + new/untracked files (new-file neutrality check active)".

## 6. Custom Denylist

- [ ] Lokale Denylist (`.ndf/public-neutrality-terms.local.txt`, ungetrackt) oder GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` geprüft/gesetzt (private Begriffe niemals ins Repo schreiben).

## 7. Release Notes

- [ ] `docs/release/FOUNDATION_0_3_RELEASE_NOTES.md` vorhanden und aktuell (DE/EN), inkl. Known Limitations.

## 8. Release Criteria

- [ ] `docs/release/FOUNDATION_0_3_RELEASE_CRITERIA.md` aktuell; release-blocking Kriterien bis auf finalen Tag/Release erfüllt.

## 9. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.3.0-foundation]` mit WP-044 bis WP-055; Status „tag pending".

## 10. README Status

- [ ] README stellt Foundation 0.3 als „für den geplanten Release vorbereitet" dar — **nicht** als released, **nicht** als v1.0.

## 11. SampleProject Validation Link

- [ ] `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md` ist vorhanden und verlinkt (PASS WITH NOTES).

## 12. Keine v1.0-Behauptung

- [ ] Keine Datei behauptet v1.0-Reife.

## 13. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 14. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 15. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 16. Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung:        GO | GO WITH NOTES | NO-GO
Begründung:          __________
Freigabe durch:      __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_3_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
