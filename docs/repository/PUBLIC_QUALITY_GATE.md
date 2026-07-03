# Public Repository Quality Gate

## Zweck

Der Public Quality Gate schützt die öffentliche Neutralität des NDF-Repositories automatisch.

Nach den Neutralisierungs-Work-Packages (WP-030, WP-031) soll verhindert werden, dass versehentlich wieder private Projektbezüge, personenbezogene Maintainer-Bezüge oder Import-Paket-Artefakte im öffentlichen Repository landen.

## Was wird geprüft?

Das Script `scripts/check_public_quality.py` prüft getrackte Textdateien (`.md`, `.mdx`, `.txt`, `.yaml`, `.yml`, `.json`, `.toml`, `.ini`, `.cfg`):

1. **Öffentliche Neutralität** – kein Treffer aus der konfigurierten Denylist (case-insensitive) in getrackten Textdateien.
2. **Root-Hygiene** – keine Paket-/Import-Artefakte im Repository-Root (`NDF_*IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md`, `CHANGELOG_*_INTEGRATION.md`, `CHANGELOG_*_PLANNING.md`, `CHANGELOG_*_VALIDATION.md`, `README_*PACK.md`). Erlaubte Root-Markdown-Dateien: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`. Andere Root-Markdown-Dateien erzeugen eine Warnung.
3. **Import-History-/Release-History-Trennung** – Import-Artefakte (`*_IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md`) dürfen nur unter `docs/import-history/` liegen.
4. **README-Basisstruktur** – `README.md` existiert und enthält die Begriffe `Nova Development Framework`, `Work Package`, `Security`, `Maintainer`, `Foundation`.

## Warum stehen keine echten privaten Namen im Repo?

Der Quality Gate selbst muss öffentlich neutral sein. Würden die zu blockierenden privaten Begriffe im Repository stehen (Config, Tests, CI-YAML), wären sie genau dadurch wieder öffentlich. Deshalb:

- Das Repository enthält nur Platzhalter (`PRIVATE_PROJECT_A`, `example-owner`, …).
- Die echte Denylist lebt ausschließlich lokal (ungetrackt) oder als GitHub Secret.

## Lokale Denylist

Beispieldatei kopieren und mit echten Begriffen füllen:

```text
.ndf/public-neutrality-terms.example.txt  ->  .ndf/public-neutrality-terms.local.txt
```

- Ein Begriff pro Zeile, `#`-Zeilen sind Kommentare.
- `.ndf/public-neutrality-terms.local.txt` steht in `.gitignore` und wird nie committet.

## Environment Variable / GitHub Secret

Alternativ oder zusätzlich:

```text
NDF_PUBLIC_NEUTRALITY_DENYLIST=term1,term2,term3
```

In GitHub Actions wird die Variable aus dem Repository-Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` befüllt. Ist das Secret leer, läuft der Gate trotzdem durch — die fehlende Denylist ist nur ein Hinweis (`No custom neutrality denylist configured.`), kein Fehler.

## Lokal prüfen

```text
python scripts/check_public_quality.py            # Standard
python scripts/check_public_quality.py --strict   # Warnungen werden Fehler
python scripts/check_public_quality.py --self-test # interne Testfälle
```

Das Script nutzt nur die Python-Standardbibliothek (Python 3.10+).

## Root-Hygiene im Alltag

Neue Import-Pakete (Import-Anleitungen, Paket-Changelogs, Pack-READMEs) gehören direkt nach `docs/import-history/`, nicht in den Root. Der Gate schlägt fehl, wenn solche Artefakte im Root auftauchen.

## Abgrenzung import-history / release-history

- `docs/import-history/` – archivierte Import-Pakete: Import-Anleitungen, Paket-Changelogs, Pack-READMEs.
- `docs/release/history/` – echte Release-Changelogs und Release-Historie. Paket-Changelogs aus der Foundation-0.1-Phase bleiben dort als eingefrorener Altbestand (der Gate prüft nur die Muster `*_IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md` und lässt den Altbestand unangetastet).

## CI

Workflow: `.github/workflows/public-quality-gate.yml`

- läuft bei `pull_request` und bei `push` auf `main`
- führt zuerst den Self-Test aus, dann den Gate im Strict-Mode
- liest optional das Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST`
