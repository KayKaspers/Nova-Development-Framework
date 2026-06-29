# Recommended Export Toolchain

## Kurzfristig

Für die Foundation-Phase:

- Markdown als Quelle
- manuelle Prüfung in GitHub
- einfache ZIP-/Dokument-Exports bei Bedarf

## Mittelfristig

Empfohlene Toolchain:

```text
Markdown
↓
Pandoc
↓
PDF / DOCX / EPUB
```

Für Website:

```text
Markdown
↓
MkDocs Material
↓
GitHub Pages
```

## Langfristig

Optional:

- eigene NDF CLI
- automatisierte Builds
- GitHub Actions
- Release-Artefakte
- Versionierte Dokumentation

## Empfehlung Nova

Für das NDF ist langfristig wahrscheinlich diese Kombination ideal:

- MkDocs Material für Website
- Pandoc für PDF/DOCX/EPUB
- GitHub Actions für automatisierte Releases
- eigenes Branding über CSS und DOCX Reference Template
