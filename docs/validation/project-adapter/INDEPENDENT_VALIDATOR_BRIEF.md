# Independent Validator Brief

> DE: Einstieg für eine Person ohne NDF-Vorwissen. / EN: Onboarding for someone with no prior NDF knowledge.

## DE – Was ist NDF?

Das **Nova Development Framework (NDF)** ist ein öffentliches, dokumentationsgetriebenes Framework für KI-gestützte Softwareentwicklung. Es organisiert Arbeit in kleinen, klar abgegrenzten **Work Packages** mit definierten Rollen und Prüfschritten. Ein Kernbaustein ist der **Project Adapter**: eine Anleitung in 11 Phasen (0–10), mit der ein bestehendes Projekt strukturiert in das Framework aufgenommen wird.

## EN – What is NDF?

The **Nova Development Framework (NDF)** is a public, documentation-driven framework for AI-assisted software development. It organizes work into small, clearly bounded **work packages** with defined roles and review steps. A core building block is the **project adapter**: an 11-phase guide (0–10) for structurally onboarding an existing project into the framework.

## DE – Die Rollen

- **Nova (ChatGPT)** – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle: plant Work Packages und reviewt Ergebnisse.
- **Implementation Agent** – eine KI-Instanz (z. B. Claude), die Work Packages im Repository umsetzt.
- **Human Maintainer** – der Mensch mit finaler Entscheidungs- und Freigabegewalt; nur er committet, taggt und released.
- **Independent Validator (deine Rolle)** – eine unbeteiligte Person/Instanz, die prüft, ob der Adapter **von außen** verständlich und anwendbar ist.

## EN – The Roles

Nova (ChatGPT) — the ChatGPT-based planning, architecture and review role; the Implementation Agent — an AI instance implementing work packages; the Human Maintainer — the human with final approval authority (only they commit, tag, release); the **Independent Validator (your role)** — an uninvolved person/instance checking whether the adapter is understandable and applicable **from the outside**.

## DE – Deine Aufgabe

Prüfe anhand der öffentlichen Dokumente und des neutralen Beispielprojekts (**SampleProject** unter `examples/neutral-example-project/`), ob du den Project Adapter nachvollziehbar anwenden könntest. Du bewertest **die Anwendbarkeit des Adapters** — nicht die Projektidee des Beispiels und nicht die Qualität des Frameworks insgesamt. Die genaue Schrittfolge steht im Runbook: `INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md`; deine Ergebnisse trägst du in das Feedback-Template ein: `INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md`.

## EN – Your Task

Using the public documents and the neutral example project (**SampleProject**), check whether you could apply the project adapter comprehensibly. You evaluate **the adapter's applicability** — not the example's project idea and not the framework's overall quality. Steps: the runbook; results: the feedback template.

## DE – Zeitbox

**60–120 Minuten.** Du musst nicht alles schaffen — ein ehrlicher Teilstand mit ausgefülltem Feedback-Template ist ein gültiges Ergebnis.

## EN – Timebox

**60–120 minutes.** You do not need to finish everything — an honest partial state with a completed feedback template is a valid result.

## DE – Was geprüft wird

Verständlichkeit des Adapters (Phasen 0–10), Nutzbarkeit der Konventionen (Manifest-Format, Output-Pfade, Health-Score-Kategorien), Nutzbarkeit der zweisprachigen Einstiegs-Prompts, Erkennbarkeit von Grenzen/Unknowns/Maintainer-Entscheidungspunkten und der neutrale Umgang mit Beispielen.

## EN – What Is Checked

Adapter understandability (phases 0–10), conventions usability (manifest format, output paths, health-score categories), usability of the bilingual entry prompts, visibility of limits/unknowns/maintainer decision points, and neutral handling of examples.

## DE – Was nicht geprüft wird

Kein echter Projektimport, keine privaten Projekte oder Kundendaten, keine Secrets, keine Code-Ausführung, keine CI, keine Release-Entscheidungen, keine v1.0-Bewertung. Du brauchst und bekommst **keine Schreibrechte** — du veränderst nichts.

## EN – What Is Not Checked

No real project import, no private projects or customer data, no secrets, no code execution, no CI, no release decisions, no v1.0 assessment. You need and receive **no write access** — you change nothing.

## DE – Rückfragen

Organisatorische Rückfragen an den Human Maintainer sind jederzeit erlaubt (Zugang, Zeitbox, Ergebnisformat). Inhaltliche Fragen („Was ist hier gemeint?") bitte **zuerst als Finding notieren** — genau diese Stellen sind das wertvollste Ergebnis der Validierung — und erst danach fragen, wenn es zum Weiterarbeiten nötig ist.

## EN – Questions

Organizational questions to the human maintainer are always fine (access, timebox, result format). Content questions ("what does this mean?") should **first be noted as findings** — those spots are the most valuable outcome — and only asked afterwards if needed to proceed.

## DE – Umgang mit Unklarheiten

Unklares als Finding festhalten, Unbekanntes als `unknown` markieren, nichts erfinden, nichts überspringen ohne Notiz. Es gibt keine „richtige" Musterlösung, an der du gemessen wirst — gemessen wird die Doku, nicht du.

## EN – Handling Ambiguity

Record ambiguity as findings, mark unknowns as `unknown`, invent nothing, skip nothing without a note. There is no "correct" model answer you are measured against — the documentation is being measured, not you.

## DE – Datenschutz und Neutralität

- Keine echten privaten Projekt-, Personen-, Organisations- oder Kundennamen in dein Feedback schreiben — neutrale Rollenbezeichnungen genügen (z. B. „external reviewer").
- Keine echten Domains, keine Secret-Werte, keine Kontaktdaten.
- Für dich gilt dasselbe: Du musst keine personenbezogenen Angaben machen; deine Unabhängigkeit beschreibst du neutral.
- Solltest du in öffentlichen Dateien private Daten oder Secret-Werte entdecken: sofort abbrechen und den Human Maintainer informieren (STOP-Regel im Runbook).

## EN – Privacy and Neutrality

No real private project, person, organization, or customer names in your feedback — neutral role labels suffice (e.g. "external reviewer"); no real domains, secret values, or contact data; you are not required to provide personal data yourself and describe your independence neutrally; if you discover private data or secret values in public files, stop immediately and inform the human maintainer (STOP rule in the runbook).
