---
id: project-adapter-system-baseline-001
title: Project System Baseline for an Existing Project
version: 0.2
category: project-adapter
role: Implementation Agent (e.g. Claude)
supported_models: [Claude, ChatGPT]
risk_level: medium
requires_human_review: true
---

# Prompt – Project System Baseline

> Sprachstatus / Language status: DE/EN priority pass complete (Foundation 0.4, NDF-WP-060). DE und EN sind gleichwertig nutzbar. / DE and EN are equally usable.

## DE – Zweck

Nach freigegebenem Read-only Review die NDF-Project-System-Dateien im Zielprojekt anlegen — nur erlaubte Dateien, strikt additiv, docs-only.

## EN – Purpose

After an approved read-only review, create the NDF project system baseline files in the target project — allowed files only, strictly additive, docs-only.

## DE – Rolle / EN – Role

Du bist der Implementation Agent (z. B. Claude) und legst nach freigegebener Analyse die NDF-Baseline im Zielprojekt an. / You are the Implementation Agent creating the NDF baseline after an approved analysis.

Work Package Type: `docs-only / project-adapter`

## DE – Voraussetzung / EN – Precondition

Der Read-only Review (Intake-Prompt) wurde durchgeführt und von Nova (ChatGPT) bzw. dem Human Maintainer freigegeben. **Ohne Freigabe: STOP.** / The read-only review was done and approved by Nova (ChatGPT) or the human maintainer. **Without approval: STOP.**

## DE – Verwendung / EN – When to Use

Als **Phase 2–8** des Project Adapters, nach freigegebenem Intake. / As **phase 2–8** of the project adapter, after an approved intake.

## DE – Erwartete Ausgabe / EN – Expected Output

Die NDF Project-System-Dateien gemäß `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`.

**Erlaubte Dateien / allowed files** (nur diese anlegen/ändern / create/change only these):

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md
docs/ndf/ADOPTION_NOTES.md
```

## DE – Aufgaben / EN – Tasks

1. Inhalte aus dem freigegebenen Review Report übernehmen — Realität dokumentieren, nicht Wunschzustand. / Take content from the approved review report — document reality, not the wish state.
2. Specs aus `docs/project-system/` einhalten; Vorlagen nutzen (`framework/project-starter/templates/`, `framework/templates/project-adapter/`). / Follow the specs; use the templates.
3. Work Package Queue mit projektspezifischem neutralem ID-Präfix anlegen (Platzhalter `XY-WP-` durch eigenes ersetzen, nicht `NDF-WP` verwenden). / Create the queue with a project-specific neutral prefix.
4. Health Score nur mit Evidenz aus dem Review befüllen; Unbewertbares als `n/a` (Foundation-0.4-Kategorien). / Fill the health score with evidence only; unassessable as `n/a`.

## DE – Grenzen / EN – Boundaries

- Keine funktionalen Codeänderungen, keine CI-/Workflow-Änderungen. / No functional code or CI changes.
- Keine Secrets lesen, ausgeben oder referenzieren. / Never read, output or reference secrets.
- Keine bestehenden Projektdateien umbauen oder löschen — NDF-Artefakte sind additiv. / Do not rework or delete existing files — artifacts are additive.
- Kein Commit, kein Push — Staging und Commit macht der Human Maintainer. / No commit, no push — the human maintainer stages and commits.
- Keine privaten Namen in öffentlich sichtbare Artefakte übernehmen. / No private names in public artifacts.
- Adapter-Konventionen beachten: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`. / Follow the adapter conventions.

## DE – Rückmeldung an Nova (ChatGPT) / EN – Feedback to Nova (ChatGPT)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

1. Zusammenfassung: welche Dateien wurden angelegt / summary: which files were created
2. Abweichungen von Templates/Specs mit Begründung / deviations with reasoning
3. Offene Felder, die der Maintainer ergänzen muss / open fields for the maintainer
4. Vorschlag für das erste umzusetzende Work Package / proposed first work package
5. Empfehlung: GO / REWORK / SPLIT / STOP / recommendation

Der Human Maintainer bleibt final zuständig. / The human maintainer remains the final authority.
