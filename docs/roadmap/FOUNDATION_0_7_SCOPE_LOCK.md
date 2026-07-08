# Foundation 0.7 Scope Lock

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.7 verbindlich ein (NDF-WP-098). Es macht aus dem Kandidatenplan (NDF-WP-097) die verbindliche Einstufung: release-blocking, optional, deferred — inklusive des WP-099-Entscheidungskorridors, der WP-100-ADR-0031-Frage, des WP-102-Upgrade-Ventils und der Change-Control-Regeln.

## EN – Purpose

This document bindingly freezes the Foundation 0.7 scope (NDF-WP-098), turning the candidate plan (NDF-WP-097) into the binding classification — including the WP-099 decision corridor, the WP-100 ADR-0031 question, the WP-102 upgrade valve, and the change control rules.

## DE – Arbeitstitel

**Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance** (v1.0-Pfad-Konsolidierung und Kompatibilitäts-Governance). **Scope locked** (NDF-WP-098, 2026-07-08). Foundation 0.7 ist gelockt, **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**.

## EN – Working Title

**Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance.** **Scope locked** (NDF-WP-098, 2026-07-08). Foundation 0.7 is locked, **not released**, **not v1.0**, and **no v1.0 release candidate**.

## DE – Gesperrter Kernfokus

Je ein Kern-Deliverable pro Titel-Hälfte: **Compatibility Governance → WP-100** (v1.x-Kompatibilitätszusage entwerfen — das letzte klar `not met` v1.0-blocking-Kriterium), **v1.0 Path Consolidation → WP-101** (Konventions-Stabilität über 0.4→0.6 bestätigen — aktuell `partially met`). Dazu die überfällige **WP-099**-Entscheidung (Checklist DE/EN — kein viertes stilles Verschieben). Foundation 0.7 **konsolidiert den v1.0-Pfad**, behauptet aber keine v1.0-Reife.

## EN – Locked Core Focus

One core deliverable per title half: compatibility governance → WP-100 (draft the v1.x compatibility promise — the last clearly `not met` blocking v1.0 criterion); v1.0 path consolidation → WP-101 (confirm convention stability across 0.4→0.6 — currently `partially met`). Plus the overdue WP-099 decision (checklist DE/EN — no fourth silent deferral). Foundation 0.7 **consolidates the v1.0 path** but claims no v1.0 maturity.

## DE – Release-blocking Work Packages

Nur diese WPs blockieren den Release:

| WP | Titel | Begründung |
|---|---|---|
| NDF-WP-098 | Scope Lock | Gate — abgeschlossen mit diesem Dokument |
| NDF-WP-099 | Checklist DE/EN Decision | Entscheidungs-WP; die seit 0.4 mehrfach offene Frage wird verbindlich entschieden (Korridor unten) — **entschieden am 2026-07-08: Option B (optional mit finaler Begründung)**, `FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md` |
| NDF-WP-100 | v1.x Compatibility Policy Decision / ADR-0031 Preparation | Kern Compatibility Governance; schließt das letzte klar `not met` v1.0-Kriterium (Entscheidungspfad unten) |
| NDF-WP-101 | Project Adapter Convention Stability Review | Kern v1.0 Path Consolidation; hebt das Stabilitäts-Kriterium Richtung `met with notes` |
| NDF-WP-104 | Release Readiness Review | Gate; entscheidet zugleich über ein etwaiges WP-102-Ventil |
| NDF-WP-105 | Release Prep | Gate |

## EN – Release-Blocking Work Packages

Only WP-098 (this gate), WP-099 (checklist decision), WP-100 (v1.x compatibility policy / ADR-0031), WP-101 (convention stability review), WP-104 (readiness review) and WP-105 (release prep) block the release.

## DE – Optionale Work Packages

Should-have, blockiert nie; Unerledigtes wird ehrlich in Release Notes und Matrix geführt:

- NDF-WP-102 – External Validation Evidence Depth Pass (mit Upgrade-Ventil, siehe unten)
- NDF-WP-103 – Academy Entry Decision
- Kleine Doku-/i18n-Konsolidierung

## EN – Optional Work Packages

WP-102 (external validation evidence depth pass, with upgrade valve below), WP-103 (academy entry decision), small documentation/i18n consolidation. None blocks; unfinished items documented honestly.

