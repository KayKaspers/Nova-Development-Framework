# Public Repository Quality Gate

## Zweck

Der Public Quality Gate schützt die öffentliche Neutralität des NDF-Repositories automatisch. / The public quality gate automatically protects the repository's public neutrality.

Nach den Neutralisierungs-Work-Packages (WP-030, WP-031) soll verhindert werden, dass versehentlich wieder private Projektbezüge, personenbezogene Maintainer-Bezüge oder Import-Paket-Artefakte im öffentlichen Repository landen.

## Neu in v0.2 (WP-052) / New in v0.2

- **New-file neutrality check:** Standardmäßig werden auch relevante **neue/untracked** Textdateien gescannt — private Begriffe werden damit **vor** dem ersten Commit gefangen, nicht erst danach. / By default, relevant **new/untracked** text files are scanned too, catching private terms **before** the first commit.
- `--tracked-only` schaltet den New-file-Check bewusst ab (z. B. für Vergleichsläufe). / disables the new-file check deliberately.
- Der Gate meldet den aktiven Scan-Modus als Notice; ohne konfigurierte Denylist erscheint der Hinweis, dass für neue Dateien nur Struktur-/Root-/README-Regeln greifen. / The gate reports its scan mode; without a denylist it notes that only structure rules apply to new files.
- Root-Hygiene- und History-Regeln prüfen jetzt ebenfalls neue Dateien (ein neues Paket-Artefakt im Root schlägt schon vor dem Commit fehl).
- Hintergrund: In Foundation 0.2 enthielt ein Review-Dokument die Kontroll-Grep-Kommandos **wörtlich** inklusive privater Begriffe, und der Final-Check übersah es, weil die Datei noch untracked war. Beides adressiert v0.2.

## Was wird geprüft?

Das Script `scripts/check_public_quality.py` prüft getrackte Textdateien (`.md`, `.mdx`, `.txt`, `.yaml`, `.yml`, `.json`, `.toml`, `.ini`, `.cfg`):

1. **Öffentliche Neutralität** – kein Treffer aus der konfigurierten Denylist (case-insensitive) in getrackten Textdateien.
2. **Root-Hygiene** – keine Paket-/Import-Artefakte im Repository-Root (`NDF_*IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md`, `CHANGELOG_*_INTEGRATION.md`, `CHANGELOG_*_PLANNING.md`, `CHANGELOG_*_VALIDATION.md`, `README_*PACK.md`). Erlaubte Root-Markdown-Dateien: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`. Andere Root-Markdown-Dateien erzeugen eine Warnung.
3. **Import-History-/Release-History-Trennung** – Import-Artefakte (`*_IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md`) dürfen nur unter `docs/import-history/` liegen.
4. **README-Basisstruktur** – `README.md` existiert und enthält die Begriffe `Nova Development Framework`, `Work Package`, `Security`, `Maintainer`, `Foundation`.

## Warum stehen keine echten privaten Namen im Repo? / Why no real private terms in the repo?

Der Quality Gate selbst muss öffentlich neutral sein. Würden die zu blockierenden privaten Begriffe im Repository stehen (Config, Tests, CI-YAML), wären sie genau dadurch wieder öffentlich. Deshalb:

- Das Repository enthält nur Platzhalter (`PRIVATE_PROJECT_A`, `example-owner`, …).
- Die echte Denylist lebt ausschließlich lokal (ungetrackt) oder als GitHub Secret.

**Verschärfung aus Foundation 0.2 (WP-052):** Private Begriffe dürfen **nirgends** in Repo-Dateien stehen — auch nicht:

- als wörtliche Grep-/Kontrollkommandos in Doku, Checklisten oder Release-Dokumenten,
- als „Beispiel" in Prompts, Tests oder CI-YAML,
- in Review-/Readiness-Berichten, die Prüfbefehle protokollieren.

In öffentlichen Dokumenten immer neutral formulieren: *private denylist terms*, *custom denylist*, *private project/person checks*, *new-file neutrality check*. Echte Begriffe gehören ausschließlich in: das GitHub Secret, die lokale ignorierte `.ndf/public-neutrality-terms.local.txt`, oder temporäre manuelle Prüfungen außerhalb des Repos. Für Self-Tests nur synthetische Begriffe wie `ExamplePrivateTerm` in temporären Dateien. / Real terms belong only in the GitHub secret, the local gitignored denylist file, or temporary checks outside the repo — never in repository files, not even inside documented grep commands; use synthetic terms like `ExamplePrivateTerm` for tests.

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

## Lokal prüfen / Local checks

```text
python scripts/check_public_quality.py                    # Standard (inkl. new-file check)
python scripts/check_public_quality.py --strict           # Warnungen werden Fehler
python scripts/check_public_quality.py --strict --tracked-only  # nur getrackte Dateien
python scripts/check_public_quality.py --self-test        # interne Testfälle (synthetisch)
```

Alternativ mit `py` statt `python` (Windows). Das Script nutzt nur die Python-Standardbibliothek (Python 3.10+).

Empfohlener Maintainer-Ablauf vor jedem Commit mit neuen Dateien: lokale Denylist pflegen → `--strict` laufen lassen (new-file check aktiv) → erst bei „passed" committen. Kurzfassung: `framework/checklists/PUBLIC_QUALITY_GATE_CHECKLIST.md`

## Root-Hygiene im Alltag

Neue Import-Pakete (Import-Anleitungen, Paket-Changelogs, Pack-READMEs) gehören direkt nach `docs/import-history/`, nicht in den Root. Der Gate schlägt fehl, wenn solche Artefakte im Root auftauchen.

## Abgrenzung import-history / release-history

- `docs/import-history/` – archivierte Import-Pakete: Import-Anleitungen, Paket-Changelogs, Pack-READMEs.
- `docs/release/history/` – echte Release-Changelogs und Release-Historie. Paket-Changelogs aus der Foundation-0.1-Phase bleiben dort als eingefrorener Altbestand (der Gate prüft nur die Muster `*_IMPORT_ANLEITUNG.md`, `README_WP_*.md`, `CHANGELOG_WP_*.md` und lässt den Altbestand unangetastet).

## CI

Workflow: `.github/workflows/public-quality-gate.yml`

- läuft bei `pull_request` und bei `push` auf `main`
- führt zuerst den Self-Test aus, dann den Gate im Strict-Mode
- liest optional das Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` — der Secret-Wert wird nie geloggt oder dokumentiert

## Maintenance-Status / Maintenance status

Foundation 0.6 reviewed (NDF-WP-089, 2026-07-07): Script, Strict-Mode, Self-Test, New-file-Scan und CI-Denylist-Wirksamkeit geprüft — Evidence-Level **strong**, kein separates Nachweis-Artefakt nötig. Details: [PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md](../quality/PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md)
