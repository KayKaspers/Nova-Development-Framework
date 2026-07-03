# Project Brain – WP-032 Public Repository Quality Gate Notes

## Warum existiert WP-032?

WP-030 und WP-031 haben das Repository öffentlich neutralisiert (private Projektnamen, Maintainer-Bezüge, Root-Cleanup, History-Trennung). Ohne automatische Absicherung würde diese Qualität mit der Zeit erodieren: ein einziges neues Import-Paket oder ein unbedachter Doku-Satz könnte private Bezüge wieder einführen.

WP-032 macht die Neutralität zum dauerhaft geprüften Zustand statt zum einmaligen Aufräumergebnis.

## Welche Checks wurden ergänzt?

`scripts/check_public_quality.py` (nur Python-Standardbibliothek):

1. Neutralitäts-Scan getrackter Textdateien gegen eine externe Denylist (Env-Variable `NDF_PUBLIC_NEUTRALITY_DENYLIST` und/oder ungetrackte Datei `.ndf/public-neutrality-terms.local.txt`).
2. Root-Hygiene: Paket-/Import-Artefakt-Muster im Root sind Fehler; fremde Root-Markdown-Dateien sind Warnungen.
3. History-Trennung: `*_IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md` nur unter `docs/import-history/`.
4. README-Basisstruktur: Pflichtbegriffe vorhanden.

Modi: Standard, `--strict` (Warnungen → Fehler), `--self-test` (interne Testfälle mit Platzhaltern).

CI: `.github/workflows/public-quality-gate.yml` (pull_request + push auf main, Strict-Mode, optionales Secret).

## Kernentscheidung

Die echten privaten Begriffe stehen bewusst **nicht** im Repository — sonst wäre der Schutzmechanismus selbst das Leck. Nur Platzhalter sind getrackt; die echte Liste lebt lokal (gitignored) oder als GitHub Secret. Ohne Denylist läuft der Gate trotzdem (Hinweis statt Fehler), damit CI ohne Secret nicht rot ist.

## Offene Grenzen

- Ohne konfigurierte Denylist prüft der Neutralitäts-Scan nichts — die Struktur-Checks laufen aber immer.
- Substring-Matching kann bei sehr kurzen Denylist-Begriffen False Positives erzeugen (Begriffe ausreichend spezifisch wählen).
- Der Gate scannt nur getrackte Textdateien; Binärdateien (Bilder, PDFs) werden nicht geprüft.
- Git-Historie wird nicht geprüft (History-Rewrite war und ist ausgeschlossen).

## Nächste empfohlene WPs

1. NDF-WP-031-Nachfolger: Academy Examples from Reference Projects (bereits geplant als NDF-WP-031 in älteren Roadmap-Tabellen, ggf. neu nummerieren).
2. Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` im GitHub-Repository setzen (manuell durch den Maintainer).
3. Optional: Pre-Commit-Hook-Empfehlung dokumentieren, damit der Gate schon vor dem Commit läuft.
