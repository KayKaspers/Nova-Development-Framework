# NDF Prompt Modes

## DE – Zweck

Dieses Dokument macht die in der [Context Economy](NDF_CONTEXT_ECONOMY.md) (NDF-WP-109) konzeptionell eingeführten **Prompt Modes** zu einer konkreten, nutzbaren NDF-Regel (NDF-WP-113). Es grenzt **Full**, **Standard** und **Short Prompt Mode** klar ab und legt fest, wann welcher Modus zulässig ist — ohne dass ein sparsamerer Modus Sicherheits-, Review- oder Release-Gates umgeht.

## EN – Purpose

This document turns the **prompt modes** introduced conceptually in the [Context Economy](NDF_CONTEXT_ECONOMY.md) (NDF-WP-109) into a concrete, usable NDF rule (NDF-WP-113). It clearly separates **Full**, **Standard**, and **Short Prompt Mode** and defines when each is allowed — without letting a leaner mode bypass security, review, or release gates.

## DE – Status

**Accepted (NDF-WP-113, 2026-07-08).** Foundation 0.8 ist scope-locked, **nicht released**, **nicht v1.0**. Dieses Dokument erstellt **keine aktiven Skills**, keine `.claude/skills`, keine `SKILL.md`, keine Scripts.

## EN – Status

**Accepted (NDF-WP-113, 2026-07-08).** Foundation 0.8 is scope-locked, **not released**, **not v1.0**. This document creates **no active skills**, no `.claude/skills`, no `SKILL.md`, no scripts.

## DE – Grundprinzip

Der Prompt Mode bestimmt die **Kontextmenge und Prompt-Größe**, niemals die Sorgfalt. Ein sparsamer Modus reduziert unnötigen Kontext, nicht Sicherheit, Review, Quality Gate, Evidenz oder Dokumentation. Im Zweifel gilt der größere Modus.

## EN – Core Principle

The prompt mode sets the **context volume and prompt size**, never the diligence. A leaner mode reduces unnecessary context, not safety, review, quality gate, evidence, or documentation. When in doubt, the larger mode applies.

## DE – Prompt Mode Übersicht

| Modus | Kontextmenge | Typische Nutzung | Nie nutzen für |
|---|---|---|---|
| **Full** | voll | Scope Lock, ADR, Security Policy, Release Readiness, Release Prep, gefährliche/governance-relevante Entscheidungen | — |
| **Standard** | mittel | normale Work Packages, Doku-Reviews, überschaubare Statusupdates | governance-/release-kritische Entscheidungen |
| **Short** | minimal | standardisierte Folgearbeit mit vorhandenem Context Pack, kleine Update-WPs, wiederkehrende Checks | alles Kritische (siehe Verbotsliste) |

## EN – Prompt Mode Overview

Same as above: Full = full context (scope lock, ADR, security policy, release readiness/prep, dangerous/governance decisions); Standard = medium context (normal work packages, doc reviews, small status updates); Short = minimal context (standardized follow-up work with an existing Context Pack, small update WPs, recurring checks — never for anything critical).

## DE – Full Prompt Mode

Voller Kontext und vollständige harte Grenzen. **Pflicht** für: Scope Lock, ADR/Governance-Entscheidungen, Skill Security Policy, Release Readiness Review, Release Prep, destructive/irreversible Aktionen, alles mit dauerhafter Governance-Wirkung. Enthält alle relevanten Kontext-Schichten (Durable Rules, Phase, WP, Evidence, Output Summary).

## EN – Full Prompt Mode

Full context and complete hard limits. **Mandatory** for: scope lock, ADR/governance decisions, skill security policy, release readiness review, release prep, destructive/irreversible actions, anything with lasting governance effect. Includes all relevant context layers.

## DE – Standard Prompt Mode

Mittlerer Kontext für vorhersehbare, klar abgegrenzte Arbeit: normale Work Packages, Doku-Reviews, überschaubare Statusupdates. Enthält Phase-, WP- und Evidence-Kontext; Durable Rules werden referenziert statt wiederholt. Endet mit Rückmeldung an Nova + Compact Context Summary.

## EN – Standard Prompt Mode

Medium context for predictable, clearly bounded work: normal work packages, doc reviews, small status updates. Includes phase, WP, and evidence context; durable rules are referenced instead of repeated. Ends with Report to Nova + Compact Context Summary.

## DE – Short Prompt Mode

Minimaler Kontext — **nur** für gut standardisierte Folgearbeiten mit **vorhandenem, aktuellem Context Pack** und klaren Grenzen: kleine Update-WPs, wiederkehrende Checks. Setzt voraus, dass ein Context Pack die Phase, die Sicherheitsgrenzen und den nächsten Schritt bereits sicher zusammenfasst. Endet trotzdem mit Compact Context Summary; überspringt **keine** Sicherheits-/Gate-Prüfung.

## EN – Short Prompt Mode

Minimal context — **only** for well-standardized follow-up work with an **existing, current Context Pack** and clear limits: small update WPs, recurring checks. It presumes a Context Pack already safely summarizes the phase, safety boundaries, and next step. It still ends with a Compact Context Summary and skips **no** safety/gate check.

## DE – Auswahlregeln

1. Governance-, Security-, ADR-, Scope-Lock-, Release- oder destructive Arbeit → **Full**.
2. Normale, klar abgegrenzte WP-Arbeit → **Standard**.
3. Standardisierte Folgearbeit mit aktuellem Context Pack → **Short**.
4. Unklare Anforderungen, fehlender/veralteter Context Pack, Zweifel → **eine Stufe höher** wählen.
5. Der Human Maintainer kann jederzeit einen größeren Modus verlangen.

