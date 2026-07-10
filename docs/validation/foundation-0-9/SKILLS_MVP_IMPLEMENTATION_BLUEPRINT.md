# Skills MVP Implementation Blueprint

## DE – Zweck

Blueprint für ein späteres, docs-only, fail-closed **NDF Skills Pack MVP** (NDF-WP-125, Full Prompt Mode). Er baut auf der [Skills MVP Implementation Decision](../../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md) (WP-124, Option B) und dem [Skills MVP Design](../../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md) (WP-111) auf und schließt die Design→Implementierungs-Lücke: konkretes (konzeptionelles) Skill-Set, Token-Economy-Bewertung, Sicherheitsmodell, Trennung Skill/Project Knowledge/Prompt, Validierungsplan und eine WP-129-Empfehlung. **Dieses WP erstellt nur einen Blueprint — kein aktives Skill Pack, keine `.claude/skills`, keine `SKILL.md`, keine Skill-Dateien, keine Scripts.**

## EN – Purpose

Blueprint for a later, docs-only, fail-closed **NDF Skills Pack MVP** (NDF-WP-125, Full Prompt Mode). It builds on the Skills MVP Implementation Decision (WP-124, Option B) and the Skills MVP Design (WP-111) and closes the design→implementation gap: a concrete (conceptual) skill set, token-economy assessment, security model, Skill/Project-Knowledge/Prompt separation, a validation plan, and a WP-129 recommendation. **This WP produces only a blueprint — no active skill pack, no `.claude/skills`, no `SKILL.md`, no skill files, no scripts.**

## DE – Status / Ergebnis

**GO WITH NOTES – WP-129 recommended with constrained docs-only MVP scope.** Foundation 0.9 ist `released / published — reconciliation documented` (`v0.9.0-foundation`, 2026-07-10), **nicht v1.0**, **kein v1.0 RC**, **ohne aktive volle v1.x-Zusage**, **ohne aktives Skill Pack**. WP-125 ist `optional/conditional — intentionally activated for blueprint` und aktiviert **weder WP-129 noch ein Skill Pack**. ADR-0032 bleibt bindend und unverändert. Nächste freie ADR-Nummer: 0033.

## EN – Status / Result

**GO WITH NOTES – WP-129 recommended with constrained docs-only MVP scope.** Foundation 0.9 is `released / published — reconciliation documented` (`v0.9.0-foundation`, 2026-07-10), **not v1.0**, **no v1.0 RC**, **no active full v1.x promise**, **no active skill pack**. WP-125 is `optional/conditional — intentionally activated for blueprint` and activates **neither WP-129 nor a skill pack**. ADR-0032 stays binding and unchanged. Next free ADR number: 0033.

## DE – Scope

Bewertet werden zehn Skill-Kandidaten; empfohlen wird ein kleines MVP-Set (3–5 Skills), ein Extended-Set für später und eine Liste nicht empfohlener Skills. Zusätzlich: Token-Economy-Bewertung, Sicherheitsmodell je Skill, Trennung Skill/Project Knowledge/Prompt, konzeptioneller Datei-Aufbau, Validierungsplan, zukünftige Prompt-Strategie und WP-129-Empfehlung. **Nicht im Scope:** Skill-Implementierung, `.claude/skills`, `SKILL.md`, Skill-Dateien, Scripts, Aktivierung optionaler WPs, Commit/Push/Tag/Release, Netzwerk, Secrets, private Daten.

## EN – Scope

Ten skill candidates are evaluated; a small MVP set (3–5 skills), an extended set for later, and a not-recommended list are proposed. Plus: token-economy assessment, per-skill security model, Skill/Project-Knowledge/Prompt separation, conceptual file layout, validation plan, future prompt strategy, and a WP-129 recommendation. **Out of scope:** skill implementation, `.claude/skills`, `SKILL.md`, skill files, scripts, activation of optional WPs, commit/push/tag/release, network, secrets, private data.

## DE – Input Summary

Ausgewertet wurden: [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md) (v1.x Compatibility Policy, Accepted), [ADR-0032](../../adr/ADR-0032-skill-security-policy.md) / [Skill Security Policy](../../agent-workflows/NDF_SKILL_SECURITY_POLICY.md) (fail-closed), [Skills MVP Design](../../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md) (WP-111), [Skills MVP Decision](../../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md) (WP-124, Option B), [Prompt Modes](../../agent-workflows/NDF_PROMPT_MODES.md) (WP-113), [Context Economy](../../agent-workflows/NDF_CONTEXT_ECONOMY.md) (WP-109), das [Context Pack Template](../../../project-brain/CONTEXT_PACK_TEMPLATE.md), der [Foundation 0.9 Context Pack](../../../project-brain/CONTEXT_PACK_FOUNDATION_0_9.md), die 0.9-Evidence ([WP-122](../context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md), [WP-123](../context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md), [WP-126](ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md)) und die [WP-133 Reconciliation Notes](../../../project-brain/WP_133_FOUNDATION_0_9_POST_RELEASE_RECONCILIATION_CLEANUP_NOTES.md).

## EN – Input Summary

