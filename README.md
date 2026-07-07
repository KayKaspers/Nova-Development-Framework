# Nova Development Framework

## DE – Überblick

Das Nova Development Framework (NDF) ist ein dokumentations- und sicherheitsorientiertes Entwicklungs-Framework: Softwareprojekte werden mit KI-Unterstützung geplant, gebaut und gepflegt — unter durchgehender menschlicher Kontrolle. NDF ist projektneutral und wurde an realen Referenzprojekten validiert.

## EN – Overview

The Nova Development Framework (NDF) is a documentation-first, security-first development framework: software projects are planned, built, and maintained with AI assistance — under continuous human control. NDF is project-neutral and was validated against real reference projects.

## DE – Wofür ist NDF gedacht?

KI-gestützte Entwicklung ist schnell, wird aber leicht unstrukturiert: Reviews werden zu Code-Umbauten, Features entstehen ohne Doku, gefährliche Funktionen ohne Schutzmaßnahmen. NDF beantwortet das mit kleinen, typisierten Work Packages, getrennten Rollen für Planung, Umsetzung und Freigabe sowie verpflichtenden Sicherheitsmustern.

## EN – What is NDF for?

AI-assisted development is fast but easily becomes unstructured: reviews turn into refactorings, features ship without documentation, dangerous operations get built without safeguards. NDF answers this with small, typed work packages, separate roles for planning, execution, and approval, and mandatory safety patterns.

## DE – Kernprinzipien

1. **Documentation First** — wichtige Entscheidungen werden dokumentiert, bevor sie dauerhaft werden.
2. **Architecture First** — komplexe Arbeit wird erst geplant, dann umgesetzt.
3. **AI creates. Humans approve.** — KI trifft keine irreversiblen Entscheidungen.
4. **Kleine, typisierte Work Packages** — kein Work Package ohne deklarierten Typ.
5. **Security first, fail closed** — riskante Funktionen brauchen explizite Sicherheitsmuster.
6. **Kontinuierliches Feedback** — validierte Erfahrung fließt zurück ins Framework.

## EN – Core Principles

1. **Documentation First** — important decisions are documented before they become permanent.
2. **Architecture First** — complex work is planned before it is implemented.
3. **AI creates. Humans approve.** — AI never makes irreversible decisions.
4. **Small, typed Work Packages** — no work package without a declared type.
5. **Security first, fail closed** — risky functionality requires explicit safety patterns.
6. **Continuous feedback** — validated experience flows back into the framework.

## DE – Rollenmodell

- **Nova (ChatGPT)** — die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle; spezifiziert Work Packages: Typ, Umfang, Akzeptanzkriterien.
- **Implementation Agent** (Umsetzung, z. B. Claude) — führt genau ein Work Package aus und berichtet strukturiert zurück.
- **Menschlicher Maintainer** (Review & Freigabe) — prüft, entscheidet GO / REWORK / SPLIT / STOP, committet und pusht.

```text
Nova (ChatGPT) → Implementierungs-Agent → menschlicher Maintainer
```

Details zur Nova-Rolle: [NOVA_CHATGPT_ROLE.md](docs/workflow/NOVA_CHATGPT_ROLE.md)

## EN – Role Model

- **Nova (ChatGPT)** — the ChatGPT-based planning, architecture and review role; specifies work packages: type, scope, acceptance criteria.
- **Implementation Agent** (execution, e.g. Claude) — executes exactly one work package and reports back in a structured format.
- **Human Maintainer** (review & approval) — reviews, decides GO / REWORK / SPLIT / STOP, commits and pushes.

```text
Nova (ChatGPT) → Implementation Agent → Human Maintainer
```

Details on the Nova role: [NOVA_CHATGPT_ROLE.md](docs/workflow/NOVA_CHATGPT_ROLE.md)

## DE – Standard-Workflow

```text
Klassifizieren -> Planen -> Umsetzen -> Rückmeldung an Nova -> Review -> Commit
```

Kein Schritt wird übersprungen. Details: [WORK_PACKAGE_LIFECYCLE.md](framework/standards/WORK_PACKAGE_LIFECYCLE.md)

## EN – Standard Workflow

```text
Classify -> Plan -> Execute -> Report to Nova -> Review -> Commit
```

No step is skipped. Details: [WORK_PACKAGE_LIFECYCLE.md](framework/standards/WORK_PACKAGE_LIFECYCLE.md)

## DE – Work Packages

