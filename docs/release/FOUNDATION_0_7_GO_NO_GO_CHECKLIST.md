# Foundation 0.7 Go/No-Go Checklist

> DE: Finale Prüfung vor Tag und GitHub Release `v0.7.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release. / EN: Final check before tag and GitHub release `v0.7.0-foundation`. Performed by the human maintainer; the Implementation Agent creates neither tag nor release.

> **Status: abgeschlossen / archived (post-release historical document).** Der Release `v0.7.0-foundation` wurde am 2026-07-08 veröffentlicht. Diese Checkliste bleibt als historischer Nachweis und Vorlage für künftige Releases erhalten — keine neuen Aktionen daraus ableiten. / Foundation 0.7 was released as `v0.7.0-foundation`; retained for audit/history.

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

- [ ] Der letzte Commit enthält den WP-105-Release-Prep-Stand.

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

- [ ] `docs/release/FOUNDATION_0_7_RELEASE_NOTES.md` vorhanden und aktuell (DE/EN), inkl. aller Known Limitations aus dem Readiness Review (WP-104).

## 9. Release Criteria

- [ ] `docs/release/FOUNDATION_0_7_RELEASE_CRITERIA.md` aktuell; release-blocking Kriterien bis auf finalen Tag/Release erfüllt.

## 10. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.7.0-foundation]` mit WP-097 bis WP-105; Status „tag pending", „Not v1.0".

## 11. README Status

- [ ] README stellt Foundation 0.7 als „für den geplanten Release vorbereitet" dar — **nicht** als released; Foundation 0.6 bleibt als „veröffentlicht" korrekt.

## 12. Keine v1.0-Darstellung

- [ ] Foundation 0.7 wird nirgends als v1.0, v1.0-nah oder v1.0 Release Candidate dargestellt.

## 13. Foundation 0.7 nicht als released vor Tagging

- [ ] Kein Dokument stellt Foundation 0.7 / `v0.7.0-foundation` vor dem Tagging als bereits released dar (nur „vorbereitet" / „tag pending").

## 14. ADR-0031 Accepted sichtbar

- [ ] ADR-0031 (v1.x Compatibility Policy) ist als **Accepted** dokumentiert und als Source of Truth referenziert; nächste freie ADR-Nummer 0032.

## 15. Volle v1.x-Kompatibilitätszusage nicht aktiv

- [ ] Kein Dokument stellt die volle v1.x-Kompatibilitätszusage als bereits aktiv dar — sie aktiviert erst mit einem künftigen v1.0-Release.

## 16. Convention Stability sichtbar

- [ ] Project Adapter Convention Stability ist als **Stable with notes** (nicht „frozen forever") korrekt dargestellt.

## 17. Checklist DE/EN Option B sichtbar

- [ ] WP-099-Entscheidung **Option B** (optional mit finaler Begründung, kein Auto-Carry, kein Folge-WP) ist korrekt dargestellt.

## 18. WP-102 / WP-103 nicht aktiviert

- [ ] WP-102 (External Validation Evidence Depth) und WP-103 (Academy Entry) sind als **optional / not activated** dokumentiert.

## 19. PSV-001 als Known Limitation

- [ ] PSV-001 ist korrekt dokumentiert: positive unabhängige externe Validierung, aber per-Schritt-Belege nicht vollständig — v1.0-tracked, sichtbar in den Release Notes.

## 20. QGM-003 als Operational Note

- [ ] QGM-003 ist korrekt dokumentiert: Bei echtem Gate-Verstoß kann der Begriff im ERROR-/CI-Log erscheinen; operative Erwartung „sofort beheben" — sichtbar in den Release Notes.

## 21. Neutralität

- [ ] Keine privaten Projektnamen, keine Reviewer-Daten, keine Kontaktwege, keine echten Domains, keine Secret-Werte in getrackten Dateien.

## 22. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 23. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 24. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 25. Release Title geprüft

```powershell
git tag --list v0.7.0-foundation
```

- [ ] Release Title lautet „Nova Development Framework v0.7.0 Foundation" — **kein** Secret-Name, kein Platzhalter, kein falscher Text (Lehre aus dem 0.2-Titel-Fehler).

## 26. Finale Entscheidung / Final decision

```text
Datum / Date:        __________
Entscheidung:        GO | GO WITH NOTES | NO-GO
Begründung:          __________
Freigabe durch:      __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_7_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
