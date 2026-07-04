# Foundation 0.4 Release Notes

Release: `v0.4.0-foundation` — Adoption Hardening & Public Usability **Pre-Release**. Vorbereitet für den geplanten Release / prepared for the planned foundation pre-release — **tag pending**. NDF ist damit bewusst noch kein v1.0.

## DE – Überblick

Foundation 0.4 härtet NDF nach dem Adoptionsbeweis aus Foundation 0.3: Der Project Adapter wird durch verbindliche Konventionen reibungsärmer, die für externe Adoption wichtigsten Prompts sind jetzt vollständig zweisprachig (DE/EN), und der Umfang blieb durch einen frühen Scope Lock kontrolliert. Motto: *Framework übernehmbar machen — konsistent und öffentlich nutzbar.*

## EN – Overview

Foundation 0.4 hardens NDF after the adoption proof from Foundation 0.3: the project adapter becomes less friction-prone through binding conventions, the prompts most relevant to external adoption are now fully bilingual (DE/EN), and the scope stayed controlled through an early scope lock. Motto: *make the framework adoptable — consistent and publicly usable.*

## DE – Was ist Foundation 0.4?

Ein **Adoption Hardening & Public Usability Release**. Nach dem 0.3-Beweis, dass NDF übernehmbar ist, schließt 0.4 die konkreten Lücken, die bei der praktischen Adapter-Validierung (WP-047) sichtbar wurden — nicht mehr.

## EN – What is Foundation 0.4?

An **adoption hardening & public usability release**. After 0.3 proved NDF is adoptable, 0.4 closes the concrete gaps surfaced by the practical adapter validation (WP-047) — nothing more.

## DE – Wichtigste Änderungen

- Project Adapter Conventions: Manifest-, Output-Pfad- und Health-Score-Konvention (WP-059)
- Prompt Library DE/EN Priority Pass: fünf Adoptions-Erstkontakt-Prompts vollständig bilingual (WP-060)
- Foundation 0.4 Scope Lock mit klar getrenntem release-blocking Umfang (WP-058)
- Release Readiness Review mit Ergebnis GO WITH NOTES (WP-067)

## EN – Highlights

- Project adapter conventions: manifest, output path and health-score conventions (WP-059)
- Prompt library DE/EN priority pass: five adoption first-contact prompts fully bilingual (WP-060)
- Foundation 0.4 scope lock with a clearly separated release-blocking scope (WP-058)
- Release readiness review with result GO WITH NOTES (WP-067)

## DE – Adoption Hardening & Public Usability

Der release-blocking Kern ist bewusst klein und gibt jeder Titel-Hälfte genau ein Deliverable: **Adoption Hardening** über die Adapter-Konventionen, **Public Usability** über den Prompt-DE/EN-Pass. Weiteres ist optional oder deferred.

## EN – Adoption Hardening & Public Usability

The release-blocking core is deliberately small and gives each half of the title exactly one deliverable: **adoption hardening** via the adapter conventions, **public usability** via the prompt DE/EN pass. Everything else is optional or deferred.

## DE – Project Adapter Conventions

`docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` legt fest:

- `PROJECT_MANIFEST.md` ist das kanonische, öffentlich reviewbare Markdown-Manifest (YAML/JSON nur eingebettet).
- Klare Output-Pfade für Validierungsläufe (`examples/<fixture>/adapter-validation-output/`), zentrale Nachweise (`docs/validation/project-adapter/`) und produktionsnahe Übernahme (`project-system/` etc., nur nach Maintainer-Entscheidung).
- Foundation-0.4-Health-Score-Kategorien mit `unknown`/`n/a`-Regeln; keine stillen Überschreibungen produktiver Doku.

## EN – Project Adapter Conventions

`docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` defines: `PROJECT_MANIFEST.md` as the canonical, publicly reviewable markdown manifest; clear output paths for validation runs, central evidence, and production-like adoption; the Foundation 0.4 health-score categories with `unknown`/`n/a` rules; no silent overwriting of productive docs.

## DE – Prompt Library DE/EN Priority Pass

Die fünf Prompts, die ein externer Nutzer beim Adoptions-Einstieg zuerst nutzt (Project Adapter Intake/Baseline/Create, Work Package Classification, Boundary Review), sind vollständig DE/EN nutzbar. Die priorisierten Security-/Gate-Prompts tragen DE/EN-Kernabschnitte. Die übrige Prompt Library bleibt gemischt (Restarbeit). Details: `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`

## EN – Prompt Library DE/EN Priority Pass

The five prompts an external user reaches first during adoption (project adapter intake/baseline/create, work package classification, boundary review) are fully usable in DE and EN. The prioritized security/gate prompts carry DE/EN core sections. The remaining prompt library stays mixed (follow-up work). Details: `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`

## DE – Scope Lock und Release-Blocking Scope