Jedes Work Package hat genau einen primären Typ — er bestimmt erlaubte Änderungen, Testerwartung und Review-Tiefe. Beispiele: `review-only`, `docs-only`, `code-fix`, `feature`, `security-baseline`, `destructive-blueprint`, `destructive-implementation`, `project-adapter`. Vollständiger Standard: [WORK_PACKAGE_TYPES.md](framework/standards/WORK_PACKAGE_TYPES.md)

## EN – Work Packages

Every work package has exactly one primary type — it decides allowed changes, test expectations, and review depth. Examples: `review-only`, `docs-only`, `code-fix`, `feature`, `security-baseline`, `destructive-blueprint`, `destructive-implementation`, `project-adapter`. Full standard: [WORK_PACKAGE_TYPES.md](framework/standards/WORK_PACKAGE_TYPES.md)

## DE – Sicherheit und destructive Actions

Gefährliche Funktionen (Löschen, Bulk-Operationen, Irreversibles) werden nie direkt implementiert: erst `destructive-blueprint`, dann nach Freigabe `destructive-implementation` — mit strikter Validierung, Read-only-Preview, Owner-only-Autorisierung, Backup-vor-Delete und Audit-Logging. Werkzeuge: [Destructive Action Toolkit](docs/toolkit/destructive-actions/DESTRUCTIVE_ACTION_TOOLKIT.md) · [Security Prompt Library](docs/toolkit/security-prompts/SECURITY_PROMPT_LIBRARY.md)

## EN – Security and Destructive Actions

Dangerous functionality (deletion, bulk operations, irreversible changes) is never implemented directly: first `destructive-blueprint`, then — after approval — `destructive-implementation`, with strict validation, read-only preview, owner-only authorization, backup-before-delete, and audit logging. Tools: [Destructive Action Toolkit](docs/toolkit/destructive-actions/DESTRUCTIVE_ACTION_TOOLKIT.md) · [Security Prompt Library](docs/toolkit/security-prompts/SECURITY_PROMPT_LIBRARY.md)

## DE – Project Adapter

Der Project Adapter v0.2 überführt bestehende Projekte strukturiert nach NDF: von der read-only-Analyse über Project Profile, Manifest und Health Score bis zur ersten sicheren Work Package Queue. Guide: [PROJECT_ADAPTER_V0_2.md](docs/project-starter/PROJECT_ADAPTER_V0_2.md)

## EN – Project Adapter

Project Adapter v0.2 brings existing projects into NDF in a structured way: from read-only analysis through project profile, manifest, and health score to the first safe work package queue. Guide: [PROJECT_ADAPTER_V0_2.md](docs/project-starter/PROJECT_ADAPTER_V0_2.md)

## DE – Repository Quality Gate

Ein automatischer Quality Gate schützt die öffentliche Neutralität dieses Repositories: Denylist-Scan (ohne private Begriffe im Repo), Root-Hygiene, History-Trennung und README-Struktur — lokal per Script, in CI bei jedem Pull Request. Doku: [PUBLIC_QUALITY_GATE.md](docs/repository/PUBLIC_QUALITY_GATE.md)

## EN – Repository Quality Gate

An automated quality gate protects this repository's public neutrality: denylist scan (no private terms stored in the repo), root hygiene, history separation, and README structure — locally via script, in CI on every pull request. Docs: [PUBLIC_QUALITY_GATE.md](docs/repository/PUBLIC_QUALITY_GATE.md)

## DE – Aktueller Status

- **Foundation 0.1:** released / frozen
- **Foundation 0.2:** ist als `v0.2.0-foundation` Foundation Pre-Release veröffentlicht — [Release Notes](docs/release/FOUNDATION_0_2_RELEASE_NOTES.md)
- **Foundation 0.3:** ist als `v0.3.0-foundation` Foundation Pre-Release veröffentlicht — [Release Notes](docs/release/FOUNDATION_0_3_RELEASE_NOTES.md)
- **Foundation 0.4:** ist als `v0.4.0-foundation` Foundation Pre-Release veröffentlicht (Adoption Hardening & Public Usability) — [Release Notes](docs/release/FOUNDATION_0_4_RELEASE_NOTES.md)
- **Foundation 0.5:** ist als `v0.5.0-foundation` Foundation Pre-Release veröffentlicht (External Validation & 1.0 Path Hardening) — [Release Notes](docs/release/FOUNDATION_0_5_RELEASE_NOTES.md) · [v1.0-Pfad](docs/roadmap/V1_0_PATH_SUMMARY.md) (v1.0 ist nicht erreicht)
- **Foundation 0.6:** ist als `v0.6.0-foundation` Foundation Pre-Release veröffentlicht (Adoptionsvertrauen & Governance-Härtung; [ADR Policy](docs/adr/ADR_POLICY.md) angenommen, kein v1.0) — [Release Notes](docs/release/FOUNDATION_0_6_RELEASE_NOTES.md) · [Plan](docs/roadmap/FOUNDATION_0_6_PLAN.md) · [v1.0-Pfad](docs/roadmap/V1_0_PATH_SUMMARY.md)
- Public Framework Cleanup: erledigt · Project Adapter v0.2: verfügbar · DE/EN-Angleichung: laufend

