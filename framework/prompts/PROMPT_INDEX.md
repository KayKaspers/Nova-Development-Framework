# NDF Prompt Index v0.2

Sprache / Language: Prompt-Titel sind englisch, Prompt-Inhalte teils DE, teils EN. DE/EN-Ausrichtung gemäß `docs/i18n/DE_EN_LANGUAGE_STANDARD.md`.

Rollen / Roles: Nova = ChatGPT-basierte Planungs-/Review-Rolle; „Rückmeldung an Nova" = Bericht an diese Rolle. / Nova = ChatGPT-based planning and review role; "Rückmeldung an Nova" = report to this role. Details: `docs/workflow/NOVA_CHATGPT_ROLE.md`

## Core

- `core/PROJECT_REVIEW.md`
- `core/WORK_PACKAGE_EXECUTION.md`
- `core/WORK_PACKAGE_CLASSIFICATION_PROMPT.md` — DE/EN core

## Architecture

- `architecture/ARCHITECTURE_REVIEW.md`

## Development

- `development/SMALL_FIX.md`
- `development/FEATURE_IMPLEMENTATION.md`

## Documentation

- `documentation/DOCUMENTATION_TASK.md`

## Testing

- `testing/TEST_REVIEW.md`

## DevOps

- `devops/DOCKER_REVIEW.md`

## Security

- `security/SECURITY_REVIEW.md`
- `security/SECURITY_BASELINE_REVIEW_PROMPT.md` — DE/EN core
- `security/SECURITY_FINDING_TRIAGE_PROMPT.md` — DE/EN core
- `security/FOCUSED_SECURITY_CODE_FIX_PROMPT.md` — DE/EN core
- `security/FAIL_CLOSED_CONFIG_PROMPT.md` — DE/EN core
- `security/SECURITY_RELEASE_GATE_PROMPT.md` — DE/EN core
- `security/DESTRUCTIVE_ACTION_BLUEPRINT_REVIEW_PROMPT.md` — DE/EN core
- `security/DESTRUCTIVE_ACTION_IMPLEMENTATION_GATE_PROMPT.md` — DE/EN core

Weitere Security-Prompts / more security prompts: `security/` (siehe / see `docs/toolkit/security-prompts/SECURITY_PROMPT_LIBRARY.md`)

## Review

- `review/NOVA_HANDOFF_REVIEW.md`
- `review/WORK_PACKAGE_BOUNDARY_REVIEW_PROMPT.md` — DE/EN core

## Project Adapter

- `project-adapter/PROJECT_ADAPTER_INTAKE_PROMPT.md` — read-only Intake & Review (v0.2, DE/EN core)
- `project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md` — Project System Baseline nach Freigabe (v0.2, DE/EN core)
- `project-adapter/CREATE_PROJECT_ADAPTER.md` — Adapter-Kurzform (v0.1, legacy)

## Blocks

- `blocks/BLOCK_ROLE.md`
- `blocks/BLOCK_LIMITS.md`
- `blocks/BLOCK_QUALITY_RULES.md`
- `blocks/BLOCK_FEEDBACK_TO_NOVA.md`
