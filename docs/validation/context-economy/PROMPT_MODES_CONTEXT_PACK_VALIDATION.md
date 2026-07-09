# Prompt Modes and Context Pack Validation

## DE – Zweck

Detail-Validierung (NDF-WP-123, Standard Prompt Mode) der in Foundation 0.8 eingeführten und in Foundation 0.9 adoptierten Artefakte: [NDF Prompt Modes](../../agent-workflows/NDF_PROMPT_MODES.md), [Context Pack Template](../../../project-brain/CONTEXT_PACK_TEMPLATE.md) und das aktuelle [Foundation-0.9 Context Pack](../../../project-brain/CONTEXT_PACK_FOUNDATION_0_9.md). Geprüft werden Klarheit, Sicherheit, Vollständigkeit und praktische Nutzbarkeit — aufbauend auf dem [Adoption Review](CONTEXT_ECONOMY_ADOPTION_REVIEW.md) (WP-122).

## EN – Purpose

Detailed validation (NDF-WP-123, Standard Prompt Mode) of the artifacts introduced in Foundation 0.8 and adopted in Foundation 0.9: the NDF prompt modes, the context pack template, and the current Foundation 0.9 context pack. Reviewed for clarity, safety, completeness, and practical usability — building on the adoption review (WP-122).

## DE – Status

Foundation 0.9 ist scope-locked (NDF-WP-121), **nicht released**, **nicht v1.0**, validation-first. Kein aktives Skill Pack. Dieses WP erstellt keine Skills, keine `.claude/skills`, keine Scripts und designt die Artefakte nicht neu.

## EN – Status

Foundation 0.9 is scope-locked (NDF-WP-121), **not released**, **not v1.0**, validation-first. No active skill pack. This WP creates no skills, `.claude/skills`, or scripts and does not redesign the artifacts.

## DE – Review-Ergebnis

**GO WITH NOTES.** Prompt Modes und Context Packs sind valide, sicher begrenzt und praktisch nutzbar. Die Notes sind bewusst und non-blocking: kontinuierliche Context-Pack-Pflege (nach jedem WP), die Skills-Entscheidung (WP-124) und die v1.0-Evidence-Summary (WP-126) folgen.

## EN – Review Result

**GO WITH NOTES.** Prompt modes and context packs are valid, safely bounded, and practically usable. The notes are deliberate and non-blocking: continuous context-pack maintenance (after each WP), the skills decision (WP-124), and the v1.0 evidence summary (WP-126) follow.

## DE – Geprüfter Scope

Validiert wurden: `NDF_PROMPT_MODES.md` (alle drei Modi, Auswahlregeln, Verbotsliste, Sicherheitsregeln, Beziehungen zu Context Packs/Skills), `CONTEXT_PACK_TEMPLATE.md` (alle Sektionen inkl. Rückmeldung-an-Nova-Struktur und Update Rules) und `CONTEXT_PACK_FOUNDATION_0_9.md` (Aktualität nach WP-122, Konsistenz zum Scope Lock). Als Praxis-Referenz: die tatsächliche Modus-Nutzung in WP-121 (Full), WP-122/123 (Standard) und die 0.8-Baseline (`CONTEXT_PACK_FOUNDATION_0_8.md`).

## EN – Reviewed Scope

Validated: `NDF_PROMPT_MODES.md` (all three modes, selection rules, forbidden list, security rules, relationships to context packs/skills), `CONTEXT_PACK_TEMPLATE.md` (all sections incl. the Report-to-Nova structure and update rules), and `CONTEXT_PACK_FOUNDATION_0_9.md` (currency after WP-122, consistency with the scope lock). As practical reference: the actual mode usage in WP-121 (Full), WP-122/123 (Standard), and the 0.8 baseline.

## DE – Validation Matrix / EN – Validation Matrix

