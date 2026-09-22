# Project Adapter Intake

Phase 0 des Project Adapters. Vom menschlichen Maintainer (ggf. gemeinsam mit Nova) ausfüllen, bevor die Analyse startet. / Phase 0 of the Project Adapter. Filled by the Human Maintainer (optionally together with Nova) before the analysis starts.

Jedes Feld ist als **AGENT-PREPARABLE** (der Implementation Agent kann read-only einen Entwurf liefern) oder **HUMAN-REQUIRED** (Absicht/Richtlinie — nur der Human Maintainer kann es liefern) gekennzeichnet. Ein AGENT-PREPARABLE-Entwurf ist beratend (PREPARED) und ersetzt nicht die Bestätigung durch den Human Maintainer (AUTHORIZED) — siehe `docs/project-starter/PROJECT_ADAPTER_V0_2.md` §4. / Each field is labelled **AGENT-PREPARABLE** (the Implementation Agent can supply a read-only draft) or **HUMAN-REQUIRED** (intent/policy — only the Human Maintainer can supply it). An AGENT-PREPARABLE draft is advisory (PREPARED) and does not replace Human-Maintainer confirmation (AUTHORIZED) — see `docs/project-starter/PROJECT_ADAPTER_V0_2.md` §4.

## Project Name — AGENT-PREPARABLE (teilweise / partial)

<!-- z. B. SampleProject / e.g. SampleProject -->
<!-- DE: aus Paket-Manifesten ableitbar, aber der autoritative Name ist eine Maintainer-Entscheidung (ein Repo kann geforkt/umbenannt sein). / EN: inferable from package manifests, but the authoritative name is a maintainer call (a repo can be forked/renamed). -->

## Project Type — AGENT-PREPARABLE

<!-- z. B. Web-Suite, CLI-Tool, API-Service, Desktop-App / e.g. web suite, CLI tool, API service, desktop app -->
<!-- DE: ableitbar aus der Repository-Struktur (Pakete, Sprachen, Entry Points). / EN: derivable from the repository shape (packages, languages, entry points). -->

## Repository URL (optional) — HUMAN-REQUIRED

<!-- z. B. https://github.com/example-owner/sample-project -->
<!-- DE: optionales Feld; eine Maintainer-Bestätigung, nicht agentenableitbar, wenn nicht bereits vorhanden. / EN: optional field; a maintainer confirmation, not agent-derivable when absent. -->

## Local Path — AGENT-PREPARABLE

<!-- z. B. D:\Projects\sample-project -->
<!-- DE: trivial ableitbar, aber ohne maintainer-bestätigten Umfang bedeutungslos. / EN: trivially derivable, but meaningless without maintainer-confirmed scope. -->

## Tech Stack — AGENT-PREPARABLE

<!-- Sprachen, Frameworks, Datenbanken, z. B. TypeScript, Node.js, PostgreSQL / languages, frameworks, databases, e.g. TypeScript, Node.js, PostgreSQL -->
<!-- DE: ableitbar aus Manifesten/Lockfiles/Imports. / EN: derivable from manifests/lockfiles/imports. -->

## Deployment Model — AGENT-PREPARABLE (teilweise / partial)

<!-- z. B. Docker/self-hosted, Cloud, Desktop, Hybrid -->
<!-- DE: Docker-/CI-Dateien sind Evidenz, aber ihr Fehlen ist kein Beweis für ein Modell. / EN: Docker/CI files are evidence; their absence is not proof of a model. -->

## Known Risks — AGENT-PREPARABLE

<!-- bekannte Baustellen: instabile CI, fehlende Tests, riskante Delete-Funktionen, ... / known trouble spots: unstable CI, missing tests, risky delete functions, ... -->
<!-- DE: ableitbar per Scan (destruktive Operationen, fehlende Tests/CI, widersprüchliche Versionsstände). / EN: derivable via scan (destructive operations, missing tests/CI, conflicting version states). -->

## Maintainer Goals — HUMAN-REQUIRED

<!-- Was soll NDF hier erreichen? z. B. Doku stabilisieren, Security-Baseline, Release-Reife / What should NDF achieve here? e.g. stabilize docs, security baseline, release readiness -->
<!-- DE: Absicht, nicht aus dem Repository-Inhalt beobachtbar. / EN: intent, not observable from repository content. -->

## Public / Private Status — HUMAN-REQUIRED

<!-- public | private | geplant public / public | private | planned public — bestimmt, wie neutral die NDF-Artefakte formuliert sein müssen / determines how neutrally the NDF artifacts must be worded -->
<!-- DE: eine Richtlinien-Entscheidung, die bestimmt, wie neutral spätere NDF-Artefakte formuliert sein müssen. / EN: a policy decision that governs how neutral later NDF artifacts must be. -->

## Safety Notes — HUMAN-REQUIRED

<!-- Bereiche, die der Implementation Agent nicht anfassen oder nicht lesen soll (z. B. .env, secrets/, Kundendaten) / areas the Implementation Agent must not touch or read (e.g. .env, secrets/, customer data) -->
<!-- DE: die eigene Ausschlussliste des Maintainers; ein Agent kann nicht ableiten, was er nicht lesen soll. / EN: the maintainer's own exclusion list; an agent cannot infer what it should not read. -->
