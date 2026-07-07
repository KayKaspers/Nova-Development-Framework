# Foundation 0.6 Scope Lock

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.6 verbindlich ein (NDF-WP-085). Es macht aus dem Kandidatenplan (NDF-WP-084) die verbindliche Einstufung: release-blocking, optional, deferred — inklusive der ADR-Entscheidungspflicht, des WP-088-Ventils und der Änderungsregeln.

## EN – Purpose

This document bindingly freezes the Foundation 0.6 scope (NDF-WP-085), turning the candidate plan (NDF-WP-084) into the binding classification — including the ADR decision duty, the WP-088 valve, and the change rules.

## DE – Release-Ziel

```text
Foundation Adoption Confidence & Governance Hardening Release
(voraussichtlich Pre-Release v0.6.0-foundation — noch nicht released)
```

**Scope locked** (NDF-WP-085, 2026-07-07). Foundation 0.6 ist gelockt, nicht released, **nicht v1.0**.

## EN – Release Target

Foundation pre-release, presumably `v0.6.0-foundation` — not released. **Scope locked** (NDF-WP-085, 2026-07-07). Not v1.0.

## DE – Leitidee

**Adoption Confidence & Governance Hardening.** Kernziel je Hälfte: Adoption Confidence → öffentliche SampleProject-Runbook-Validierung (WP-088); Governance Hardening → ADR-Policy-Entscheidung (WP-086) plus Quality-Gate-Wartung (WP-089). Die in 0.5 sichtbar gemachten Punkte werden abgearbeitet oder bewusst entschieden — nicht erneut verschoben.

## EN – Theme

**Adoption Confidence & Governance Hardening.** Core per half: adoption confidence → the public SampleProject runbook validation (WP-088); governance hardening → the ADR policy decision (WP-086) plus quality gate maintenance (WP-089). The items made visible in 0.5 get worked off or consciously decided — not deferred again.

## DE – Finaler release-blocking Scope

Nur diese WPs blockieren den Release:

| WP | Titel | Begründung |
|---|---|---|
| NDF-WP-085 | Scope Lock | Gate — abgeschlossen mit diesem Dokument |
| NDF-WP-086 | ADR Policy Decision | Governance-Kern; 0.5-Sonderregel verlangt eine Entscheidung (siehe unten) — **entschieden am 2026-07-07: Minimal ADR Policy adopted** (`docs/adr/ADR_POLICY.md`) |
| NDF-WP-088 | Public SampleProject Runbook Validation Run | Adoption-Confidence-Kern; schließt die 0.5-Lücke (privater statt öffentlicher Kontext) — **durchgeführt am 2026-07-07: PASS WITH NOTES**, Ventil nicht benötigt; WP-087 skipped |
| NDF-WP-089 | Quality Gate Maintenance Review | leichtgewichtiger Gate-Nachlauf, erstmals seit v0.2 fällig; inkl. CI-Denylist-Wirksamkeitsbewertung — **durchgeführt am 2026-07-07: Evidence-Level strong, WP-090 not needed** |
| NDF-WP-094 | Release Readiness Review | Gate; entscheidet zugleich über das WP-088-Ventil |
| NDF-WP-095 | Release Prep | Gate |

## EN – Final Release-Blocking Scope

Only WP-085 (this gate), WP-086 (ADR decision), WP-088 (public runbook validation run, with a strict valve), WP-089 (gate maintenance incl. CI denylist effectiveness assessment), WP-094 (readiness review, also decides the valve), and WP-095 (release prep) block the release.

## DE – Optionale Work Packages

Should-have, blockiert nie; Unerledigtes wird ehrlich in Release Notes und Translation-Status-Matrix geführt:

- NDF-WP-087 – Public SampleProject Runbook Validation Preparation — **nur falls nötig**: Die WP-073-Unterlagen sind nutzbar; kann WP-088 direkt damit starten, wird WP-087 übersprungen (skipped).
- NDF-WP-090 – CI Denylist Effectiveness Proof — **merged/conditional**: Der Nachweis ist Teil von WP-089; WP-090 wird nur eigenständig nachgezogen, wenn WP-089 ausdrücklich feststellt, dass ein separates Nachweis-Artefakt nötig ist.
- NDF-WP-091 – Checklist Library DE/EN Priority Pass
- NDF-WP-092 – Academy Band 1 Entry Pass
- NDF-WP-093 – v1.x Compatibility Policy Draft (v1.0-tracked; Draft, kein Versprechen)

## EN – Optional Work Packages

