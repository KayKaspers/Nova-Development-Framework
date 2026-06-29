# Export Pipeline Design

## Pipeline 1 – Website

```text
Markdown Sources
   ↓
Navigation Config
   ↓
MkDocs Build
   ↓
Static Site
   ↓
GitHub Pages
```

## Pipeline 2 – PDF

```text
Markdown Sources
   ↓
Book Manifest
   ↓
Pandoc
   ↓
PDF Theme
   ↓
PDF Output
```

## Pipeline 3 – Word

```text
Markdown Sources
   ↓
Book Manifest
   ↓
Pandoc
   ↓
DOCX Reference Template
   ↓
Word Output
```

## Pipeline 4 – EPUB

```text
Markdown Sources
   ↓
Book Manifest
   ↓
Pandoc
   ↓
EPUB Metadata
   ↓
EPUB Output
```

## Book Manifest

Ein Book Manifest definiert, welche Dateien in welcher Reihenfolge exportiert werden.

Beispiel:

```yaml
title: NDF Academy Band 1
version: 0.1
chapters:
  - academy/band-1-foundation/chapters/01-willkommen-in-der-softwareentwicklung.md
  - academy/band-1-foundation/chapters/02-was-ist-ndf.md
```
