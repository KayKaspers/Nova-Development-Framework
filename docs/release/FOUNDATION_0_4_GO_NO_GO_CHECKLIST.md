# Foundation 0.4 Go/No-Go Checklist

> **Status: abgeschlossen / archived (post-release).** Der Release `v0.4.0-foundation` wurde am 2026-07-04 veröffentlicht. Diese Checkliste bleibt als Vorlage für künftige Releases erhalten.

> DE: Finale Prüfung vor Tag und GitHub Release `v0.4.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release. / EN: Final check before tag and GitHub release `v0.4.0-foundation`. Performed by the human maintainer; the Implementation Agent creates neither tag nor release.

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

- [ ] Der letzte Commit enthält den WP-068-Release-Prep-Stand.

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

- [ ] `docs/release/FOUNDATION_0_4_RELEASE_NOTES.md` vorhanden und aktuell (DE/EN), inkl. Known Limitations.

## 8. Release Criteria

- [ ] `docs/release/FOUNDATION_0_4_RELEASE_CRITERIA.md` aktuell; release-blocking Kriterien bis auf finalen Tag/Release erfüllt.

## 9. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.4.0-foundation]` mit WP-057 bis WP-068; Status „tag pending".

## 10. README Status

- [ ] README stellt Foundation 0.4 als „für den geplanten Release vorbereitet" dar — **nicht** als released, **nicht** als v1.0.

## 11. Project Adapter Conventions Link

- [ ] `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` ist vorhanden und verlinkt.

## 12. Prompt Priority Pass Link

- [ ] `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md` ist vorhanden und verlinkt.

## 13. Keine v1.0-Behauptung

- [ ] Keine Datei behauptet v1.0-Reife.

## 14. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 15. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 16. Release Title geprüft

- [ ] Release Title lautet „Nova Development Framework v0.4.0 Foundation" — **kein** Secret-Name, kein falscher Text.

## 17. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 18. Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung:        GO | GO WITH NOTES | NO-GO
Begründung:          __________
Freigabe durch:      __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_4_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
