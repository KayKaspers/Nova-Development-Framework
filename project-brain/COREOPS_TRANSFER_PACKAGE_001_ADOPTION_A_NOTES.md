# CoreOps Transfer Package 001 – Adoption A (Notes)

## Quellpaket

Cross-Project Transfer Package 001 (externes Quellprojekt), Intake abgeschlossen als `NDF-INTAKE-COREOPS-001` (Intake-Commit `d08e35e`). Adoption A = Work-Package Prompt Safety Baseline Update (`NDF-ADOPT-COREOPS-001A`, docs-only / standards-adoption). Nur generalisierte Safety-Muster übernommen; kein Quellinhalt, keine privaten Pfade/Details in öffentliche NDF-Regeln.

## Drei adoptierte Kandidaten

- **001** Git Read versus Git Write — explizite Read-only-Allowlist im Prompt-Block, Write nicht aus Read ableitbar, Netzwerkgrenze, Human-Maintainer-only.
- **003** Source-Handoff — Preflight (Verfügbarkeit/Identität/Vollständigkeit/Trunkierung/Version-Provenance) vor Änderung; fail-closed bei fehlender/unvollständiger Quelle; keine Erfindung, keine Erinnerung als Ersatzquelle.
- **004** Blocked Report ohne künstlichen Commit — strukturierter No-Change-Report; kein künstlicher Zwischen-Commit; Blocked ≠ completed; Human-Maintainer-Gate.

## Geänderte Standards (additiv)

- `framework/prompts/blocks/BLOCK_LIMITS.md` (Git Read/Write-Abschnitt)
- `standards/git-standard.md` (Git-Read/Write-Taxonomie, Human-Maintainer-Kontrolle)
- `framework/standards/WORK_PACKAGE_LIFECYCLE.md` (Source-Handoff-Preflight, fail-closed → blocked, Blocked Report, No-Change/kein-künstlicher-Commit, Resume, Human-Maintainer-Gate)
- `framework/prompts/blocks/BLOCK_FEEDBACK_TO_NOVA.md` (Statusfeld + optionale Felder + Blocked-/No-Change-Abschnitt)

## Nicht adoptiert

Kandidaten `002` (Adoption B), `005`/`006`/`007` (Adoption C) — nicht behandelt, nicht verändert.

## Status

- NDF-Version noch nicht zugeordnet.
- Nova Review pending.
- Human-Maintainer-Commit pending.
- CoreOps-Backlink pending.

## Kompatibilität / Sicherheit

Additiv, rückwärtskompatibel; bestehende Write-Verbote erhalten; Prompt-Blöcke bleiben kompakt/wiederverwendbar; keine implizite Git-Schreibfreigabe; kein Netzwerk durch Read-only-Git; Human-Maintainer-Kontrolle unverändert; keine neue NDF-Version behauptet. ADR-0031/0032 unberührt/unverändert. Breaking-Change-Potenzial: low.

## Nächster NDF-Schritt nach Review

Nach Nova-Review + Human-Maintainer-Entscheidung/-Commit: **NDF Adoption B** (Skill Provenance and Integrity Lock Guidance) beginnen. Adoption A hat keine WP-150-Datei verändert; WP-150 bleibt ein separater Human-Maintainer-Commit (`42ce7f8`).
