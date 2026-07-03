# Foundation 0.2 Release Notes

Release: `v0.2.0-foundation` — Foundation/Stabilization **Pre-Release**. NDF ist damit bewusst noch kein v1.0.

## DE – Überblick

Foundation 0.2 macht das Nova Development Framework öffentlich nutzbar: Das Repository wurde vollständig neutralisiert, ein automatischer Quality Gate schützt diesen Zustand, der Project Adapter v0.2 macht NDF auf bestehende Projekte anwendbar, und die zentralen Einstiegspunkte sind zweisprachig (DE/EN). Motto des Releases: *Framework beweisen statt Framework aufbauen.*

## EN – Overview

Foundation 0.2 makes the Nova Development Framework publicly usable: the repository was fully neutralized, an automated quality gate protects that state, Project Adapter v0.2 makes NDF applicable to existing projects, and the central entry points are bilingual (DE/EN). Release motto: *prove the framework instead of building it.*

## DE – Was ist neu?

- Work Package Type Standard: jedes Work Package hat genau einen deklarierten Typ (WP-027)
- Destructive Action Toolkit: Blueprint-vor-Implementierung, Owner-only, Audit Privacy (WP-028)
- Security Prompt Library (WP-029)
- Public Repository Quality Gate mit CI-Workflow (WP-032)
- Project Adapter v0.2: Guide mit Phasen 0–10, 6 Templates, Checkliste, Prompts (WP-034/035)
- DE/EN-Sprachstandard und Translation-Status-Matrix (WP-035)
- Nova (ChatGPT)-Rollendokument (WP-037)
- Release Readiness Review und diese Release-Vorbereitung (WP-040/041)

## EN – What is new?

- Work Package Type Standard: every work package carries exactly one declared type (WP-027)
- Destructive Action Toolkit: blueprint-before-implementation, owner-only, audit privacy (WP-028)
- Security Prompt Library (WP-029)
- Public Repository Quality Gate with CI workflow (WP-032)
- Project Adapter v0.2: guide with phases 0–10, 6 templates, checklist, prompts (WP-034/035)
- DE/EN language standard and translation status matrix (WP-035)
- Nova (ChatGPT) role document (WP-037)
- Release readiness review and this release preparation (WP-040/041)

## DE – Wichtigste Änderungen

Das Repository wirkt nicht mehr wie interne Projektdokumentation, sondern wie ein allgemein nutzbares Framework: neutrale Referenzprojekte statt konkreter Projektnamen, neutrale Rollen statt Personen, aufgeräumter Root, getrennte Import-/Release-Historie, konsistente Statusaussagen und ein bilingualer öffentlicher Einstieg.

## EN – Highlights

The repository no longer reads like internal project documentation but like a generally usable framework: neutral reference projects instead of concrete project names, neutral roles instead of persons, a clean root, separated import/release history, consistent status statements, and a bilingual public entry point.

## DE – Öffentliche Neutralisierung

Alle privaten Projekt- und Personenbezüge wurden aus den getrackten Dateien entfernt (WP-030/031). Validierungserkenntnisse blieben vollständig erhalten und laufen jetzt unter neutralen Referenzprojekten (Referenzprojekt A: Destructive Operations; Referenzprojekt B: CI/Docker).

## EN – Public Neutralization

All private project and person references were removed from tracked files (WP-030/031). Validation findings were fully preserved and are now attributed to neutral reference projects (Reference Project A: destructive operations; Reference Project B: CI/Docker).

## DE – Repository Quality Gate

`scripts/check_public_quality.py` prüft Neutralität (über eine bewusst nicht im Repo liegende Denylist), Root-Hygiene, History-Trennung und README-Struktur — lokal und bei jedem Push/PR über GitHub Actions. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## EN – Repository Quality Gate

`scripts/check_public_quality.py` checks neutrality (via a denylist deliberately kept out of the repo), root hygiene, history separation and README structure — locally and on every push/PR via GitHub Actions. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## DE – Project Adapter v0.2

Bestehende Projekte lassen sich strukturiert nach NDF überführen: read-only-Analyse → Project Profile/Manifest/Brain → Capability Matrix → Compliance Check → Health Score → Work Package Queue → erstes sicheres Work Package. Guide: `docs/project-starter/PROJECT_ADAPTER_V0_2.md`

## EN – Project Adapter v0.2