| # | Kriterium / Criterion | Status | Nachweis / Evidence |
|---|---|---|---|
| 1 | Full Prompt Mode clearly defined | **Met** | eigener Abschnitt mit Zweck + Kontextumfang |
| 2 | Full Prompt required for scope lock/ADR/security policy/readiness/prep | **Met** | Pflichtliste im Full-Abschnitt + Übersichtstabelle |
| 3 | Standard Prompt Mode clearly defined | **Met** | eigener Abschnitt (normale WPs, Reviews, Updates) |
| 4 | Standard Prompt appropriate for validation/review WPs | **Met** | WP-122/123 liefen praktisch im Standard Mode |
| 5 | Short Prompt Mode clearly defined | **Met** | eigener Abschnitt (Folgearbeit mit aktuellem Context Pack) |
| 6 | Short Prompt has explicit forbidden cases | **Met** | eigene Verbotsliste (Scope Lock/ADR/Security/Release/destructive/Git-Write-Tag/unklar) |
| 7 | Short Prompt cannot bypass Public Quality Gate | **Met** | „Gate in jedem Modus Pflicht" + „Short Prompts umgehen keine Sicherheitsprüfungen" |
| 8 | Short Prompt cannot bypass Human Maintainer review | **Met** | „kein Modus umgeht ein Human-Maintainer-Gate" |
| 9 | Prompt Modes do not request chain-of-thought | **Met** | „Keine Chain-of-Thought-Anforderung" explizit in Sicherheitsregeln + Nicht-Zielen |
| 10 | Template has complete status and scope sections | **Met** | Status/Scope/Phase/Phasenstatus vorhanden |
| 11 | Template includes last WP and next WP | **Met** | „Last Completed Work Package" / „Next Work Package" |
| 12 | Template includes blocking/optional/deferred WPs | **Met** | drei eigene Sektionen |
| 13 | Template includes ADRs and safety boundaries | **Met** | „Accepted ADRs" + „Current Safety Boundaries" |
| 14 | Template includes Compact Context History | **Met** | eigene Sektion (letzte 3–5 Summaries) |
| 15 | Template includes what must not be claimed/included | **Met** | zwei eigene Sektionen |
| 16 | 0.9 Context Pack reflects scope after WP-122 | **Met** | WP-122 done (GO WITH NOTES), History ergänzt |
| 17 | 0.9 Context Pack identifies WP-123 as next/current WP | **Met** | „Next Work Package: NDF-WP-123" (Stand bei Review-Beginn) |
| 18 | Context Packs include no raw chat logs | **Met** | nur kompakte Status-Snapshots; Verbot in „What Must Not Be Included" |
| 19 | Context Packs include no chain-of-thought | **Met** | Verbot in Template + Packs eingehalten |
| 20 | Context Packs include no secrets/private data | **Met** | Neutralitäts-Greps sauber; Verbot im Template |
| 21 | Context Packs do not replace current-file review | **Met** | Update Rules + Header-Hinweis in beiden Packs |
| 22 | Context Packs do not replace Public Quality Gate | **Met** | Update Rules explizit |
| 23 | Context Packs do not replace Human Maintainer review | **Met** | Update Rules explizit |
| 24 | Rückmeldung an Nova structure available | **Met** | Standardstruktur im Template integriert |
| 25 | Compact Context Summary reusable for handover | **Met** | in jeder Brain-Notiz + als Context-Pack-History wiederverwendet |
| 26 | No active Claude Skills Pack created | **Met** | kein `.claude`-Verzeichnis, keine `SKILL.md` |
| 27 | WP-129 remains optional and not activated | **Met** | Scope Lock + Queue: optional/nicht aktiviert |
| 28 | Evidence sufficient for WP-126 summary | **Met with notes** | Adoption (WP-122) + Validation (dieses WP) liegen vor; Zusammenführung folgt in WP-126 |

## DE – Prompt Modes Validation

Alle drei Modi sind klar definiert, gegeneinander abgegrenzt und mit Auswahlregeln versehen. Das Grundprinzip — „Modus bestimmt Kontextmenge, nie Sorgfalt; im Zweifel größerer Modus" — verhindert strukturell, dass Sparsamkeit Sicherheitsprüfungen ersetzt. Die Übersichtstabelle plus Beispiele machen die Wahl praktisch nachvollziehbar; der laufende 0.9-Zyklus belegt die korrekte Anwendung (WP-121 Full, WP-122/123 Standard, per Context-Pack-Empfehlung).

## EN – Prompt Modes Validation

All three modes are clearly defined, mutually delimited, and equipped with selection rules. The core principle — mode sets context volume, never diligence; when in doubt, the larger mode — structurally prevents frugality from replacing safety checks. The overview table plus examples make the choice practically traceable; the running 0.9 cycle evidences correct usage (WP-121 Full, WP-122/123 Standard, per context-pack recommendation).

## DE – Full Prompt Mode

Bestätigt: Full ist für Scope Lock, ADR, Security Policy, Release Readiness, Release Prep und gefährliche/irreversible/governance-relevante Entscheidungen verbindlich; voller Kontext und vollständige harte Grenzen. Praktisch korrekt genutzt in WP-121 (Scope Lock).

## EN – Full Prompt Mode

