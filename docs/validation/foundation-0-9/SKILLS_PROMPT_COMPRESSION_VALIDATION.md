# Skills Prompt Compression Validation

## DE – Titel

Validierung der Prompt-Kompression und Token-Economy des NDF Docs-only Skills MVP (NDF-WP-134, Full Prompt Mode).

## DE – Status / Ergebnis

**GO WITH NOTES.** Das in WP-129 implementierte Docs-only Skills MVP ist docs-only, governance-stabil und ADR-0032-konform. Die strukturelle Prompt-Kompression ist qualitativ **hoch bis sehr hoch**. Known Note **DSK-001** wird auf **Partially closed** gesetzt: eine strukturelle Kompressions-Baseline liegt vor, eine empirische Real-Use-Messung steht weiter aus. Keine neuen Skills, keine Extended Skills, keine v1.0-Aktivierung. Foundation 0.9 bleibt released/published, **nicht v1.0**.

## EN – Status / Result

**GO WITH NOTES.** The docs-only skills MVP (WP-129) is docs-only, governance-stable, and ADR-0032-compliant. Structural prompt compression is qualitatively **high to very high**. Known note **DSK-001** is set to **Partially closed**: a structural compression baseline exists, an empirical real-use measurement is still pending. No new skills, no extended skills, no v1.0 activation. Foundation 0.9 stays released/published, **not v1.0**.

## DE – Scope

Bewertet wird, ob die vier MVP-Skills die gewünschte Prompt-Kompression bringen, ohne Governance zu schwächen: welche Prompt-Blöcke künftig entfallen, welche bleiben müssen, ob Public Neutrality / ADR-0032 / Human-Maintainer-only / Rückmeldung an Nova stabil bleiben, und ob das MVP alltagstauglich für Claude Pro ist. **Nicht im Scope:** neue Skills, Extended Skills, Scripts, empirische Token-Messung mit Live-Instrumentierung, Commit/Push/Tag/Release.

## EN – Scope

Assess whether the four MVP skills deliver the intended prompt compression without weakening governance: which prompt blocks can be dropped, which must stay, whether public neutrality / ADR-0032 / human-maintainer-only / Report to Nova stay stable, and whether the MVP is viable for everyday Claude Pro use. Out of scope: new/extended skills, scripts, live-instrumented token measurement, commit/push/tag/release.

## DE – Input Summary

