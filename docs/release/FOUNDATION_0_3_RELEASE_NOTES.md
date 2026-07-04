# Foundation 0.3 Release Notes

Release: `v0.3.0-foundation` — Foundation Adoption **Pre-Release**. Vorbereitet für den geplanten Release / prepared for the planned foundation pre-release — **tag pending**. NDF ist damit bewusst noch kein v1.0.

## DE – Überblick

Foundation 0.3 beweist, dass das Nova Development Framework **praktisch übernehmbar** ist: Der Project Adapter v0.2 wurde vollständig an einem neutralen Beispielprojekt durchgespielt, ein gehärteter Public Quality Gate schützt neue Dateien schon vor dem Commit, und der Umfang blieb durch einen frühen Scope Lock kontrolliert. Motto: *Framework übernehmbar machen, nicht nur beweisen.*

## EN – Overview

Foundation 0.3 proves that the Nova Development Framework is **practically adoptable**: Project Adapter v0.2 was fully exercised on a neutral example project, a hardened public quality gate protects new files even before commit, and the scope stayed controlled through an early scope lock. Motto: *make the framework adoptable, not just proven.*

## DE – Was ist Foundation 0.3?

Ein **Foundation Adoption Release**. Nach Foundation 0.2 (öffentlich sauber, DE/EN-Einstieg) zeigt 0.3, wie ein externer Nutzer NDF auf ein bestehendes Projekt anwendet — nachvollziehbar am neutralen SampleProject, nicht an einem realen privaten Projekt.

## EN – What is Foundation 0.3?

A **foundation adoption release**. After Foundation 0.2 (publicly clean, DE/EN entry), 0.3 shows how an external user applies NDF to an existing project — traceable via the neutral SampleProject, not a real private project.

## DE – Wichtigste Änderungen

- Neutrales Beispielprojekt (SampleProject) als Adapter-Fixture (WP-046)
- Praktische Adapter-Validierung mit Ergebnis PASS WITH NOTES (WP-047)
- Public Quality Gate v0.2 mit new-file neutrality check (WP-052)
- Foundation 0.3 Scope Lock mit klar getrenntem release-blocking Umfang (WP-045)
- Release Readiness Review mit Ergebnis GO WITH NOTES (WP-054)

## EN – Highlights

- Neutral example project (SampleProject) as adapter fixture (WP-046)
- Practical adapter validation with result PASS WITH NOTES (WP-047)
- Public quality gate v0.2 with new-file neutrality check (WP-052)
- Foundation 0.3 scope lock with a clearly separated release-blocking scope (WP-045)
- Release readiness review with result GO WITH NOTES (WP-054)

## DE – Foundation Adoption Release

Der Release-Kern ist der **Adoptionsbeweis**: README → Adapter-Guide → SampleProject → Adapter-Output → zentraler Nachweis. Ein externer Nutzer kann diesen Pfad ohne interne Vorkenntnisse nachvollziehen.

## EN – Foundation Adoption Release

The release core is the **adoption proof**: README → adapter guide → SampleProject → adapter output → central validation. An external user can follow this path without insider knowledge.

## DE – SampleProject

SampleProject (`examples/neutral-example-project/`) ist ein **fiktives, neutrales Fixture im Pre-Adoption-Zustand** — kein echtes Produkt, keine lauffähige Software, keine echten privaten Daten (nur Platzhalter). Es simuliert ein gewachsenes Projekt mit typischen Lücken, damit der Adapter etwas zu finden hat.

## EN – SampleProject

SampleProject (`examples/neutral-example-project/`) is a **fictitious, neutral pre-adoption fixture** — not a real product, not runnable software, no real private data (placeholders only). It simulates a grown project with typical gaps so the adapter has something to find.

## DE – Project Adapter Practical Validation

Der Adapter v0.2 wurde über alle Phasen 0–10 durchgespielt (`docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md`). **Ergebnis: PASS WITH NOTES.** Keine release-blocking Findings; die Notes sind Konventionsverbesserungen im Improvement Backlog.

## EN – Project Adapter Practical Validation

Adapter v0.2 was exercised across all phases 0–10 (`docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md`). **Result: PASS WITH NOTES.** No release-blocking findings; the notes are convention improvements in the improvement backlog.

## DE – Public Quality Gate v0.2

`scripts/check_public_quality.py` scannt jetzt standardmäßig auch relevante **neue/untracked** Textdateien (new-file neutrality check) — private Begriffe werden vor dem ersten Commit gefangen. `--tracked-only` schaltet das bewusst ab. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## EN – Public Quality Gate v0.2

