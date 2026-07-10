# NDF-WP-137 – Docs-only Extended Core Skills MVP Implementation (Notes)

## Ziel

Das Docs-only Extended Core Skills MVP umsetzen: genau die vier Default-Core-Skills aus WP-136 als reine Markdown-`SKILL.md`, ADR-0032-konform, fail-closed, ohne Scripts/Netz/Secrets/private Daten/Git-Release-Aktionen. Keine optionalen +2 Skills, kein funktionaler Umbau der bestehenden MVP-Skills.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-136 committet `ae4b973`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## Scope-Bestätigung

Human Maintainer hat für diesen Lauf ausdrücklich vorgegeben: „Implementiere nur die vier Default-Core-Skills. Keine optionalen +2 Skills." → umgesetzt.

## Implementierte Extended Core Skills (genau vier)

1. `ndf-skill-quality-reviewer` — prüft Skill-Dokumente auf Qualität/Scope/ADR-0032/Neutralität/Overlap/Fail-closed/Output-Contract (advisory, keine Freigabe).
2. `ndf-existing-project-analysis-runner` — neutrale, advisory Bestandsprojekt-Analyse; keine privaten Inhalte im Public NDF.
3. `ndf-docs-polish-runner` — Docs-Politur (Klarheit/Struktur/Konsistenz/Neutralität), keine Substanz-/Governance-Änderung.
4. `ndf-changelog-writer` — konsistente, WP-referenzierte Changelog-Einträge; kein Release-/Tag-/Versions-Trigger.

## Nicht implementiert

`ndf-release-safety`, `ndf-adr-governance-review` (optionale +2 — für diesen Lauf ausgeschlossen); alle übrigen Kandidaten aus WP-135.

## Angelegte / geänderte Dateien

- **NEU** `.claude/skills/ndf-skill-quality-reviewer/SKILL.md`
- **NEU** `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md`
- **NEU** `.claude/skills/ndf-docs-polish-runner/SKILL.md`
- **NEU** `.claude/skills/ndf-changelog-writer/SKILL.md`
- `.claude/skills/README.md` (dokumentarisch: Core-MVP + Extended-Core, acht Skills)
- **NEU** `docs/validation/foundation-0-9/EXTENDED_CORE_SKILLS_MVP_VALIDATION.md`
- **NEU** `project-brain/WP_137_DOCS_ONLY_EXTENDED_CORE_SKILLS_MVP_IMPLEMENTATION_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Jede neue SKILL.md enthält

Title, Purpose, When to use, Required inputs, Expected outputs, Allowed actions, Forbidden actions, Fail-closed behavior, Public-neutrality requirements, ADR-0032 safety boundaries, Human-maintainer-only boundaries, Output contract, Interaction with existing NDF skills. Keine Chain-of-Thought, keine privaten Daten, keine Secret-Werte, keine Scripts.

## Validierung

Genau vier neue Skills: ja · keine optionalen +2: ja · docs-only: ja · keine Scripts: ja · kein Netzwerk: ja · keine Secrets (nur Name): ja · keine privaten Daten/Namen/Domains: ja · keine Git-/Release-Aktionen: ja · ADR-0032 unverändert: ja · Public Neutrality: Gate grün · bestehende Skills unverändert: ja (nur README ergänzt). Details: [Validation](../docs/validation/foundation-0-9/EXTENDED_CORE_SKILLS_MVP_VALIDATION.md) (18-Punkte-Matrix).

## Token-Economy-Einschätzung

Qualitativ erwartet (advisory Strukturierung reduziert Review-/Docs-/Changelog-Prompt-Overhead); reale Vorher/Nachher-Messung offen (ECS-001, konsistent mit DSK-001 Partially closed) → WP-138.

## Risiken / offene Punkte

ECS-001 (Ersparnis noch nicht empirisch gemessen); Scope Creep (nur vier Skills, optionale +2 ausgeschlossen); Neutralitäts-Sensibilität von `ndf-existing-project-analysis-runner` (Grenze explizit); Scheinsicherheit (advisory ≠ Gate); Release-Nähe von `ndf-changelog-writer` (kein Trigger).

## Nächster empfohlener Schritt

**NDF-WP-138 – Skill Prompt Compression Real-use Validation** (schließt DSK-001/ECS-001). Danach optional Project Enablement Skills Blueprint, dann v1.0 Gap Review & Scope Lock.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-137 hat genau vier docs-only Extended Core Skills implementiert (skill-quality-reviewer, existing-project-analysis-runner, docs-polish-runner, changelog-writer), keine optionalen +2, bestehende MVP-Skills unverändert. GO WITH NOTES; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-138 (Real-use-Validierung).
