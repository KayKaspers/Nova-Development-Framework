# Independent Adapter Validation Preparation

## DE – Zweck

Dieses Dokument bereitet die unabhängige Validierung des Project Adapters vor (NDF-WP-073, release-blocking für Foundation 0.5). Es definiert Ziel, Rolle, Umfang und Übergabe, damit der eigentliche unabhängige Testlauf (NDF-WP-074) ohne weitere Planung starten kann. **Dieses WP führt keine Validierung durch.**

## EN – Purpose

This document prepares the independent validation of the project adapter (NDF-WP-073, release-blocking for Foundation 0.5). It defines goal, role, scope, and handoff so the actual independent run (NDF-WP-074) can start without further planning. **This work package performs no validation.**

## DE – Status

Vorbereitung erstellt in NDF-WP-073. **Update (NDF-WP-074):** Ein unabhängiger Lauf wurde durchgeführt und ausgewertet — neutralisierte Rückmeldung aus einem privaten Referenzkontext, Ergebnis **PASS WITH NOTES**: [`independent-runs/2026-07-06-private-reference-validation/`](independent-runs/2026-07-06-private-reference-validation/README.md). Das öffentliche Repository dokumentiert nur neutralisierte Ergebnisse. Ein Runbook-Lauf gegen das öffentliche Fixture bleibt wünschenswert (v1.0-tracked); die Unterlagen dieses Dokuments bleiben dafür sofort nutzbar.

## EN – Status

Preparation created in NDF-WP-073. **Update (NDF-WP-074):** an independent run was performed and evaluated — neutralized feedback from a private reference context, verdict **PASS WITH NOTES** (folder above). The public repository records only neutralized results. A runbook-based run against the public fixture remains desirable (v1.0-tracked); these materials stay immediately usable for it.

## DE – Validierungsziel

Ein Independent Validator prüft, ob ein externer Nutzer **allein anhand der öffentlichen NDF-Dokumente und des neutralen SampleProject-Fixtures** den Project Adapter nachvollziehbar anwenden kann. Geprüft werden:

- Verständlichkeit des Project Adapter v0.2 (`docs/project-starter/PROJECT_ADAPTER_V0_2.md`)
- Nutzbarkeit der Project Adapter Conventions (`docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`)
- Nachvollziehbarkeit der Adapter-Phasen 0–10
- Klarheit der Output-Pfade (Fixture-Output vs. zentrale Nachweise vs. produktive Übernahme)
- Klarheit der `PROJECT_MANIFEST.md`-Konvention
- Klarheit der Health-Score-Kategorien
- Nutzbarkeit der fünf priorisierten DE/EN-Prompts (`docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`)
- Erkennbarkeit von Grenzen, Unknowns und Human-Maintainer-Entscheidungspunkten
- Public-neutraler Umgang mit Beispielen

Adressierte Lücke: der **Selbstvalidierungs-Bias** aus der WP-047-Validierung (Backlog-Punkt 6 in `PROJECT_ADAPTER_V0_2_IMPROVEMENT_BACKLOG.md`) — bisher wurde der Adapter nur von der Rollenkette validiert, die ihn gebaut hat.

## EN – Validation Goal

An independent validator checks whether an external user can apply the project adapter comprehensibly **using only the public NDF documents and the neutral SampleProject fixture** — covering adapter v0.2 understandability, conventions usability, phases 0–10 traceability, output path clarity, `PROJECT_MANIFEST.md` and health-score convention clarity, usability of the five prioritized DE/EN prompts, visibility of limits/unknowns/maintainer decision points, and public-neutral handling of examples. Addressed gap: the **self-validation bias** from the WP-047 validation (backlog item 6).

## DE – Rolle des Independent Validators

