# NDF-WP-136 – Extended Skills Pack Blueprint (Notes)

## Ziel

Die nächste sichere Skill-Ausbaustufe für NDF-Core, Governance und Docs planen (nur Blueprint, keine Implementierung). Fokus: NDF Core Workflow, Security/ADR/Governance, Docs/Release/Communication, Existing Project Analysis. Nicht Fokus (spätere WPs): kreative/Branding/Product/UX/projektlokale Skills, App-/Netz-/Git-Automation.

## Input Summary

Vier MVP-Skills (`.claude/skills/`), WP-125-Blueprint, WP-129-Validation, WP-134-Operating-Mode/Compression, WP-135-Landscape (P0/P1), ADR-0031/0032.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-135 committet `478630b`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## Reconciliation-Hinweis (WP-Nummerierung)

WP-135 hatte WP-137 vorläufig als „Project Enablement Skills Blueprint" skizziert. WP-136 legt **WP-137 = Docs-only Extended Core Skills MVP Implementation** fest; Project-Enablement-Blueprint verschiebt sich auf ein späteres WP (Kandidat, nicht aktiviert).

## Empfohlenes Extended Core Skills Pack

**Kern (4, sicherer Default):** `ndf-skill-quality-reviewer`, `ndf-existing-project-analysis-runner`, `ndf-docs-polish-runner`, `ndf-changelog-writer`.
**Optional (bis +2, nur bei ausdrücklichem WP-137-Scope):** `ndf-release-safety`, `ndf-adr-governance-review`. Max. 6. Lieber klein und sicher.

## Zurückgestellte Skills

`ndf-v1-readiness-review` (vor v1.0), `ndf-readme-quality-reviewer`, `ndf-release-notes-runner`, `ndf-project-brief-runner` (Project-Enablement-WP) — alle P1, später.

## Abgelehnt (nicht als eigener Skill)

Eigenständiger `ndf-prompt-mode-selector` (bleibt in `ndf-work-package-runner` integriert). Grundsätzlich abgelehnt: Git-/Release-/Netz-/Secret-/Automations-Skills (Rejectlist aus WP-135).

## Skill-Design-Zusammenfassung

Jeder empfohlene Kern-Skill konzeptionell mit 13 Feldern entworfen (Title, Purpose, When to use, Inputs, Outputs, Allowed/Forbidden actions, Fail-closed, Public-neutrality, ADR-0032-Grenzen, Human-maintainer-only, Output contract, Interaction). Alle docs-only, advisory, ersetzen keine Gates/Human Review.

## Overlap-Bewertung

Neutralität bleibt bei `ndf-public-neutrality-guard`; Rahmen/Self-Check bei `ndf-work-package-runner`; Abschluss bei `ndf-compact-context-summary-runner`. `ndf-changelog-writer` ist eigener Skill (Changelog ≠ Summary). Extended-Skills verweisen, statt zu duplizieren. Kein Overlap mit `ndf-context-pack-maintainer`. Project Knowledge: ADR-Texte, Prompt-Mode-Definitionen, Status/Context Pack, Known/v1.0 Notes. Prompt: WP-Ziele, Dateipfade, Sonderregeln, Commit-Message.

## WP-137 Implementierungsplan

Genau die 4 Kern-Skills als docs-only `SKILL.md` (+ ggf. 2 optionale bei ausdrücklichem Scope); erwartete Dateien: `.claude/skills/<name>/SKILL.md`, README-Update, `EXTENDED_CORE_SKILLS_MVP_VALIDATION.md`, `WP_137_...NOTES.md`; Validierung: genau freigegebene Skills, docs-only, 13 Felder, keine Scripts/Netz/Secrets/privaten Daten/Git-Release, ADR-0032 unverändert, Gate grün, kein v1.0; Prompt Mode Skill-assisted Full; Modell Opus 4.8.

## Geänderte / neue Dateien

- **NEU** `docs/validation/foundation-0-9/EXTENDED_SKILLS_PACK_BLUEPRINT.md`
- **NEU** `project-brain/WP_136_EXTENDED_SKILLS_PACK_BLUEPRINT_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0032 / Public Neutrality

ADR-0032 unverändert bindend; keine Skills implementiert/erweitert; `.claude/skills` unverändert; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine privaten Projektnamen/Domains; Secret-Name nur als Name; Gate grün.

## Risiken / offene Punkte

Scope Creep (max 4–6, Default 4); Overlap (verweisen statt duplizieren); Scheinsicherheit (advisory ≠ Gate); Release-/Git-Nähe (kein Auto-Release/Version); ADR-Urteile ohne Human Review (nichts autonom finalisieren); Neutralitäts-Fehldeutung (keine privaten Projektinhalte im Public NDF); Nutzen vor Breite.

## Nächster empfohlener Schritt

**NDF-WP-137 – Docs-only Extended Core Skills MVP Implementation** (Skill-assisted Full Prompt Mode, Opus 4.8) mit dem 4-Skill-Kern. Danach WP-138 (Real-use-Validierung, schließt DSK-001), später Project-Enablement-Blueprint.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-136 empfiehlt ein kleines Extended Core Skills Pack (4 Kern + bis 2 optional), konzeptionell entworfen, nicht implementiert; Overlap-Analyse und WP-137-Implementierungsplan erstellt. GO WITH NOTES; keine Skills implementiert/aktiviert; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-137.
