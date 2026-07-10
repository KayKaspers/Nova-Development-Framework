# Skills-first Operating Mode

## DE – Zweck

Definiert den **Skills-first Operating Mode** für NDF (NDF-WP-134): Ab sofort nutzen Nova→Claude-Prompts die vier docs-only MVP-Skills aktiv, damit der wiederkehrende Prompt-Rahmen kürzer wird und Claude-Pro-Usage-Limits weniger belastet werden — ohne NDF-Governance zu schwächen. Baut auf der [Skills Prompt Compression Validation](SKILLS_PROMPT_COMPRESSION_VALIDATION.md) (WP-134) und der [Docs-only Skills MVP Validation](DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (WP-129) auf.

## EN – Purpose

Defines the **skills-first operating mode** for NDF (NDF-WP-134): from now on Nova→Claude prompts actively use the four docs-only MVP skills so the recurring prompt frame shrinks and Claude Pro usage limits are eased — without weakening NDF governance.

## DE – Status / Ergebnis

**GO WITH NOTES.** Skills-first Operating Mode dokumentiert und aktiv empfohlen. Keine neuen Skills, keine Extended Skills, keine Automation. ADR-0032 unverändert bindend. Foundation 0.9 bleibt released/published, **nicht v1.0**.

## EN – Status / Result

**GO WITH NOTES.** Skills-first operating mode documented and actively recommended. No new/extended skills, no automation. ADR-0032 unchanged. Foundation 0.9 stays released/published, **not v1.0**.

## DE – Scope

Ein Arbeitsmodus + Prompt-Kompressionsregeln + drei skill-basierte Prompt-Profile + Beispielprompts + priorisierte nächste Skill-WPs. **Nicht im Scope:** neue/Extended Skills, Scripts, Automation, Commit/Push/Tag/Release, v1.0-Aktivierung.

## EN – Scope

An operating mode + compression rules + three skill-assisted prompt profiles + example prompts + a prioritized next-skill-WP roadmap. Out of scope: new/extended skills, scripts, automation, commit/push/tag/release, v1.0 activation.

## DE – Verwendete Skills

Verbindlich für Struktur, Sicherheitsgrenzen, Rückmeldung an Nova, Compact Context Summary und Context-Pack-Pflege — **nicht** als Ersatz für Human Review, Public-Neutrality-Gates, ADR-0032, konkrete WP-Ziele/Dateipfade oder Commit/Push/Tag/Release durch den Human Maintainer:

- `ndf-work-package-runner`
- `ndf-compact-context-summary-runner`
- `ndf-public-neutrality-guard`
- `ndf-context-pack-maintainer`

**Hinweis:** Diese Skills sind docs-only Repository-Artefakte; sie wirken als **Verhaltens-/Struktur-Leitfaden** (Prompt-Kompression), nicht als autonom ausführende Tools.

## EN – Skills Used

Binding for structure, safety boundaries, Report to Nova, Compact Context Summary, and context-pack upkeep — not a substitute for human review, the neutrality gate, ADR-0032, concrete WP goals/paths, or human-maintainer commit/push/tag/release. These skills are docs-only repo artifacts acting as a behavioral/structural guide, not autonomous tools.

## DE – Modus-Auswahlregeln

- Skills werden **verpflichtend referenziert** für Rahmen, Abschlussblöcke und Context-Pack-Pflege in jedem WP.
- **Full Prompt Mode** bleibt nötig für: Security, ADR, Scope Lock, Release Readiness/Prep, v1.0-Reviews, neue Skill-Implementierungen, destruktive/Git-Write-/Tag-Fälle, unklare Anforderungen.
- **Standard Prompt Mode** wird **Default** für normale inhaltliche WPs, Blueprint-WPs, Review-WPs.
- **Short Prompt Mode** ist erlaubt für kleine Checks, Statuspflege, einfache Doku-Updates mit aktuellem Context Pack — nie für die Full-Pflichtfälle.

## EN – Mode Selection Rules

Skills are mandatorily referenced for frame, closing blocks, and context-pack upkeep. Full stays required for security/ADR/scope-lock/release/v1.0/new-skill/destructive/git-write/tag/unclear cases. Standard becomes the default for normal content/blueprint/review WPs. Short is allowed for small checks/status upkeep/simple doc updates with a current Context Pack, never for full-mandatory cases.

## DE – Prompt-Kompressionsregeln (Matrix)

| Prompt-Bestandteil | Künftig durch Skill? | Weiter explizit im Prompt? | Grund |
|---|---|---|---|
| NDF-Rollenbeschreibung | ✅ `work-package-runner` | ➖ | stabil, wiederkehrend |
| Human-Maintainer-only | ✅ | ➖ | invariant, sicherheitsrelevant |
| Keine Git-/Release-Aktionen | ✅ | ➖ | invariante Grenze |
| Public Neutrality | ✅ `public-neutrality-guard` | ➖ | invariante Regel |
| Secret-Regeln (Name ja, Wert nie) | ✅ | ➖ | invariant |
| Rückmeldung an Nova | ✅ `compact-context-summary-runner` | ➖ (Inhalt Pflicht) | fixes Format |
| Compact Context Summary | ✅ `compact-context-summary-runner` | ➖ (Inhalt Pflicht) | fixes Format |
| Context-Pack-Pflege | ✅ `context-pack-maintainer` | ➖ | wiederkehrende Pflege |
| Self-Check (`git status`/`diff`) | ✅ `work-package-runner` | ➖ | wiederkehrend |
| ADR-0031 | ➖ | ✅ (bei Bezug) | Governance-Substanz |
| ADR-0032 | ✅ (als Grenze erinnert) | ✅ (Wortlaut/Entscheidung) | Grenze via Skill, Substanz explizit |
| konkrete WP-Ziele | ➖ | ✅ | veränderlich |
| konkrete Dateipfade | ➖ | ✅ | WP-spezifisch |
| konkrete Known Notes | ➖ | ✅ | WP-spezifisch |
| erwartete Commit-Message | ➖ | ✅ | WP-spezifisch (nur Vorschlag) |
| Modellregel / empfohlenes Modell | ✅ (Erinnerung) | ✅ (Override möglich) | stabile Regel |
| Prompt Mode | ✅ (Vorschlag) | ✅ (Override möglich) | Skill schlägt vor |
| Startgate | ✅ `work-package-runner` | ➖ | wiederkehrender Prüfschritt |

## EN – Prompt Compression Rules (Matrix)

The table assigns each block to skill-carried and/or still-explicit. Stable frame (role, human-only, no-git/release, neutrality, secret rules, closing blocks, context-pack upkeep, self-check, startgate) is skill-carried; WP-specific substance (goals, file paths, known notes, commit message) and governance substance (ADR texts/decisions) stay explicit. Model rule and prompt mode are skill-suggested but prompt-overridable.

## DE – Neue Nova→Claude Prompt-Profile

### A. Skill-assisted Short Prompt

Für kleine Checks, Statuspflege, einfache Doku-Updates. Muss enthalten: WP-ID · Ziel · zu verwendende Skills · konkrete Dateien · erwartetes Ergebnis · Commit-Message · (Rückmeldung an Nova + Compact Context Summary via Skill).

### B. Skill-assisted Standard Prompt

Für normale WPs, Blueprint-WPs, Review-WPs. Muss enthalten: WP-ID · Ziel · aktueller Kontext kompakt · zu verwendende Skills · harte Sondergrenzen · erwartete Artefakte · Commit-Message · (Rückmeldung an Nova + Compact Context Summary via Skill).

### C. Skill-assisted Full Prompt

Für Release, ADR, Security, v1.0, neue Skill-Implementierungen. Bleibt ausführlicher, ersetzt aber Standardblöcke durch Skills. Muss enthalten: alles aus Standard + volle Governance-/Release-/v1.0-Substanz, Nicht-Aktivierungs-Listen, ausdrückliche Scope-Grenzen.

## EN – New Nova→Claude Prompt Profiles

A (Short) — small checks/status/simple docs: WP-ID, goal, skills, files, expected result, commit message, closing blocks via skill. B (Standard) — normal/blueprint/review WPs: adds compact context, hard special limits, expected artifacts. C (Full) — release/ADR/security/v1.0/new-skill: stays fuller, replaces standard blocks with skills, keeps full governance substance and non-activation lists.

## DE – Beispielprompts (nur Illustration, keine echten WP-Starts)

### Beispiel 1 – Normaler Doku-WP (Short)

```text
NDF-WP-XXX – <kurzes Doku-Update>
Prompt Mode: Skill-assisted Short
Skills: ndf-work-package-runner, ndf-compact-context-summary-runner, ndf-public-neutrality-guard
Ziel: <ein Satz>.
Dateien: <konkrete Pfade>.
Ergebnis: GO WITH NOTES falls sauber.
Commit-Vorschlag: docs(scope): <message>
Abschluss: Rückmeldung an Nova + Compact Context Summary via Skill.
```

### Beispiel 2 – Review-WP (Standard)

```text
NDF-WP-XXX – <Review-Titel>
Prompt Mode: Skill-assisted Standard
Skills: ndf-work-package-runner, ndf-compact-context-summary-runner, ndf-public-neutrality-guard, ndf-context-pack-maintainer
Kontext (kompakt): Foundation 0.9 released/published; nicht v1.0; ADR-0032 bindend.
Ziel: <Review-Ziel>. Sondergrenzen: <falls vorhanden>.
Erwartete Artefakte: <Validation-Doc, Notes>. Commit-Vorschlag: docs(validation): <message>
Abschluss: Rückmeldung an Nova + Compact Context Summary via Skill.
```

### Beispiel 3 – Skills-/Governance-WP (Full)

```text
NDF-WP-XXX – <Governance-/Skill-Titel>
Prompt Mode: Skill-assisted Full
Skills: alle vier MVP-Skills
Kontext + volle Substanz: <ADR-Bezug, Scope-Grenzen, Nicht-Aktivierungs-Liste, Secret-Name-Regel>.
Harte Grenzen: keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; docs-only; fail-closed.
Ziel: <Governance-Ziel>. Erwartete Artefakte: <Docs>. Commit-Vorschlag: docs(...): <message>
Abschluss: Rückmeldung an Nova + Compact Context Summary via Skill.
```

## EN – Example Prompts (illustration only, no real WP starts)

Three short skill-assisted example prompts (Short/Standard/Full) show how Nova can give markedly shorter prompts while keeping WP-ID, goal, skills, files, commit suggestion, and the mandatory closing blocks. These are documentation examples, not activated WPs.

## DE – DSK-001 Bewertung

**DSK-001 → Partially closed.** Strukturelle Prompt-Kompressions-Baseline erstellt (siehe Validation-Doc); empirische Real-Use-Messung bleibt offen und ist Ziel einer späteren Real-use-Validierung (WP-139).

## EN – DSK-001 Assessment

**DSK-001 → Partially closed.** Structural compression baseline created; empirical real-use measurement remains open for a later real-use validation (WP-139).

## DE – Priorisierte nächste Skill-WPs (Kandidaten, nicht aktiviert)

Da der Human Maintainer Skills priorisiert, empfohlene Reihenfolge:

1. `WP-135 – External Skills Landscape & Project Skill Prioritization`
2. `WP-136 – NDF Extended Skills Pack Blueprint`
3. `WP-137 – Project Enablement Skills Blueprint`
4. `WP-138 – Docs-only Extended Skills MVP Implementation`
5. `WP-139 – Skill Prompt Compression Real-use Validation` (schließt DSK-001)
6. danach `v1.0 Gap Review & Scope Lock`

**Begründung der Reihenfolge:** zuerst Landschaft/Priorisierung (135) → Blueprints (136/137) vor Implementierung (138) → Real-use-Messung (139) vor dem v1.0-Pfad. Alle bleiben **Kandidaten**; keine Aktivierung durch WP-134. Optionale WP-130/131/132 bleiben unberührt.

## EN – Prioritized Next Skill WPs (candidates, not activated)

Recommended order: WP-135 (external skills landscape & prioritization) → WP-136 (extended skills pack blueprint) → WP-137 (project enablement skills blueprint) → WP-138 (docs-only extended skills MVP implementation) → WP-139 (real-use compression validation, closes DSK-001) → then v1.0 gap review & scope lock. Rationale: landscape/prioritization before blueprints, blueprints before implementation, real-use measurement before the v1.0 path. All stay candidates; WP-134 activates none. WP-130/131/132 stay untouched.

## DE – Risks / Open Notes

- DSK-001 teilweise offen (Real-use-Messung, WP-139).
- Over-Compression: Full-Pflichtfälle + Short-Verbotsliste bleiben bindend.
- Skills sind keine Gates/Human-Review-Ersatz; der reale Public Quality Gate bleibt maßgeblich.
- Neue Skill-WPs (135–139) sind Kandidaten, nicht aktiviert; keine Extended Skills durch WP-134.

## EN – Risks / Open Notes

DSK-001 partially open (real-use measurement, WP-139); over-compression mitigated by full-mandatory cases + Short forbidden list; skills are not gates/human-review substitutes; WP-135–139 are candidates, not activated; no extended skills via WP-134.

## DE – Decision

**GO WITH NOTES.** Skills-first Operating Mode aktiv dokumentiert; Standard Prompt Mode als Default, Full für kritische Fälle; DSK-001 Partially closed; keine neuen/Extended Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0.

## EN – Decision

**GO WITH NOTES.** Skills-first operating mode documented; Standard as default, Full for critical cases; DSK-001 partially closed; no new/extended skills; ADR-0032 unchanged; Foundation 0.9 stays not v1.0.