Confirmed: Full is mandatory for scope lock, ADR, security policy, release readiness, release prep, and dangerous/irreversible/governance-relevant decisions; full context and complete hard limits. Correctly used in practice in WP-121.

## DE – Standard Prompt Mode

Bestätigt: Standard passt für normale Work Packages, Doku-Reviews und überschaubare Statusupdates; Durable Rules werden referenziert statt wiederholt; endet mit Rückmeldung an Nova + Compact Context Summary. Praktisch korrekt genutzt in WP-122/123.

## EN – Standard Prompt Mode

Confirmed: Standard fits normal work packages, doc reviews, and small status updates; durable rules are referenced instead of repeated; ends with Report to Nova + Compact Context Summary. Correctly used in WP-122/123.

## DE – Short Prompt Mode

Bestätigt: Short ist streng begrenzt — nur für standardisierte Folgearbeit mit **vorhandenem, aktuellem Context Pack**; die Verbotsliste (Scope Lock, ADR, Security Policy, Release Readiness/Prep, destructive actions, Git-Write-/Tag-/Release-Aktionen, unklare Anforderungen) ist explizit; Gate- und Human-Maintainer-Prüfungen sind ausdrücklich nicht umgehbar; die Eskalationsregel „im Zweifel eine Stufe höher" schließt Grauzonen. Hinweis: Short wurde in 0.9 noch nicht praktisch eingesetzt — die Definition ist valide, der erste reale Einsatz bleibt Beobachtungspunkt (PMV-003).

## EN – Short Prompt Mode

Confirmed: Short is strictly bounded — only for standardized follow-up work with an **existing, current context pack**; the forbidden list is explicit; gate and human-maintainer checks are expressly non-bypassable; the escalation rule ("when in doubt, one level higher") closes gray areas. Note: Short has not yet been used in practice in 0.9 — the definition is valid, its first real use remains an observation point (PMV-003).

## DE – Context Pack Template Validation

Das Template ist vollständig: Status/Scope/Phase, letztes+nächstes WP, blocking/optional/deferred, relevante ADRs, Sicherheitsgrenzen, Notes, Quelldateien, Compact Context History, Next Prompt Recommendation, What-Must-Not-Be-Claimed/-Included, Update Rules — plus die integrierte Rückmeldung-an-Nova-Standardstruktur. Die Update Rules stellen die drei Nicht-Ersetzungs-Garantien (Datei-Prüfung, Gate, Human-Review) explizit sicher. Wartbar: beide realen Packs (0.8, 0.9) folgen dem Template ohne Strukturabweichung.

## EN – Context Pack Template Validation

The template is complete (all sections listed above plus the integrated Report-to-Nova standard structure). The update rules explicitly secure the three non-replacement guarantees (file review, gate, human review). Maintainable: both real packs (0.8, 0.9) follow the template without structural deviation.

## DE – Foundation-0.9 Context Pack Validation

Aktuell und konsistent: Status scope-locked/validation-first, WP-122 als letztes abgeschlossenes WP (GO WITH NOTES), WP-123 als nächstes WP zum Review-Zeitpunkt, blocking/optional-Listen deckungsgleich mit dem Scope Lock, ADR-0031/0032 + nächste Nummer 0033 korrekt, Compact Context History bis WP-122 gepflegt, Next Prompt Recommendation (Standard für WP-123) zutreffend. Die Pflege-Disziplin „nach jedem WP" wurde bisher eingehalten (CPV-002 bleibt als Dauer-Note).

## EN – Foundation 0.9 Context Pack Validation

Current and consistent: status scope-locked/validation-first, WP-122 as last completed WP, WP-123 as next WP at review time, blocking/optional lists congruent with the scope lock, ADRs and next number correct, compact context history maintained through WP-122, next prompt recommendation accurate. The "update after each WP" discipline has been kept so far (CPV-002 stays as a standing note).

## DE – Rückmeldung an Nova und Compact Context Summary

Die Standardstruktur (Zusammenfassung / Geänderte Dateien / Entscheidung / Quality Gate / Neutralität / Risiken / Empfehlung / Commit-Message / Compact Context Summary) ist im Template verankert und wird in jeder WP-Rückmeldung praktisch genutzt. Die Compact Context Summary (5–10 Zeilen, keine privaten Daten, keine Chain-of-Thought) ist wiederverwendbar und speist die Context-Pack-History — der Handover-Kreislauf funktioniert nachweislich seit WP-109.

## EN – Rückmeldung an Nova and Compact Context Summary

The standard structure is anchored in the template and practically used in every WP report. The Compact Context Summary (5–10 lines, no private data, no chain-of-thought) is reusable and feeds the context-pack history — the handover loop demonstrably works since WP-109.