Existing projects can be brought into NDF in a structured way: read-only analysis → project profile/manifest/brain → capability matrix → compliance check → health score → work package queue → first safe work package. Guide: `docs/project-starter/PROJECT_ADAPTER_V0_2.md`

## DE – DE/EN-Ausrichtung

README und Workflow-Kern sind vollständig bilingual; 12 Kern-Prompts und 7 zentrale Checklisten tragen DE/EN-Zweck-, Grenzen- und Rückmeldungs-Blöcke. Der ehrliche Reststand steht in `docs/i18n/TRANSLATION_STATUS.md`.

## EN – DE/EN Alignment

The README and the workflow core are fully bilingual; 12 core prompts and 7 central checklists carry DE/EN purpose, boundary and feedback blocks. The honest remaining state is tracked in `docs/i18n/TRANSLATION_STATUS.md`.

## DE – Nova (ChatGPT)-Rolle

Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle — ist jetzt in allen zentralen Einstiegspunkten erklärt. Der Standard-Workflow lautet: Nova (ChatGPT) → Implementation Agent → Human Maintainer. Details: `docs/workflow/NOVA_CHATGPT_ROLE.md`

## EN – Nova (ChatGPT) Role

Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role — is now explained in all central entry points. The standard workflow is: Nova (ChatGPT) → Implementation Agent → Human Maintainer. Details: `docs/workflow/NOVA_CHATGPT_ROLE.md`

## DE – Security und destructive Actions

Security-first bleibt Kernprinzip: Security Review ≠ Security Fix ≠ Health Score Update; destruktive Funktionen laufen zweistufig über `destructive-blueprint` → `destructive-implementation` mit Owner-only-Autorisierung, typed confirmation, Audit Privacy und Tests. Werkzeuge: `docs/toolkit/destructive-actions/`, `docs/toolkit/security-prompts/`

## EN – Security and Destructive Actions

Security-first remains a core principle: security review ≠ security fix ≠ health score update; destructive functionality runs in two stages via `destructive-blueprint` → `destructive-implementation` with owner-only authorization, typed confirmation, audit privacy and tests. Tools: `docs/toolkit/destructive-actions/`, `docs/toolkit/security-prompts/`

## DE – Bekannte Einschränkungen

- NDF ist ein Foundation-Release, kein v1.0: Website, Export-Pipeline und CLI sind Konzepte bzw. Pläne.
- Nicht alle Dokumente sind bereits bilingual (Reststand in der Translation-Status-Matrix).
- Die ADR-Nummerierung enthält dokumentierte Altbestands-Überschneidungen zwischen `adr/` und `docs/adr/`.
- Die Git-Historie enthält Begriffe aus der Zeit vor der Neutralisierung; ein History-Rewrite wurde bewusst ausgeschlossen.
- Der CI-Neutralitäts-Scan wird erst mit gesetztem GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` scharf.

## EN – Known Limitations

- NDF is a foundation release, not v1.0: website, export pipeline and CLI are concepts or plans.
- Not all documents are bilingual yet (remaining state in the translation status matrix).
- The ADR numbering contains documented legacy overlaps between `adr/` and `docs/adr/`.
- The git history contains terms from before the neutralization; a history rewrite was deliberately ruled out.
- The CI neutrality scan only becomes active once the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` is set.

## DE – Upgrade von Foundation 0.1

Foundation 0.1 bleibt eingefroren und unverändert (Tag `v0.1.0-foundation`). Es gibt keine Migrationsschritte: Foundation 0.2 ist additiv und ersetzt keine 0.1-Artefakte. Projekte, die mit 0.1-Vorlagen gestartet sind, können die 0.2-Werkzeuge (Adapter, Typen-Standard, Toolkits) direkt übernehmen.

## EN – Upgrade from Foundation 0.1

Foundation 0.1 stays frozen and unchanged (tag `v0.1.0-foundation`). There are no migration steps: Foundation 0.2 is additive and replaces no 0.1 artifacts. Projects started from 0.1 templates can adopt the 0.2 tooling (adapter, type standard, toolkits) directly.

## DE – Empfohlene nächste Schritte

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen (Maintainer).
2. Adapter-Praxistest an einem externen Projekt.
3. ADR-Konsolidierung als eigenes Work Package.
4. i18n-Voll-Pass gemäß Translation-Status-Matrix.

## EN – Recommended Next Steps

1. Set the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` (maintainer).
2. Field-test the project adapter on an external project.
3. ADR consolidation as its own work package.
4. Full i18n pass following the translation status matrix.
