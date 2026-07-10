# External Skills Landscape & Project Skill Prioritization

## DE – Zweck

Bewertung externer Claude-Skill-Quellen (als Inspiration, nicht als Copy/Paste-Vorlage) und der vorhandenen NDF-Skills, um daraus priorisierte Skill-Families und eine Skill-Roadmap für NDF-Core und NDF-basierte Projekte abzuleiten (NDF-WP-135, Skill-assisted Standard Prompt Mode). **Dieses WP implementiert keine neuen Skills und aktiviert keine Extended Skills.**

## EN – Purpose

Assessment of external Claude-skill sources (as inspiration, not copy/paste) and the existing NDF skills, to derive prioritized skill families and a skill roadmap for NDF core and NDF-based projects (NDF-WP-135, skill-assisted Standard Prompt Mode). **This WP implements no new skills and activates no extended skills.**

## DE – Status / Ergebnis

**GO WITH NOTES.** Externe Quellen werden als Kategorie-/Inspirationsmodell genutzt, nichts wird 1:1 übernommen. Sieben Skill-Families priorisiert; NDF-Core und Project-Enablement getrennt; Allowlist/Watchlist/Rejectlist erstellt; nächste Skill-WPs (135→v1.0) empfohlen. Keine neuen/Extended Skills, keine Scripts, kein Netzwerk, keine privaten Projektnamen. ADR-0032 unverändert. Foundation 0.9 bleibt released/published, **nicht v1.0**.

## EN – Status / Result

**GO WITH NOTES.** External sources used as a category/inspiration model, nothing copied verbatim. Seven skill families prioritized; NDF core and project enablement separated; allow/watch/reject lists created; next skill WPs (135→v1.0) recommended. No new/extended skills, scripts, network, or private project names. ADR-0032 unchanged. Foundation 0.9 stays released/published, **not v1.0**.

## DE – Scope

Quellenbewertung, Skill-Family-Priorisierung, Kandidatenbewertung (P0–P3), Allow/Watch/Reject, Public-vs-Project-local-Trennung, Skill-Roadmap. **Nicht im Scope:** Skill-Implementierung, Extended-Skill-Aktivierung, Kopieren fremder Skills/Lizenztexte/Scripts, Netzwerkzugriff, private Projektlogik, Commit/Push/Tag/Release, v1.0-Aktivierung.

## EN – Scope

Source assessment, skill-family prioritization, candidate rating (P0–P3), allow/watch/reject, public-vs-project-local split, skill roadmap. Out of scope: skill implementation, extended-skill activation, copying third-party skills/licenses/scripts, network access, private project logic, commit/push/tag/release, v1.0 activation.

## DE – Input Summary

Ausgewertet: die vier vorhandenen MVP-Skills (`.claude/skills/*/SKILL.md`), der [Skills-first Operating Mode](SKILLS_FIRST_OPERATING_MODE.md) (WP-134), die [Prompt Compression Validation](SKILLS_PROMPT_COMPRESSION_VALIDATION.md) (WP-134), der [Skills MVP Blueprint](SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md) (WP-125), [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), [ADR-0032](../../adr/ADR-0032-skill-security-policy.md) und die vier genannten externen GitHub-Quellen (als Kategoriemodell).

## EN – Input Summary

Reviewed: the four existing MVP skills, the skills-first operating mode (WP-134), the prompt compression validation (WP-134), the Skills MVP Blueprint (WP-125), ADR-0031, ADR-0032, and the four named external GitHub sources (as a category model).

## DE – Netzwerk-Hinweis (wichtig)

Gemäß ADR-0032 wurde **kein Netzwerkzugriff** ausgeführt; die externen Quellen wurden **nicht live** abgerufen. Sie werden hier als **Kategorie-/Muster-Inspiration** aus allgemeinem Ökosystem-Wissen bewertet — der aktuelle konkrete Inhalt der Repositories wird **nicht** behauptet. Vor einer späteren Adaption einzelner Muster ist eine ausdrückliche, vom Human Maintainer freigegebene Lizenz-/Attributionsprüfung nötig.

## EN – Network Note (important)

