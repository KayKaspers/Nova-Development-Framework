# Project Brain – WP-052 Public Quality Gate v0.2 Notes

## Ausgangsproblem

Zwei reale Vorfälle aus Foundation 0.2: (1) Ein Readiness-Report dokumentierte die Kontroll-Grep-Kommandos wörtlich inklusive privater Begriffe (WP-040, in WP-041 neutralisiert). (2) Der Final-Check übersah das, weil `git grep` nur getrackte Dateien durchsucht und der Report beim Check noch untracked war. Gate v0.1 prüfte ausschließlich getrackte Dateien.

## Bewertung Gate v0.1 (Aufgabe 1)

Scan: nur `git ls-files` (tracked); Denylist via Env + lokale ignorierte Datei, kombiniert/dedupliziert; `--strict` eskaliert nur Warnungen (Notices nie); `--self-test` mit 8 synthetischen Fällen in Temp-Dateien; CI: self-test + strict, Secret optional ohne Fehlschlag. **Lücke:** untracked Dateien unsichtbar → genau die Fehlerklasse aus WP-040.

## Technische Änderung (scripts/check_public_quality.py)

- `git_untracked_files()` (`git ls-files --others --exclude-standard`, gitignore-respektierend) + `merge_file_lists()`.
- Standardlauf scannt jetzt tracked **und** neue/untracked Dateien (Neutralität, Root-Hygiene, History-Trennung); `--tracked-only` als bewusstes Opt-out.
- Scan-Modus wird als Notice gemeldet; ohne Denylist expliziter Hinweis, dass für neue Dateien nur Strukturregeln greifen; Anzahl einbezogener neuer Textdateien wird genannt.
- CLI-Hilfe erweitert (Flags, Denylist-Quellen, Niemals-committen-Regel im Epilog); Docstring auf v0.2.

## Self-Test-Erweiterung

Neu: synthetischer Begriff in untracked-like Datei wird über die Merge-Liste erkannt; `merge_file_lists` Order/Dedupe; `ExampleInternalName` in tracked-like Datei. Bestehende Tests (fehlende Denylist = Notice, Root-Hygiene, README-Regel) unverändert grün. Nur synthetische Begriffe (`ExamplePrivateTerm`, `ExampleInternalName`, `ExampleSensitivePlaceholder`) in Temp-Dateien.

## Verifikation

strict/default/tracked-only grün; E2E: neue untracked Datei mit synthetischem Begriff + Env-Denylist → **FAILED (exit 1)** im Standardmodus, unsichtbar im tracked-only-Modus — exakt die WP-040-Fehlerklasse wird jetzt vor dem Commit gefangen.

## Dokumentationsänderung

`PUBLIC_QUALITY_GATE.md`: v0.2-Sektion (DE/EN-Kern), verschärfte Niemals-Regel (private Begriffe auch nicht in Grep-Beispielen/Review-Berichten; neutrale Sprechweisen; synthetische Testbegriffe), lokaler Prüfablauf mit `--tracked-only`-Beispiel. Neu: `framework/checklists/PUBLIC_QUALITY_GATE_CHECKLIST.md` (DE/EN, vor Commit/Release/nach neuen Dateien).

## CI

Workflow bewusst unverändert: CI-Checkouts haben keine untracked Dateien, der neue Default ist dort verhaltensneutral; Secret-Handling wie gehabt (fehlend = Notice).

## Grenzen

1. New-file-Scan wirkt nur mit gepflegter lokaler Denylist bzw. Env — ohne Begriffe bleiben nur Strukturregeln (bewusst, Design-Invariante).
2. Ignorierte Dateien (gitignore) werden nicht gescannt — korrekt, dort liegt die lokale Denylist selbst.
3. Git-Historie bleibt außerhalb des Scans (History-Rewrite ausgeschlossen).

## Nächste empfohlene WPs

1. Optional vor WP-054: „Adapter Conventions Polish" (Backlog WP-047, Punkte 1–3).
2. NDF-WP-054 – Foundation 0.3 Release Readiness Review (alle inhaltlichen blocking WPs sind damit fertig).