WP-087 (only if needed — skipped if WP-088 can start with the WP-073 materials), WP-090 (merged/conditional: part of WP-089 unless WP-089 explicitly finds a separate proof artifact necessary), WP-091 (checklist DE/EN), WP-092 (academy entry), WP-093 (v1.x compatibility policy draft — v1.0-tracked, a draft, not a promise). None blocks; unfinished items are documented honestly.

## DE – Deferred Scope

Vollständige Doku-Website; vollständige i18n-Abdeckung; ADR-Massenmigration (erst nach der WP-086-Entscheidung, eigenes Vorhaben); v1.0 Release Candidate (ausschließlich späterer eigener v1.0-Zyklus); großer Framework-Rewrite; neue Applikations-Features.

## EN – Deferred Scope

Full documentation website; full i18n completion; ADR mass migration (only after the WP-086 decision, as its own effort); v1.0 release candidate (a later dedicated v1.0 cycle only); large framework rewrite; new application features.

## DE – ADR-Policy-Entscheidung

**NDF-WP-086 ist release-blocking und muss eine Entscheidung treffen.** Grundlage ist die verbindliche Foundation-0.5-Sonderregel: Die ADR-Policy wurde zweimal verschoben (0.4/WP-063, 0.5/WP-076) — ein drittes stilles Verschieben ist unzulässig.

Zulässige Ergebnisse von WP-086:

- **A) Minimal ADR Policy adopted** — entschiedene Minimal-Policy (Nummernraum, Ablageort, Umgang mit Altbestand), nur Policy, keine Migration.
- **B) ADR Policy explicitly dropped** — ehrliches Streichen mit dokumentierter Begründung; das offene v1.0-Kriterium wird dann als „dokumentiert gestrichen" geschlossen.
- **C) REWORK/STOP** — nur wenn weder Annahme noch ehrliches Streichen möglich ist.

**Unzulässig:** „defer again", „later", „decide in a future foundation release" — in jeder Formulierung.

## EN – ADR Policy Decision

**NDF-WP-086 is release-blocking and must decide.** Based on the binding Foundation 0.5 special rule (deferred twice, no third silent carry-over), the admissible outcomes are: (A) a minimal ADR policy adopted (policy only, no migration); (B) an explicit, documented drop — which then closes the open v1.0 criterion as "documented as dropped"; (C) REWORK/STOP only if neither is possible. **Inadmissible:** "defer again", "later", "decide in a future foundation release" — in any wording.

## DE – Public SampleProject Runbook Validation

**NDF-WP-088 ist release-blocking.** Ziel: ein Runbook-basierter unabhängiger Lauf gegen das **öffentliche** SampleProject-Fixture (`examples/neutral-example-project/`) gemäß den WP-073-Unterlagen — das schließt die 0.5-Known-Limitation (privater Referenzkontext, summarisches Feedback) und kann External Validation im v1.0-Draft von `partially met` Richtung `met` heben. **Auch bei Erfolg gilt: Foundation 0.6 ist dadurch nicht v1.0.** WP-087 (Vorbereitung) nur, falls die bestehenden Unterlagen für den öffentlichen Lauf nachgeschärft werden müssen.

## EN – Public SampleProject Runbook Validation

**NDF-WP-088 is release-blocking:** a runbook-based independent run against the **public** SampleProject fixture per the WP-073 materials — closing the 0.5 known limitation and potentially lifting external validation in the v1.0 draft from `partially met` toward `met`. **Even on success, Foundation 0.6 is not v1.0.** WP-087 (preparation) only if the existing materials need sharpening for the public run.

## DE – Downgrade-/Ventil-Regel

WP-088 bleibt release-blocking. WP-094 (Release Readiness Review) darf WP-088 nur dann auf **non-blocking / Known Limitation** herabstufen, wenn **alle** folgenden Bedingungen erfüllt sind:

1. WP-088 wurde tatsächlich versucht oder nachvollziehbar vorbereitet (dokumentierter Stand, kein bloßes Auslassen).
2. Ein ausführbarer öffentlicher Runbook-/Fixture-Plan liegt vor (WP-073-Unterlagen, ggf. via WP-087 nachgeschärft).
3. Der konkrete Hinderungsgrund ist dokumentiert (neutral, ohne private Namen/Kanäle).
4. Der Hinderungsgrund ist **nicht** durch kleine Dokumentationskorrekturen lösbar.
5. Im Validierungspfad liegen keine privaten Daten, keine privaten Projektnamen und keine Secrets.
6. Die Lücke wird in den Foundation-0.6-Release-Notes als Known Limitation dokumentiert.
7. Die öffentliche SampleProject-Runbook-Validierung bleibt **v1.0-tracked** — das Ventil ist kein Dauerausweg.
8. Der Human Maintainer bestätigt die Downgrade-Entscheidung im Go/No-Go.