## DE – Deferred / Nicht-Ziele

Vollständige Doku-Website; vollständige i18n-Abdeckung; v1.0 Release Candidate; großer Framework-Rewrite; neue Applikations-Features; vollständige ADR-Massenmigration; vollständige externe Zertifizierung. **Manuell/kosmetisch (kein WP, keine GitHub-Schreibaktion):** optionaler v0.6-GitHub-Release-Body-Polish — der Body enthält die Pflichtaussage „This is not a v1.0 release.", ist aber minimal; der Human Maintainer kann ihn optional per Release-Edit erweitern.

## EN – Deferred / Non-Goals

Full documentation website; full i18n; v1.0 release candidate; large rewrite; new application features; full ADR mass migration; full external certification. **Manual/cosmetic (no work package, no GitHub write action):** optional v0.6 GitHub release body polish.

## DE – WP-099 Checklist DE/EN Entscheidungskorridor

WP-099 ist release-blocking und **muss** einen der drei Wege wählen — verbindlich:

- **A) Priorisieren:** Checklist-DE/EN-Arbeit für Foundation 0.7 als release-blocking aufnehmen; ein Folge-WP für die tatsächliche Arbeit darf vorgeschlagen werden.
- **B) Optional mit expliziter finaler Begründung:** als optional behalten, aber mit einer Begründung, die belastbar genug ist, um kein weiteres stilles Verschieben zu erzeugen.
- **C) Streichen mit Begründung:** aus dem Foundation-Pfad entfernen, dokumentiert begründet.

**Ausdrücklich verboten:** stilles Verschieben, viertes leises Weiterschleppen, unklares „später". Die seit 0.4 mitgeschleppte Frage wird in 0.7 entschieden.

## EN – WP-099 Checklist DE/EN Decision Corridor

WP-099 is release-blocking and **must** choose one of three paths: (A) prioritize as release-blocking (a follow-up work package for the actual work may be proposed); (B) keep optional with an explicit final rationale strong enough to prevent further silent deferral; (C) drop from the foundation path with a documented rationale. **Explicitly forbidden:** silent deferral, a fourth quiet carry-over, an unclear "later".

## DE – WP-100 Kompatibilitätspolitik / ADR-0031 Entscheidung

WP-100 ist release-blocking und muss klären: Wird die v1.x-Kompatibilitätszusage als **ADR-0031** vorbereitet oder als Policy-Dokument mit ADR-Verweis? Welche Kompatibilitätsaussagen sind vor v1.0 erlaubt, welche Zusagen bleiben ausdrücklich offen? **Empfehlung dieses Scope Locks:** ADR-0031 ist der bevorzugte Pfad, weil Kompatibilitäts-/Versionierungsregeln dauerhafte Governance-Wirkung haben; WP-100 darf jedoch begründet auf ein reines Policy-Dokument abweichen. **Keine v1.0-Kompatibilitätszusage darf überhöht werden** — der Entwurf bleibt Draft, kein Versprechen. ADR-0031 ist die bestätigte nächste freie ADR-Nummer; die Datei wird **erst in WP-100** erstellt, nicht in diesem WP.

## EN – WP-100 Compatibility Policy / ADR-0031 Decision

WP-100 is release-blocking and must decide whether the v1.x compatibility promise is prepared as **ADR-0031** or as a policy document with ADR linkage, which compatibility statements are allowed before v1.0, and which promises stay explicitly open. **Recommendation of this scope lock:** ADR-0031 is the preferred path (compatibility/versioning rules have lasting governance effect); WP-100 may deviate to a policy-only document with a documented stronger reason. **No v1.0 compatibility promise may be overclaimed** — the draft stays a draft. ADR-0031 is the confirmed next free number; the file is created **only in WP-100**, not here.

## DE – WP-102 External Validation Evidence Depth

WP-102 bleibt **optional, nicht release-blocking**. Begründung: WP-088 hat External Validation bereits auf `met with notes` gehoben; vollständige per-Schritt-Belege wären wertvoll, hängen aber an der Verfügbarkeit eines detaillierten Independent Validators und dürfen Foundation 0.7 nicht blockieren. **PSV-001 bleibt v1.0-tracked, aber non-blocking für 0.7.**

