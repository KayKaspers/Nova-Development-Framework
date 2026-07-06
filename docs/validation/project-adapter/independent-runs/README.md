# Independent Runs

> DE: Ablageort für die **tatsächlichen** Ergebnisse unabhängiger Adapter-Validierungsläufe (ab NDF-WP-074). / EN: Location for the **actual** results of independent adapter validation runs (from NDF-WP-074 on).

## DE – Zweck

NDF-WP-074 legt hier pro Lauf einen Ordner an:

```text
docs/validation/project-adapter/independent-runs/<YYYY-MM-DD>-adapter-validation/
```

Inhalt pro Lauf: das ausgefüllte Feedback-Template des Independent Validators und der Auswertungsbericht aus WP-074.

## EN – Purpose

NDF-WP-074 creates one folder per run (pattern above), containing the validator's completed feedback template and the WP-074 evaluation report.

## DE/EN – Regeln / Rules

- **Keine Fake-Ergebnisse** — hier liegt nur, was tatsächlich durchgeführt wurde. / No fake results — only what was actually performed.
- Expected und actual bleiben getrennt; historische WP-047-Outputs unter `examples/neutral-example-project/` werden **nie** überschrieben. / Expected and actual stay separate; historical WP-047 outputs are **never** overwritten.
- Keine privaten Namen, Organisationen, Domains oder Secret-Werte — neutrale Rollenbezeichnungen (z. B. „external reviewer"). / No private names, organizations, domains, or secret values — neutral role labels only.
- Der Public Quality Gate v0.2 (new-file neutrality check) gilt auch für alle Dateien in diesem Ordner. / The public quality gate v0.2 also applies to every file in this folder.

Vorbereitung / preparation: `../INDEPENDENT_ADAPTER_VALIDATION_PREPARATION.md` · Runbook: `../INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md`
