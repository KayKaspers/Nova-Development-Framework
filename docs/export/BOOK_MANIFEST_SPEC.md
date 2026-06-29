# Book Manifest Specification

## Zweck

Ein Book Manifest beschreibt ein exportierbares Handbuch oder einen Band.

## Beispiel

```yaml
id: ndf-academy-band-1
title: NDF Academy Band 1
subtitle: Vom absoluten Anfänger zum ersten professionellen Projekt
version: 0.1
language: de
author: Nova Development Framework
output:
  pdf: true
  docx: true
  website: true
  epub: false
chapters:
  - path: academy/band-1-foundation/README.md
    title: Einführung
  - path: academy/band-1-foundation/chapters/01-willkommen-in-der-softwareentwicklung.md
    title: Willkommen in der Softwareentwicklung
```

## Pflichtfelder

- id
- title
- version
- language
- chapters

## Nutzen

Book Manifests ermöglichen später:

- automatischen Export
- Inhaltsverzeichnis
- Versionierung
- mehrere Bücher/Bände