**Missbrauchsklausel:** Das Ventil dient nicht dazu, unbequeme Arbeit zu überspringen. Ist WP-088 mit vertretbarem Aufwand möglich, bleibt es blocking. Das Ventil gilt **nur** für WP-088 und erlaubt keine Aufweichung von WP-086 oder WP-089.

## EN – Downgrade / Valve Rule

WP-088 stays release-blocking. WP-094 may downgrade it to **non-blocking / known limitation** only if **all** eight conditions hold: (1) actually attempted or traceably prepared; (2) an executable public runbook/fixture plan exists; (3) the concrete impediment is documented neutrally; (4) the impediment is not solvable by small documentation fixes; (5) no private data/names/secrets in the validation path; (6) the gap is documented as a known limitation in the 0.6 release notes; (7) the public runbook validation stays **v1.0-tracked** — the valve is no permanent escape; (8) the human maintainer confirms the downgrade in the go/no-go. **Abuse clause:** the valve must not be used to skip inconvenient work — if WP-088 is feasible with reasonable effort, it stays blocking. The valve applies **only** to WP-088.

## DE – Änderungsregeln nach Scope Lock

**Erlaubt (ohne Scope-Änderung):** kleine Dokumentationskorrekturen; Link-/Statuskorrekturen; Klarstellungen ohne Scope-Erweiterung; Quality-Gate-Fixes; Review-Fixes aus blocking WPs.

**Nur mit expliziter Nova-(ChatGPT)-/Human-Maintainer-Entscheidung:** neue release-blocking WPs; Verschieben von blocking zu optional; neue große Dokumentfamilien; neue Tooling-/CI-Funktionen; neue v1.0-Claims (grundsätzlich unzulässig, siehe unten); Änderungen an der WP-088-Ventilregel.

**Verboten:** stilles Verschieben der ADR-Policy-Entscheidung; v1.0 Release Candidate; Foundation-0.6 Release Prep vor WP-094; Tagging/Release durch den Implementation Agent.

## EN – Change Rules after Scope Lock

**Allowed:** small documentation fixes, link/status corrections, clarifications without scope extension, quality gate fixes, review fixes from blocking work packages. **Requires explicit Nova (ChatGPT) / human maintainer decision:** new release-blocking work packages, moving blocking to optional, new large document families, new tooling/CI features, new v1.0 claims (fundamentally inadmissible, see below), changes to the WP-088 valve rule. **Forbidden:** silently deferring the ADR policy decision, a v1.0 release candidate, Foundation 0.6 release prep before WP-094, tagging/releasing by the Implementation Agent.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; kein Rewrite; keine Website/Export-Pipeline/CLI; keine vollständige i18n-Abdeckung; keine ADR-Massenmigration; keine Integration realer privater Projekte; keine neuen Großkonzepte ohne Scope-Lock-Änderung; keine 0.6-Release-Zusage (der Release folgt erst nach WP-094/095 und manueller Freigabe).

## EN – Non-Goals

No v1.0 or release candidate; no rewrite; no website/export pipeline/CLI; no full i18n; no bulk ADR migration; no real private projects; no new large concepts without a scope lock change; no 0.6 release promise (the release follows only after WP-094/095 and manual approval).

## DE – v1.0-Abgrenzung

Foundation 0.6 **reduziert v1.0-Unsicherheit** — mehr nicht. Auch wenn WP-086, WP-088 und WP-093 v1.0-Kriterien schließen oder entwerfen: Kein 0.6-Dokument darf v1.0-Reife behaupten oder implizieren. Ob und wann v1.0 kommt, entscheidet ausschließlich ein späterer eigener v1.0-Zyklus (Scope Lock → Readiness → Prep → Maintainer-Freigabe).

## EN – v1.0 Boundary

Foundation 0.6 **reduces v1.0 uncertainty** — nothing more. Even where WP-086/088/093 close or draft v1.0 criteria, no 0.6 document may claim or imply v1.0 maturity. Whether and when v1.0 happens is decided solely by a later dedicated v1.0 cycle.

## DE – Nächster Schritt

**NDF-WP-086 – ADR Policy Decision** (parallel möglich: WP-088-Vorbereitung prüfen bzw. WP-089). Kein anderes inhaltliches WP vor diesen.

## EN – Next Step

**NDF-WP-086 – ADR policy decision** (in parallel where useful: assess WP-088 preparation needs, or WP-089). No other content work package before these.
