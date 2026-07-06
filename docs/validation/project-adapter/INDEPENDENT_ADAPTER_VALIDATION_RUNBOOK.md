# Independent Adapter Validation Runbook

## DE – Zweck

Schritt-für-Schritt-Anleitung für den unabhängigen Adapter-Validierungslauf (NDF-WP-074). Zielgruppe: der Independent Validator — und der Human Maintainer als Begleiter. Der Lauf ist mit diesem Runbook **sofort ausführbar** (Ventil-Bedingung 2 aus dem Foundation-0.5 Scope Lock).

## EN – Purpose

Step-by-step guide for the independent adapter validation run (NDF-WP-074), addressed to the independent validator and the accompanying human maintainer. With this runbook the run is **immediately executable** (valve condition 2 of the Foundation 0.5 scope lock).

## DE – Vor dem Start

- Validator Brief gelesen: `INDEPENDENT_VALIDATOR_BRIEF.md`
- Lesezugriff auf das öffentliche Repository (keine Schreibrechte nötig)
- Feedback-Template bereit: `INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md`
- Zeitbox vereinbart: 60–120 Minuten
- Klar: Bewertet wird die **Anwendbarkeit des Adapters**, nicht die Projektidee des Beispiels — und nichts wird im Repository verändert.

## EN – Before Starting

Validator brief read; read access to the public repository (no write access needed); feedback template at hand; agreed timebox of 60–120 minutes; clear that the **applicability of the adapter** is evaluated, not the example's project idea — and nothing in the repository is modified.

## DE – Rollen

- **Independent Validator:** führt den Lauf durch, füllt das Feedback-Template aus; nicht am Adapter-Design beteiligt.
- **Human Maintainer:** stellt Unterlagen bereit, beantwortet nur organisatorische Rückfragen (keine inhaltlichen Vorsagen), legt die Ergebnisse ab.
- **Implementation Agent:** wertet in NDF-WP-074 aus — greift in den Lauf selbst nicht ein.

## EN – Roles

Independent validator (runs and reports, not involved in adapter design); human maintainer (provides materials, answers organizational questions only — no content prompting, files the results); Implementation Agent (evaluates in NDF-WP-074, does not intervene in the run).

## DE – Benötigte Dateien

1. `docs/project-starter/PROJECT_ADAPTER_V0_2.md` — der Adapter (Phasen 0–10)
2. `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` — Manifest-, Output-Pfad- und Health-Score-Konventionen
3. `examples/neutral-example-project/` — SampleProject-Fixture (Brief, Anforderungen, Mock-Repository-Baum usw.)
4. `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md` — Übersicht der fünf priorisierten DE/EN-Prompts
5. `framework/prompts/project-adapter/PROJECT_ADAPTER_INTAKE_PROMPT.md` — Beispiel eines Adoptions-Prompts
6. Nur als Referenz, nicht als Vorlage: `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md` (historischer WP-047-Lauf) — **erst nach dem eigenen Urteil ansehen**, um Anker-Effekte zu vermeiden.

## EN – Required Files

Adapter v0.2 (phases 0–10), adapter conventions, the SampleProject fixture, the DE/EN priority pass overview, the intake prompt as an adoption prompt example — and, as reference only and **only after forming your own judgment** (to avoid anchoring), the historical WP-047 run.

## DE – Schritt 1: Orientierung (ca. 15 Min.)