## EN – Selection Rules

(1) Governance/security/ADR/scope-lock/release/destructive work → Full; (2) normal, clearly bounded WP work → Standard; (3) standardized follow-up work with a current Context Pack → Short; (4) unclear requirements, missing/stale Context Pack, or doubt → pick one level higher; (5) the human maintainer may demand a larger mode at any time.

## DE – Verbotene Short-Prompt-Fälle

Short Prompt Mode darf **nie** genutzt werden für: Security Policy; ADR; Scope Lock; Release Readiness; Release Prep; destructive actions; Git-Write-Aktionen; Tag-/Release-Aktionen; unklare Anforderungen. In diesen Fällen ist mindestens Standard, für governance-/release-kritische Fälle Full Pflicht.

## EN – Forbidden Short-Prompt Cases

Short Prompt Mode must **never** be used for: security policy; ADR; scope lock; release readiness; release prep; destructive actions; git write actions; tag/release actions; unclear requirements. In these cases at least Standard applies, and Full is mandatory for governance/release-critical cases.

## DE – Sicherheits- und Neutralitätsregeln

Public Quality Gate und Public Neutrality bleiben in jedem Modus Pflicht. Kein Modus umgeht ein Human-Maintainer-Gate. Keine Chain-of-Thought-Anforderung — NDF arbeitet mit shareable summaries, Rückmeldung an Nova und Compact Context Summary. Keine Secrets, keine privaten Daten, keine echten Domains/Kontakte; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie.

## EN – Security and Neutrality Rules

The public quality gate and public neutrality remain mandatory in every mode. No mode bypasses a human-maintainer gate. No chain-of-thought requirement — NDF works with shareable summaries, the Report to Nova, and the Compact Context Summary. No secrets, no private data, no real domains/contacts; naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never.

## DE – Beziehung zu Context Packs

Short Prompt Mode setzt einen aktuellen [Context Pack](../../project-brain/CONTEXT_PACK_TEMPLATE.md) voraus — dieser liefert Phasenstatus, Sicherheitsgrenzen und nächsten Schritt kompakt und wiederverwendbar. Ein Context Pack **ersetzt keine** Prüfung der aktuellen Dateien, keinen Public Quality Gate und kein Human-Maintainer-Review; er beschleunigt nur den Einstieg.

## EN – Relationship to Context Packs

Short Prompt Mode presumes a current [Context Pack](../../project-brain/CONTEXT_PACK_TEMPLATE.md) — it provides phase status, safety boundaries, and the next step compactly and reusably. A Context Pack **replaces neither** a check of the current files, nor the public quality gate, nor human-maintainer review; it only speeds up the entry.

## DE – Beziehung zu Claude Skills

Prompt Modes sind eine Dokumentationsregel, **kein** Skill. Ein späterer `ndf-token-economy`-Skill (Design in WP-111, Implementierung optional in WP-112) könnte die Modus-Auswahl unterstützen, muss aber die [Skill Security Policy](NDF_SKILL_SECURITY_POLICY.md) (ADR-0032) einhalten. Dieses WP erstellt **keine Skills**.

## EN – Relationship to Claude Skills

Prompt modes are a documentation rule, **not** a skill. A later `ndf-token-economy` skill (design in WP-111, implementation optional in WP-112) could support mode selection but must comply with the [Skill Security Policy](NDF_SKILL_SECURITY_POLICY.md) (ADR-0032). This WP creates **no skills**.

## DE – Beispiele

- **Full:** „NDF-WP-1xx Scope Lock" oder „ADR-00xx Governance-Entscheidung".
- **Standard:** „NDF-WP-1xx Doku-Review eines bestehenden Abschnitts".
- **Short:** „Kleiner Status-Sync-WP nach aktuellem Context Pack: Queue-Zeile abhaken und Compact Context Summary liefern."

## EN – Examples

- **Full:** "NDF-WP-1xx scope lock" or "ADR-00xx governance decision".
- **Standard:** "NDF-WP-1xx doc review of an existing section".
- **Short:** "Small status-sync WP against the current Context Pack: check a queue row and deliver a Compact Context Summary."

## DE – Nicht-Ziele

Keine Chain-of-Thought-Anforderung; keine aktiven Skills; keine `.claude/skills`; keine Scripts; kein Modus, der Sicherheits-/Gate-/Human-Gate-Prüfungen umgeht; kein v1.0-Claim; keine aktive volle v1.x-Kompatibilitätszusage; keine Foundation-0.8-Release-Behauptung.

## EN – Non-Goals

No chain-of-thought requirement; no active skills; no `.claude/skills`; no scripts; no mode that bypasses safety/gate/human-gate checks; no v1.0 claim; no active full v1.x compatibility promise; no Foundation 0.8 release claim.

## DE – Nächste Schritte

**NDF-WP-114 – Foundation 0.8 Release Readiness Review.** Danach WP-115 (Release Prep). Optional WP-112 (Skills MVP Implementation, nur per Human-Maintainer-Scope-Change).

## EN – Next Steps

**NDF-WP-114 – Foundation 0.8 Release Readiness Review.** Then WP-115 (release prep). Optionally WP-112 (skills MVP implementation, only via human-maintainer scope change).
