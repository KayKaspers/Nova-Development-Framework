# ADR-0020: Repository Structure Cleanup Plan

## Status

Accepted

## Kontext

Das NDF ist in kurzer Zeit stark gewachsen. Ohne klare Repository-Regeln drohen doppelte Strukturen, unklare Root-Dateien und schwer wartbare Dokumentationsbereiche.

## Entscheidung

Ein Repository Structure Cleanup Plan wird eingeführt.

## Konsequenzen

- Root-Verzeichnis wird begrenzt.
- `framework/prompts/` wird kanonische Prompt-Quelle.
- `framework/templates/` wird kanonische Template-Quelle.
- `docs/` wird thematisch strukturiert.
- Cleanup erfolgt schrittweise und nicht durch unkontrollierte Massenverschiebung.
