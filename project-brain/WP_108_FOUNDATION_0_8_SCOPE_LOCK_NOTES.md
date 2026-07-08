# Project Brain – WP-108 Foundation 0.8 Scope Lock Notes

## Summary

Foundation-0.8-Scope verbindlich gelockt: gesperrter Kernfokus **Context Economy + Skill Security + Skills MVP Design**. Release-blocking: 108/109/110/111/113/114/115. **WP-112 (Skills MVP Implementation) bleibt optional (Option A).** Skill Security Policy wird als **ADR-0032 in WP-110** erstellt. Kein Skill Pack/Script/`.claude/skills` in diesem WP. Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

FOUNDATION_0_8_PLAN/WORK_PACKAGES/RELEASE_CRITERIA, NEXT_PHASE_0_8, WP-107-Brain-Notiz; README, CHANGELOG, V1_0_PATH_SUMMARY, 0.7-Release-Notes, ADR-0031, ADR/README (nächste freie Nummer 0032). Gate strict/self-test grün, Working Tree sauber (WP-107 committed als `0b45ffe`).

## Scope decision

Kleiner, sicherer Kern statt Feature-Breite. Design/Security/Concept zuerst; tatsächliche Skill-Implementierung bewusst nachgelagert.

## Release-blocking WPs

108 Scope Lock (Gate, done) · 109 Context Economy Concept (nächster Schritt) · 110 Skill Security Policy / ADR-0032 · 111 Skills Pack MVP Design (nur Design) · 113 Context Pack Template & Prompt Modes · 114 Readiness · 115 Release Prep.

## Optional WPs

112 Skills MVP Implementation (Option A, mit Upgrade-Regel) · 116 Skill-to-Cursor-Export-Assessment · 117 Workflow-Builder-Evaluation · 118 Docs-Polish-Skill-Evaluation.

## Deferred / Non-Goals

Vollständige Automatisierungsplattform; autonome Multi-Agent-Workflows; Scripts in Skills; netzwerkfähige Skills; Git-Schreib-/Release-/Tag-Aktionen durch Skills; Cursor-Rules-Export-Implementierung; Workflow-Implementierung; Drittanbieter-Skill-Import; private projektspezifische Skills; v1.0 RC; Aktivierung der vollen v1.x-Zusage.

## Decision on WP-112

**Option A: optional, nicht release-blocking.** Begründung: reduziert Scope Creep; Security Policy (110) und MVP Design (111) zuerst; keine `.claude/skills` vor der Sicherheitsentscheidung. Upgrade-Regel: nur per ausdrücklichem Human-Maintainer-Scope-Change, und nur wenn 110+111 fertig und die Implementierung strikt docs-only bleibt (keine Scripts/Netz/Git-Writes/Release-Tag/Secrets/privaten Daten; Human-Gates verbindlich). Keine Mischentscheidung.

## Decision on ADR-0032

**ADR-0032 bevorzugter Pfad** für die Skill Security Policy (dauerhafte Governance: Agenten-Grenzen, Tool-/Script-Erlaubnis, Schreibaktionen, Secrets, Public Neutrality, Human-Gates, Release Safety). **Erstellung erst in WP-110**, nicht in WP-108. Nächste freie ADR-Nummer bleibt 0032 bis WP-110.

## Security boundaries

Skills docs-only zuerst; keine Scripts im MVP ohne späteren ausdrücklichen Scope-Change; keine Netzwerkzugriffe; keine Git-Schreib-/Release-/Tag-Aktionen; keine Secrets (Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nennbar, Wert nie); keine privaten Projektdaten; keine Drittanbieter-Skill-Inhalte/Branding; Public Quality Gate v0.2 Pflicht; jeder WP-bezogene Skill unterstützt Rückmeldung an Nova + Compact Context Summary. Human Maintainer bleibt finaler Owner.

## Change control

Kein neues release-blocking WP ohne expliziten Scope-Change; keine Skills-Implementierung vor abgeschlossener Security Policy (WP-110); keine Scripts ohne spätere ausdrückliche Entscheidung; keine Netz/Git-Writes/Release-Tag durch Skills; kein Drittanbieter-Skill-Import; optionale WPs bleiben optional bis Human-Maintainer-Upgrade; keine stille Scope-Erweiterung; kein v1.0-Claim; keine Release Prep vor WP-114; redaktionelle Korrekturen sind keine Scope-Änderung.

## Impact on v1.0 path

Foundation 0.8 ist **kein v1.0-Schritt** und adressiert kein offenes v1.0-Kriterium direkt; es verbessert die Arbeitsweise (Effizienz, Skill-Governance). V1_0_PATH_SUMMARY DE+EN aktualisiert (0.8 scope-locked, kein v1.0-Schritt). Kein v1.0-Claim, keine aktive volle v1.x-Zusage.

## What was not done

Keine Skills/`.claude/skills`/Cursor-Rules/Workflows/Scripts erstellt; kein ADR-0032 (erst WP-110); keine Drittanbieter-Skills importiert; kein Commit/Push/Tag/Release; keine CI-/Script-Änderung; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt.

## Risks

Scope Creep (Kandidatenliste) → blocking Kern klein gehalten, WP-112 optional. Skill-Security-Risiko → Security Policy (WP-110/ADR-0032) fail closed, docs-only zuerst. Missverständnis „Skill Pack existiert" → überall als geplant/designt markiert. Ein-Personen-Engpass unverändert.

## Recommendation

**GO WITH NOTES** — Scope sauber gelockt; bewusste Notes: WP-112 bleibt optional, ADR-0032 erst in WP-110.

## Compact Context Summary

Foundation 0.8 **scope-locked** (WP-108, 2026-07-08): Kern Context Economy + Skill Security + Skills MVP Design. Release-blocking 108/109/110/111/113/114/115; **WP-112 Skills MVP Implementation optional (Option A, Upgrade-Regel)**; 116/117/118 optional; Automatisierung/Scripts/Netz/Git-Writes/Drittanbieter-Skills deferred. **ADR-0032 (Skill Security Policy) wird in WP-110 erstellt**; nächste freie ADR-Nummer bleibt 0032. Security: Skills docs-only zuerst, keine Git-/Release-/Netz-/Secret-Zugriffe, Human-Gates. 0.7 released (`v0.7.0-foundation`). Nächster Schritt: WP-109 Context Economy Concept. Kein Release, kein v1.0, kein Skill Pack erstellt.
