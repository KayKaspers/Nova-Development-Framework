# Foundation 0.6 Go/No-Go Checklist

> DE: Finale Prüfung vor Tag und GitHub Release `v0.6.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release. / EN: Final check before tag and GitHub release `v0.6.0-foundation`. Performed by the human maintainer; the Implementation Agent creates neither tag nor release.

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

- [ ] Der letzte Commit enthält den WP-095-Release-Prep-Stand.

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

- [ ] GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (seit WP-070 verifiziert; Wirksamkeit seit WP-089 mit Evidence strong belegt) — private Begriffe niemals ins Repo schreiben.

## 8. Release Notes

- [ ] `docs/release/FOUNDATION_0_6_RELEASE_NOTES.md` vorhanden und aktuell (DE/EN), inkl. PSV-001, QGM-003 und aller Known Limitations aus dem Readiness Review (WP-094).

## 9. Release Criteria

- [ ] `docs/release/FOUNDATION_0_6_RELEASE_CRITERIA.md` aktuell; release-blocking Kriterien bis auf finalen Tag/Release erfüllt.

## 10. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.6.0-foundation]` mit WP-084 bis WP-095; Status „tag pending", „Not v1.0".

## 11. README Status

- [ ] README stellt Foundation 0.6 als „für den geplanten Release vorbereitet" dar — **nicht** als released.

## 12. Keine v1.0-Darstellung

- [ ] Foundation 0.6 wird nirgends als v1.0, v1.0-nah oder v1.0 Release Candidate dargestellt.

## 13. WP-088-Note als Known Limitation

- [ ] PSV-001 ist korrekt dokumentiert: positive unabhängige öffentliche Validierung, aber per-Schritt-Belege nicht vollständig — sichtbar in den Release Notes.

## 14. WP-089-Note als Operational Note

- [ ] QGM-003 ist korrekt dokumentiert: Bei echtem Gate-Verstoß kann der Begriff im ERROR-/CI-Log erscheinen; operative Erwartung „sofort beheben" — sichtbar in den Release Notes.

## 15. WP-090-Status

- [ ] WP-090 ist als **not needed** dokumentiert (Nachweis in WP-089 erbracht).

## 16. ADR-Status

- [ ] ADR Policy adopted (Status Accepted), **ADR-Massenmigration bleibt deferred** — beides korrekt dargestellt.

## 17. Neutralität

- [ ] Keine privaten Projektnamen, keine Reviewer-Daten, keine Kontaktwege, keine echten Domains, keine Secret-Werte in getrackten Dateien.

## 18. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 19. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 20. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 21. Release Title geprüft

```powershell
git tag --list v0.6.0-foundation
```

- [ ] Release Title lautet „Nova Development Framework v0.6.0 Foundation" — **kein** Secret-Name, kein Platzhalter, kein falscher Text (Lehre aus dem 0.2-Titel-Fehler).

## 22. Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung:        GO | GO WITH NOTES | NO-GO
Begründung:          __________
Freigabe durch:      __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_6_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
