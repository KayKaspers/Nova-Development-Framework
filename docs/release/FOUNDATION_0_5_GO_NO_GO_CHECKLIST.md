# Foundation 0.5 Go/No-Go Checklist

> **Status: abgeschlossen / archived (post-release).** Der Release `v0.5.0-foundation` wurde am 2026-07-07 veröffentlicht. Diese Checkliste bleibt als historischer Nachweis und Vorlage für künftige Releases erhalten — keine neuen Aktionen daraus ableiten.

> DE: Finale Prüfung vor Tag und GitHub Release `v0.5.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release. / EN: Final check before tag and GitHub release `v0.5.0-foundation`. Performed by the human maintainer; the Implementation Agent creates neither tag nor release.

## 1. Working Tree

```powershell
git status
```

- [ ] Working Tree sauber.

## 2. Branch

```powershell
git branch --show-current
```

- [ ] Branch ist `main`.

## 3. Latest Commit

```powershell
git log -1 --oneline
```

- [ ] Der letzte Commit enthält den WP-082-Release-Prep-Stand.

## 4. Public Quality Gate (strict)

```powershell
python scripts/check_public_quality.py --strict
```

Alternativ / alternatively: `py scripts/check_public_quality.py --strict`

- [ ] Ergebnis: `Public quality gate passed.` (0 errors, 0 warnings)

## 5. Self-Test

```powershell
python scripts/check_public_quality.py --self-test
```

- [ ] Ergebnis: `self-test passed`

## 6. New-file Neutrality Check

- [ ] Die Gate-Ausgabe meldet Scan-Modus „tracked + new/untracked files (new-file neutrality check active)".

## 7. Custom Denylist / GitHub Secret

- [ ] GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (seit WP-070 verifiziert) bzw. lokale Denylist geprüft — private Begriffe niemals ins Repo schreiben.

## 8. Release Notes

- [ ] `docs/release/FOUNDATION_0_5_RELEASE_NOTES.md` vorhanden und aktuell (DE/EN), inkl. aller Known Limitations aus dem Readiness Review (WP-081).

## 9. Release Criteria

- [ ] `docs/release/FOUNDATION_0_5_RELEASE_CRITERIA.md` aktuell; release-blocking Kriterien bis auf finalen Tag/Release erfüllt.

## 10. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.5.0-foundation]` mit WP-071 bis WP-082; Status „tag pending".

## 11. README Status

- [ ] README stellt Foundation 0.5 als „für den geplanten Release vorbereitet" dar — **nicht** als released.

## 12. Keine v1.0-Darstellung

- [ ] Foundation 0.5 wird nirgends als v1.0 oder v1.0-nah dargestellt.

## 13. WP-074-Notes als Known Limitations

- [ ] PASS WITH NOTES ist korrekt dokumentiert: summarisch/neutralisiert, privater Referenzkontext, kein vollständiger öffentlicher Runbook-Lauf — sichtbar in den Release Notes.

## 14. v1.0-Draft-Abgrenzung

- [ ] Der v1.0 Readiness Criteria Draft ist überall als Entwurf/Messlatte erkennbar — kein v1.0-Claim, kein Release Candidate.

## 15. Neutralität

- [ ] Keine privaten Projektnamen, keine Reviewer-Identität, keine Kontaktwege, keine echten Domains, keine Secret-Werte in getrackten Dateien.

## 16. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 17. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 18. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 19. Release Title geprüft

```powershell
git tag --list v0.5.0-foundation
```

- [ ] Release Title lautet „Nova Development Framework v0.5.0 Foundation" — **kein** Secret-Name, kein Platzhalter, kein falscher Text (Lehre aus dem 0.2-Titel-Fehler).

## 20. Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung:        GO | GO WITH NOTES | NO-GO
Begründung:          __________
Freigabe durch:      __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_5_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
