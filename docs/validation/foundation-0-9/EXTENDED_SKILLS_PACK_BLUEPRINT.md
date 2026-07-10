# Extended Skills Pack Blueprint

## DE – Zweck

Blueprint für die nächste sichere Skill-Ausbaustufe für **NDF-Core, Governance und Docs** (NDF-WP-136, Skill-assisted Full Prompt Mode). Baut auf der [External Skills Landscape & Prioritization](EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION.md) (WP-135), dem [Skills-first Operating Mode](SKILLS_FIRST_OPERATING_MODE.md) (WP-134), der [Docs-only Skills MVP Validation](DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (WP-129) und dem [Skills MVP Blueprint](SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md) (WP-125) auf. **Dieses WP implementiert keine Skills, verändert keine `.claude/skills` und aktiviert keine Extended Skills.**

## EN – Purpose

Blueprint for the next safe skill expansion for **NDF core, governance, and docs** (NDF-WP-136, skill-assisted Full Prompt Mode). Builds on WP-135/134/129/125. **This WP implements no skills, changes no `.claude/skills`, and activates no extended skills.**

## DE – Status / Ergebnis

**GO WITH NOTES.** Ein kleines **Extended Core Skills Pack** (4 Kern + bis zu 2 optionale) wird empfohlen; nur konzeptionell entworfen, nicht implementiert. Fokus: NDF Core Workflow, Security/ADR/Governance, Docs/Release/Communication, Existing Project Analysis. **Nicht Fokus** (spätere Project-Enablement-WPs): kreative/Branding/Product/UX/projektlokale Skills, App-Automation, Netzwerk-/API-/MCP-Skills, Git-/Release-Automation. ADR-0032 unverändert. Foundation 0.9 bleibt released/published, **nicht v1.0**.

## EN – Status / Result

**GO WITH NOTES.** A small **Extended Core Skills Pack** (4 core + up to 2 optional) is recommended; designed conceptually only, not implemented. Focus: NDF core workflow, security/ADR/governance, docs/release/communication, existing-project analysis. Not in focus (later project-enablement WPs): creative/branding/product/UX/project-local skills, app automation, network/API/MCP skills, git/release automation. ADR-0032 unchanged. Foundation 0.9 stays released/published, **not v1.0**.

## DE – Scope

Bewertung der P0/P1-Kern-Kandidaten, ein Extended-MVP-Vorschlag (max. 4–6 Skills), konzeptionelle Skill-Designs, Overlap-Analyse mit den bestehenden vier MVP-Skills, ein Implementierungsplan für WP-137 und eine Risikobewertung. **Nicht im Scope:** Skill-Implementierung, `.claude/skills`-Änderung, Extended-Skill-Aktivierung, Scripts, Netzwerk, private Daten, Commit/Push/Tag/Release, v1.0-Aktivierung.

## EN – Scope

Rating of the P0/P1 core candidates, an extended-MVP proposal (max 4–6 skills), conceptual skill designs, overlap analysis with the four existing MVP skills, a WP-137 implementation plan, and a risk assessment. Out of scope: skill implementation, `.claude/skills` changes, extended-skill activation, scripts, network, private data, commit/push/tag/release, v1.0 activation.

## DE – Input Summary

Ausgewertet: die vier MVP-Skills (`.claude/skills/*/SKILL.md`), WP-125-Blueprint, WP-129-Validation, WP-134-Operating-Mode/Compression, WP-135-Landscape (P0/P1-Kandidaten), [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), [ADR-0032](../../adr/ADR-0032-skill-security-policy.md).

## EN – Input Summary

Reviewed: the four MVP skills, the WP-125 blueprint, WP-129 validation, WP-134 operating mode/compression, WP-135 landscape (P0/P1 candidates), ADR-0031, ADR-0032.

## DE – Reconciliation-Hinweis zur WP-Nummerierung

WP-135 hatte WP-137 vorläufig als „Project Enablement Skills Blueprint" skizziert. Dieser Blueprint (WP-136) legt **WP-137 = Docs-only Extended Core Skills MVP Implementation** fest (Umsetzung der hier empfohlenen Core-Skills). Der Project-Enablement-Blueprint verschiebt sich damit auf ein **späteres WP** (Kandidat, nicht aktiviert).

## EN – Reconciliation Note on WP Numbering

WP-135 tentatively sketched WP-137 as a "Project Enablement Skills Blueprint." This blueprint sets **WP-137 = Docs-only Extended Core Skills MVP Implementation** (implementing the core skills recommended here). The project-enablement blueprint moves to a **later WP** (candidate, not activated).

## DE – P0/P1-Kandidatenbewertung

Empfehlung: **MVP Extended** / später / zurückstellen / ablehnen.

### P0

| Skill | Zweck / Problem | Token-Wert | NDF-Core | Projekt | Risiko | docs-only | Empfehlung |
|---|---|---|---|---|---|---|---|
| `ndf-skill-quality-reviewer` | prüft neue/geänderte Skill-Dokumente auf ADR-0032-Konformität, docs-only, Fail-closed, Vollständigkeit | mittel | **hoch** | mittel | gering | ja | **MVP Extended** |
| `ndf-existing-project-analysis-runner` | strukturiert die neutrale Analyse eines Bestandsprojekts (Onboarding) advisory | hoch | mittel | **hoch** | mittel | ja | **MVP Extended** |
| `ndf-docs-polish-runner` | strukturiert Docs-Politur (Klarheit, Konsistenz, Neutralität) advisory | hoch | **hoch** | hoch | gering | ja | **MVP Extended** |
| `ndf-changelog-writer` | strukturiert Changelog-Einträge im NDF-Stil (Keep-a-Changelog-artig) advisory | hoch | **hoch** | hoch | gering | ja | **MVP Extended** |

### P1 (Core/Governance/Docs)

| Skill | Zweck / Problem | Token-Wert | Risiko | docs-only | Empfehlung |
|---|---|---|---|---|---|
| `ndf-release-safety` | Release-Prep/Go-No-Go-Struktur; wiederholt „nur Human Maintainer taggt/releast" | mittel | **mittel** (release-nah) | ja | **MVP Extended optional** |
| `ndf-adr-governance-review` | ADR-Bedarf/nächste Nummer/Security-Review-Struktur (ADR-0032) | mittel | **mittel** | ja | **MVP Extended optional** |
| `ndf-v1-readiness-review` | v1.0-Readiness-Struktur | mittel | mittel | ja | später (vor v1.0) |
| `ndf-readme-quality-reviewer` | README-Qualitäts-/Vollständigkeitsprüfung | mittel | gering | ja | später |
| `ndf-release-notes-runner` | Release-Notes-Struktur | mittel | mittel (release-nah) | ja | später |
| `ndf-project-brief-runner` | Projekt-Brief-Struktur (Project-Enablement-nah) | mittel | gering | ja | später (Project-Enablement-WP) |

## EN – P0/P1 Candidate Assessment

The tables rate each P0/P1 candidate by purpose/problem, token value, NDF-core/project value, risk, docs-only fit, and recommendation. The four P0 skills are **MVP Extended**; `ndf-release-safety` and `ndf-adr-governance-review` are **MVP Extended optional** (release/governance-adjacent, medium risk); the remaining P1 skills are deferred to later WPs (readiness before v1.0; project-brief to a project-enablement WP).

## DE – Recommended Extended MVP

**Sicherer Default: 4 Kern-Skills** (die vier P0), optional erweiterbar auf **6**:

**Kern (4):**
1. `ndf-skill-quality-reviewer`
2. `ndf-existing-project-analysis-runner`
3. `ndf-docs-polish-runner`
4. `ndf-changelog-writer`

**Optional (bis zu +2, nur falls WP-137-Scope es ausdrücklich aufnimmt):**
5. `ndf-release-safety`
6. `ndf-adr-governance-review`

**Begründung:** Die vier Kern-Skills haben hohen Token-/Qualitätswert bei geringem Risiko und sind rein advisory/docs-only. Die zwei optionalen sind release-/governance-nah (mittleres Risiko) — sie bleiben wertvoll, sollten aber nur mit besonders strengen „kein Auto-Release / keine autonome ADR-Finalisierung"-Grenzen aufgenommen werden. **Lieber klein und sicher.**

## EN – Recommended Extended MVP

Safe default: **4 core skills** (the four P0), optionally extendable to **6**. Core: skill-quality-reviewer, existing-project-analysis-runner, docs-polish-runner, changelog-writer. Optional (+2, only if the WP-137 scope explicitly includes them): release-safety, adr-governance-review. Rationale: the four core skills are high-value, low-risk, purely advisory/docs-only; the two optional ones are release/governance-adjacent (medium risk) and need especially strict "no auto-release / no autonomous ADR finalization" limits. Prefer small and safe.

## DE – Skill-Designs (konzeptionell — keine Skill-Dateien)

### 1. `ndf-skill-quality-reviewer`

- **Title:** NDF Skill Quality Reviewer (docs-only).
- **Purpose:** prüft neue/geänderte Skill-Dokumente auf ADR-0032-Konformität, docs-only-Charakter, Fail-closed-Verhalten und Struktur-Vollständigkeit.
- **When to use:** vor Vorschlag/Übergabe eines neuen oder geänderten Skill-Dokuments (z. B. in WP-137).
- **Required inputs:** Entwurf eines Skill-Dokuments (Markdown), ADR-0032, Skill-Struktur-Checkliste.
- **Expected outputs:** Konformitäts-Checkliste (13 Pflichtfelder vorhanden?), Fail-closed-/Verbots-Prüfung, Neutralitäts-Hinweis, GO/REWORK-Vorschlag.
- **Allowed actions:** Skill-Dokumente lesen und prüfen; Struktur-/Grenz-Lücken benennen.
- **Forbidden actions:** Skills aktivieren/erstellen/erweitern; `.claude/skills` ändern; Scripts; Netz; Secrets; Git-/Release-Aktionen.
- **Fail-closed behavior:** bei fehlendem Pflichtfeld oder unklarer Grenze → REWORK, nicht GO.
- **Public-neutrality requirements:** keine privaten Namen/Domains/Suchmuster; Secret-Name nur genannt.
- **ADR-0032 safety boundaries:** docs-only, fail-closed; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen.
- **Human-maintainer-only boundaries:** Freigabe eines Skills bleibt beim Human Maintainer.
- **Output contract:** Prüf-Checkliste + GO/REWORK-Vorschlag; nie eine Aktivierung.
- **Interaction:** ergänzt `ndf-work-package-runner` (Rahmen) und `ndf-public-neutrality-guard` (Neutralität); Ergebnis fließt in `ndf-compact-context-summary-runner`.

### 2. `ndf-existing-project-analysis-runner`

- **Title:** NDF Existing Project Analysis Runner (docs-only, neutral).
- **Purpose:** strukturiert die neutrale, advisory Analyse eines Bestandsprojekts (Architektur-Überblick, Risiken, Onboarding-Fragen) ohne private Details zu fixieren.
- **When to use:** beim Onboarding eines bestehenden Projekt-Repos in einen NDF-Workflow.
- **Required inputs:** öffentlich/lokal lesbare Projektstruktur, WP-Ziel; keine Secrets/privaten Daten.
- **Expected outputs:** strukturierte Analyse-Gliederung (Struktur, offene Fragen, Risiken, nächste Schritte) als Vorschlag.
- **Allowed actions:** Projektdateien lesen; neutrale, generische Analyse-Struktur vorschlagen.
- **Forbidden actions:** private Projektnamen/Domains/Suchmuster in Public-NDF-Artefakte schreiben; Secrets lesen/ausgeben; Scripts; Netz; Git-/Release-Aktionen.
- **Fail-closed behavior:** bei privatem/unklarem Inhalt → nicht aufnehmen, als Lücke markieren.
- **Public-neutrality requirements:** Analyse-Struktur bleibt generisch; projektspezifische Konkretisierung nur im jeweiligen Projekt-Repo, nie im Public NDF.
- **ADR-0032 safety boundaries:** docs-only, fail-closed; keine Automation.
- **Human-maintainer-only boundaries:** Bewertungs-/Scope-Entscheidungen bleiben beim Human Maintainer.
- **Output contract:** advisory Analyse-Gliederung; nie eine ausgeführte Änderung.
- **Interaction:** nutzt `ndf-work-package-runner`-Rahmen; Ergebnisse via `ndf-compact-context-summary-runner`; Neutralität via `ndf-public-neutrality-guard`.

### 3. `ndf-docs-polish-runner`

- **Title:** NDF Docs Polish Runner (docs-only).
- **Purpose:** strukturiert die Politur von NDF-Dokumenten (Klarheit, Konsistenz, DE/EN-Parität, Neutralität) als Vorschlag.
- **When to use:** vor Übergabe/Commit eines größeren Doku-Artefakts.
- **Required inputs:** Doku-Entwurf; NDF-Stil-/Neutralitätsregeln.
- **Expected outputs:** Politur-Vorschläge (Struktur, Klarheit, Konsistenz, Neutralität); keine erzwungene Umschreibung von Substanz.
- **Allowed actions:** Doku lesen; Verbesserungsvorschläge machen.
- **Forbidden actions:** Substanz/Evidenz verändern ohne Auftrag; private Daten einfügen; Scripts; Netz; Git-/Release-Aktionen.
- **Fail-closed behavior:** bei Zweifel an Faktenlage → markieren statt umschreiben.
- **Public-neutrality requirements:** keine privaten Namen/Domains; Secret-Name nur genannt.
- **ADR-0032 safety boundaries:** docs-only, fail-closed.
- **Human-maintainer-only boundaries:** finale Textannahme beim Human Maintainer.
- **Output contract:** Politur-Vorschläge; nie automatische Massenumschreibung.
- **Interaction:** ergänzt `ndf-public-neutrality-guard`; Rahmen via `ndf-work-package-runner`.

### 4. `ndf-changelog-writer`

- **Title:** NDF Changelog Writer (docs-only).
- **Purpose:** strukturiert Changelog-Einträge im NDF-Stil (Keep-a-Changelog-artig, WP-referenziert, neutral) als Vorschlag.
- **When to use:** am Ende eines WPs, um den Changelog-Eintrag vorzubereiten.
- **Required inputs:** WP-Ergebnis, betroffene Artefakte, WP-ID.
- **Expected outputs:** ein neutraler, konsistenter Changelog-Eintragsvorschlag mit WP-Referenz und „not v1.0"-Invarianten wo passend.
- **Allowed actions:** Eintrag strukturieren; Stil/Konsistenz sichern.
- **Forbidden actions:** Version/Tag/Release behaupten oder auslösen; private Daten; Scripts; Netz; Git-Aktionen.
- **Fail-closed behavior:** kein erfundener Release-/Versionsstatus; bei Unsicherheit neutral formulieren.
- **Public-neutrality requirements:** keine privaten Namen/Domains/Suchmuster.
- **ADR-0032 safety boundaries:** docs-only, fail-closed.
- **Human-maintainer-only boundaries:** Version/Tag/Release bleibt beim Human Maintainer.
- **Output contract:** ein Changelog-Eintragsvorschlag; nie ein Commit/Tag.
- **Interaction:** ergänzt `ndf-compact-context-summary-runner`; Rahmen via `ndf-work-package-runner`.

### Optional 5–6 (kondensiert)

- **`ndf-release-safety`** — strukturiert Release-Prep/Go-No-Go **als Dokumentation**; verbotene Aktionen: jede Tag-/Release-/GitHub-Schreibaktion; wiederholt „nur Human Maintainer taggt/releast"; fail-closed; nur mit besonders strengen Grenzen aufnehmen.
- **`ndf-adr-governance-review`** — ADR-Bedarfsprüfung, nächste freie Nummer, Security-Review-Struktur (ADR-0032); verbotene Aktionen: autonome Accepted-Entscheidung/Umnummerierung/Massenmigration; fail-closed; finalisiert nichts ohne Human-Maintainer-Review.

## EN – Skill Designs (conceptual — no skill files)

The German section specifies each recommended extended-MVP skill with the 13 fields (title, purpose, when-to-use, required inputs, expected outputs, allowed/forbidden actions, fail-closed behavior, public-neutrality, ADR-0032 boundaries, human-maintainer-only boundaries, output contract, interaction with existing MVP skills). In summary: skill-quality-reviewer checks skill docs against ADR-0032/structure; existing-project-analysis-runner structures neutral advisory project analysis; docs-polish-runner structures documentation polish; changelog-writer structures neutral changelog entries. Optional release-safety and adr-governance-review stay documentation-only and finalize/trigger nothing autonomously.

## DE – Overlap-Bewertung

| Aspekt | Bestehender Skill | Extended-Skill | Entscheidung |
|---|---|---|---|
| Neutralitätsprüfung | `ndf-public-neutrality-guard` | `ndf-docs-polish-runner`, `ndf-skill-quality-reviewer` | **integriert bleiben** (Guard bleibt maßgeblich; Extended-Skills verweisen darauf) |
| Abschlussblöcke | `ndf-compact-context-summary-runner` | `ndf-changelog-writer` | **eigener Skill** (Changelog ≠ Rückmeldung/Summary), aber gemeinsame Nutzung |
| WP-Rahmen/Self-Check | `ndf-work-package-runner` | alle Extended | **integriert bleiben** (Rahmen kommt vom Runner) |
| Context-Pack | `ndf-context-pack-maintainer` | — | **kein Overlap** |
| Prompt-Mode-Auswahl | (in `work-package-runner`) | — | **kein neuer Skill** (bleibt integriert) |

**Was in Project Knowledge gehört:** ADR-Texte, Prompt-Mode-Definitionen, Phasenstatus/Context Pack, Known Notes, v1.0 Notes. **Was im Prompt bleiben muss:** konkrete WP-Ziele, Dateipfade, Sonderregeln, erwartete Commit-Message. **Redundant/abgelehnt:** eigenständiger `ndf-prompt-mode-selector` (bleibt integriert).

## EN – Overlap Assessment

The table maps each overlap: neutrality checks stay integrated (the guard remains authoritative; extended skills reference it); changelog-writer is a distinct skill from the summary runner; the WP frame/self-check comes from the runner (extended skills do not duplicate it); no overlap for the context-pack maintainer; a standalone prompt-mode-selector stays rejected (integrated). Project knowledge holds ADR texts, prompt-mode definitions, phase status/Context Pack, known notes, v1.0 notes; the prompt keeps WP goals, file paths, special rules, expected commit message.

## DE – WP-137 Implementierungsplan

**NDF-WP-137 – Docs-only Extended Core Skills MVP Implementation** (Kandidat, nicht aktiviert):

- **Umgesetzt werden genau:** die 4 Kern-Skills (`ndf-skill-quality-reviewer`, `ndf-existing-project-analysis-runner`, `ndf-docs-polish-runner`, `ndf-changelog-writer`) als docs-only `SKILL.md`. Die 2 optionalen (`ndf-release-safety`, `ndf-adr-governance-review`) nur, falls der Human Maintainer sie ausdrücklich in den Scope nimmt.
- **Nicht umgesetzt:** alle übrigen Kandidaten; keine Project-Enablement-/Creative-/Product-Skills; keine Extended-Aktivierung ohne Scope-Change.
- **Erwartete Dateien:** `.claude/skills/<name>/SKILL.md` je Skill; aktualisierter `.claude/skills/README.md`; `docs/validation/foundation-0-9/EXTENDED_CORE_SKILLS_MVP_VALIDATION.md`; `project-brain/WP_137_...NOTES.md`.
- **Validierungscheck:** genau die freigegebenen Skills; alle docs-only; 13-Pflichtfelder je `SKILL.md`; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; ADR-0032 unverändert; Gate grün; kein v1.0.
- **Nicht-Ziele:** Automation, Scripts, Netz, Extended-über-6-Skills, Project-Enablement-Skills, v1.0-Aktivierung.
- **Harte Grenzen:** wie ADR-0032; `.claude/skills` nur additiv für die freigegebenen Skills.
- **Vorgeschlagener Prompt Mode:** Skill-assisted Full Prompt Mode.
- **Empfohlenes Modell:** Claude Opus 4.8.

## EN – WP-137 Implementation Plan

WP-137 (candidate, not activated) implements exactly the four core skills as docs-only `SKILL.md` (plus the two optional only on explicit human-maintainer scope inclusion); implements nothing else; expected files are the per-skill `SKILL.md`, an updated skills README, an extended-core validation doc, and a WP-137 notes file; the validation check confirms exactly the approved skills, all docs-only, 13 fields each, no scripts/network/secrets/private-data/git-release, ADR-0032 unchanged, gate green, not v1.0; non-goals are automation/scripts/network/>6 skills/project-enablement/v1.0; prompt mode skill-assisted Full; model Opus 4.8.

## DE – Risks / Open Notes

- **Scope Creep:** max. 4–6 Skills; Default 4; Kandidatenliste ≠ Aktivierung.
- **Overlap:** Neutralität/Rahmen bleiben bei den bestehenden Skills; Extended-Skills verweisen statt duplizieren.
- **Scheinsicherheit:** Skills sind advisory; sie ersetzen keine Gates/Human Review.
- **Release-/Git-Nähe:** `ndf-release-safety`/`ndf-changelog-writer` dürfen nie Tag/Release/Version auslösen.
- **ADR-/Security-Urteile ohne Human Review:** `ndf-adr-governance-review` finalisiert nichts autonom.
- **Public-Neutrality-Fehldeutung:** `ndf-existing-project-analysis-runner` darf keine privaten Projektinhalte ins Public NDF bringen.
- **Token-Ersparnis ohne Qualitätsgewinn / zu viele Skills:** kleines Pack bevorzugt; Nutzen vor Breite.

## EN – Risks / Open Notes

Scope creep (max 4–6, default 4; candidates ≠ activation); overlap (neutrality/frame stay with existing skills; extended skills reference not duplicate); false security (skills are advisory, not gates/human review); release/git proximity (release-safety/changelog-writer never trigger tag/release/version); autonomous ADR/security judgments (adr-governance-review finalizes nothing); neutrality misreading (existing-project-analysis-runner must not bring private project content into public NDF); token saving without quality / too many skills (prefer a small pack).

## DE – Decision

**GO WITH NOTES.** Extended Core Skills Pack empfohlen (4 Kern + bis zu 2 optionale, max. 6); nur konzeptionell entworfen, keine Implementierung, keine Extended-Aktivierung; nächster WP: **WP-137 – Docs-only Extended Core Skills MVP Implementation**. ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0.

## EN – Decision

**GO WITH NOTES.** Extended core skills pack recommended (4 core + up to 2 optional, max 6); conceptual only, no implementation, no extended activation; next WP: WP-137 – Docs-only Extended Core Skills MVP Implementation. ADR-0032 unchanged; Foundation 0.9 stays not v1.0.

## DE – Recommendation

**NDF-WP-137 – Docs-only Extended Core Skills MVP Implementation** (Skill-assisted Full Prompt Mode, Opus 4.8) mit dem 4-Skill-Kern; die 2 optionalen nur auf ausdrücklichen Human-Maintainer-Scope. Danach WP-138 (Real-use-Validierung, schließt DSK-001) und später ein Project-Enablement-Blueprint. Nächste freie ADR-Nummer: 0033.

## EN – Recommendation

WP-137 (skill-assisted Full, Opus 4.8) with the 4-skill core; the 2 optional only on explicit human-maintainer scope. Then WP-138 (real-use validation, closes DSK-001) and later a project-enablement blueprint. Next free ADR number: 0033.
