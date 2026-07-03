# Nova Development Framework (NDF)

The Nova Development Framework is a structured, documentation-first development framework for planning, building, securing, and maintaining software projects with AI assistance under human control.

It is not tied to any single project. It is a general, reusable methodology validated against real reference projects.

## Purpose

Modern AI-assisted development is fast but easily becomes unstructured: reviews turn into code changes, features ship without documentation, and dangerous operations get built without safeguards.

NDF solves this with a clear operating model:

- every change is a small, explicitly typed work package
- planning, execution, and approval are separate roles
- documentation and architecture come before implementation
- security and destructive operations follow mandatory safety patterns
- lessons learned from real projects flow back into the framework

## Core Principles

1. **Documentation First** – important decisions and structures are documented before they become permanent.
2. **Architecture First** – complex work is planned before it is implemented.
3. **AI creates. Humans approve.** – AI never makes irreversible decisions autonomously.
4. **Small, typed work packages** – no work package without a declared type and scope.
5. **Security first, fail closed** – risky functionality requires explicit safety patterns.
6. **Continuous feedback** – validated experience from real projects is fed back into the framework.

## NDF Workflow

```text
Nova (planning) -> Implementation Agent (execution) -> Human Maintainer (review & approval)
```

- **Nova** plans and specifies work packages, defines type, scope, and acceptance criteria.
- **The implementation agent** (e.g. Claude) executes exactly one work package at a time and reports back in a structured format.
- **The human maintainer** reviews the result, decides GO / REWORK / SPLIT / STOP, and performs commit and push.

No step is skipped: classify → plan → execute → report → review → commit.

## Work Package Types

Every work package has exactly one primary type. The type decides which changes are allowed, which tests are expected, and how deep the review must be. Defined types include:

| Type | Purpose |
|---|---|
| `review-only` | inspect and report, no changes |
| `docs-only` | documentation updates only |
| `code-fix` | one targeted code correction with tests |
| `feature` | small scoped feature addition |
| `test-only` | add or adjust tests |
| `security-baseline` | security review and findings |
| `security-code-fix` | mitigate one approved security finding |
| `health-score-update` | update project score based on evidence |
| `ci-diagnostic` | diagnose CI or build failures |
| `release-prep` | release documentation and checklists |
| `destructive-blueprint` | plan a high-risk destructive action |
| `destructive-implementation` | implement an approved destructive action |
| `project-adapter` | adapt NDF to an existing project |

The full standard lives in [framework/standards/WORK_PACKAGE_TYPES.md](framework/standards/WORK_PACKAGE_TYPES.md).

## Security First / Destructive Action Safety

Dangerous functionality (deletion, bulk operations, irreversible changes) is never implemented directly. NDF requires:

- a `destructive-blueprint` work package **before** any implementation
- strict validation, read-only preview, and explicit confirmation flows
- owner-only authorization for critical operations
- backup-before-delete patterns
- audit logging with privacy constraints
- fail-closed behavior for secrets and security configuration

The patterns are documented in the [Destructive Action Toolkit](docs/toolkit/destructive-actions/DESTRUCTIVE_ACTION_TOOLKIT.md) and the [Security Prompt Library](docs/toolkit/security-prompts/SECURITY_PROMPT_LIBRARY.md).

## Project Neutrality

NDF is project-neutral. Its rules and toolkits were validated against real reference projects:

- **Reference Project A** – a suite with high-risk destructive operations (backup/delete flows, owner-only controls, audit privacy, agent endpoint security)
- **Reference Project B** – a Docker-first suite with CI, build gates, and security baseline hardening (CI/Docker reference)

The validated findings are preserved in neutral form under [docs/validation/](docs/validation/), so any project can apply them without depending on a specific codebase.

## Repository Structure

| Path | Content |
|---|---|
| `docs/` | framework documentation: constitution, blueprint, roadmap, validation, toolkit, ADRs |
| `framework/` | operational assets: standards, prompts, templates, checklists |
| `standards/` | general development standards |
| `templates/` | reusable document and project templates |
| `adr/` | architecture decision records (Foundation 0.1) |
| `academy/`, `docs/academy/` | learning material for the NDF method |
| `examples/` | minimal usage examples |
| `project-brain/` | framework working memory: notes, decisions, next steps |
| `docs/import-history/` | archived import packages from earlier framework iterations |

## Language / Sprache

NDF is maintained bilingually (German/English) going forward. New central framework documents are either bilingual or clearly language-mirrored. / NDF wird künftig zweisprachig (Deutsch/Englisch) geführt; neue zentrale Framework-Dokumente sind bilingual oder klar sprachlich gespiegelt.

Details: [docs/i18n/DE_EN_LANGUAGE_STANDARD.md](docs/i18n/DE_EN_LANGUAGE_STANDARD.md) · Status: [docs/i18n/TRANSLATION_STATUS.md](docs/i18n/TRANSLATION_STATUS.md)

## Status

- **Foundation 0.2 – in development.** Current focus: work package type standard, destructive action toolkit, security prompt library, real project validation, and reference project integration.
- **Foundation 0.1 – frozen.** The 0.1 release is preserved unchanged as the first stable baseline; see [docs/release/FOUNDATION_0_1_RELEASE_NOTES.md](docs/release/FOUNDATION_0_1_RELEASE_NOTES.md).

## License

See [LICENSE](LICENSE).