`scripts/check_public_quality.py` now scans relevant **new/untracked** text files by default (new-file neutrality check) — private terms are caught before the first commit. `--tracked-only` disables this deliberately. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## DE – Scope Lock und Release-Blocking Scope

Foundation 0.3 wurde früh eingefroren (`docs/roadmap/FOUNDATION_0_3_SCOPE_LOCK.md`). Release-blocking: WP-045, WP-046, WP-047, WP-052, WP-054, WP-055. Optionale WPs (048–051) blockieren nicht; WP-053 ist deferred. Kein Scope Creep.

## EN – Scope Lock and Release-Blocking Scope

Foundation 0.3 was frozen early (`docs/roadmap/FOUNDATION_0_3_SCOPE_LOCK.md`). Release-blocking: WP-045, WP-046, WP-047, WP-052, WP-054, WP-055. Optional work packages (048–051) do not block; WP-053 is deferred. No scope creep.

## DE – Bekannte Einschränkungen

- NDF ist ein Foundation-Release, kein v1.0.
- Optionale DE/EN-Restarbeiten offen: übrige Prompts (WP-048), Checklisten (WP-049), Academy-Einstieg (WP-050) — Reststand in `docs/i18n/TRANSLATION_STATUS.md`.
- ADR-Policy-Konsolidierung (WP-051) noch offen; ADR-Nummernkollisionen bleiben dokumentierter Altbestand.
- Adapter-Conventions-Backlog offen (Manifest-Format, Health-Score-Kategorien, Output-Pfad-Konvention) — `docs/validation/project-adapter/PROJECT_ADAPTER_V0_2_IMPROVEMENT_BACKLOG.md`.
- Unabhängiger Adapter-Testlauf (durch Unbeteiligte) steht noch aus (later).
- WP-053 Docs-Export-/Website-Konzept ist deferred (Foundation 0.4).
- Der CI-Neutralitäts-Scan wird erst mit gesetztem GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` scharf.
- Die Git-Historie bleibt unverändert (History-Rewrite bewusst ausgeschlossen).

## EN – Known Limitations

- NDF is a foundation release, not v1.0.
- Optional DE/EN work remains open: remaining prompts (WP-048), checklists (WP-049), academy entry (WP-050) — remaining state in `docs/i18n/TRANSLATION_STATUS.md`.
- ADR policy consolidation (WP-051) still open; ADR numbering overlaps remain documented legacy.
- Adapter conventions backlog open (manifest format, health-score categories, output-path convention) — `docs/validation/project-adapter/PROJECT_ADAPTER_V0_2_IMPROVEMENT_BACKLOG.md`.
- An independent adapter test run (by an uninvolved party) is still pending (later).
- WP-053 docs-export/website concept is deferred (Foundation 0.4).
- The CI neutrality scan only becomes active once the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` is set.
- The git history stays unchanged (history rewrite deliberately ruled out).

## DE – Upgrade von Foundation 0.2

Foundation 0.2 bleibt released (Tag `v0.2.0-foundation`). Foundation 0.3 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.2 nutzt, kann Adapter, Fixture und Quality Gate v0.2 direkt übernehmen.

## EN – Upgrade from Foundation 0.2

Foundation 0.2 stays released (tag `v0.2.0-foundation`). Foundation 0.3 is additive: no migration steps, no replaced artifacts. Users of 0.2 can adopt the adapter, fixture and quality gate v0.2 directly.

## DE – Nicht-Ziele

Kein v1.0, keine vollständige Website, keine Export-Pipeline, keine CLI, keine vollständige Academy-Übersetzung, kein History-Rewrite, keine privaten Projektbeispiele, keine ADR-Massenmigration ohne Policy.

## EN – Non-Goals

No v1.0, no complete website, no export pipeline, no CLI, no full academy translation, no history rewrite, no private project examples, no bulk ADR migration without a policy.

## DE – Empfohlene nächste Schritte

1. Manuell: GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen; Foundation-0.2-Release-Titel korrigieren.
2. Optionale i18n-WPs (048–051) priorisiert abarbeiten.
3. Adapter Conventions Polish und unabhängiger Adapter-Testlauf.

## EN – Recommended Next Steps

1. Manual: set/verify the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST`; correct the Foundation 0.2 release title.
2. Work through the optional i18n work packages (048–051) by priority.
3. Adapter conventions polish and an independent adapter test run.
