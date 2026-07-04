# Project Manifest – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.
>
> Formathinweis: In einem echten Projekt wäre dies `project-system/PROJECT_MANIFEST.yaml` (siehe Template). Für die Validierung als Markdown gehalten; die Abweichung ist im Improvement Backlog vermerkt.

```yaml
name: "SampleProject"
slug: "sample-project"
owner: "<project-owner>"            # Fixture: example-owner
architecture_lead: "Nova (ChatGPT)"
implementation_assistant: "Implementation Agent (e.g. Claude)"
repository: "sample-project (fiktiv / fictitious)"
status: "active, pre-adoption"
ndf_level: 0                        # Level Guide: keine NDF-Struktur vorhanden

project_type: "self-hosted task/notes web app for a small team"
primary_language: "TypeScript (laut Brief; not evidenced)"
deployment:
  docker: true
  compose: true
  self_hosted: true
  host: "example.local"
  port: "unknown (3000 vs. 8080 widersprüchlich)"

data_classes:
  - tasks (team-intern)
  - notes (team-intern, löschbar -> destructive Kandidat)
  - user accounts (aktuell geteilt)

security_assumptions:
  authentication: "username/password, session cookie"
  authorization: "none (eingeloggt = darf alles)"
  secrets: "unmanaged (.env, Pflichtvariablen unknown)"
  audit: "none"

documentation_status: "incomplete and contradictory"
release_status: "no process, no backup, no rollback"
system_boundaries: "kein Mandantenbetrieb, keine Mobile-App, Team bleibt klein (REQUIREMENTS)"

open_decisions:
  - port clarification (3000 vs 8080)
  - required environment variables + fail-closed behavior
  - role model (member/owner) enforcement point
  - DE/EN target for public docs
  - fate of scripts/reset-db.sh
```
