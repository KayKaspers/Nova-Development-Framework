# Skill Prompt Compression Real-use Validation

## DE – Titel

Real-use-Validierung des NDF Docs-only Skill-Packs (acht Skills) für Prompt-Kompression und Token-Economy (NDF-WP-138, Skill-assisted Full Prompt Mode).

## DE – Status / Ergebnis

**GO WITH NOTES.** Das acht-teilige Skill-Pack ist praktisch verwendbar und verkürzt wiederkehrende NDF-Prompts real. **DSK-001 → Closed with notes** (Kern-Skills seit WP-134 über mehrere reale WPs genutzt; strukturell + praktisch belegt, keine exakte Token-Instrumentierung). **ECS-001 → Partially closed** (Extended-Core-Skills erst seit WP-137, geringe Nutzungshistorie). Skill-assisted Standard Prompt Mode bleibt **Default (bestätigt mit Notes)**. Keine neuen/geänderten Skills. ADR-0032 unverändert. Foundation 0.9 bleibt released/published, **nicht v1.0**.

## EN – Status / Result

**GO WITH NOTES.** The eight-skill pack is practically usable and really shortens recurring NDF prompts. **DSK-001 → Closed with notes** (core skills used across multiple real WPs since WP-134; structurally and practically evidenced, no exact token instrumentation). **ECS-001 → Partially closed** (extended core skills exist only since WP-137, limited usage history). Skill-assisted Standard Prompt Mode stays **default (confirmed with notes)**. No new/changed skills. ADR-0032 unchanged. Foundation 0.9 stays released/published, **not v1.0**.

## DE – Scope

Real-use-Prüfung der acht Skills anhand bestehender NDF-Promptmuster: praktische Verwendbarkeit, reale Prompt-Verkürzung, profitierende Prompt-Typen, Governance-/Neutralitäts-/ADR-0032-Stabilität, Default-Bestätigung, nächste Roadmap. **Nicht im Scope:** neue Skills, Skill-Änderungen, `.claude/skills`-Änderung, Scripts, Netzwerk, Live-Token-Instrumentierung, Commit/Push/Tag/Release, v1.0-Aktivierung.

## EN – Scope

Real-use check of the eight skills against existing NDF prompt patterns: practical usability, real prompt shortening, benefiting prompt types, governance/neutrality/ADR-0032 stability, default confirmation, next roadmap. Out of scope: new skills, skill changes, `.claude/skills` changes, scripts, network, live token instrumentation, commit/push/tag/release, v1.0 activation.

## DE – Input Summary