1. `PROJECT_ADAPTER_V0_2.md` lesen: Zweck, Rollenmodell, Phasen-Tabelle (0–10), Sicherheitsregeln, minimale Variante.
2. `PROJECT_ADAPTER_CONVENTIONS.md` lesen: Wo landen Outputs? Was ist das kanonische Manifest-Format? Welche Health-Score-Kategorien gibt es?
3. Im Feedback-Template („Verständlichkeit") notieren: Was war sofort klar? Wo brauchte es mehrfaches Lesen? Was blieb offen?

## EN – Step 1: Orientation (approx. 15 min)

Read adapter v0.2 (purpose, roles, phase table 0–10, safety rules, minimal variant) and the conventions (output locations, canonical manifest format, health-score categories). Note in the feedback template what was immediately clear, what needed re-reading, what stayed open.

## DE – Schritt 2: SampleProject prüfen (ca. 10 Min.)

1. `examples/neutral-example-project/README.md` und `PROJECT_BRIEF.md` lesen.
2. Prüfen: Reicht das Fixture, um die Adapter-Phasen gedanklich durchzuspielen? Ist erkennbar, dass es ein neutrales Doku-Fixture ohne echten Code ist?
3. Notieren: Fehlt etwas, das ein externer Nutzer für den Einstieg bräuchte?

## EN – Step 2: Review SampleProject (approx. 10 min)

Read the fixture's README and project brief; check whether the fixture suffices to mentally walk the adapter phases and whether it is recognizable as a neutral documentation fixture without real code; note anything an external user would miss.

## DE – Schritt 3: Adapter-Phasen anwenden (ca. 30–60 Min.)

Mindestens die **minimale Variante** als Trockenlauf gegen das Fixture durchspielen — pro Phase beantworten: „Wüsste ich jetzt, was zu tun ist, was herauskommt und wohin es gehört?"

| Phase | Prüffrage |
|---|---|
| 0 – Intake | Ist klar, welche Informationen das Intake-Template verlangt und woher sie im Fixture kommen? |
| 1 – Read-only Review | Ist klar, dass nichts verändert wird und was der Review Report enthält? |
| 2 – Project Profile | Ist der erwartete Inhalt/Ort des Profils eindeutig? |
| 3 – Project Manifest | Ist die `PROJECT_MANIFEST.md`-Konvention (Markdown kanonisch, YAML nur eingebettet) eindeutig? |
| 8 – Work Package Queue | Ist klar, wie eine kleine Queue aussieht und was das `XY-WP-`-Präfix bedeutet? |
| 10 – Review & Commit | Ist klar, dass der Human Maintainer entscheidet und der Validator/Agent nicht committet? |

Optional bei Zeit: Phasen 4–7 und 9 ebenso durchspielen (Project Brain, Capability Matrix, Compliance Check, Health Score mit den 8 Kategorien und `unknown`/`n/a`-Regeln, First Safe WP). Schriftliche Phasen-Outputs sind **nicht erforderlich** — bewertet wird Nachvollziehbarkeit; kurze Stichproben (z. B. ein skizziertes Manifest-Gerüst) sind willkommen und gehen ins Feedback, nicht ins Repository.

## EN – Step 3: Apply Adapter Phases (approx. 30–60 min)

Walk at least the **minimal variant** as a dry run against the fixture — per phase answer: "Would I now know what to do, what comes out, and where it belongs?" (phase questions in the table above; phases 4–7 and 9 optional). Written phase outputs are **not required** — traceability is what is evaluated; short samples are welcome and go into the feedback, not the repository.

## DE – Schritt 4: Outputs prüfen (ca. 10 Min.)

1. Gegen die Conventions prüfen: Ist eindeutig, dass Validierungsläufe nach `examples/<fixture-name>/adapter-validation-output/` gehören, zentrale Nachweise nach `docs/validation/project-adapter/` und produktive Übernahme nur nach Maintainer-Entscheidung erfolgt?
2. Am historischen Beispiel (`examples/neutral-example-project/adapter-validation-output/`) stichprobenartig prüfen: Tragen die Dateien den „Validierungsoutput, keine produktive Doku"-Hinweis? Sind expected und actual getrennt?
3. **Nichts überschreiben** — die historischen WP-047-Outputs bleiben unverändert.

## EN – Step 4: Review Outputs (approx. 10 min)

Check against the conventions (validation runs → fixture output dir, central evidence → validation docs, production adoption only after a maintainer decision); spot-check the historical outputs for the "validation output, not production documentation" note and the expected/actual separation; **overwrite nothing**.

## DE – Schritt 5: Feedback erfassen (ca. 15 Min.)

`INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md` vollständig ausfüllen. Unbekanntes als `unknown` markieren — **nichts erfinden**. Keine privaten Namen, Organisationen, Domains oder Secrets ins Feedback schreiben.

## EN – Step 5: Capture Feedback (approx. 15 min)

Fill the feedback template completely; mark unknowns as `unknown` — **invent nothing**; no private names, organizations, domains, or secrets in the feedback.

## DE – Schritt 6: Ergebnis bewerten

Gesamtbewertung nach den Entscheidungswerten unten wählen und kurz begründen. Das Feedback geht an den Human Maintainer; die Auswertung erfolgt in NDF-WP-074.

## EN – Step 6: Evaluate Result

Choose an overall verdict per the decision values below with a short justification; the feedback goes to the human maintainer, evaluation happens in NDF-WP-074.

## DE – Entscheidungswerte / EN – Decision Values

| Wert / Value | Bedeutung / Meaning |
|---|---|
| **PASS** | Unabhängige Anwendung funktioniert ohne relevante Nacharbeit. / Independent application works without relevant rework. |
| **PASS WITH NOTES** | Anwendung funktioniert, aber mit dokumentierten Verbesserungen. / Works, with documented improvements. |
| **REWORK** | Doku/Prompts müssen vor der Release Prep korrigiert werden. / Docs/prompts must be fixed before release prep. |
| **FAIL** | Adapter ist für externe Nutzung nicht ausreichend nachvollziehbar. / Adapter not sufficiently traceable for external use. |
| **STOP** | Sicherheits-/Neutralitätsproblem, private Daten, Secret-Werte oder falsche Release-/v1.0-Behauptung gefunden. / Security/neutrality issue, private data, secret values, or a false release/v1.0 claim found. |

## DE – Abbruchkriterien

Sofort abbrechen (STOP) und den Human Maintainer informieren, wenn: private Projekt-/Personennamen, echte Domains oder Secret-Werte in öffentlichen Dateien auftauchen; Unterlagen zu einer schreibenden oder destruktiven Aktion auffordern; oder eine Datei fälschlich einen 0.5-Release oder v1.0-Reife behauptet. Wenn die Zeitbox deutlich überschritten ist und kein Fortschritt mehr erfolgt: Lauf beenden und den Stand als Feedback abgeben — das ist ein gültiges Teilergebnis, kein Scheitern.

## EN – Stop Criteria

Stop immediately and inform the maintainer if private names, real domains, or secret values appear in public files; if materials request a writing or destructive action; or if a file falsely claims a 0.5 release or v1.0 maturity. If the timebox is clearly exceeded without progress, end the run and submit the current state — a valid partial result, not a failure.

## DE – Nach dem Lauf

1. Ausgefülltes Feedback-Template an den Human Maintainer übergeben.
2. Ablage durch Maintainer/Implementation Agent unter `docs/validation/project-adapter/independent-runs/<YYYY-MM-DD>-adapter-validation/` (siehe `independent-runs/README.md`) — historische WP-047-Outputs bleiben unangetastet.
3. NDF-WP-074 wertet aus: Ergebnis, Findings, ggf. Folge-WPs; danach fließt das Ergebnis in die Release Readiness (NDF-WP-081) ein.

## EN – After the Run

Hand the completed feedback template to the human maintainer; results are filed under `docs/validation/project-adapter/independent-runs/<YYYY-MM-DD>-adapter-validation/` (see the folder README) — historical WP-047 outputs stay untouched; NDF-WP-074 evaluates (result, findings, follow-up work packages), then the result feeds the release readiness review (NDF-WP-081).
