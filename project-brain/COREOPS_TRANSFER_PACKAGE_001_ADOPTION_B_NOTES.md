# CoreOps Transfer Package 001 – Adoption B (Notes)

## Kandidat

`NDF-FC-COREOPS-002` — Full local skills availability with selective activation, provenance and integrity lock. Intake-Klassifikation `partially-covered` → `merge-with-existing-work`. Adoption B (`NDF-ADOPT-COREOPS-001B`, docs-only / security-governance).

## Bereits bestehende Skills-first-Abdeckung

Verfügbarkeit + selektive Aktivierung sind bereits abgedeckt (`SKILLS_FIRST_OPERATING_MODE.md`, `NDF_CONTEXT_ECONOMY.md`, `NDF_SKILL_SECURITY_POLICY.md`/ADR-0032). Nur die Provenance-/Integritäts-Lock-Lücke wurde adoptiert — kein paralleles Skills-System, keine Duplikation der Verfügbarkeits-/Aktivierungsregeln.

## Adoptierte Provenance-/Lock-Lücke

Neue Governance-Datei `docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md` (20 Abschnitte): Provenance-Pflichtfelder, technologieunabhängiges Lock-Modell (Schema/Framework-Release/Digest je Datei/Algorithmus/Source/Approval), SHA-256-Baseline, deterministische Serialisierung (stabile Sortierung, normalisierte relative POSIX-Pfade, eindeutiges Encoding, keine Zeitstempel im Hash-Payload), Verifikationsstatus (`verified…not-checked`), fail-closed bei unbekannt/verändert/unverifiziert, Update-/Refresh-Governance, Human-Maintainer-Gate. Additiver Verweis in `NDF_SKILL_SECURITY_POLICY.md` (keine Volldup).

## Kein ausführbares Tool implementiert

Governance only — kein Lock-Generator, keine Manifestdatei, keine Skill-Verifikation technisch ausgeführt, kein Hash-Tool ausgeführt. Scripts bleiben unter ADR-0032 verboten.

## Nova Review Notes eingearbeitet (Resume Correction)

- **Migration bestehender Projekte:** neue §20 — kein historischer Lock ≠ kompromittiert; Migrationsstatus (`migration-pending / legacy-unlocked / migration-exception-active / lock-enforced`); `verified` Lock Pflicht vor Import/Update/Refresh/Enforcement/Nutzung geänderter Skills; temporäre Ausnahme nur mit Scope/Risk/Human-Maintainer-Approval/Review-Expiry/Follow-up; fehlender Lock ≠ Manipulationsbeweis; Legacy nicht still als verified; Ausnahmen nicht dauerhaft-implizit.
- **Integrity Payload vs Governance Metadata:** neue §19 — per-file Digest nur über Skill-Bytes/kanonischen Inhalt; mutable Metadata beeinflusst die erwarteten Digests nicht; künftiger Whole-Lock-Digest muss Payload + ausgeschlossene mutable Felder explizit definieren; Approval-Änderung ändert Content-Digests nicht still.
- **Manuelle Verifikation als zulässige Anfangsevidenz:** neue §21 — `verified` zunächst per dokumentierter manueller Prüfung (Quelle, Version/Commit, Pfade, verglichene Integritätswerte, Methode, Ergebnis, Human-Maintainer-Approval, Datum/Phase); Governance-Requirement vs manueller Evidenzprozess vs Future Tooling vs Automated Enforcement klar getrennt.
- **Kein Validator oder Lock-Generator implementiert; keine automatische Durchsetzung behauptet** (`Tooling: not implemented`).
- Additiver Verweis in `NDF_SKILL_SECURITY_POLICY.md` entsprechend erweitert (manuelle Prüfung / keine Automatik behauptet / Migrationsstatus / fail-closed).

## Keine Skill-Datei verändert

`.claude/skills/` unberührt; keine Adoption-A-Datei verändert (`framework/`, `standards/git-standard.md` sind Forbidden Files in Adoption B).

## Status

- NDF-Version noch nicht zugeordnet.
- Nova Review pending.
- Human-Maintainer-Commit pending.
- CoreOps-Backlink pending.
- Adoption C noch offen (nicht begonnen).

## Kompatibilität / Sicherheit

Additiv, rückwärtskompatibel; Skills-first/Context Economy unverändert; bestehende Projekte nicht rückwirkend fehlerhaft; fehlende historische Locks = Migrationsthema; keine automatische Skill-Ausführung; keine neue NDF-Version; ADR-0031/0032 unberührt. Breaking-Change-Potenzial: low to medium. Sicherheits-positiv (stille Skill-Manipulation erkennbar; lokale Verfügbarkeit ≠ Vertrauen).

## Nächster NDF-Schritt nach Review

Nach Nova-Review + Human-Maintainer-Entscheidung/-Commit: **NDF Adoption C** (Governance Status Modeling Patterns, Kandidaten 005/006/007) beginnen. Adoption A bleibt separater Commit `1ebffa6`; WP-150 bleibt `42ce7f8`.
