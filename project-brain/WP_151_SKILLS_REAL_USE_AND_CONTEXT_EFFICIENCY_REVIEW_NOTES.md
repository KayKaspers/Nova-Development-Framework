# NDF-WP-151 – Skills Real-use and Context Efficiency Review (Notes)

## Ziel

Post-v1.0 Review-/Mess-/Entscheidungs-WP: öffentlichen v1.0/v1.1-Status reconciliieren, das reale Token-/Kontextproblem analysieren, die 38 docs-only Skills auf Real-use/Trigger/Overlap/Kosten prüfen, Kontextklassen + Context Budgets + Prompt-Modi + Lean-Prompt-Architektur + Handoff-Modell entwerfen und eine WP-152-Entscheidungsvorlage liefern. Kein Implementierungs-WP; keine neuen Skills; kein v1.1 Scope Lock.

## Ergebnis

**GO WITH NOTES – skills real-use and context efficiency review completed.** Startgate bestanden (Working Tree sauber, `v1.0.0` annotated → `9dcadc1`, ADR-0031/0032 vorhanden, keine Tag-Manipulation). Review-Dokument: `docs/validation/v1-1/SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW.md`.

## Reconciliation

- **README** war veraltet (Status endete bei „0.9 scope-locked, kein v1.0"; „bewusst noch kein v1.0" 2×; „geplantes Skills-MVP") → minimal korrigiert: 0.9 released, **v1.0.0 final released**, v1.x aktiv, 38 Skills, v1.1 planning, WP-151 neuer Titel.
- **CHANGELOG `[Unreleased]`** um die drei committeten CoreOps-Adoptionen (A/B/C: `1ebffa6`/`e894c6f`/`ebf716c`) und die WP-151-Zeile ergänzt.
- **V1_1_PLAN / Context Pack / Next Phase**: WP-151-Titel präzisiert zu „Skills Real-use **and Context Efficiency** Review".
- **V1_0_PATH_SUMMARY**: konsistent, keine Änderung. **ADR-0031/0032, Skills README**: unverändert.

## Kernbefunde Token-/Kontextproblem

Belegt: Full-Prompt-Wiederholung des stabilen Rahmens trotz Skills-first; sehr lange Pflicht-Rückmeldungen (15–17 Abschnitte auch bei kleinen WPs); additiv wachsende Status-Dokumente; real erreichte Session-Limits (dokumentierte Resume-WPs). Hypothesen: Skill-Aufzählungen (10–15 je Prompt) als Kontextkosten; Prompt↔Rückmeldung-Doppelung; fehlendes Handoff-Artefakt; Layer-Trennung konzeptionell vorhanden, praktisch nicht gelebt.

## Modelle (im Review-Doc)

- **Messmodell:** 8 Fälle (klein/groß/Fortsetzung/Rückmeldung/Review/Scope-Change/Fix/Übergabe) mit Baseline/Zielkorridor/Mindestverbesserung/Abbruch-/Qualitätsgrenzen; keine schein-präzisen Tokenwerte.
- **Kontextklassen:** 6 Klassen; Lücken v. a. bei Übergabekontext (SESSION_HANDOFF) und kompaktem Status (CURRENT_STATE).
- **Context Budgets:** B0 Micro / B1 Lean / B2 Standard / B3 Extended / B4 Exceptional; B4 nie Standard (sonst splitten).
- **Prompt-Modi:** Lean als bevorzugter Normalfall (additiv); Handoff/Review-only/Fix als additive Profile; Full nur bei echter Kritikalität, nicht als Scheinsicherheit.
- **Lean-WP-Prompt:** 8 Kernelemente ≤ 1 Seite; Standards nur referenziert; sichtbar bleiben WP-ID/Typ, Allowed/Forbidden Files, Sonderregeln, Fail-closed-Trigger, Commit-Message.
- **Handoff:** Template + additiver Modus + Compact-Context-Summary-Ausbau; kein neuer Skill; project-local Pilot zuerst.
- **Kleine Dateien:** CURRENT_STATE + SESSION_HANDOFF empfohlen; PROJECT_MAP project-local/Adapter; CONTEXT_INDEX/ACTIVE_DECISIONS/ACTIVE_RISKS nicht separat (Router/CURRENT_STATE genügen).

## Skills Real-use (38)

Häufig 4 (work-package-runner, compact-context-summary-runner, public-neutrality-guard, changelog-writer — Kandidaten für Auto-Load) · gelegentlich 9 · selten 25 (nur explizite Referenz). Alle 30 WP-145/146-Skills weiterhin *nicht ausreichend validiert* (RDS-001/ADS-001). Merge-Kandidaten (später, kompatibel per ADR-0031-Deprecation): behavioral+ethical, branding+creative(+naming), public-release-body+release-notes, onboarding+ux-flow, content-tone↔docs-polish. **16 Adapter-Kandidaten** (Engineering/Product/UX/Creative-Familie → project-local/Adapter-Profile). Keine Deprecation jetzt; nichts entfernt/umbenannt. Kernregel: normale WPs nennen ≤ 3–5 Skills.

## Neue Skills (geprüft, abgelehnt)

`ndf-token-budget-reviewer` → Budget-Tabelle/Guidance statt Skill (Kriterien 3+4 verfehlt). `ndf-session-handoff-runner` → Template + Modus + Summary-Ausbau statt Skill (Kriterium 3 verfehlt; Re-Evaluation nach Pilot). **Keine neuen Skills erstellt.**

## WP-152-Entscheidungsvorlage

GO / REDUCE / PILOT PROJECT-LOCAL / NO-GO bewertet. **Empfehlung: GO mit reduziertem, additivem Scope + paralleler project-local Pilot** — WP-152 „Token Efficiency & Context Budget Baseline" (docs-only additiv: Lean/Handoff/Review-only/Fix-Profile, B0–B4-Guidance, SESSION_HANDOFF-Template, CURRENT_STATE-Muster, Kurzreport-Variante; kein neuer Skill). Einschub-Renumbering der v1.1-Roadmap (bisherige 152…156 → 153…157) entscheidet Nova/Human Maintainer.

## Verbraucherprojekte

Im öffentlichen Review nur als neutrale Archetypen bewertet (Design-System / Operations-Control-Plane [belegt durch realen Cross-Projekt-Intake] / Dokument-Framework / Voice-Community / Streaming-Operations). Pilot-Empfehlung: zuerst der Operations-Archetyp (reale NDF-Arbeitslast vorhanden).

## Grenzen eingehalten

Keine neuen Skills; keine Entfernung/Umbenennung; Prompt Modes nur additiv bewertet; kein v1.1 Scope Lock/Release Prep; keine Scripts/Automation/Netz; ADR-0031/0032 unverändert; keine privaten Projektnamen im Public NDF; Human-Maintainer-Gates erhalten.

## Nächster Schritt

Human-Maintainer-Entscheidung über die WP-152-Vorlage (Empfehlung GO additiv-schlank + Pilot); danach Roadmap-Renumbering durch Nova. Vorgeschlagene Commit-Message: `docs(v1): review skills real-use and context efficiency`.
