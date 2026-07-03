# Repository Structure Review (WP-033)

## Zweck

Konsistenzprüfung der Repository-Struktur nach den Neutralisierungs- und Quality-Gate-Work-Packages (WP-030 bis WP-032): Links, alte Pfadverweise, ADR-Struktur, History-Trennung, Status-Aussagen.

## Geprüfte Bereiche

- alle relativen Markdown-Links (getrackte `*.md`)
- Klartext-Dateiverweise auf verschobene/umbenannte Dateien
- alte neutralisierte Pfade und IDs (`docs/validation/…`, `CCI_WP`, `CC-WP`, …)
- `adr/` und `docs/adr/`
- `docs/import-history/` vs. `docs/release/history/`
- README, CHANGELOG, `docs/roadmap/`, `docs/release/`, `project-brain/`
- Public Quality Gate (Strict-Mode)

## Linkprüfung – Ergebnis

- 7 relative Markdown-Links im Repository, **0 kaputt**.
- 1 fehlendes Bild: `docs/export/MARKDOWN_FOR_EXPORT_STANDARD.md` verweist auf `../../assets/images/example.png` — bewusstes Syntax-Beispiel im Export-Standard, kein Fehler. Dokumentiert, nicht „repariert".
- Klartext-Dateiverweise: alle Treffer sind Glob-Muster, Spec-Beispiele oder als „geplant" markierte Strukturen (z. B. `mkdocs.yml`, `docs-check.yml`, Website-Navigation-Draft). Keine veralteten Verweise auf verschobene Dateien gefunden.

## ADR-Struktur – Ergebnis

Bestand:

- `adr/` – ADR-0001 bis ADR-0026 (Foundation-0.1-Kernentscheidungen, eingefroren; Nummer 0003 nicht vergeben)
- `docs/adr/` – ADR-0027 bis ADR-0030 (Foundation 0.2) sowie frühe thematische ADR-0001 bis ADR-0005

Bekannte Altbestands-Probleme (dokumentiert, keine Migration in diesem WP):

1. Nummernkollision: `docs/adr/ADR-0002/0004/0005` behandeln andere Themen als `adr/ADR-0002/0004/0005`.
2. Themendopplung: `adr/ADR-0002` und `adr/ADR-0006` behandeln beide den VS-Code/GitHub-Desktop-Standard.

Entscheidung: beide Orte bleiben bestehen. Abgrenzung jetzt dokumentiert in `adr/README.md` und `docs/adr/README.md`:

- `adr/` = Foundation-/Framework-Kernentscheidungen (eingefroren)
- `docs/adr/` = spätere dokumentationsnahe/thematische ADRs; neue ADRs entstehen hier (nächste freie Nummer: 0031)

## Import-History / Release-History – Ergebnis

Konsistent. Die Abgrenzung ist gleichlautend dokumentiert in `docs/import-history/README.md`, `docs/release/history/README.md`, `PRE_RELEASE_CLEANUP_GUIDE.md` und `PUBLIC_QUALITY_GATE.md`:

- `docs/import-history/` = importierte Work-Package-/Paket-Artefakte
- `docs/release/history/` = echte Release-Historie plus eingefrorener Foundation-0.1-Altbestand

Der Quality Gate erzwingt die Trennung für neue Artefakte automatisch.

## Roadmap / Status – Ergebnis

Korrigiert:

- `CHANGELOG.md`: Foundation 0.1 von „Prepared" auf „Released" (Tag `v0.1.0-foundation` existiert); neue `[Unreleased] – Foundation 0.2`-Sektion mit WP-027 bis WP-033.
- `docs/roadmap/FOUNDATION_0_2_PLAN.md`: Status „Planned" → „In development".
- `docs/repository/ROOT_DIRECTORY_POLICY.md`: an den Quality Gate angeglichen (LICENSE statt LICENSE.md, kein ROADMAP.md im Root, Import-Artefakte im Root nicht mehr „temporär erlaubt", sondern direkt nach `docs/import-history/`).

Nicht geändert (bewusst): historische Plan-/Konzeptdokumente wie `REPOSITORY_STRUCTURE_CLEANUP_PLAN.md` (Foundation-0.1-Altbestand, beschreibt u. a. `LICENSE.md`/`ROADMAP.md` als damalige Zielstruktur) und `project-brain/NEXT_PHASE_FOUNDATION_0_2.md` (Planungsnotiz, weiterhin gültige Reihenfolge).

## Offene Punkte

1. ADR-Konsolidierung (Nummernkollisionen, Themendopplung) als eigenes Work Package.
2. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` ist noch nicht gesetzt (manuell).
3. `REPOSITORY_STRUCTURE_CLEANUP_PLAN.md` beschreibt eine ältere Zielstruktur; bei nächster Überarbeitung als historisch kennzeichnen oder aktualisieren.

## Empfohlene nächste Work Packages

1. NDF-WP-03x – ADR Consolidation (Nummern harmonisieren, Duplikate zusammenführen, ohne History-Rewrite)
2. NDF-WP-03x – Academy Examples from Reference Projects (bereits in Roadmap-Tabellen als P2 geführt)
3. Optional: Link-/Verweisprüfung als Erweiterung des Public Quality Gate