Reviewed: ADR-0031 (v1.x compatibility, Accepted), ADR-0032 / Skill Security Policy (fail-closed), the Skills MVP Design (WP-111), the Skills MVP Decision (WP-124, Option B), Prompt Modes (WP-113), Context Economy (WP-109), the Context Pack Template, the Foundation 0.9 Context Pack, the 0.9 evidence (WP-122/123/126), and the WP-133 reconciliation notes.

## DE – Problem Statement

Das größte praktische Hindernis ist derzeit nicht die NDF-Architektur, sondern der **Token- und Prompt-Overhead**. Full-Prompt-, Release-, ADR-/Security- und v1.0-WPs wiederholen dieselben Blöcke: Rollenbeschreibung, harte Grenzen, Public-Neutrality-Regeln, Secret-Regeln, Abschlussformat, „Rückmeldung an Nova" und „Compact Context Summary". Für einen Claude-Pro-Nutzer führt das nach wenigen großen Prompts zu Usage-Limits. Skills können diese wiederkehrenden, stabilen Regelblöcke als wiederverwendbare Bausteine kapseln — der Prompt trägt dann nur noch das WP-Spezifische. Ziel: weniger Wiederholung, weniger Tokens, gleiche oder bessere Sicherheit.

## EN – Problem Statement

The main practical obstacle today is not NDF architecture but **token/prompt overhead**. Full-prompt, release, ADR/security, and v1.0 WPs repeat the same blocks: role description, hard limits, public-neutrality rules, secret rules, closing format, "Report to Nova," and "Compact Context Summary." For a Claude Pro user this hits usage limits after a few large prompts. Skills can encapsulate these recurring, stable rule blocks as reusable building blocks — the prompt then carries only the WP-specific parts. Goal: less repetition, fewer tokens, equal or better safety.

## DE – Design Goals

1. **Token-Economy first:** maximale, sichere Reduktion wiederholter Prompt-Blöcke.
2. **Fail-closed & docs-only:** was nicht ausdrücklich erlaubt ist, ist verboten (ADR-0032).
3. **Sicherheit nie schwächen:** kürzere Prompts dürfen kein Gate, kein Human-Review, keine Evidenz entfernen.
4. **Klein & fokussiert:** ein MVP mit wenigen, klar abgegrenzten Skills.
5. **Klare Schichtung:** Skill vs Project Knowledge vs Prompt sauber trennen.
6. **v1.0-Alltagstauglichkeit:** die Arbeitsweise für den Regelbetrieb tragfähig machen.
7. **Human-first:** jede Entscheidung/Ausführung bleibt beim Human Maintainer.

## EN – Design Goals

(1) Token-economy first — maximal, safe reduction of repeated prompt blocks. (2) Fail-closed & docs-only per ADR-0032. (3) Never weaken safety — leaner prompts must not remove a gate, human review, or evidence. (4) Small & focused MVP. (5) Clear layering Skill vs Project Knowledge vs Prompt. (6) v1.0 everyday viability. (7) Human-first — every decision/execution stays with the Human Maintainer.

## DE – Non-Goals

Kein aktives Skill Pack; keine `.claude/skills`; keine `SKILL.md`; keine Skill-Dateien; keine Scripts; keine Netzwerk-Skills; keine autonomen Git-/Release-/Tag-Aktionen; keine Aktivierung von WP-129/130/131/132; keine Lockerung von ADR-0031/0032; kein v1.0-Claim; keine aktive volle v1.x-Zusage; keine Cursor-Rules-/Workflow-Implementierung; kein Drittanbieter-Skill-Import; keine Chain-of-Thought-Dokumentation.

## EN – Non-Goals

No active skill pack; no `.claude/skills`; no `SKILL.md`; no skill files; no scripts; no network skills; no autonomous git/release/tag actions; no activation of WP-129/130/131/132; no relaxation of ADR-0031/0032; no v1.0 claim; no active full v1.x promise; no Cursor-rules/workflow implementation; no third-party skill import; no chain-of-thought documentation.

## DE – Skill Candidate Matrix

Bewertung der zehn vorgegebenen Kandidaten. Token-Ersparnis-Skala: gering / mittel / hoch / sehr hoch (bezogen auf realistisch wiederholten Prompt-Overhead pro WP-Zyklus). Risiko: gering / mittel / hoch (Nähe zu Git-/Release-/Governance-Aktionen).

