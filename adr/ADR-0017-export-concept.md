# ADR-0017: NDF Export Concept

## Status

Accepted

## Kontext

Das NDF soll langfristig nicht nur als Markdown-Repository existieren, sondern als Website, PDF-Handbuch und Word-Dokument exportierbar sein.

## Entscheidung

Markdown bleibt die primäre Quelle. Exporte werden als abgeleitete Artefakte betrachtet.

## Konsequenzen

- Inhalte werden Git-freundlich gepflegt.
- PDF/Word/Web können aus derselben Quelle entstehen.
- Exportierte Dateien werden nicht manuell als Primärquelle bearbeitet.
- Spätere Automatisierung wird vorbereitet.
