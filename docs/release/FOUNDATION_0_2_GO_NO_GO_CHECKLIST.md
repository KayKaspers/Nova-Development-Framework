# Foundation 0.2 Go/No-Go Checklist

Finale Prüfung vor Tag und GitHub Release `v0.2.0-foundation`. Durchführung durch den Human Maintainer; der Implementation Agent erstellt weder Tag noch Release.

## 1. Public Quality Gate (strict)

```powershell
python scripts/check_public_quality.py --strict
```

Alternativ / alternatively: `py scripts/check_public_quality.py --strict`

- [ ] Ergebnis: `Public quality gate passed.` (0 errors, 0 warnings)

## 2. Self-Test

```powershell
python scripts/check_public_quality.py --self-test
```

Alternativ / alternatively: `py scripts/check_public_quality.py --self-test`

- [ ] Ergebnis: `self-test passed`

## 3. Neutralitäts-Grep: private Projektnamen

Die konkreten privaten Begriffe stehen **bewusst nicht** in diesem Repository (Grundprinzip des Quality Gate). Prüfung daher über die lokale Denylist bzw. das Secret:

```powershell
# lokale Denylist anlegen (ungetrackt): .ndf/public-neutrality-terms.local.txt
# Vorlage: .ndf/public-neutrality-terms.example.txt
python scripts/check_public_quality.py --strict
```

- [ ] Neutralitäts-Scan mit konfigurierter Denylist: 0 Treffer

Hinweis: Wer die historischen Grep-Muster kennt, kann zusätzlich manuell `git grep -n -i "<begriff1>\|<begriff2>"` ausführen — die Begriffe dabei nicht in getrackte Dateien schreiben.

## 4. Neutralitäts-Grep: private Personen-/Owner-Namen

- [ ] Wie Punkt 3 — Personen-/Owner-Begriffe gehören in die lokale Denylist bzw. das Secret, nicht ins Repo. Scan: 0 Treffer.

## 5. README Sanity Check

- [ ] README ist bilingual, erklärt Zweck, Rollen (Nova (ChatGPT) → Implementation Agent → Human Maintainer), Workflow, Work Packages, Security, Adapter und Quality Gate; alle Links funktionieren.

## 6. Release Notes

- [ ] `docs/release/FOUNDATION_0_2_RELEASE_NOTES.md` existiert und ist aktuell (DE/EN).

## 7. Changelog

- [ ] `CHANGELOG.md` enthält die Sektion `[0.2.0-foundation]` mit WP-027 bis WP-041.

## 8. Release Criteria

- [ ] `docs/release/FOUNDATION_0_2_RELEASE_CRITERIA.md` ist aktualisiert; Pflichtkriterien abgehakt.

## 9. GitHub Secret

- [ ] Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` in den Repository-Settings gesetzt (Inhalt: private Begriffe, kommagetrennt; niemals ins Repo schreiben). Fehlendes Secret bricht CI nicht, ist aber vor dem öffentlichen Release empfohlen.

## 10. Sauberer Stand vor dem Tag

```powershell
git status
git pull origin main
```

- [ ] Keine uncommitteten Änderungen; lokaler `main` ist identisch mit `origin/main`.

## 11. Tagging nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag erstellt.

## 12. GitHub Release nur durch den Human Maintainer

- [ ] Bestätigt: Der Implementation Agent hat kein GitHub Release erstellt.

## 13. Human-Maintainer-Freigabe

- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## 14. Finale Entscheidung

```text
Datum / Date:       __________
Entscheidung:       GO | GO WITH NOTES | NO-GO
Begründung:         __________
Freigabe durch:     __________ (Human Maintainer)
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_2_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`