Struktur-Review: [REPOSITORY_STRUCTURE_REVIEW.md](docs/repository/REPOSITORY_STRUCTURE_REVIEW.md) — NDF ist bewusst noch kein v1.0.

## EN – Current Status

- **Foundation 0.1:** released / frozen
- **Foundation 0.2:** published as the `v0.2.0-foundation` foundation pre-release — [Release Notes](docs/release/FOUNDATION_0_2_RELEASE_NOTES.md)
- **Foundation 0.3:** published as the `v0.3.0-foundation` foundation pre-release — [Release Notes](docs/release/FOUNDATION_0_3_RELEASE_NOTES.md)
- **Foundation 0.4:** published as the `v0.4.0-foundation` foundation pre-release (adoption hardening & public usability) — [Release Notes](docs/release/FOUNDATION_0_4_RELEASE_NOTES.md)
- **Foundation 0.5:** published as the `v0.5.0-foundation` foundation pre-release (external validation & 1.0 path hardening) — [Release Notes](docs/release/FOUNDATION_0_5_RELEASE_NOTES.md) · [v1.0 path](docs/roadmap/V1_0_PATH_SUMMARY.md) (v1.0 is not reached)
- **Foundation 0.6:** published as the `v0.6.0-foundation` foundation pre-release (adoption confidence & governance hardening; [ADR policy](docs/adr/ADR_POLICY.md) adopted, not v1.0) — [Release Notes](docs/release/FOUNDATION_0_6_RELEASE_NOTES.md) · [Plan](docs/roadmap/FOUNDATION_0_6_PLAN.md) · [v1.0 path](docs/roadmap/V1_0_PATH_SUMMARY.md)
- Public framework cleanup: done · Project Adapter v0.2: available · DE/EN alignment: in progress

Structure review: [REPOSITORY_STRUCTURE_REVIEW.md](docs/repository/REPOSITORY_STRUCTURE_REVIEW.md) — NDF is deliberately not v1.0 yet.

## DE – Einstieg

1. Kernprinzipien und Rollenmodell oben lesen.
2. Work-Package-Typen verstehen: [WORK_PACKAGE_TYPES.md](framework/standards/WORK_PACKAGE_TYPES.md)
3. Bestehendes Projekt anbinden: [PROJECT_ADAPTER_V0_2.md](docs/project-starter/PROJECT_ADAPTER_V0_2.md) — Beispiel-Fixture: [examples/neutral-example-project/](examples/neutral-example-project/README.md)
4. Vorlagen und Prompts: `framework/templates/` · `framework/prompts/`

## EN – Getting Started

1. Read the core principles and role model above.
2. Understand work package types: [WORK_PACKAGE_TYPES.md](framework/standards/WORK_PACKAGE_TYPES.md)
3. Adapt an existing project: [PROJECT_ADAPTER_V0_2.md](docs/project-starter/PROJECT_ADAPTER_V0_2.md) — example fixture: [examples/neutral-example-project/](examples/neutral-example-project/README.md)
4. Templates and prompts: `framework/templates/` · `framework/prompts/`

## DE – Sprache / Übersetzung

NDF wird zweisprachig (Deutsch/Englisch) geführt. Neue zentrale Dokumente sind bilingual oder klar sprachlich zugeordnet. Standard: [DE_EN_LANGUAGE_STANDARD.md](docs/i18n/DE_EN_LANGUAGE_STANDARD.md) · Status: [TRANSLATION_STATUS.md](docs/i18n/TRANSLATION_STATUS.md)

## EN – Language / Translation

NDF is maintained bilingually (German/English). New central documents are bilingual or clearly language-assigned. Standard: [DE_EN_LANGUAGE_STANDARD.md](docs/i18n/DE_EN_LANGUAGE_STANDARD.md) · Status: [TRANSLATION_STATUS.md](docs/i18n/TRANSLATION_STATUS.md)

## License / Lizenz

See [LICENSE](LICENSE).
