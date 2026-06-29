# NDF Export Concept v0.1

## Zweck

Das NDF soll nicht nur im Repository lesbar sein, sondern später professionell veröffentlicht werden können.

Ziel-Ausgaben:

- GitHub Markdown
- Dokumentations-Website
- PDF-Handbuch
- Word-Dokument
- optional EPUB

## Grundsatz

> One source. Multiple outputs.

Die Hauptquelle bleibt Markdown im Repository. Daraus werden alle anderen Formate erzeugt.

## Warum Markdown als Quelle?

Markdown ist:

- einfach zu lesen
- gut versionierbar
- Git-freundlich
- gut für Reviews
- kompatibel mit vielen Export-Werkzeugen
- ideal für Zusammenarbeit mit KI

## Zielstruktur

```text
academy/
docs/
framework/
project-brain/
```

bleiben die Quellbereiche.

Exports gehen nach:

```text
exports/
├── pdf/
├── word/
├── web/
└── epub/
```

## Export-Philosophie

1. Inhalte zuerst.
2. Struktur danach.
3. Design zuletzt.
4. Automatisierung erst, wenn der manuelle Prozess verstanden ist.

## Nicht-Ziele in v0.1

- kein fertiger PDF-Builder
- kein fertiger Word-Builder
- keine automatische Website
- kein verpflichtender Toolchain-Wechsel

v0.1 ist die Spezifikation.