Ausgewertet: die vier MVP-Skills (`.claude/skills/*/SKILL.md`) + `README.md`, der [Skills MVP Blueprint](SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md) (WP-125), die [Docs-only Skills MVP Validation](DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (WP-129), die [Prompt Modes](../../agent-workflows/NDF_PROMPT_MODES.md) (WP-113), die [Context Economy](../../agent-workflows/NDF_CONTEXT_ECONOMY.md) (WP-109), [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md) und [ADR-0032](../../adr/ADR-0032-skill-security-policy.md).

## EN – Input Summary

Reviewed: the four MVP skills + README, the Skills MVP Blueprint (WP-125), the Docs-only Skills MVP Validation (WP-129), Prompt Modes (WP-113), Context Economy (WP-109), ADR-0031, and ADR-0032.

## DE – Skills Reviewed

| Skill | Vorhanden | Docs-only | ADR-0032-konform | Für Kompression nutzbar |
|---|---|---|---|---|
| `ndf-work-package-runner` | ja | ja | ja | ja (WP-Rahmen, Guardrails, Self-Check) |
| `ndf-compact-context-summary-runner` | ja | ja | ja | ja (Rückmeldung an Nova + Compact Context Summary) |
| `ndf-public-neutrality-guard` | ja | ja | ja | ja (Neutralitäts-/Secret-Regeln) |
| `ndf-context-pack-maintainer` | ja | ja | ja | ja (Context-Pack-Pflege) |

Jede `SKILL.md` enthält Zweck, Wann nutzen, Inputs/Outputs, erlaubte/verbotene Aktionen, Fail-closed-Verhalten, Public-Neutrality- und ADR-0032-Grenzen sowie Human-Maintainer-only-Grenzen. Keine Scripts, keine Automation, keine Git-/Release-Aktionen, keine Secret-Werte, keine privaten Daten.

## EN – Skills Reviewed

The table above confirms all four skills exist, are docs-only, ADR-0032-compliant, and usable for compression. Each `SKILL.md` carries purpose, when-to-use, inputs/outputs, allowed/forbidden actions, fail-closed behavior, public-neutrality and ADR-0032 boundaries, and human-maintainer-only boundaries. No scripts, automation, git/release actions, secret values, or private data.

## DE – Validation Method

Da ADR-0032 keine Live-Instrumentierung/Scripts erlaubt, ist die Methode **strukturell und qualitativ**: Für drei repräsentative NDF-Prompt-Typen wird verglichen, welche Blöcke ohne Skills explizit im Prompt stehen müssten und welche künftig von Skills getragen werden. Die Reduktion wird als **Prozentbereich** grob geschätzt (keine falsche Genauigkeit) und die Governance-Auswirkung bewertet. Grundlage der Schätzung: der stabile Rahmen (Rolle, harte Grenzen, Neutralitäts-/Secret-Regeln, Abschlussformat, Rückmeldung an Nova, Compact Context Summary, Self-Check) macht in bisherigen Full-Prompts den Großteil des wiederkehrenden Overheads aus.

## EN – Validation Method

Since ADR-0032 forbids live instrumentation/scripts, the method is **structural and qualitative**: for three representative NDF prompt types, compare which blocks would need to be explicit without skills versus which are skill-carried. Reduction is estimated as a **percentage range** (no false precision) and governance impact is assessed. Basis: the stable frame (role, hard limits, neutrality/secret rules, closing format, Report to Nova, Compact Context Summary, self-check) is most of the recurring overhead in current full prompts.

## DE – Prompt Compression Comparisons

### Vergleich 1 – Normaler Work-Package-Prompt

- **Baseline ohne Skills (explizit nötig):** Rolle, harte Grenzen, Public Neutrality, Secret-Regeln, Self-Check-Anweisungen, Abschlussformat, Rückmeldung-an-Nova-Vorlage, Compact-Context-Summary-Vorlage + WP-Ziel, Kontext, Dateien, Commit-Message.
- **Skill-komprimiert (getragen von):** `ndf-work-package-runner` (Rolle, Grenzen, Self-Check, Abschlussstruktur), `ndf-compact-context-summary-runner` (Rückmeldung + Summary), `ndf-public-neutrality-guard` (Neutralität/Secret).
- **Weiterhin explizit:** WP-Ziel, aktueller Kontext, konkrete Dateien, Sonderregeln, erwartete Commit-Message.
- **Qualitative Ersparnis:** **hoch**. **Grobe Reduktion:** ~40–60 % des Prompt-Overheads (ohne WP-Inhalt). **Governance:** unverändert. **Entscheidung:** geeignet.

### Vergleich 2 – Release-/Post-Release-Prompt

- **Baseline ohne Skills:** wie oben + Release-Safety-Grenzen, „nur Human Maintainer taggt/releast", Go/No-Go-Erinnerungen, Reconciliation-Regeln.
- **Skill-komprimiert:** Standardrahmen via `ndf-work-package-runner` + `ndf-compact-context-summary-runner` + `ndf-public-neutrality-guard`. **Release-spezifische** Grenzen bleiben explizit (kein Extended `ndf-release-safety` im MVP).
- **Weiterhin explizit:** Release-/Tag-/Reconciliation-Sonderregeln, konkrete Release-Artefakte, Commit-Message, v1.0-Abgrenzung.
- **Qualitative Ersparnis:** **mittel**. **Grobe Reduktion:** ~25–40 %. **Governance:** unverändert (release-kritische Grenzen bewusst explizit). **Entscheidung:** geeignet mit Notes (Full Prompt Mode bleibt Pflicht).

### Vergleich 3 – Skills-/Governance-Prompt

- **Baseline ohne Skills:** Standardrahmen + ADR-0032-Grenzen, Skill-Scope-Grenzen, Nicht-Aktivierungs-Regeln, Public-Neutrality-Details.
- **Skill-komprimiert:** Standardrahmen skill-getragen; ADR-0032-Kernaussagen teils via `ndf-public-neutrality-guard` und `ndf-work-package-runner` erinnert. **Governance-Entscheidungen** und ADR-Wortlaut bleiben explizit.
- **Weiterhin explizit:** konkrete Governance-/ADR-Entscheidung, Scope-Grenzen, Nicht-Aktivierungs-Liste, Commit-Message.
- **Qualitative Ersparnis:** **hoch** beim Rahmen, **gering** bei der Governance-Substanz. **Grobe Reduktion:** ~30–45 %. **Governance:** unverändert. **Entscheidung:** geeignet mit Notes (Full Prompt Mode bleibt Pflicht).

## EN – Prompt Compression Comparisons

Three representative types were compared. (1) Normal WP prompt — high saving (~40–60 % of overhead), governance unchanged, suitable. (2) Release/post-release prompt — medium saving (~25–40 %), release-critical limits kept explicit, suitable with notes (Full mode mandatory). (3) Skills/governance prompt — high saving on the frame, low on governance substance (~30–45 % overall), governance unchanged, suitable with notes (Full mode mandatory). In all cases the still-explicit blocks are: concrete WP goal, current context, concrete files, special limits, expected commit message.

## DE – DSK-001 Assessment

**DSK-001 – reale Token-Ersparnis noch nicht empirisch gemessen → Partially closed.** Begründung: Eine strukturelle Kompressions-Baseline (drei Prompt-Typen, Blocklisten, grobe Prozentbereiche) ist erstellt und belegt qualitativ hohe Kompression. Eine empirische Real-Use-Messung (echte Vorher/Nachher-Token an realen Sessions) ist mit den ADR-0032-Grenzen (keine Scripts/Instrumentierung) hier nicht robust möglich und bleibt für eine spätere Real-Use-Validierung offen.

## EN – DSK-001 Assessment

**DSK-001 → Partially closed.** A structural compression baseline (three prompt types, block lists, rough ranges) evidences qualitatively high compression; an empirical real-use token measurement is not robustly possible within ADR-0032 limits here and stays open for a later real-use validation.

## DE – Token-Economy Findings

- Der stabile Rahmen ist der Haupttreiber des Overheads und am besten skill-komprimierbar.
- Normale WPs profitieren am stärksten; release-/governance-kritische WPs profitieren beim Rahmen, nicht bei der Substanz.
- Rückmeldung an Nova und Compact Context Summary sind sehr hoch komprimierbar, bleiben aber inhaltlich Pflicht.
- Kein Zahlenversprechen ohne Messbasis; Prozentbereiche sind Schätzungen.

## EN – Token-Economy Findings

The stable frame drives overhead and compresses best; normal WPs benefit most; release/governance WPs benefit on the frame not the substance; Report to Nova and Compact Context Summary are highly compressible but stay mandatory in content; no numeric promise without a measurement base.

## DE – Governance Findings

Public Neutrality, ADR-0031, ADR-0032, Human-Maintainer-only, Rückmeldung an Nova und Compact Context Summary bleiben **stabil**: Die Skills tragen diese Regeln, ersetzen aber keine Gates und keine Human Review. Release-/Security-/v1.0-kritische Substanz bleibt explizit im Prompt. Kein Skill führt Git-/Release-Aktionen aus. ADR-0032 unverändert.

## EN – Governance Findings

Public neutrality, ADR-0031, ADR-0032, human-maintainer-only, Report to Nova, and Compact Context Summary stay **stable**: skills carry these rules but replace neither gates nor human review. Release/security/v1.0-critical substance stays explicit. No skill performs git/release actions. ADR-0032 unchanged.

## DE – Prompt Rules After Skill Introduction

- Skills verpflichtend referenzieren für Rahmen, Abschlussblöcke und Context-Pack-Pflege.
- **Full Prompt Mode** bleibt Pflicht für Security, ADR, Scope Lock, Release Readiness/Prep, v1.0-Reviews, neue Skill-Implementierungen, destruktive/Git-Write-/Tag-Fälle, unklare Anforderungen.
- **Standard Prompt Mode** wird künftig Default für normale inhaltliche WPs.
- **Short Prompt Mode** nur für standardisierte Folgearbeit mit aktuellem Context Pack; nie für die Full-Pflichtfälle.
- Nie entfallen dürfen: konkrete WP-Ziele, konkrete Dateien, Sonderregeln, Commit-Message, sowie die Pflicht zu Rückmeldung an Nova + Compact Context Summary.
- Skills dürfen keine Gates/Human Review umgehen; der reale Public Quality Gate bleibt maßgeblich.

## EN – Prompt Rules After Skill Introduction

Reference skills for frame, closing blocks, and context-pack upkeep. Full stays mandatory for security/ADR/scope-lock/release/v1.0/new-skill/destructive/git-write/tag/unclear cases. Standard becomes the default for normal content WPs. Short only for standardized follow-up with a current Context Pack, never for full-mandatory cases. Never drop: concrete WP goals, files, special rules, commit message, and the mandatory Report to Nova + Compact Context Summary. Skills must not bypass gates/human review; the real gate stays authoritative.

## DE – Target Prompt Profiles

| Profil | Prompt-Overhead ohne WP-Inhalt | Skill-getragene Standardregeln | Explizit nötiger WP-Kontext | Ziel ggü. bisheriger Full-Basis |
|---|---|---|---|---|
| Short (skill-assisted) | minimal | Rahmen + Abschlussblöcke | WP-ID, Ziel, Skills, Dateien, Ergebnis, Commit-Message | ~20–30 % der Full-Basis |
| Standard (skill-assisted) | klein | Rahmen + Abschlussblöcke + Context-Pack | + kompakter Kontext, Sondergrenzen, Artefakte | ~40–55 % der Full-Basis |
| Full (skill-assisted) | reduziert | Rahmen + Abschlussblöcke | + volle Governance-/Release-/v1.0-Substanz | ~60–75 % der Full-Basis |

Werte sind Zielkorridore, keine exakten Tokenversprechen (siehe DSK-001).

## EN – Target Prompt Profiles

The table gives target corridors relative to the prior full-prompt base for Short/Standard/Full skill-assisted profiles. Values are corridors, not exact token promises (see DSK-001).

## DE – Risks / Open Notes

- **DSK-001 bleibt teilweise offen:** empirische Real-Use-Messung ausstehend.
- **Over-Compression:** zu kurze Prompts könnten Substanz verlieren → Full-Pflichtfälle + Short-Verbotsliste bleiben bindend.
- **Skill-Fehlgebrauch:** Skills sind keine Gates; Missverständnis vermeiden.
- **Kein Extended-Skill-Bedarf ausgelöst:** Bewertung bleibt beim Human Maintainer.

## EN – Risks / Open Notes

DSK-001 stays partially open (empirical real-use measurement pending); over-compression risk mitigated by full-mandatory cases + Short forbidden list; skills are not gates; no extended-skill need is triggered here.

## DE – Decision

**GO WITH NOTES.** Das Skills MVP bringt qualitativ hohe strukturelle Prompt-Kompression bei stabiler Governance; DSK-001 ist Partially closed. Keine neuen/Extended Skills, keine v1.0-Aktivierung.

## EN – Decision

**GO WITH NOTES.** The skills MVP delivers qualitatively high structural prompt compression with stable governance; DSK-001 is partially closed. No new/extended skills, no v1.0 activation.

## DE – Recommendation

**Skills-first Operating Mode** einführen (siehe [SKILLS_FIRST_OPERATING_MODE.md](SKILLS_FIRST_OPERATING_MODE.md)): Standard Prompt Mode als Default, Full nur für kritische Fälle. Eine spätere **Real-use-Validierung** (WP-139) kann DSK-001 vollständig schließen. Nächste freie ADR-Nummer: 0033.

## EN – Recommendation

Introduce the **skills-first operating mode** (see SKILLS_FIRST_OPERATING_MODE.md): Standard as default, Full only for critical cases. A later **real-use validation** (WP-139) can fully close DSK-001. Next free ADR number: 0033.