Per ADR-0032, **no network access** was performed; the external sources were **not fetched live**. They are assessed as **category/pattern inspiration** from general ecosystem knowledge — the current concrete repository contents are **not** asserted. Any later adaptation of a pattern requires an explicit, human-maintainer-approved license/attribution check.

## DE – Quellenbewertung

Bewertung als Inspirations-/Kategoriemodell (keine 1:1-Übernahme, keine Datei-/Lizenz-/Script-Kopie):

| Quelle | Quellentyp (Kategorie) | Nutzen NDF-Core | Nutzen Projekte | Direkte Übernahme | Geeignete NDF-Adaption | Risiken |
|---|---|---|---|---|---|---|
| Jeffallan / claude-skills | Einzel-Sammlung praktischer Skill-Beispiele | mittel | mittel | **nein** | Skill-Struktur-/Format-Ideen (neutral nachbauen) | Lizenz-/Attributionslage vor Übernahme unklar; ggf. Automations-/Script-Muster (ADR-0032-Konflikt) |
| BehiSecc / awesome-claude-skills | kuratierte „awesome"-Liste (Katalog) | hoch (Kategoriemodell) | hoch | **nein** | Taxonomie/Kategorien als Inspiration für NDF-Families | Katalog verweist auf Dritt-Skills mit gemischten Lizenzen/Automation |
| rastian / behavioral-design-skills | thematische Skill-Sammlung (Behavioral/UX) | niedrig–mittel | hoch (Product/UX) | **nein** | Konzepte für UX-/Adoption-/Onboarding-Reviewer (neutral, docs-only) | „Behavioral"-Muster dürfen nicht in dark-pattern-/manipulatives Wachstum kippen |
| ComposioHQ / awesome-claude-skills | kuratierte „awesome"-Liste (Katalog, tool-/integrationsnah) | mittel | mittel | **nein** | Kategorie-Inspiration; **Vorsicht:** viele Einträge tool-/API-/integrationsgetrieben | starke Nähe zu Netzwerk-/API-/Automations-Skills → für NDF überwiegend Rejectlist |

**Gemeinsamer Befund:** Externe Quellen sind als **Landkarte/Kategoriemodell** wertvoll, aber keine direkte Bezugsquelle für NDF-Skills. NDF-Skills werden **neutral selbst formuliert**, docs-only, ADR-0032-konform.

## EN – Source Assessment

The table rates each source as an inspiration/category model only (no verbatim, license, or script copy). Common finding: the sources are valuable as a **map/category model**, not a direct supply of NDF skills; NDF skills are authored **neutrally in-house**, docs-only, ADR-0032-compliant. Composio's catalog in particular skews tool/API/integration-driven → mostly Rejectlist for NDF.

## DE – Skill Families (priorisiert)

| # | Family | Zweck | NDF-Core-Nutzen | Projekt-Nutzen | Token-Economy | Risiko | MVP-Kandidaten | Extended-Kandidaten | Nicht empfohlen |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NDF Core Workflow Skills | WP/Review/Release/Context-Rahmen | **sehr hoch** | mittel | sehr hoch | gering | (bereits im MVP) | `ndf-release-safety` | — |
| 2 | Security / ADR / Governance Skills | ADR-/Security-Review-Struktur | hoch | mittel | mittel | mittel | — | `ndf-adr-governance-review`, `ndf-v1-readiness-review` | autonome Security-Runner |
| 3 | Docs / Release / Communication Skills | Docs-/Changelog-/Release-Notes-Struktur | hoch | hoch | hoch | gering | — | `ndf-docs-polish-runner`, `ndf-changelog-writer`, `ndf-release-notes-runner` | Auto-Publishing |
| 4 | Engineering & Architecture Skills | Architektur-/Feature-Scope-/Analyse-Advisory | mittel | **hoch** | mittel | mittel | — | `ndf-architecture-blueprint-runner`, `ndf-feature-scope-runner`, `ndf-existing-project-analysis-runner` | Auto-Codegen/Auto-Refactor-Runner |
| 5 | Product / UX / Adoption Skills | Discovery-/UX-/Onboarding-Advisory | niedrig | **hoch** | mittel | mittel | — | `ndf-product-discovery-runner`, `ndf-ux-flow-reviewer`, `ndf-onboarding-friction-reviewer` | dark-pattern-/manipulatives Growth |
| 6 | Creative / Branding / Content Skills | Branding-/Naming-/Content-Advisory | niedrig | mittel | mittel | gering–mittel | — | `ndf-branding-kit-runner`, `ndf-naming-runner`, `ndf-content-tone-reviewer` | Auto-Social-Posting |
| 7 | Project Setup / Migration / Existing-Project-Analysis | Projekt-Onboarding/-Analyse-Advisory | mittel | **hoch** | mittel | mittel | — | `ndf-existing-project-analysis-runner`, `ndf-project-brief-runner` | private Projektlogik im Public NDF |