Der Independent Validator ist eine Person oder Instanz **außerhalb der bisherigen Rollenkette** (Nova (ChatGPT), Implementation Agent, Human Maintainer): nicht am Adapter-Design beteiligt, idealerweise ohne oder mit wenig NDF-Vorwissen. Der Validator braucht **keine Schreibrechte** — Lesen des öffentlichen Repos genügt; Ergebnisse gehen über das Feedback-Template zurück an den Human Maintainer. Die Unabhängigkeit wird neutral beschrieben (z. B. „external reviewer, not involved in prior adapter design"), ohne personenbezogene Pflichtangaben.

## EN – Independent Validator Role

A person or instance **outside the existing role chain** — not involved in the adapter design, ideally with little or no prior NDF context. No write access is needed; reading the public repository suffices, and results go back to the human maintainer via the feedback template. Independence is described neutrally, with no mandatory personal data.

## DE – Voraussetzungen

1. Foundation 0.5 Scope Lock beschlossen (erfüllt: NDF-WP-072).
2. Öffentliches Repository lesbar; Public Quality Gate grün.
3. Neutrales Fixture vorhanden (erfüllt: SampleProject unter `examples/neutral-example-project/`).
4. Vorbereitungsunterlagen vollständig (dieses WP): Runbook, Validator Brief, Feedback-Template, Outreach-Template.
5. Human Maintainer hat einen Independent Validator angefragt (spätere Aktion, Ventil-Bedingung 3).

## EN – Prerequisites

Scope lock done (WP-072); public repository readable and gate green; neutral fixture available (SampleProject); preparation materials complete (this WP); human maintainer has reached out to an independent validator (later action, valve condition 3).

## DE – Validierungsumfang

Zeitbox 60–120 Minuten. Der Validator arbeitet ausschließlich mit dem neutralen SampleProject-Fixture und den öffentlichen Dokumenten — mindestens die minimale Adapter-Variante (Phase 0 → 1 → 2 → 3 → 8 → 10 als Trockenlauf/Dokumentenprüfung), optional weitere Phasen. Details und Schritte: `INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md`

## EN – Validation Scope

Timebox 60–120 minutes; the validator works exclusively with the neutral SampleProject fixture and the public documents — at least the minimal adapter variant (phases 0 → 1 → 2 → 3 → 8 → 10 as a dry run/document review), optionally more. Details: `INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md`

## DE – Nicht-Ziele

Kein echter produktiver Projektimport; keine echten privaten Projekte, Kundendaten oder Secrets; keine Foundation-0.5-Release-Vorbereitung; keine v1.0-Freigabe; keine Website-/Export-Arbeit; keine CI-Implementierung; keine Bewertung der Projektidee des Fixtures — bewertet wird die **Anwendbarkeit des Adapters**.

## EN – Non-Goals

No real production project import; no real private projects, customer data, or secrets; no Foundation 0.5 release preparation; no v1.0 approval; no website/export work; no CI implementation; no judgment of the fixture's project idea — what is evaluated is the **applicability of the adapter**.

## DE – Benötigte Unterlagen

| Unterlage | Pfad |
|---|---|
| Runbook (Schritt-für-Schritt) | `docs/validation/project-adapter/INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md` |
| Validator Brief (Einstieg ohne Vorwissen) | `docs/validation/project-adapter/INDEPENDENT_VALIDATOR_BRIEF.md` |
| Feedback-Template | `docs/validation/project-adapter/INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md` |
| Outreach-Template (für den Human Maintainer) | `docs/validation/project-adapter/INDEPENDENT_VALIDATION_OUTREACH_TEMPLATE.md` |
| Project Adapter v0.2 | `docs/project-starter/PROJECT_ADAPTER_V0_2.md` |
| Adapter Conventions | `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` |
| SampleProject-Fixture | `examples/neutral-example-project/` |
| Historischer Erstlauf (WP-047, nur Referenz — nicht überschreiben) | `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md` |
| Priorisierte DE/EN-Prompts | `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md` |

## EN – Required Materials

See the table above — runbook, validator brief, feedback template, outreach template, adapter v0.2, conventions, the SampleProject fixture, the historical WP-047 run (reference only — do not overwrite), and the prioritized DE/EN prompts.

## DE – Erfolgskriterien für WP-073

WP-073 gilt **nur** als erfüllt, wenn alle folgenden Unterlagen vorhanden und in sich vollständig sind:

- [x] Dieses Vorbereitungsdokument (Ziel, Rolle, Umfang, Übergabe)
- [x] Runbook — so konkret, dass WP-074 ohne neue Planung starten kann
- [x] Validator Brief — verständlich ohne NDF-Vorwissen
- [x] Feedback-Template — strukturierte Ergebniserfassung inkl. Gesamtbewertung
- [x] Outreach-Template — versandfertige neutrale Anfrage mit Platzhaltern
- [x] Definierter Ergebnisort für WP-074 (`independent-runs/`, siehe Übergabe)

## EN – Success Criteria for WP-073

WP-073 only counts as fulfilled once all materials above exist and are complete in themselves: this preparation document, the runbook (concrete enough for WP-074 to start without new planning), the validator brief (understandable without prior NDF knowledge), the feedback template, the ready-to-send outreach template, and the defined WP-074 result location.

## DE – Übergabe an WP-074

1. Human Maintainer verschickt die Anfrage (Outreach-Template) und dokumentiert den Versuch neutral (Kanal/Rolle, Datum — keine privaten Namen).
2. Sagt ein Independent Validator zu: Brief + Runbook + Feedback-Template übergeben; Repo-Lesezugriff genügt.
3. Der Validator führt den Lauf gemäß Runbook durch und füllt das Feedback-Template aus.
4. Ergebnisse werden unter `docs/validation/project-adapter/independent-runs/<YYYY-MM-DD>-adapter-validation/` abgelegt (durch den Human Maintainer oder den Implementation Agent im Rahmen von WP-074) — **niemals** in den historischen WP-047-Outputs unter `examples/neutral-example-project/adapter-validation-output/`.
5. NDF-WP-074 wertet den Lauf aus und endet mit PASS / PASS WITH NOTES / REWORK / FAIL / STOP.

## EN – Handoff to WP-074

Maintainer sends the outreach and documents the attempt neutrally; on acceptance, the validator receives brief + runbook + feedback template (read access suffices); the validator runs per the runbook and fills the feedback template; results go to `docs/validation/project-adapter/independent-runs/<YYYY-MM-DD>-adapter-validation/` — **never** into the historical WP-047 outputs; WP-074 evaluates the run and ends with PASS / PASS WITH NOTES / REWORK / FAIL / STOP.

## DE – Bezug zum WP-074-Downgrade-Ventil

Das Ventil (8 Bedingungen, verbindlich in `docs/roadmap/FOUNDATION_0_5_SCOPE_LOCK.md`) wird durch dieses WP **vorbereitet, nicht ausgelöst**:

- Bedingung 1 („WP-073 vollständig abgeschlossen") wird mit diesem WP erfüllbar.
- Bedingung 2 („sofort ausführbarer Validierungsplan") wird durch das Runbook erfüllt.
- Bedingung 3 („dokumentierter Anfrage-Versuch") wird durch das Outreach-Template **ermöglicht** — der tatsächliche Versuch bleibt eine spätere Human-Maintainer-Aktion und wird hier nicht behauptet.
- Bedingungen 4–8 liegen vollständig bei WP-081/Human Maintainer.

## EN – Relation to the WP-074 Downgrade Valve

The valve (8 conditions, binding in the scope lock) is **prepared, not triggered**: condition 1 becomes satisfiable with this WP, condition 2 is satisfied by the runbook, condition 3 is enabled by the outreach template (the actual attempt remains a later maintainer action and is not claimed here), conditions 4–8 rest entirely with WP-081 and the human maintainer.

## DE – Neutralität und Datenschutz

Alle Unterlagen verwenden ausschließlich neutrale Rollen (Independent Validator, External Reviewer, Human Maintainer). Keine echten Namen, Organisationen, Domains oder Kontaktwege; keine Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden); keine personenbezogenen Pflichtangaben im Feedback. Der Public Quality Gate v0.2 (inkl. new-file neutrality check) gilt auch für alle künftigen WP-074-Ergebnisdateien.

## EN – Neutrality and Privacy

All materials use neutral roles only; no real names, organizations, domains, or contact channels; no secret values (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed); no mandatory personal data in feedback. The public quality gate v0.2 (incl. new-file neutrality check) also applies to all future WP-074 result files.
