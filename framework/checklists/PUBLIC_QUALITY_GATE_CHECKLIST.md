# Checklist – Public Quality Gate

## DE – Zweck

Kurzritual für den Human Maintainer, damit private Begriffe nie in öffentliche Dateien gelangen — auch nicht in neue, noch nicht committete Dateien.

## EN – Purpose

Short ritual for the human maintainer so that private terms never reach public files — including new, not-yet-committed files.

## Vor jedem Commit / Before every commit

- [ ] `python scripts/check_public_quality.py --strict` (oder `py …`) → `Public quality gate passed.`
- [ ] Scan-Modus in der Ausgabe ist „tracked + new/untracked files" (new-file neutrality check aktiv)
- [ ] Lokale Denylist gepflegt (`.ndf/public-neutrality-terms.local.txt`, ungetrackt) — sonst prüft der Gate neue Dateien nur strukturell

## Nach neuen Dateien / After adding new files

- [ ] Neue Dateien erscheinen in der Notice „new text file(s) included in scan"
- [ ] Sichtprüfung: keine privaten Namen, keine echten Domains/Secrets, keine wörtlichen privaten Grep-Muster (auch nicht als Beispiel oder Prüfprotokoll)

## Vor jedem Release / Before every release

- [ ] `--strict` und `--self-test` grün
- [ ] GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt (kommagetrennte Begriffe; niemals ins Repo schreiben)
- [ ] Letzter CI-Lauf des Gates grün

## Was niemals dokumentiert werden darf / Never document

- echte private Projekt-/Personen-/Organisationsnamen
- echte Domains oder Secrets
- private Suchmuster in Kommandos, Beispielen, Tests oder Berichten

Stattdessen neutral: *private denylist terms · custom denylist · private project/person checks · new-file neutrality check*. Synthetische Testbegriffe (z. B. `ExamplePrivateTerm`) nur in temporären Testkontexten.