**Leitprinzip:** Families 1–3 sind NDF-Core-nah (public-neutral, hoher Wiederverwendungswert); 4–7 sind primär Project-Enablement (advisory, docs-only), müssen aber private Projektlogik aus dem Public NDF heraushalten.

## EN – Skill Families (prioritized)

The table prioritizes seven families by purpose, NDF-core value, project value, token economy, risk, and MVP/extended/not-recommended candidates. Families 1–3 are NDF-core-adjacent (public-neutral, high reuse); 4–7 are primarily project enablement (advisory, docs-only) and must keep private project logic out of public NDF.

## DE – Konkrete Skill-Kandidaten (P0–P3)

Priorität: P0 = hoher Wert/geringes Risiko/kurzfristig; P1 = hoher Wert, nach Blueprint; P2 = mittlerer Wert/später; P3 = niedriger Wert oder integriert. Empfehlung: **implementieren** (docs-only, nach Scope-Change) / **blueprinten** / **zurückstellen** / **ablehnen**.

### NDF-Core / Governance

| Skill | NDF-/Projekt-Nutzen | Token-Wert | Risiko | docs-only | Priorität | Empfehlung |
|---|---|---|---|---|---|---|
| `ndf-release-safety` | Release-Prep/Go-No-Go-Struktur | mittel | mittel (release-nah) | ja | **P1** | blueprinten (WP-136) |
| `ndf-adr-governance-review` | ADR-/Security-Review-Struktur | mittel | mittel | ja | **P1** | blueprinten (WP-136) |
| `ndf-v1-readiness-review` | v1.0-Readiness-Struktur | mittel | mittel | ja | **P1** | blueprinten (WP-136), vor v1.0 |
| `ndf-prompt-mode-selector` | Modus-Auswahl | gering | gering | ja | **P3** | zurückstellen (in `work-package-runner` integriert) |
| `ndf-skill-quality-reviewer` | Skill-Qualität/ADR-0032-Konformität prüfen | mittel | gering | ja | **P0** | blueprinten (WP-136) — nützlich, um weitere Skills sicher zu bauen |

### Engineering / Architecture

| Skill | Nutzen | Token-Wert | Risiko | docs-only | Priorität | Empfehlung |
|---|---|---|---|---|---|---|
| `ndf-architecture-blueprint-runner` | Architektur-Advisory | mittel | mittel | ja | **P1** | blueprinten (WP-137) |
| `ndf-feature-scope-runner` | Feature-Scope-Advisory | mittel | mittel | ja | **P1** | blueprinten (WP-137) |
| `ndf-existing-project-analysis-runner` | Bestandsprojekt-Analyse (Onboarding) | hoch | mittel | ja | **P0** | blueprinten (WP-137) — hoher Projektnutzen |
| `ndf-implementation-review-runner` | Implementierungs-Review-Struktur | mittel | mittel | ja | **P2** | zurückstellen |
| `ndf-test-strategy-runner` | Teststrategie-Advisory | mittel | gering | ja | **P2** | zurückstellen |
| `ndf-debugging-root-cause-reviewer` | Root-Cause-Advisory | mittel | gering | ja | **P2** | zurückstellen |

### Product / UX / Adoption