| # | Kandidat | Zweck | Token-Ersparnis | Risiko | docs-only | v1.0-Relevanz | MVP-Relevanz | Eigenständig vs integriert |
|---|---|---|---|---|---|---|---|---|
| 1 | `ndf-work-package-runner` | WP-Ausführung strukturieren, harte Grenzen/Guardrails wiederholen | **sehr hoch** | mittel | ja | hoch | **hoch (MVP-Kern)** | eigenständig; nimmt Prompt-Mode-Auswahl auf |
| 2 | `ndf-release-runner` | Release-Prep-/Go-No-Go-/Tagging-Struktur | mittel | **hoch** | ja | mittel | niedrig | **Extended** (selten, release-/tag-nah) |
| 3 | `ndf-public-neutrality-guard` (statt „gate-runner") | an Neutralität + Secret-Namensregel erinnern | hoch | gering | ja | hoch | **hoch (MVP-Kern)** | eigenständig; **führt den Gate nicht aus** |
| 4 | `ndf-compact-context-summary-runner` | „Rückmeldung an Nova" + „Compact Context Summary" erzeugen | **sehr hoch** | gering | ja | hoch | **hoch (MVP-Kern)** | eigenständig; nimmt Handoff-Struktur auf |
| 5 | `ndf-adr-review-runner` | ADR-Bedarf/-Struktur prüfen, nächste freie Nummer | mittel | mittel | ja | mittel | niedrig | **Extended** |
| 6 | `ndf-security-review-runner` | Security-Review-Struktur (ADR-0032) | mittel | **hoch** | ja | hoch | niedrig | **Extended**; teils in ADR-Review integriert |
| 7 | `ndf-context-pack-maintainer` | Context Pack aktuell/konsistent halten (Short-Prompt-Grundlage) | hoch | gering | ja | hoch | **mittel–hoch (MVP-4.)** | eigenständig |
| 8 | `ndf-prompt-mode-selector` | Full/Standard/Short sicher auswählen | gering | gering | ja | mittel | niedrig | **in `work-package-runner` integriert** |
| 9 | `ndf-human-maintainer-handoff-runner` | Handoff-Struktur an Human Maintainer | mittel | gering | ja | mittel | niedrig | **in `compact-context-summary-runner` integriert** |
| 10 | `ndf-v1-readiness-review-runner` | v1.0-Readiness-Review-Struktur | gering | **hoch** | ja | hoch | niedrig | **Extended** (selten, Full-Prompt-Pflicht) |

**Namens-Hinweis:** Kandidat 3 wird bewusst als **`-guard`** statt `-gate-runner` geführt. „Runner" auf dem Gate würde nahelegen, den Quality-Gate-Check auszuführen; das ist ein Script und daher nach ADR-0032 im MVP verboten. Der Skill **erinnert** nur an Neutralität; der reale Gate (`scripts/check_public_quality.py`) bleibt eine getrennte, vom Menschen/CI ausgelöste Prüfung.

## EN – Skill Candidate Matrix

The table above evaluates all ten candidates by purpose, token saving (low/medium/high/very-high), risk (low/medium/high, i.e. proximity to git/release/governance actions), docs-only fit, v1.0 relevance, MVP relevance, and standalone-vs-integrated. Naming note: candidate 3 is deliberately a **`-guard`**, not a `-gate-runner` — "runner" on the gate would imply executing the quality-gate script, which is a script and therefore forbidden in the MVP under ADR-0032. The skill only *reminds* of neutrality; the real gate (`scripts/check_public_quality.py`) stays a separate, human/CI-triggered check.

## DE – Recommended MVP Skill Set

**Vier Skills**, gewählt nach höchster sicherer Token-Ersparnis bei geringem Risiko:

1. **`ndf-work-package-runner`** — der WP-Rahmen: Rolle, harte Grenzen, Vorprüfungen, Prompt-Mode-Auswahl und Standard-Abschlussstruktur als wiederverwendbarer Baustein. Größter Overhead-Treiber, daher zuerst.
2. **`ndf-compact-context-summary-runner`** — die zwei am häufigsten wiederholten Abschluss­blöcke „Rückmeldung an Nova" und „Compact Context Summary" (inkl. Human-Maintainer-Handoff). Sehr hohe Frequenz, geringes Risiko.
3. **`ndf-public-neutrality-guard`** — Neutralitäts- und Secret-Namensregeln als Erinnerung vor Übergabe; ersetzt **nicht** den Gate.
4. **`ndf-context-pack-maintainer`** — hält den Context Pack aktuell; ist die Voraussetzung dafür, dass Standard/Short Prompt Mode überhaupt sicher greifen.

Gemeinsame Eigenschaften: docs-only, fail-closed, keine Scripts, kein Netz, keine Secrets, keine autonomen Git-/Release-Aktionen; jede Ausgabe ist ein Vorschlag.

## EN – Recommended MVP Skill Set

Four skills, chosen for the highest safe token saving at low risk: (1) `ndf-work-package-runner` — the WP frame (role, hard limits, pre-checks, prompt-mode selection, standard closing structure) as a reusable block; the biggest overhead driver, hence first. (2) `ndf-compact-context-summary-runner` — the two most-repeated closing blocks "Report to Nova" and "Compact Context Summary" (incl. human-maintainer handoff); very high frequency, low risk. (3) `ndf-public-neutrality-guard` — neutrality and secret-name rules as a reminder before handover; does **not** replace the gate. (4) `ndf-context-pack-maintainer` — keeps the Context Pack current, the precondition for Standard/Short Prompt Mode to work safely. Shared: docs-only, fail-closed, no scripts, no network, no secrets, no autonomous git/release actions; every output is a suggestion.

## DE – Recommended Extended Skill Set

Für später (nach erfolgreichem MVP, jeweils separater Human-Maintainer-Entscheid):

- **`ndf-release-safety`** (statt `ndf-release-runner`) — Release-Prep-/Go-No-Go-/Tagging-Struktur **als Dokumentation**, wiederholt „nur Human Maintainer taggt/releast".
- **`ndf-adr-governance-review`** (fasst `ndf-adr-review-runner` + `ndf-security-review-runner` zusammen) — ADR-Bedarf, nächste freie Nummer, Security-Review-Struktur nach ADR-0032; finalisiert nichts autonom.
- **`ndf-v1-readiness-review`** — v1.0-Readiness-Struktur; bleibt Full-Prompt-pflichtig.
- **`ndf-prompt-mode-selector`** — nur falls sich die integrierte Variante in `work-package-runner` als unzureichend erweist.

## EN – Recommended Extended Skill Set

For later (after a successful MVP, each on a separate human-maintainer decision): `ndf-release-safety` (not `ndf-release-runner`) — release-prep/go-no-go/tagging structure **as documentation**, repeating "only the Human Maintainer tags/releases"; `ndf-adr-governance-review` (merges `ndf-adr-review-runner` + `ndf-security-review-runner`) — ADR need, next free number, ADR-0032 security-review structure, finalizing nothing autonomously; `ndf-v1-readiness-review` — v1.0-readiness structure, stays Full-prompt-mandatory; `ndf-prompt-mode-selector` — only if the integrated variant in `work-package-runner` proves insufficient.

## DE – Not Recommended / Deferred Skills

- **`ndf-release-runner` als eigenständiger MVP-Skill:** zu release-/tag-nah, seltene Nutzung, geringe Frequenz-Ersparnis → nur als Extended `ndf-release-safety`.
- **`ndf-security-review-runner` eigenständig im MVP:** Risiko, autonome Sicherheitsurteile zu implizieren → in `ndf-adr-governance-review` integrieren.
- **`ndf-human-maintainer-handoff-runner` eigenständig:** redundant zu `ndf-compact-context-summary-runner` → integrieren.
- **`ndf-prompt-mode-selector` eigenständig im MVP:** geringe Eigen-Ersparnis → in `ndf-work-package-runner` integrieren.
- **`ndf-v1-readiness-review-runner` im MVP:** selten, hoch, Full-Prompt-Pflicht → Extended.
- **Generell abgelehnt (nie als Skill):** alles, was Git-/Release-Aktionen ausführt, Scripts startet, Netzwerk nutzt, Secret-Werte liest/dokumentiert oder private Projektlogik kapselt. Solche Inhalte gehören nicht in einen Skill.

## EN – Not Recommended / Deferred Skills

`ndf-release-runner` as a standalone MVP skill — too release/tag-adjacent, rare, low frequency saving → only as extended `ndf-release-safety`. `ndf-security-review-runner` standalone in the MVP — risk of implying autonomous security judgments → merge into `ndf-adr-governance-review`. `ndf-human-maintainer-handoff-runner` standalone — redundant with `ndf-compact-context-summary-runner` → merge. `ndf-prompt-mode-selector` standalone in the MVP — low own-saving → integrate into `ndf-work-package-runner`. `ndf-v1-readiness-review-runner` in the MVP — rare, high-stakes, Full-prompt-mandatory → extended. Categorically rejected (never a skill): anything that executes git/release actions, runs scripts, uses the network, reads/documents secret values, or encapsulates private project logic.

## DE – Skill vs Project Knowledge vs Prompt Matrix

Leitprinzip: **stabile, öffentliche Verhaltensregeln → Skill**; **stabiler, öffentlicher Kontext → Project Knowledge**; **WP-spezifische, veränderliche Details → Prompt**.

| Inhalt | Skill | Project Knowledge | Prompt | Begründung |
|---|---|---|---|---|
| NDF-Rollenbeschreibung (Nova/Claude/Cursor/Human Maintainer) | ✅ | ➖ | ➖ | stabil, wiederkehrend, öffentlich-neutral |
| Human-Maintainer-only-Regel | ✅ | ➖ | ➖ | invariant, sicherheitsrelevant |
| Public Neutrality | ✅ | ➖ | ➖ | invariante Verhaltensregel |
| Secret-Regeln (Name ja, Wert nie) | ✅ | ➖ | ➖ | invariant; Wert existiert nie im Repo |
| ADR-0031 (v1.x-Kompatibilität) | ➖ | ✅ | ➖ | Faktenlage; Skill verweist darauf |
| ADR-0032 (Skill Security Policy) | ✅ (als Grenze) | ✅ (als Faktum) | ➖ | Grenze steuert Skill-Verhalten; Text bleibt Project Knowledge |
| Prompt Modes (Definitionen) | ➖ | ✅ | ➖ | stabiles Referenzwissen |
| Prompt-Mode-Auswahl im konkreten WP | ✅ | ➖ | ➖ (nur Override) | Skill schlägt Modus vor; Prompt kann übersteuern |
| Rückmeldung an Nova (Struktur) | ✅ | ➖ | ➖ | fixes Format |
| Compact Context Summary (Struktur) | ✅ | ➖ | ➖ | fixes Format |
| Self-Check (`git status`/`diff`) | ✅ | ➖ | ➖ | wiederkehrender Prüfschritt |
| konkrete WP-Ziele | ➖ | ➖ | ✅ | veränderlich, WP-spezifisch |
| aktuelle WP-Ergebnisse / Evidence | ➖ | ✅ (Context Pack) | ➖ | Statuswissen, gepflegt vom Context-Pack-Skill |
| Release Known Notes | ➖ | ✅ | ➖ | Statuswissen |
| konkrete Dateipfade | ➖ | ➖ | ✅ | WP-spezifisch |
| erwartete Commit-Message | ➖ | ➖ | ✅ | WP-spezifisch (nur Vorschlag) |
| v1.0 Notes | ➖ | ✅ | ➖ | Statuswissen |
| Skill Security Policy (Wortlaut) | ➖ | ✅ | ➖ | Referenzdokument |
| Modellregel / empfohlenes KI-Modell | ✅ (Erinnerung) | ✅ (Regel) | ➖ (nur Override) | stabile Regel; Prompt kann abweichen |

## EN – Skill vs Project Knowledge vs Prompt Matrix

Guiding principle: **stable public behavior rules → Skill**; **stable public context → Project Knowledge**; **WP-specific, changing details → Prompt**. The table above assigns each required item accordingly. Highlights: role description, human-maintainer-only rule, neutrality, secret rules, closing-block structures, and the self-check are stable behavior → Skill; ADR texts, prompt-mode definitions, current WP results/evidence, release known notes, and v1.0 notes are stable context → Project Knowledge (kept current by the context-pack skill); concrete WP goals, file paths, and the proposed commit message are WP-specific → Prompt. Prompt-mode selection and the model rule live in a Skill as a suggestion but the Prompt may override.

## DE – Token-Economy Assessment

**Entfallbare Prompt-Blöcke (durch Skills/Project Knowledge ersetzbar):** Rollenbeschreibung, harte Grenzen/Guardrails, Public-Neutrality-Regeln, Secret-Regeln, Abschlussformat, „Rückmeldung an Nova"-Vorlage, „Compact Context Summary"-Vorlage, Self-Check-Anweisungen. Diese Blöcke sind über WPs hinweg nahezu identisch → **sehr hohe** Ersparnis.

**Bleibende Prompt-Blöcke (WP-spezifisch, müssen bleiben):** konkrete WP-Ziele, konkrete Aufgabenliste, betroffene Dateipfade, erwartete Commit-Message, WP-spezifische Sonderregeln/Abweichungen, das erwartete Ergebnis.

**Am stärksten profitierende Prompts:** Full-Prompt-WPs (Release, ADR/Security, v1.0-Reviews) und lange Rückmeldungen — dort ist der Wiederhol-Anteil am größten.

| Prompt-Block | Ersparnis-Potenzial |
|---|---|
| Rollenbeschreibung | hoch |
| harte Grenzen / Guardrails | sehr hoch |
| Public-Neutrality-Regeln | hoch |
| Secret-Regeln | mittel |
| Abschlussformat | hoch |
| Rückmeldung an Nova | sehr hoch |
| Compact Context Summary | sehr hoch |
| Self-Check-Anweisungen | mittel |
| WP-spezifische Ziele/Dateien | keine (bleibt) |

**Realistische Reduktion:** Der wiederkehrende Overhead großer Full-Prompts ist qualitativ **hoch bis sehr hoch** reduzierbar; konservativ als Zielkorridor genannt, ohne exakte Zahl zu behaupten. **Risiken zu starker Kompression:** verlorener Sicherheits-/Evidenzkontext, unbemerkte Guardrail-Auslassung, Short-Prompt-Missbrauch. **Gegenmaßnahme:** Skills tragen die Guardrails selbst; Short Prompt Mode bleibt an einen aktuellen Context Pack gebunden und darf laut [Prompt Modes](../../agent-workflows/NDF_PROMPT_MODES.md) **nie** für Security/ADR/Scope-Lock/Release/destruktive/Git-Write-/Tag-Fälle genutzt werden. **Prompt-Längen-Zielwerte:** NDF sollte künftig anstreben, dass Standard-WP-Prompts nur noch WP-Spezifika + Modus + Dateipfade enthalten und die Guardrails per Skill referenzieren — der stabile Rahmen wandert aus dem Prompt heraus.

## EN – Token-Economy Assessment

Removable prompt blocks (replaceable by skills/project knowledge): role description, hard limits/guardrails, public-neutrality rules, secret rules, closing format, the "Report to Nova" template, the "Compact Context Summary" template, self-check instructions — nearly identical across WPs → **very high** saving. Remaining prompt blocks (WP-specific): concrete WP goals, task list, affected file paths, proposed commit message, WP-specific exceptions, expected result. Most-benefiting prompts: Full-prompt WPs (release, ADR/security, v1.0 reviews) and long reports. Realistic reduction: **high to very high** qualitatively, stated as a target corridor without asserting an exact figure. Risks of over-compression: lost safety/evidence context, unnoticed guardrail omission, Short-prompt misuse. Mitigations: skills carry the guardrails themselves; Short Prompt Mode stays bound to a current Context Pack and must **never** be used for security/ADR/scope-lock/release/destructive/git-write/tag cases. Prompt-length target: Standard WP prompts should carry only WP-specifics + mode + file paths and reference guardrails via a skill — the stable frame moves out of the prompt.

## DE – Security Model

Jeder empfohlene Skill hält [ADR-0032](../../adr/ADR-0032-skill-security-policy.md) strikt ein. Gemeinsame Grenzen für **alle** Skills: docs-only; **keine Scripts**; **kein Netzwerk**; **keine Secrets**; **keine privaten Daten**; **keine Git-/Release-/Tag-Aktionen**; keine autonomen Änderungen außer dokumentarischen Repo-Vorschlägen; Public Neutrality Pflicht; fail-closed (Unerlaubtes ist verboten); jede Ausgabe ist ein Vorschlag, der Human Maintainer entscheidet.

| Skill | Erlaubte Aktionen | Verbotene Aktionen | Inputs | Outputs | Fail-closed-Verhalten |
|---|---|---|---|---|---|
| `ndf-work-package-runner` | WP-Schritte strukturieren, Grenzen wiederholen, Modus vorschlagen, Dateien identifizieren | Commit/Push/Tag/Release, Scope-Erweiterung, destruktive Aktionen | WP-Prompt, öffentliche Dateien | strukturierte Schritte, Statusupdate-Vorschläge | bei fehlendem Kontext: kein Vorschlag, Rückfrage/Full Prompt anfordern |
| `ndf-compact-context-summary-runner` | „Rückmeldung an Nova" + „Compact Context Summary" erzeugen | Gate-Fehler verschweigen, Maintainer-Entscheid ersetzen | WP-Ergebnis, Gate-Status, Known Notes | feste Abschnittsstruktur | Ergebnis ehrlich; bei Unsicherheit REWORK/Notes statt GO |
| `ndf-public-neutrality-guard` | an Neutralität/Secret-Namensregel erinnern, neutrale Formulierungen vorschlagen | Secret-Werte/Denylist-Inhalte nennen, Gate ersetzen | öffentliche Textentwürfe | Neutralitäts-Erinnerungen, Gate-Hinweis | im Zweifel als nicht-neutral markieren |
| `ndf-context-pack-maintainer` | Context Pack dokumentarisch aktualisieren/prüfen | private Daten aufnehmen, Evidenz kürzen | öffentlicher Repo-/WP-Kontext | konsistenter Context-Pack-Vorschlag | keine Aufnahme unklarer/privater Inhalte |

**Secret-Regel:** Der Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden; sein Wert/Inhalt niemals — kein Skill liest, rekonstruiert oder dokumentiert ihn.

## EN – Security Model

Every recommended skill strictly complies with ADR-0032. Shared limits for **all** skills: docs-only; **no scripts**; **no network**; **no secrets**; **no private data**; **no git/release/tag actions**; no autonomous changes beyond documentary repo suggestions; public neutrality mandatory; fail-closed (anything not allowed is forbidden); every output is a suggestion, the Human Maintainer decides. The table above gives per-skill allowed/forbidden actions, inputs, outputs, and fail-closed behavior. Secret rule: the name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value/content never — no skill reads, reconstructs, or documents it.

## DE – Public-Neutrality Model

Skills und ihre Outputs müssen public-neutral bleiben: keine privaten Projektnamen, keine echten privaten Domains, keine Secret-Werte, keine privaten Suchmuster, keine echten Reviewer-Identitäten, keine organisationsinternen Namen, keine persönlichen Daten. Zulässige Rollenformulierungen: DE „Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN „Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role." Der `ndf-public-neutrality-guard` erinnert an diese Regeln, **ersetzt aber nicht** den Public Quality Gate v0.2 (`scripts/check_public_quality.py --strict`), der maßgeblich bleibt und getrennt (Mensch/CI) ausgelöst wird.

## EN – Public-Neutrality Model

Skills and their outputs must stay public-neutral: no private project names, real private domains, secret values, private search patterns, real reviewer identities, org-internal names, or personal data. Allowed role phrasings as above. The `ndf-public-neutrality-guard` reminds of these rules but does **not** replace the Public Quality Gate v0.2 (`scripts/check_public_quality.py --strict`), which stays authoritative and is triggered separately (human/CI).

## DE – Conceptual Skill Structure

**Nur Vorschlag — in WP-125 wird nichts angelegt.** Ein späteres docs-only Skill Pack könnte konzeptionell so aufgebaut sein (Pfade/Namen sind Vorschläge, keine erstellten Dateien):

- möglicher Skill-Name: z. B. `ndf-work-package-runner`
- mögliche Skill-Beschreibung: ein Satz, was der Skill tut und wann er greift
- mögliche Inhalte: Zweck, Wann nutzen / Wann nicht, erlaubte/verbotene Inputs, erlaubte/verbotene Outputs, Pflichtprüfungen (Gate, harte Grenzen), Pflicht-Handover (Rückmeldung an Nova / Compact Context Summary), Security Notes
- mögliche Inputs/Outputs: siehe Security-Model-Tabelle
- mögliche Validierungschecks: docs-only bestätigt, keine Scripts, keine Secrets, Public Neutrality, Handover erzeugt

**Nicht angelegt in WP-125:** keine `.claude/skills`, keine `SKILL.md`, keine Skill-Dateien, keine Scripts. Der konkrete Datei-Layout-Entwurf (Verzeichnisstruktur, `SKILL.md`-Felder, Regeltexte) ist Aufgabe eines späteren, ausdrücklich aktivierten WP-129 — nicht dieses Blueprints.

## EN – Conceptual Skill Structure

**Proposal only — nothing is created in WP-125.** A later docs-only skill pack could conceptually consist of, per skill: a possible name, a one-sentence description, possible contents (purpose; when to use / not; allowed/forbidden inputs; allowed/forbidden outputs; required checks — gate, hard limits; required handover — Report to Nova / Compact Context Summary; security notes), possible inputs/outputs (see the security-model table), and possible validation checks (docs-only confirmed, no scripts, no secrets, public neutrality, handover produced). Not created in WP-125: no `.claude/skills`, no `SKILL.md`, no skill files, no scripts. The concrete file layout (directory structure, `SKILL.md` fields, rule texts) is the task of a later, explicitly activated WP-129 — not this blueprint.

## DE – Validation Plan

Prüfplan für eine **spätere** Skill-Implementierung (WP-129). Jeder Skill muss vor Aktivierung nachweislich:

1. die Prompt-Länge tatsächlich reduzieren (Vorher/Nachher-Vergleich an einem realen WP);
2. keine Governance-Regel verändern (ADR-0031/0032, Scope-Lock-Regeln unberührt);
3. keine optionalen WPs aktivieren (129/130/131/132 bleiben inaktiv);
4. Public Neutrality nicht verletzen (Gate strict + self-test grün, new-file neutrality check aktiv);
5. keine Scripts ausführen;
6. kein Netzwerk nutzen;
7. keine Secrets lesen (Name erlaubt, Wert nie);
8. keine Git-/Release-Aktionen erlauben;
9. weiterhin eine „Rückmeldung an Nova" erzeugen;
10. weiterhin eine „Compact Context Summary" erzeugen;
11. mit Full, Standard und Short Prompt Mode funktionieren (Short nur innerhalb seiner Verbotsliste);
12. auch ohne private Projekte nutzbar sein (public-neutral, generisch);
13. Tokens sparen, ohne die Entscheidungsqualität zu senken (kein Verlust von Sicherheits-/Evidenzkontext).

Abnahme: alle 13 Punkte erfüllt + Human-Maintainer-GO; sonst REWORK/STOP. Fail-closed: ein nicht abgenommener Skill bleibt inaktiv.

## EN – Validation Plan

Validation plan for a **later** skill implementation (WP-129). Before activation each skill must demonstrably: (1) reduce prompt length (before/after on a real WP); (2) change no governance rule (ADR-0031/0032, scope-lock rules untouched); (3) activate no optional WPs; (4) not violate public neutrality (gate strict + self-test green, new-file neutrality check active); (5) run no scripts; (6) use no network; (7) read no secrets (name allowed, value never); (8) allow no git/release actions; (9) still produce a "Report to Nova"; (10) still produce a "Compact Context Summary"; (11) work with Full, Standard, and Short Prompt Mode (Short only within its forbidden list); (12) be usable without private projects (public-neutral, generic); (13) save tokens without lowering decision quality (no loss of safety/evidence context). Acceptance: all 13 met + human-maintainer GO; otherwise REWORK/STOP. Fail-closed: an unaccepted skill stays inactive.

## DE – Future Prompt Strategy

Nach Skill-Einführung empfohlene Strategie:

- **Full Prompt Mode** bleibt Pflicht für: Security Policy, ADR, Scope Lock, Release Readiness, Release Prep, v1.0-Reviews, destruktive/Git-Write-/Tag-Fälle, unklare Anforderungen.
- **Standard Prompt Mode** sollte für die meisten inhaltlichen WPs reichen, sobald die Guardrails per Skill getragen werden — der Prompt trägt dann Ziele + Modus + Dateien.
- **Short Prompt Mode** ist sicher nutzbar für standardisierte Folgearbeit mit aktuellem Context Pack (kleine Update-WPs, wiederkehrende Checks) — **nie** für die Full-Pflichtfälle.
- **In den Prompt gehören:** WP-Ziele, Aufgabenliste, Dateipfade, erwartete Commit-Message, WP-Sonderregeln, erwartetes Ergebnis.
- **Durch Skills ersetzt:** Rolle, Guardrails, Neutralität/Secret-Regeln, Abschlussformat, Rückmeldung-/Summary-Struktur, Self-Check.
- **In Project Knowledge:** ADR-Texte, Prompt-Mode-Definitionen, aktueller Phasenstatus/Context Pack, Release Known Notes, v1.0 Notes, Modellregel.
- **Zuverlässigkeit:** „Rückmeldung an Nova" und „Compact Context Summary" bleiben **Pflicht** — der `ndf-compact-context-summary-runner` erzwingt beide Blöcke, sodass Kompression sie nie entfallen lässt.

Ziel: weniger Usage-Limit-Probleme, weniger Wiederholung, keine Sicherheitsverschlechterung, bessere Alltagstauglichkeit für v1.0.

## EN – Future Prompt Strategy

Recommended after skill introduction: Full stays mandatory for security policy, ADR, scope lock, release readiness, release prep, v1.0 reviews, destructive/git-write/tag cases, and unclear requirements. Standard should suffice for most content WPs once guardrails are skill-carried (prompt = goals + mode + files). Short is safe for standardized follow-up work with a current Context Pack (small update WPs, recurring checks) — never for the Full-mandatory cases. In the prompt: WP goals, task list, file paths, proposed commit message, WP exceptions, expected result. Replaced by skills: role, guardrails, neutrality/secret rules, closing format, report/summary structure, self-check. In project knowledge: ADR texts, prompt-mode definitions, current phase status/Context Pack, release known notes, v1.0 notes, model rule. Reliability: "Report to Nova" and "Compact Context Summary" stay **mandatory** — the `ndf-compact-context-summary-runner` enforces both, so compression never drops them. Goal: fewer usage-limit problems, less repetition, no safety regression, better v1.0 everyday viability.

## DE – WP-129 Activation Recommendation

**Empfehlung: Bedingt aktivieren (Ja, mit engem Scope).** WP-129 sollte auf ausdrücklichen Human-Maintainer-Wunsch mit einem **eng begrenzten, docs-only, fail-closed** MVP-Scope aktiviert werden:

- **Minimaler Scope:** genau die vier empfohlenen MVP-Skills (`ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, `ndf-context-pack-maintainer`) — nichts aus dem Extended-Set.
- **Bedingungen vor Start:** ausdrücklicher Human-Maintainer-Scope-Change; ADR-0032 unverändert bindend; Public Quality Gate v0.2 grün; Validierungsplan (13 Punkte) als Abnahmekriterium übernommen; kein Scripts/Netz/Secrets/private Daten; keine Git-/Release-Automation.
- **Fehlende Voraussetzungen (bedingt, nicht Nein):** eine formale WP-129-Aktivierungsentscheidung durch den Human Maintainer und ein bestätigter Prompt-Vorher/Nachher-Nachweis liegen noch nicht vor — beides ist im WP-129-Start selbst zu erbringen.

**WP-125 setzt WP-129 nicht um und aktiviert es nicht.** Es empfiehlt nur die Aktivierung.

## EN – WP-129 Activation Recommendation

**Recommendation: conditionally activate (Yes, with a narrow scope).** WP-129 should, on explicit human-maintainer request, be activated with a **tightly bounded, docs-only, fail-closed** MVP scope: exactly the four recommended MVP skills (nothing from the extended set); conditions before start — explicit human-maintainer scope change, ADR-0032 unchanged and binding, Public Quality Gate v0.2 green, the 13-point validation plan adopted as acceptance criteria, no scripts/network/secrets/private data, no git/release automation. Missing prerequisites (conditional, not No): a formal WP-129 activation decision by the human maintainer and a confirmed before/after prompt-length proof — both to be delivered in the WP-129 start itself. **WP-125 does not implement or activate WP-129** — it only recommends activation.

## DE – Risks / Open Notes

- **Scope Creep (Hauptrisiko):** „Blueprint" könnte als „Implementierung" missverstanden werden. Gegenmittel: Nicht-Aktivierung explizit in Blueprint, Queue, Context Pack.
- **Over-Compression:** zu kurze Prompts könnten Sicherheits-/Evidenzkontext verlieren → Skills tragen Guardrails; Short-Prompt-Verbotsliste bleibt bindend.
- **Neutralitäts-Fehldeutung:** `-guard` ist kein Gate-Runner; der reale Gate bleibt maßgeblich.
- **Skill-Overlap:** Handoff/Prompt-Mode/Security bewusst integriert, um Redundanz/Token-Overhead zu vermeiden.
- **Blueprint-Verfall:** Falls WP-129 lange nicht startet, vor Aktivierung erneut gegen aktuelle ADRs prüfen.
- **Kein Zahlenversprechen:** Token-Ersparnis ist qualitativ (Ziel-Korridor), nicht exakt zugesichert.

## EN – Risks / Open Notes

Scope creep (main risk) — "blueprint" ≠ "implementation"; non-activation is explicit in blueprint, queue, and context pack. Over-compression — leaner prompts could lose safety/evidence context; skills carry guardrails and the Short-prompt forbidden list stays binding. Neutrality misreading — `-guard` is not a gate-runner; the real gate stays authoritative. Skill overlap — handoff/prompt-mode/security deliberately integrated to avoid redundancy/token overhead. Blueprint staleness — if WP-129 starts late, re-check against current ADRs before activation. No numeric promise — token saving is qualitative (target corridor), not exactly guaranteed.

## DE – Decision

**GO WITH NOTES – WP-129 recommended with constrained docs-only MVP scope.** Skills sind für NDF sinnvoll und wegen der Claude-Usage-Limits ein echter Produktivitätsbaustein; das MVP soll klein, docs-only und fail-closed sein; WP-129 wird mit engem Scope empfohlen, aber **nicht** durch WP-125 umgesetzt. Nach WP-125 gibt es weiterhin **kein aktives Skill Pack**. Foundation 0.9 bleibt released/published, **nicht v1.0**, kein RC, ohne aktive volle v1.x-Zusage.

## EN – Decision

**GO WITH NOTES – WP-129 recommended with constrained docs-only MVP scope.** Skills are worthwhile for NDF and a genuine productivity building block given Claude usage limits; the MVP should be small, docs-only, and fail-closed; WP-129 is recommended with a narrow scope but is **not** implemented by WP-125. After WP-125 there is still **no active skill pack**. Foundation 0.9 stays released/published, **not v1.0**, no RC, no active full v1.x promise.