Ausgewertet: die acht Skills (`.claude/skills/*/SKILL.md` + README), der [Skills-first Operating Mode](SKILLS_FIRST_OPERATING_MODE.md) (WP-134), die [Prompt Compression Validation](SKILLS_PROMPT_COMPRESSION_VALIDATION.md) (WP-134), die [Docs-only Skills MVP Validation](DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (WP-129), die [Extended Core Skills MVP Validation](EXTENDED_CORE_SKILLS_MVP_VALIDATION.md) (WP-137), [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), [ADR-0032](../../adr/ADR-0032-skill-security-policy.md) — sowie die praktische Nutzung des Skill-Rahmens über die WPs 134–137.

## EN – Input Summary

Reviewed: the eight skills + README, the skills-first operating mode (WP-134), the prompt compression validation (WP-134), the docs-only MVP validation (WP-129), the extended-core MVP validation (WP-137), ADR-0031, ADR-0032 — plus the practical use of the skill frame across WPs 134–137.

## DE – Skills Reviewed

| Skill | Herkunft | Markdown-only | ADR-0032-konform | Real-use-tauglich |
|---|---|---|---|---|
| `ndf-work-package-runner` | WP-129 | ja | ja | **ja** (Rahmen/Guardrails/Self-Check) |
| `ndf-compact-context-summary-runner` | WP-129 | ja | ja | **ja** (Abschlussblöcke) |
| `ndf-public-neutrality-guard` | WP-129 | ja | ja | **ja** (Neutralität/Secret-Namensregel) |
| `ndf-context-pack-maintainer` | WP-129 | ja | ja | **ja** (Context-Pack-Pflege) |
| `ndf-skill-quality-reviewer` | WP-137 | ja | ja | ja (bei Skill-WPs) |
| `ndf-existing-project-analysis-runner` | WP-137 | ja | ja | ja (bei Onboarding-WPs) |
| `ndf-docs-polish-runner` | WP-137 | ja | ja | ja (bei Docs-WPs) |
| `ndf-changelog-writer` | WP-137 | ja | ja | ja (bei WP-Abschluss/Changelog) |

Prüfung: genau acht Skills, alle Markdown-only, keine Scripts/ausführbaren Dateien, keine optionalen Release-/ADR-Skills, keine privaten Daten/Secret-Werte, keine Git-/Release-Aktionen in Skill-Texten; ADR-0032 unverändert; Public Neutrality eingehalten.

## EN – Skills Reviewed

The table confirms all eight skills are markdown-only, ADR-0032-compliant, and real-use-suitable (the four core skills carry the frame/closing/neutrality/context-pack; the four extended-core skills apply to skill/onboarding/docs/changelog WPs). Exactly eight skills; no scripts/executables; no optional release/ADR skills; no private data/secret values; no git/release actions in skill texts; ADR-0032 unchanged; neutrality preserved.

## DE – Validation Method

ADR-0032 verbietet Live-Instrumentierung/Scripts; die Methode ist daher **strukturell + erfahrungsbasiert**: vier reale NDF-Prompt-Typen werden verglichen (Baseline ohne Skills vs. skill-assisted), gestützt auf die **tatsächliche Nutzung** des Skill-Rahmens über die WPs 134–138. Reduktion als **Prozentbereich** (keine falsche Genauigkeit), plus Governance-Auswirkung und Eignungsentscheidung. Der Unterschied zu WP-134: dort rein strukturelle Baseline; hier zusätzlich reale Nutzungserfahrung mit dem vollständigen acht-teiligen Pack.

## EN – Validation Method

ADR-0032 forbids live instrumentation/scripts; the method is **structural + experience-based**: four real NDF prompt types are compared (baseline vs. skill-assisted), grounded in the **actual use** of the skill frame across WPs 134–138. Reduction as a **percentage range** (no false precision), plus governance impact and a suitability decision. Difference from WP-134: that was a purely structural baseline; here real usage experience with the full eight-skill pack is added.

## DE – Real-use Prompt Comparisons

### Fall 1 – Normaler Doku-/Review-WP

- **Baseline ohne Skills (explizit nötig):** Rolle, harte Grenzen, Neutralität, Secret-Regeln, Self-Check, Abschlussformat, Rückmeldung-an-Nova-/Compact-Context-Summary-Vorlagen + WP-Ziel, Kontext, Dateien, Commit-Message.
- **Skill-assisted (getragen von):** `ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, ggf. `ndf-docs-polish-runner`.
- **Weiterhin explizit:** WP-ID, Ziel, konkreter Kontext, Dateien, Sonderregeln, Commit-Message.
- **Reduktion:** ~45–60 %. **Governance:** unverändert. **Entscheidung:** geeignet.

### Fall 2 – Skills-/Governance-WP

- **Baseline:** Standardrahmen + ADR-0032-Grenzen, Skill-Scope-/Nicht-Aktivierungs-Regeln, Neutralitätsdetails.
- **Skill-assisted:** Rahmen skill-getragen; `ndf-skill-quality-reviewer` strukturiert die Konformitätsprüfung; ADR-Substanz bleibt explizit.
- **Weiterhin explizit:** Governance-/Scope-Entscheidung, Nicht-Aktivierungs-Liste, Commit-Message.
- **Reduktion:** ~30–45 % (Rahmen hoch, Substanz gering). **Governance:** verbessert (strukturierte Skill-Review-Checkliste). **Entscheidung:** geeignet mit Notes (Full Prompt Mode bleibt Pflicht).

### Fall 3 – Existing-Project-Analysis-WP

- **Baseline:** Standardrahmen + Analyse-Struktur, Neutralitätsregeln (keine privaten Projektinhalte).
- **Skill-assisted:** Rahmen + `ndf-existing-project-analysis-runner` (neutrale Analyse-Gliederung) + `ndf-public-neutrality-guard`.
- **Weiterhin explizit:** konkretes Zielprojekt-Ziel, betroffene (lokale) Dateien, Sonderregeln, Commit-Message.
- **Reduktion:** ~40–55 %. **Governance:** verbessert (Neutralitätsgrenze strukturell verankert). **Entscheidung:** geeignet mit Notes (Neutralität besonders beachten).

### Fall 4 – Changelog-/Docs-Polish-WP

- **Baseline:** Standardrahmen + Changelog-Format, Docs-Stil-/Neutralitätsregeln, „not v1.0"-Invarianten.
- **Skill-assisted:** Rahmen + `ndf-changelog-writer` + `ndf-docs-polish-runner` + `ndf-compact-context-summary-runner`.
- **Weiterhin explizit:** WP-Ergebnis, betroffene Dateien, Commit-Message.
- **Reduktion:** ~50–65 % (stark wiederkehrender Rahmen). **Governance:** unverändert. **Entscheidung:** geeignet.

## EN – Real-use Prompt Comparisons

Four real prompt types were compared. (1) Normal doc/review WP — ~45–60 % reduction, governance unchanged, suitable. (2) Skills/governance WP — ~30–45 % (frame high, substance low), governance improved via the skill-review checklist, suitable with notes (Full mandatory). (3) Existing-project-analysis WP — ~40–55 %, governance improved (neutrality boundary structurally embedded), suitable with notes (watch neutrality). (4) Changelog/docs-polish WP — ~50–65 % (highly recurring frame), governance unchanged, suitable. Still-explicit blocks in all: WP-ID, goal, concrete context, files, special rules, commit message.

## DE – DSK-001 Assessment

**DSK-001 → Closed with notes.** Begründung: Die Kern-Skills tragen den wiederkehrenden Rahmen seit WP-134 über mehrere reale WPs; die strukturelle Baseline (WP-134) plus die praktische Nutzung belegen eine reale, deutliche Prompt-Overhead-Reduktion (~40–65 % je Prompt-Typ). **Note:** keine exakte Token-Instrumentierung (ADR-0032-konform nicht möglich); die Prozentbereiche sind belastbare Schätzungen, keine Messwerte.

## EN – DSK-001 Assessment

**DSK-001 → Closed with notes.** Core skills have carried the recurring frame across multiple real WPs since WP-134; the structural baseline plus practical use evidence a real, marked prompt-overhead reduction (~40–65 % per type). Note: no exact token instrumentation (not ADR-0032-possible); the ranges are robust estimates, not measurements.

## DE – ECS-001 Assessment

**ECS-001 → Partially closed.** Die Extended-Core-Skills (WP-137) sind strukturell tragfähig und in den Fällen 2–4 nutzbar, aber erst seit WP-137 vorhanden; die reale Nutzungshistorie ist noch kurz. Vollständiger Abschluss nach breiterer praktischer Anwendung (z. B. im v1.0-Pfad oder in Projekt-Enablement-WPs).

## EN – ECS-001 Assessment

**ECS-001 → Partially closed.** The extended-core skills are structurally sound and usable in cases 2–4 but exist only since WP-137; usage history is still short. Full closure after broader practical application (e.g., in the v1.0 path or project-enablement WPs).

## DE – Token-Economy Findings

- Der stabile Rahmen (Rolle, Grenzen, Neutralität, Abschlussblöcke, Self-Check) ist der Haupttreiber und real am stärksten reduzierbar.
- Docs-/Changelog-/normale WPs profitieren am stärksten (~45–65 %); Governance-WPs beim Rahmen (~30–45 %), nicht bei der Substanz.
- Die Extended-Core-Skills verbessern zusätzlich die Qualität/Konsistenz (Review-, Analyse-, Docs-, Changelog-Struktur), nicht nur die Länge.
- Kein exaktes Tokenversprechen; Prozentbereiche sind Schätzungen.

## EN – Token-Economy Findings

The stable frame drives and reduces most; docs/changelog/normal WPs benefit most (~45–65 %); governance WPs benefit on the frame (~30–45 %), not substance; extended-core skills also improve quality/consistency, not just length; no exact token promise (ranges are estimates).

## DE – Governance Findings

Public Neutrality, ADR-0031, ADR-0032, Human-Maintainer-only, Rückmeldung an Nova und Compact Context Summary bleiben **stabil oder verbessert**: `ndf-skill-quality-reviewer` und `ndf-public-neutrality-guard` erhöhen die strukturelle Prüftiefe, ohne Gates/Human Review zu ersetzen. Release-/v1.0-Substanz bleibt explizit. Kein Skill führt Git-/Release-Aktionen aus. ADR-0032 unverändert.

## EN – Governance Findings

Public neutrality, ADR-0031/0032, human-maintainer-only, Report to Nova, and Compact Context Summary stay **stable or improved**: the skill-quality-reviewer and neutrality-guard raise structural check depth without replacing gates/human review; release/v1.0 substance stays explicit; no skill performs git/release actions; ADR-0032 unchanged.

## DE – Skills-first Default Decision

**Bestätigt mit Notes.** Der WP-134-Default trägt in der Praxis:

- **Skill-assisted Standard Prompt Mode = Default** für normale inhaltliche WPs.
- **Skill-assisted Full Prompt Mode** für Security/Release/ADR/v1.0/neue Skills.
- **Skill-assisted Short Prompt Mode** für kleine Checks mit aktuellem Context Pack.

**Note:** Governance-/Release-/v1.0-Substanz bleibt explizit; die Extended-Core-Skills brauchen breitere Nutzung (ECS-001), bevor der Default für governance-nahe WPs weiter gelockert wird.

## EN – Skills-first Default Decision

**Confirmed with notes.** The WP-134 default holds in practice: Standard as default for normal content WPs; Full for security/release/ADR/v1.0/new-skill; Short for small checks with a current Context Pack. Note: governance/release/v1.0 substance stays explicit; the extended-core skills need broader use (ECS-001) before further loosening for governance-adjacent WPs.

## DE – Roadmap Recommendation

Bewertet:

| Option | Claude-Limit-Entlastung | v1.0-Readiness | NDF-Core-Stabilität | Projektnutzen | Risiko/Scope Creep |
|---|---|---|---|---|---|
| **A. v1.0 Gap Review & Scope Lock** | hoch (Skills genügen) | **hoch** | hoch | mittel | gering |
| B. Project Enablement Skills Blueprint | mittel | mittel | mittel | hoch | mittel |
| C. Additional Core Governance Skills Blueprint | mittel | mittel–hoch | hoch | niedrig | mittel |

**Empfehlung: Option A – `WP-139 – v1.0 Gap Review & Scope Lock`.** Das acht-teilige Skill-Pack ist real-use-tauglich und trägt den NDF-Arbeitsmodus ausreichend, um den v1.0-Pfad strukturiert zu prüfen. Die optionalen Governance-Skills (`ndf-release-safety`, `ndf-adr-governance-review`, `ndf-v1-readiness-review`) und Project-Enablement bleiben Kandidaten und können **innerhalb/nach** dem v1.0 Gap Review priorisiert werden — kein Blocker für den Review-Start.

## EN – Roadmap Recommendation

The table rates options A/B/C by Claude-limit relief, v1.0 readiness, NDF-core stability, project value, and risk. **Recommendation: Option A — `WP-139 – v1.0 Gap Review & Scope Lock`.** The eight-skill pack is real-use-suitable and carries the NDF way of working enough to review the v1.0 path in a structured way. The optional governance skills and project enablement stay candidates and can be prioritized within/after the v1.0 gap review — not a blocker.

## DE – Risks / Open Notes

- **ECS-001 teilweise offen:** breitere Real-use-Historie der Extended-Core-Skills nötig.
- **Keine exakte Token-Messung** (ADR-0032): Prozentbereiche sind Schätzungen.
- **Over-Compression:** Full-Pflichtfälle + Short-Verbotsliste bleiben bindend; Governance-Substanz explizit.
- **Skill-Scheinsicherheit:** Skills sind advisory; Gates/Human Review bleiben maßgeblich.

## EN – Risks / Open Notes

ECS-001 partially open (broader real-use history needed); no exact token measurement (ranges are estimates); over-compression mitigated by full-mandatory cases + Short forbidden list and explicit governance substance; skills are advisory, not gates/human review.

## DE – Decision

**GO WITH NOTES.** Skill-Pack real-use-tauglich; Prompt-Overhead real deutlich reduziert (~40–65 %); **DSK-001 Closed with notes**, **ECS-001 Partially closed**; Skills-first Standard-Default bestätigt mit Notes; keine neuen/geänderten Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. **Nächster empfohlener WP: WP-139 – v1.0 Gap Review & Scope Lock.**

## EN – Decision

**GO WITH NOTES.** Pack real-use-suitable; prompt overhead really reduced (~40–65 %); DSK-001 closed with notes, ECS-001 partially closed; skills-first Standard default confirmed with notes; no new/changed skills; ADR-0032 unchanged; Foundation 0.9 stays not v1.0. Next recommended WP: WP-139 – v1.0 Gap Review & Scope Lock.