| Skill | Nutzen | Token-Wert | Risiko | docs-only | Priorität | Empfehlung |
|---|---|---|---|---|---|---|
| `ndf-product-discovery-runner` | Discovery-Advisory | mittel | gering | ja | **P2** | blueprinten (WP-137) |
| `ndf-ux-flow-reviewer` | UX-Flow-Advisory | mittel | gering | ja | **P2** | blueprinten (WP-137) |
| `ndf-behavioral-adoption-reviewer` | Adoption-Advisory | mittel | **mittel–hoch** | ja | **P2** | zurückstellen — nur mit strengen Ethik-Grenzen |
| `ndf-onboarding-friction-reviewer` | Onboarding-Reibung senken | mittel | gering | ja | **P2** | blueprinten (WP-137) |
| `ndf-ethical-growth-reviewer` | ethische Wachstums-Leitplanken | mittel | gering | ja | **P1** | blueprinten (WP-137) — Gegen-Guard zu dark patterns |

### Creative / Branding / Content

| Skill | Nutzen | Token-Wert | Risiko | docs-only | Priorität | Empfehlung |
|---|---|---|---|---|---|---|
| `ndf-branding-kit-runner` | Branding-Advisory | gering | gering | ja | **P3** | zurückstellen |
| `ndf-creative-direction-runner` | Creative-Direction | gering | gering | ja | **P3** | zurückstellen |
| `ndf-naming-runner` | Naming-Advisory | gering | gering | ja | **P3** | zurückstellen |
| `ndf-ui-style-system-runner` | UI-Style-System-Advisory | mittel | gering | ja | **P2** | zurückstellen |
| `ndf-landing-page-concept-runner` | Landing-Page-Konzept | gering | gering | ja | **P3** | zurückstellen |
| `ndf-content-tone-reviewer` | Ton-/Content-Review | mittel | gering | ja | **P2** | zurückstellen |

### Docs / Communication

| Skill | Nutzen | Token-Wert | Risiko | docs-only | Priorität | Empfehlung |
|---|---|---|---|---|---|---|
| `ndf-docs-polish-runner` | Docs-Politur | hoch | gering | ja | **P0** | blueprinten (WP-136) |
| `ndf-readme-quality-reviewer` | README-Qualität | mittel | gering | ja | **P1** | blueprinten (WP-136) |
| `ndf-changelog-writer` | Changelog-Struktur | hoch | gering | ja | **P0** | blueprinten (WP-136) |
| `ndf-release-notes-runner` | Release-Notes-Struktur | mittel | mittel (release-nah) | ja | **P1** | blueprinten (WP-136) |
| `ndf-project-brief-runner` | Projekt-Brief-Struktur | mittel | gering | ja | **P1** | blueprinten (WP-137) |

## EN – Concrete Skill Candidates (P0–P3)

The tables rate each named candidate by NDF/project value, token value, risk, docs-only fit, priority (P0 high value/low risk/near-term; P1 after blueprint; P2 later; P3 low value or integrated), and recommendation (implement/blueprint/defer/reject). Highlights: P0 = `ndf-skill-quality-reviewer`, `ndf-existing-project-analysis-runner`, `ndf-docs-polish-runner`, `ndf-changelog-writer`. `ndf-prompt-mode-selector` stays deferred (already integrated). `ndf-behavioral-adoption-reviewer` is deferred pending strict ethics limits; `ndf-ethical-growth-reviewer` is P1 as its counter-guard.

## DE – Allowlist / Watchlist / Rejectlist

### Allowlist (kurzfristig sicher docs-only adaptierbar)

`ndf-skill-quality-reviewer`, `ndf-docs-polish-runner`, `ndf-changelog-writer`, `ndf-release-notes-runner`, `ndf-readme-quality-reviewer`, `ndf-adr-governance-review`, `ndf-release-safety`, `ndf-v1-readiness-review`, `ndf-existing-project-analysis-runner`, `ndf-project-brief-runner`.

### Watchlist (hoher Nutzen, erst nach zusätzlicher Prüfung)

`ndf-architecture-blueprint-runner`, `ndf-feature-scope-runner`, `ndf-product-discovery-runner`, `ndf-ux-flow-reviewer`, `ndf-onboarding-friction-reviewer`, `ndf-ethical-growth-reviewer`, `ndf-ui-style-system-runner`, `ndf-content-tone-reviewer`, `ndf-test-strategy-runner`, `ndf-implementation-review-runner`, `ndf-debugging-root-cause-reviewer`, `ndf-behavioral-adoption-reviewer` (nur mit Ethik-Grenzen).