**Upgrade-Ventil:** WP-102 darf **nur** per ausdrücklichem Human-Maintainer-Scope-Change-Vermerk auf release-blocking hochgestuft werden, und nur wenn (a) ein detaillierter Independent Validator früh genug verfügbar ist und (b) die Hochstufung den gesperrten Kern-Scope nicht gefährdet. Ohne diesen Vermerk bleibt WP-102 optional.

## EN – WP-102 External Validation Evidence Depth

WP-102 stays **optional, not release-blocking**: WP-088 already lifted external validation to `met with notes`; full per-step evidence would be valuable but depends on independent reviewer availability and must not block Foundation 0.7. **PSV-001 remains v1.0-tracked but non-blocking for 0.7.** **Upgrade valve:** WP-102 may be upgraded to release-blocking **only** via an explicit human-maintainer scope-change note, and only if a detailed independent validator is available early enough and the upgrade does not endanger the locked core scope.

## DE – Change Control nach Scope Lock

Nach NDF-WP-098 gilt:

- **Kein neues release-blocking WP** ohne ausdrücklichen Scope-Change-Vermerk (kleines Nova-(ChatGPT)-Review + Human-Maintainer-Freigabe).
- **Keine stille Scope-Erweiterung, kein Feature Creep.**
- **Kein v1.0-Claim.**
- **Keine Release Prep vor WP-104.**
- **Verbindlich unzulässig:** stilles Verschieben der WP-099-Entscheidung; Tagging/Release durch den Implementation Agent.
- Redaktionelle Korrekturen (Tippfehler, Links, Statusklarstellungen) sind keine Scope-Änderung.

## EN – Change Control After Scope Lock

No new release-blocking work package without an explicit scope-change note (small Nova (ChatGPT) review + human-maintainer approval); no silent scope expansion or feature creep; no v1.0 claim; no release prep before WP-104; forbidden: silently deferring the WP-099 decision, tagging/releasing by the Implementation Agent. Editorial fixes are not scope changes.

## DE – v1.0-Abgrenzung

Foundation 0.7 **reduziert v1.0-Unsicherheit und konsolidiert den Pfad**, behauptet aber keine v1.0-Reife. Auch wenn WP-100 und WP-101 offene v1.0-Kriterien schließen oder entwerfen: Kein 0.7-Dokument darf v1.0 als erreicht darstellen. Ob und wann v1.0 kommt, entscheidet ausschließlich ein späterer eigener v1.0-Zyklus (Scope Lock → Readiness → Prep → Maintainer-Freigabe). Der Human Maintainer bleibt finaler Release-Owner; Nova (ChatGPT) plant und reviewt; der Implementation Agent implementiert nur beauftragte WPs.

## EN – v1.0 Boundary

Foundation 0.7 **reduces v1.0 uncertainty and consolidates the path** but claims no v1.0 maturity. Even where WP-100/101 close or draft open v1.0 criteria, no 0.7 document may present v1.0 as reached. A v1.0 release is decided solely by a later dedicated v1.0 cycle. The human maintainer stays final release owner; Nova (ChatGPT) plans and reviews; the Implementation Agent implements only commissioned work packages.

## DE – Public Quality Gate und Neutralität

Der Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante über alle 0.7-WPs — zuletzt in WP-089 mit Evidence-Level strong bestätigt. Keine privaten Projekt-/Personennamen, keine Reviewer-Identitäten, keine Kontaktwege, keine echten Domains, keine Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden).

## EN – Public Quality Gate and Neutrality

The public quality gate v0.2 stays a mandatory invariant across all 0.7 work packages (last confirmed at evidence level strong in WP-089). No private project/person names, reviewer identities, contacts, domains, or secret values (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed).

## DE – Nächster Schritt

**NDF-WP-099 – Checklist DE/EN Decision** (parallel möglich: WP-100 v1.x Policy / ADR-0031, WP-101 Convention Stability). Kein anderes inhaltliches WP vor diesen.

## EN – Next Step

**NDF-WP-099 – Checklist DE/EN decision** (in parallel where useful: WP-100 v1.x policy / ADR-0031, WP-101 convention stability). No other content work package before these.
