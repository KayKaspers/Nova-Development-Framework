# Prompt Library DE/EN Priority Pass

> Foundation 0.4, NDF-WP-060. Release-blocking Kern „Public Usability", bewusst eng gefasst. / Release-blocking core "public usability", deliberately narrow.

## DE – Zweck

Die für externe Adoption zuerst genutzten Kern-Prompts sollen auf Deutsch und Englisch gleichwertig sicher nutzbar sein. Dieser Pass übersetzt **nicht** die gesamte Prompt Library.

## EN – Purpose

The core prompts an external user reaches first during adoption must be safely usable in German and English alike. This pass does **not** translate the entire prompt library.

## DE – Scope / EN – Scope

Eng: die Adoptions-Erstkontakt-Prompts (Project Adapter, Work-Package-Klassifizierung/Boundary-Review) werden vollständig bilingual. Die priorisierten Security-/Release-Gate-Prompts tragen bereits DE/EN-Kernabschnitte (Zweck, Grenzen, Rückmeldung) seit NDF-WP-039; ihre vollständige Übersetzung bleibt Restarbeit. / Narrow: the adoption first-contact prompts become fully bilingual; the prioritized security/release-gate prompts already carry DE/EN core sections since NDF-WP-039, full translation remains follow-up work.

## DE – Priorisierte Prompt-Dateien / EN – Prioritized Prompt Files

**Vollständig bilingual in WP-060 / fully bilingual in WP-060:**

- `framework/prompts/project-adapter/PROJECT_ADAPTER_INTAKE_PROMPT.md`
- `framework/prompts/project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md`
- `framework/prompts/project-adapter/CREATE_PROJECT_ADAPTER.md` (Legacy v0.1)
- `framework/prompts/core/WORK_PACKAGE_CLASSIFICATION_PROMPT.md`
- `framework/prompts/review/WORK_PACKAGE_BOUNDARY_REVIEW_PROMPT.md`

**Bereits DE/EN-Kern (WP-039), bestätigt / already DE/EN core, confirmed:**

- `framework/prompts/security/SECURITY_BASELINE_REVIEW_PROMPT.md`
- `framework/prompts/security/SECURITY_FINDING_TRIAGE_PROMPT.md`
- `framework/prompts/security/SECURITY_RELEASE_GATE_PROMPT.md`
- `framework/prompts/security/DESTRUCTIVE_ACTION_BLUEPRINT_REVIEW_PROMPT.md`
- `framework/prompts/security/DESTRUCTIVE_ACTION_IMPLEMENTATION_GATE_PROMPT.md`
- `framework/prompts/security/FOCUSED_SECURITY_CODE_FIX_PROMPT.md`
- `framework/prompts/security/FAIL_CLOSED_CONFIG_PROMPT.md`

## DE – DE/EN-Mindeststandard / EN – DE/EN Minimum Standard

Vollständig bilingualisierte Prompts nutzen: Zweck/Purpose, Rolle/Role, Verwendung/When to Use, Eingaben/Inputs, Aufgabe(n)/Tasks, Grenzen/Boundaries, Erwartete Ausgabe/Expected Output, Rückmeldung an Nova (ChatGPT)/Feedback to Nova. DE und EN sind inhaltlich gleichwertig; Sicherheits- und Human-Maintainer-Grenzen bleiben in beiden Sprachen erhalten.

## DE – Nicht Teil dieses WPs / EN – Out of Scope for this WP

- WP-061 Checklist Library DE/EN — optional, nicht hier.
- WP-062 Academy Entry Pass — optional, nicht hier.
- WP-063 ADR Policy — optional, nicht hier.
- Vollübersetzung aller ~30 Prompts — bewusst nicht.
- Foundation 0.4 wird dadurch **nicht** v1.0.

## DE – Ergebnis / EN – Result

Die fünf Adoptions-Erstkontakt-Prompts sind vollständig DE/EN nutzbar; die sieben priorisierten Security-/Gate-Prompts haben bestätigte DE/EN-Kernabschnitte. Ein externer DE- oder EN-Nutzer kann den Adoptionseinstieg und die zentralen Work-Package-/Gate-Entscheidungen sicher durchführen.

## DE – Bekannte Restarbeiten / EN – Known Remaining Work

Non-blocking, nach Foundation 0.4: vollständige DE/EN-Übersetzung der übrigen Security-/Fach-Prompts, Blocks und Rollen-Prompts; Checklisten (WP-061) und Academy (WP-062). Stand transparent in `docs/i18n/TRANSLATION_STATUS.md`.