### Rejectlist (gehört nicht in NDF)

- Git-/Release-Automation-Skills
- App-Automation mit OAuth/API
- Netzwerk-Skills
- Secret-verarbeitende Skills
- Payment-/Wallet-/Crypto-Automation
- Social-Media-Autoposting
- offensive Security Tool Runner
- autonome Multi-Agent-Orchestrierung
- Skills mit unklarer Lizenz-/Attributionslage für direkte Übernahme
- private Projektlogik im Public NDF

## EN – Allowlist / Watchlist / Rejectlist

Allowlist (safely docs-only-adaptable near-term): the ten listed core/docs/governance skills. Watchlist (high value, needs more review): the engineering/product/UX/creative-adjacent skills, with `ndf-behavioral-adoption-reviewer` only under ethics limits. Rejectlist (does not belong in NDF): git/release automation, OAuth/API app automation, network skills, secret-processing skills, payment/wallet/crypto automation, social autoposting, offensive security tool runners, autonomous multi-agent orchestration, unclear-license direct copies, and private project logic in public NDF.

## DE – Public NDF vs Project-local Skills

**Public NDF Skills:** neutral, wiederverwendbar, keine privaten Projektmuster — z. B. die MVP-Skills, Governance-, Docs- und generische Architektur-/UX-Advisory-Skills.

**Project-local Skills:** in einzelnen Projekt-Repos sinnvoll, aber **nicht** im Public NDF, weil sie domänenspezifische Muster kapseln. Bewertet als **neutrale Archetypen** (bewusst ohne private Projektnamen, gemäß Public-Neutrality-Regel):

| Projekt-Archetyp (neutral) | Beispielhafte Project-local Skills | Warum nicht Public NDF |
|---|---|---|
| Streaming-/Broadcast-Operations-Projekt | Streaming-Workflow-/Kanal-Konzept-Advisory | domänenspezifische Betriebslogik |
| Self-hosted Voice-/Community-Server-Projekt | Voice-Server-/Rollen-/Moderations-Advisory | plattformspezifische Muster |
| Dashboard-/IoT-/Monitoring-Projekt | Telemetrie-/Dashboard-Layout-Advisory | gerätespezifische Datenmodelle |
| Community-/Web-Plattform-Projekt | Community-Onboarding-/Content-Advisory | organisationsspezifische Flows |
| Branding-/Produkt-/UX-Neuprojekt | projektspezifische Branding-/Naming-Kits | projekteigene Markenidentität |

**Regel:** Public-NDF-Skills bleiben generisch; jede Konkretisierung auf ein reales Projekt (inkl. Namen, Domains, Suchmuster) gehört ausschließlich in das jeweilige Projekt-Repo, nicht ins Public NDF.

## EN – Public NDF vs Project-local Skills

Public NDF skills are neutral, reusable, and free of private project patterns (the MVP skills, governance, docs, and generic architecture/UX advisory). Project-local skills belong in individual project repos, not public NDF, because they encapsulate domain-specific patterns. They are described as **neutral archetypes** (deliberately without private project names, per the neutrality rule): streaming/broadcast-operations, self-hosted voice/community-server, dashboard/IoT/monitoring, community/web-platform, and branding/product/UX-greenfield archetypes. Rule: public NDF skills stay generic; any concretization to a real project (names, domains, search patterns) belongs solely in that project's repo.

## DE – Priorisierte Skill-Roadmap (nächste WPs, Kandidaten – nicht aktiviert)

