# NDF-WP-135 – External Skills Landscape & Project Skill Prioritization (Notes)

## Ziel

Externe Claude-Skill-Quellen (als Inspiration) und die vorhandenen NDF-Skills auswerten, daraus priorisierte Skill-Families und eine Skill-Roadmap für NDF-Core und NDF-basierte Projekte ableiten. Keine Skill-Implementierung, keine Extended-Skill-Aktivierung.

## Input Summary

Vier MVP-Skills (`.claude/skills/`), Skills-first Operating Mode + Prompt Compression Validation (WP-134), Skills MVP Blueprint (WP-125), ADR-0031/0032, vier externe GitHub-Quellen (als Kategoriemodell, nicht live abgerufen).

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-134 committet `b73a739`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## Netzwerk-/Neutralitäts-Hinweis

Kein Netzwerkzugriff (ADR-0032) — externe Quellen nicht live abgerufen, nur als Kategorie-/Muster-Inspiration bewertet; konkrete Repo-Inhalte nicht behauptet. Keine privaten Projektnamen im Public-NDF: Project-local-Skills nur als **neutrale Archetypen** beschrieben (Streaming-Operations, Voice-/Community-Server, Dashboard-/IoT, Community-/Web, Branding-/Produkt-/UX — ohne reale Namen).

## Skills geprüft

Vier MVP-Skills bestätigt (docs-only, ADR-0032-konform). Externe Quellen als Inspirations-/Kategoriemodell, keine 1:1-Übernahme.

## Quellenbewertung (Kategoriemodell)

- Jeffallan/claude-skills — Einzel-Sammlung; Struktur-Ideen; keine Übernahme (Lizenz/Automation unklar).
- BehiSecc/awesome-claude-skills — Katalog; Taxonomie-Inspiration; keine Übernahme.
- rastian/behavioral-design-skills — Behavioral/UX-Sammlung; Konzepte für UX-/Adoption-Reviewer; Ethik-Guard nötig.
- ComposioHQ/awesome-claude-skills — tool-/integrationsnaher Katalog; überwiegend Rejectlist (API-/Netz-/Automations-Nähe).

## Skill Families (priorisiert)

1 NDF Core Workflow (sehr hoch) · 2 Security/ADR/Governance · 3 Docs/Release/Communication · 4 Engineering/Architecture · 5 Product/UX/Adoption · 6 Creative/Branding/Content · 7 Project Setup/Migration/Existing-Project-Analysis. Families 1–3 NDF-Core-nah/public-neutral; 4–7 primär Project-Enablement (advisory, docs-only).

## Empfohlene Kandidaten (Priorität)

- **P0:** `ndf-skill-quality-reviewer`, `ndf-existing-project-analysis-runner`, `ndf-docs-polish-runner`, `ndf-changelog-writer`
- **P1:** `ndf-release-safety`, `ndf-adr-governance-review`, `ndf-v1-readiness-review`, `ndf-readme-quality-reviewer`, `ndf-release-notes-runner`, `ndf-project-brief-runner`, `ndf-architecture-blueprint-runner`, `ndf-feature-scope-runner`, `ndf-ethical-growth-reviewer`
- **P2:** `ndf-implementation-review-runner`, `ndf-test-strategy-runner`, `ndf-debugging-root-cause-reviewer`, `ndf-product-discovery-runner`, `ndf-ux-flow-reviewer`, `ndf-onboarding-friction-reviewer`, `ndf-ui-style-system-runner`, `ndf-content-tone-reviewer`, `ndf-behavioral-adoption-reviewer` (nur mit Ethik-Grenzen)
- **P3 (zurückstellen/integriert):** `ndf-prompt-mode-selector`, `ndf-branding-kit-runner`, `ndf-creative-direction-runner`, `ndf-naming-runner`, `ndf-landing-page-concept-runner`

## Allowlist / Watchlist / Rejectlist

- **Allowlist:** P0/P1 Core-/Docs-/Governance-Skills (kurzfristig docs-only adaptierbar).
- **Watchlist:** Engineering/Product/UX/Creative-Kandidaten (nach Prüfung).
- **Rejectlist:** Git-/Release-Automation, OAuth/API-App-Automation, Netzwerk-Skills, Secret-verarbeitende Skills, Payment/Crypto, Social-Autoposting, offensive Security-Runner, autonome Multi-Agent-Orchestrierung, unklare Lizenz für Direktübernahme, private Projektlogik im Public NDF.

## Public NDF vs Project-local

Public NDF = neutral/wiederverwendbar (MVP-, Governance-, Docs-, generische Architektur-/UX-Advisory-Skills). Project-local = domänenspezifisch, nur in Projekt-Repos, als neutrale Archetypen beschrieben.

## Empfohlene nächste WPs (Kandidaten, nicht aktiviert)

WP-136 (Extended Skills Pack Blueprint, Core/Governance/Docs) → WP-137 (Project Enablement Skills Blueprint) → WP-138 (Docs-only Extended Skills MVP, braucht Human-Maintainer-Scope-Change) → WP-139 (Real-use-Validierung, schließt DSK-001) → v1.0 Gap Review & Scope Lock.

## Geänderte / neue Dateien

- **NEU** `docs/validation/foundation-0-9/EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION.md`
- **NEU** `project-brain/WP_135_EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0032 / Public Neutrality

ADR-0032 unverändert bindend; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine fremden Skills/Lizenztexte kopiert; Secret-Name nur genannt. Gate grün. Keine privaten Projektnamen/Domains/Suchmuster.

## Risiken / offene Punkte

Keine Live-Quellenprüfung (Kategoriemodell); Lizenz-/Attributionsprüfung vor Adaption nötig; Scope Creep (Kandidaten ≠ Aktivierung, MVP bleibt vier Skills); Ethik-Guards für Adoption-/Behavioral-Skills.

## Nächster empfohlener Schritt

**NDF-WP-136 – NDF Extended Skills Pack Blueprint** (Core/Governance/Docs, P0/P1-Allowlist; Skill-assisted Full Prompt Mode, Opus 4.8). Nächste freie ADR-Nummer: 0033.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-135 hat externe Skill-Quellen als Kategoriemodell bewertet (keine Übernahme), sieben NDF-Skill-Families priorisiert, NDF-Core und Project-Enablement getrennt, Allow/Watch/Reject und eine Skill-Roadmap (136→v1.0) erstellt. GO WITH NOTES; keine neuen/Extended Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-136.