Foundation 0.4 wurde früh eingefroren (`docs/roadmap/FOUNDATION_0_4_SCOPE_LOCK.md`). Release-blocking: WP-058, WP-059, WP-060, WP-067, WP-068. Optional: WP-061, WP-062, WP-063, WP-066. Deferred: WP-064, WP-065. Kein Scope Creep.

## EN – Scope Lock and Release-Blocking Scope

Foundation 0.4 was frozen early. Release-blocking: WP-058, WP-059, WP-060, WP-067, WP-068. Optional: WP-061, WP-062, WP-063, WP-066. Deferred: WP-064, WP-065. No scope creep.

## DE – Public Quality Gate

Der Public Quality Gate v0.2 bleibt aktiv: er scannt standardmäßig auch neue/untracked Dateien (new-file neutrality check), lokal und in CI. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## EN – Public Quality Gate

The public quality gate v0.2 stays active: by default it also scans new/untracked files (new-file neutrality check), locally and in CI. Details: `docs/repository/PUBLIC_QUALITY_GATE.md`

## DE – Bekannte Einschränkungen

- NDF ist ein Foundation-Release, kein v1.0.
- Optionale WPs offen: Checklist DE/EN (WP-061), Academy Entry (WP-062), ADR Policy Plan (WP-063), Quality Gate Maintenance (WP-066).
- Deferred: Independent Adapter Validation Run (WP-064), Docs Export / Website Concept (WP-065).
- Restliche i18n-Arbeiten offen; Security-/Gate-Prompts sind DE/EN-Kern, aber nicht vollständig übersetzt — Stand in `docs/i18n/TRANSLATION_STATUS.md`.
- Der CI-Neutralitäts-Scan wird erst mit gesetztem GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` scharf.
- Die Git-Historie bleibt unverändert (History-Rewrite bewusst ausgeschlossen).
- ADR-Nummernkollisionen bleiben dokumentierter Altbestand.

## EN – Known Limitations

- NDF is a foundation release, not v1.0.
- Optional work packages open: checklist DE/EN (WP-061), academy entry (WP-062), ADR policy plan (WP-063), quality gate maintenance (WP-066).
- Deferred: independent adapter validation run (WP-064), docs export/website concept (WP-065).
- Remaining i18n work is open; security/gate prompts are DE/EN core but not fully translated — state in `docs/i18n/TRANSLATION_STATUS.md`.
- The CI neutrality scan only becomes active once the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` is set.
- The git history stays unchanged (history rewrite deliberately ruled out).
- ADR numbering overlaps remain documented legacy.

## DE – Upgrade von Foundation 0.3

Foundation 0.3 bleibt released (Tag `v0.3.0-foundation`). Foundation 0.4 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.3 nutzt, kann die Adapter-Konventionen und die bilingualen Prompts direkt übernehmen.

## EN – Upgrade from Foundation 0.3

Foundation 0.3 stays released (tag `v0.3.0-foundation`). Foundation 0.4 is additive: no migration steps, no replaced artifacts. Users of 0.3 can adopt the adapter conventions and the bilingual prompts directly.

## DE – Nicht-Ziele

Kein v1.0, keine vollständige Repo-Übersetzung, keine vollständige Academy, keine Website, keine Export-Pipeline, keine CLI, kein History-Rewrite, keine privaten Projektbeispiele, keine ADR-Massenmigration ohne Policy, keine Release-Automation.

## EN – Non-Goals

No v1.0, no full-repo translation, no complete academy, no website, no export pipeline, no CLI, no history rewrite, no private project examples, no bulk ADR migration without a policy, no release automation.

## DE – Empfohlene nächste Schritte

1. Manuell: GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen/prüfen; Foundation-0.2-Release-Titel korrigieren.
2. Optionale WPs (061–063, 066) priorisiert abarbeiten.
3. Independent Adapter Validation Run (064) und Docs Export/Website Concept (065) nach 0.4.

## EN – Recommended Next Steps

1. Manual: set/verify the GitHub secret `NDF_PUBLIC_NEUTRALITY_DENYLIST`; correct the Foundation 0.2 release title.
2. Work through the optional work packages (061–063, 066) by priority.
3. Independent adapter validation run (064) and docs export/website concept (065) after 0.4.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.4.0 Foundation is an adoption hardening and public usability pre-release.

Highlights:
- Project Adapter Conventions for manifest, output paths, and health score
- Prompt Library DE/EN Priority Pass for core adoption prompts
- locked Foundation 0.4 scope
- release readiness review with no blockers
- Public Quality Gate v0.2 remains active

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_4_RELEASE_NOTES.md

---

DE: Adoption-Hardening- und Public-Usability-Pre-Release. Vollständige zweisprachige
Release Notes im Repository unter docs/release/FOUNDATION_0_4_RELEASE_NOTES.md.
```