| WP | Ziel | Modellklasse | Prompt Mode | Risiko | Abhängigkeiten | Erwartetes Ergebnis | Vor v1.0? |
|---|---|---|---|---|---|---|---|
| WP-135 | Skill-Priorisierung / Landscape (dieses WP) | Opus 4.8 | Skill-assisted Standard | gering | WP-134 | GO WITH NOTES | ja |
| WP-136 | NDF Extended Skills Pack Blueprint (Core/Governance/Docs) | Opus 4.8 | Skill-assisted Full | mittel | WP-135 | Blueprint (keine Implementierung) | ja |
| WP-137 | Project Enablement Skills Blueprint (Eng/Arch/Product/UX) | Opus 4.8 | Skill-assisted Full | mittel | WP-135 | Blueprint (keine Implementierung) | optional vor v1.0 |
| WP-138 | Docs-only Extended Skills MVP Implementation | Opus 4.8 | Skill-assisted Full | mittel | WP-136 (+ggf. 137), Human-Maintainer-Scope-Change | erweitertes docs-only Skill Set | optional |
| WP-139 | Skill Prompt Compression Real-use Validation (schließt DSK-001) | Opus 4.8 | Skill-assisted Standard | gering | WP-138 | DSK-001 Closed | empfohlen vor v1.0 |
| — | v1.0 Gap Review & Scope Lock | Opus 4.8 | Full | mittel | WP-139 | v1.0-Pfad-Review | — |

**Begründung:** Priorisierung/Scope (135) vor Blueprints (136/137) vor Implementierung (138) vor Real-use-Messung (139) vor v1.0. Alle bleiben **Kandidaten**; WP-135 aktiviert keinen davon.

## EN – Prioritized Skill Roadmap (next WPs, candidates – not activated)

The table sequences WP-135 → 136 (extended core/governance/docs blueprint) → 137 (project-enablement blueprint) → 138 (docs-only extended MVP, needs a human-maintainer scope change) → 139 (real-use validation, closes DSK-001) → v1.0 gap review & scope lock, with per-WP goal, model class (Opus 4.8), prompt mode, risk, dependencies, expected result, and pre-v1.0 flag. Rationale: prioritization before blueprints before implementation before real-use measurement before v1.0. All stay candidates; WP-135 activates none.

## DE – Risks / Open Notes

- **Keine Live-Quellenprüfung** (ADR-0032): externe Repos nicht abgerufen; Bewertung als Kategoriemodell; konkrete Inhalte nicht behauptet.
- **Lizenz-/Attribution:** vor jeder Adaption ausdrückliche, human-maintainer-freigegebene Prüfung nötig.
- **Scope Creep:** die vielen Kandidaten sind Kandidaten, nicht Aktivierungen; MVP bleibt vier Skills.
- **Neutralität:** Project-local-Skills nur als neutrale Archetypen; keine privaten Projektnamen im Public NDF.
- **Ethik:** Adoption-/Behavioral-Skills brauchen Ethik-Guards (kein dark-pattern-Growth).

## EN – Risks / Open Notes

No live source check (ADR-0032); license/attribution needs explicit human-maintainer-approved review before any adaptation; the many candidates are candidates, not activations (MVP stays four skills); project-local skills only as neutral archetypes (no private names in public NDF); adoption/behavioral skills need ethics guards.

## DE – Decision

**GO WITH NOTES.** Externe Quellen als Inspirations-/Kategoriemodell genutzt, nichts 1:1 übernommen; sieben Families priorisiert; NDF-Core und Project-Enablement getrennt; Allow/Watch/Reject und Roadmap erstellt; keine neuen/Extended Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0.

## EN – Decision

**GO WITH NOTES.** External sources used as inspiration/category model, nothing copied verbatim; seven families prioritized; NDF core and project enablement separated; allow/watch/reject and roadmap produced; no new/extended skills; ADR-0032 unchanged; Foundation 0.9 stays not v1.0.

## DE – Recommendation

**NDF-WP-136 – NDF Extended Skills Pack Blueprint** als nächster Schritt (Core/Governance/Docs, P0/P1-Allowlist), Skill-assisted Full Prompt Mode, Opus 4.8; parallel/danach WP-137 (Project Enablement). Real-use-Validierung (WP-139) schließt DSK-001 vor dem v1.0 Gap Review. Nächste freie ADR-Nummer: 0033.

## EN – Recommendation

**NDF-WP-136 – NDF Extended Skills Pack Blueprint** next (core/governance/docs, the P0/P1 allowlist), skill-assisted Full prompt mode, Opus 4.8; WP-137 (project enablement) alongside/after. Real-use validation (WP-139) closes DSK-001 before the v1.0 gap review. Next free ADR number: 0033.