## DE – Sicherheits- und Neutralitätsprüfung

Public Quality Gate `--strict`/`--self-test` grün; new-file neutrality check aktiv. Prompt Modes und Context Packs ersetzen keine der geschützten Pflichten (Gate, Neutralität, Evidence, Human-Review, Security-Grenzen, Release Safety, ADR-Governance, Rückmeldung an Nova, Compact Context Summary) — in allen drei Dokumenten explizit verankert. „chain-of-thought"/„raw chat" ausschließlich als Verbot. Keine privaten Namen/Reviewer/Kontakte/Domains/Secret-Werte.

## EN – Security and Neutrality Review

Public quality gate strict/self-test green; new-file neutrality check active. Prompt modes and context packs replace none of the protected duties — explicitly anchored in all three documents. "chain-of-thought"/"raw chat" only as prohibitions. No private names/reviewer/contacts/domains/secret values.

## DE – Abgrenzung zu WP-124 / WP-129

WP-123 validiert Prompt Modes und Context Packs — es entscheidet **nicht** über Skill-Implementierung. **WP-124 entscheidet, ob eine docs-only Skills-MVP-Implementierung empfohlen wird. WP-129 bleibt optional und nicht aktiviert.** Es werden keine `.claude/skills`, keine `SKILL.md` und keine Skill-Scripts erstellt; ADR-0032 bleibt bindend.

## EN – Boundary to WP-124 / WP-129

WP-123 validates prompt modes and context packs — it does **not** decide skill implementation. **WP-124 decides whether a docs-only skills MVP implementation is recommended. WP-129 stays optional and not activated.** No `.claude/skills`, `SKILL.md`, or skill scripts are created; ADR-0032 stays binding.

## DE – Findings / EN – Findings

- **PMV-001 (Strength):** Die Prompt-Mode-Grenzen sind klar — Übersichtstabelle, Auswahlregeln und Eskalationsregel greifen ineinander.
- **PMV-002 (Strength):** Short Prompt Mode hat eine explizite, vollständige Verbotsliste und kann Gate/Human-Review nicht umgehen.
- **PMV-003 (Note):** Short Prompt Mode wurde in 0.9 noch nicht praktisch eingesetzt; erster realer Einsatz bleibt Beobachtungspunkt (kein Blocker — die Definition ist valide).
- **CPV-001 (Strength):** Das Context Pack Template trägt den wiederverwendbaren Phasen-Handover; beide realen Packs folgen ihm ohne Abweichung.
- **CPV-002 (Note):** Das Foundation-0.9 Context Pack braucht weiterhin disziplinierte Updates nach jedem WP (bisher eingehalten).
- **CPV-003 (Note):** Context Packs bleiben Summaries und ersetzen keine Quell-Prüfung — in Update Rules verankert, gilt dauerhaft.

Keine Validation Gaps oder Validation Risks mit Blocker-Charakter gefunden. Keine kleinen Korrekturen nötig — WP-122 hatte alle Statusfelder bereits sauber nachgezogen.

## DE – Empfehlungen / EN – Recommendations

1. WP-124 (Optional Skills MVP Implementation Decision) im Full Prompt Mode durchführen.
2. Den ersten realen Short-Prompt-Einsatz bewusst beobachten und in WP-126 dokumentieren (PMV-003).
3. Context-Pack-Pflege nach jedem WP beibehalten (CPV-002).
4. Adoption- (WP-122) und Validation-Evidence (WP-123) in WP-126 zur v1.0-Path-Summary zusammenführen.

## DE – Bekannte Notes / Limitations

- Short Prompt Mode noch ohne praktischen Ersteinsatz (Definition valide).
- Skills-Entscheidung folgt in WP-124; WP-129 optional/nicht aktiviert.
- v1.0-Path-Evidence-Summary folgt in WP-126.
- Foundation 0.9 ist nicht released und nicht v1.0.

## EN – Known Notes / Limitations

Short Prompt Mode not yet used in practice (definition valid); skills decision follows in WP-124, WP-129 optional/not activated; v1.0-path evidence summary follows in WP-126; Foundation 0.9 is not released and not v1.0.

## DE – Nächster Schritt

**NDF-WP-124 – Optional Skills MVP Implementation Decision** (Full Prompt Mode empfohlen — governance-relevante Entscheidung).

## EN – Next Step

**NDF-WP-124 – Optional Skills MVP Implementation Decision** (Full Prompt Mode recommended — governance-relevant decision).
