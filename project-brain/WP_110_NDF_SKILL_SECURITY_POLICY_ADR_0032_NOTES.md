# Project Brain – WP-110 NDF Skill Security Policy / ADR-0032 Notes

## Summary

Skill Security Policy als Governance-Entscheidung angenommen: **ADR-0032 (Accepted)** + operatives Regelwerk `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md`. Fail-Closed-Prinzip; Skills docs-only zuerst; keine autonomen Git-/Release-/Netz-/Secret-Aktionen; Human-Maintainer-Gates und Public Quality Gate verbindlich. **Kein Skill Pack/Script/`.claude/skills` erstellt.** Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

0.8 Scope Lock/Plan/Queue/Criteria, Context Economy (WP-109), NEXT_PHASE_0_8, WP-108/109-Brain-Notizen; ADR-0031 (Format), ADR-Policy, ADR/README (nächste Nummer 0032 frei), README, CHANGELOG. Gate strict/self-test grün, Working Tree sauber (WP-109 `f1f00ff`).

## Decision: ADR-0032 and policy document

**Option A gewählt:** ADR-0032 dokumentiert die Governance-Entscheidung; das separate `NDF_SKILL_SECURITY_POLICY.md` ist das operative, von WP-111 und optional WP-112 referenzierbare Regelwerk. Begründung: dauerhafte Governance gehört in eine ADR (ADR-Policy), die operative Anwendung braucht ein eigenständiges, verlinkbares Dokument. Keine Mischentscheidung.

## ADR-0032

Status Accepted, 2026-07-08, `docs/adr/ADR-0032-skill-security-policy.md`. Fail-Closed-Prinzip; erlaubter Scope (docs-only, read-only-orientiert, Vorschläge); verbotene Fähigkeiten; Human-Gates; Gate/Neutralität; Secrets/private Daten; Drittanbieter-Skills; Scripts/Netzwerk/Git/Release; destruktive Aktionen; Context-Economy-Beziehung; Rückmeldung an Nova + Compact Context Summary; Change Control; Consequences; Non-Goals; Follow-ups. Pflicht-Non-Goals enthalten (kein aktives Skill Pack, keine Scripts/Netz/autonomen Aktionen, kein Ersatz der Human-Kontrolle, kein v1.0).

## Skill Security Policy

`docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (DE/EN), Status Accepted (WP-110). Gilt für alle künftigen NDF-Skills, auch während WP-112 optional bleibt. Spiegelt ADR-0032 operativ, verlinkt zurück auf ADR-0032 und Context Economy.

## Allowed skill scope

Docs-only, read-only-orientiert: Struktur-/Textvorschläge für WP-Arbeit; Formulierungshilfe für Rückmeldung an Nova + Compact Context Summary; Neutralitäts-/Checklisten-Erinnerungen; Zusammenfassen vorhandener öffentlicher Repo-Inhalte. Skill-Ausgaben sind Vorschläge; Human Maintainer entscheidet/führt aus.

## Forbidden capabilities

Autonome Commits/Pushes/Tags/Releases; GitHub-Release-Erstellung/-Änderung; Netzwerkzugriffe; Secret-Verarbeitung; private Projektlogik; Drittanbieter-Skill-Import; Scripts im MVP; destruktive Aktionen; Umgehung von Gate / Rückmeldung an Nova / Human-Gates.

## Human Maintainer Gates

Human Maintainer bleibt finaler Owner (GO/GO WITH NOTES/REWORK/STOP, Commit, Push, Tag, Release). Skills treffen keine irreversiblen Entscheidungen, lösen keine Git-/Release-Aktionen aus.

## Public Quality Gate / Public Neutrality

Gate v0.2 Pflichtinvariante, von Skills weder umgehbar noch abschaltbar; Skill-Dateien unterliegen ihm. Keine privaten Namen/Reviewer/Kontakte/Domains; Secret-Name nennbar, Wert nie.

## Secrets / private data / third-party skills

Keine Secret-Verarbeitung/-Dokumentation, keine privaten Projektdaten, keine Roh-Chat-Historie, keine Chain-of-Thought; kein ungeprüfter Drittanbieter-Skill-Import; keine externen Branding-/Autorenhinweise.

## Scripts / network / Git / release actions

Scripts verboten bis spätere ausdrückliche ADR-/Scope-Entscheidung (mit Grenzen/Review/Freigabe); Netzwerkzugriffe verboten; Git-Schreib- und Release-/Tag-Aktionen verboten (nur Human Maintainer); destruktive Aktionen verboten.

## Context Economy relationship

Context Economy (WP-109) reduziert unnötigen Kontext, nicht Sicherheit. Short Prompts/Token-Sparen ersetzen/umgehen keine Sicherheitsprüfung, keine erforderliche Evidenz, kein Human-Gate.

## Foundation 0.8 updates

WP-110 in Queue/Criteria/Plan als erledigt; **WP-111 (Skills MVP Design) als nächster release-blocking Schritt**; WP-112 optional. ADR/README: ADR-0032 eingetragen, nächste freie Nummer **0033**. README (DE/EN): Link auf Skill Security Policy im Workflow-Abschnitt. CHANGELOG: ADR-0032- + Policy-Zeile. NEXT_PHASE_0_8 aktualisiert.

## What was not done

Keine Skills/`.claude/skills`/Cursor-Rules/Workflows/Scripts; kein Drittanbieter-Skill-Import; keine Netzwerk-/Secret-Implementierung; kein Commit/Push/Tag/Release; keine CI-Änderung; keine alten ADRs umnummeriert; ADR-0031 unverändert; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt.

## Risks

Gering: Policy ist bewusst restriktiv (fail closed) → wenig Missbrauchsfläche; Lockerung nur per neuer ADR/Scope-Entscheidung. Risiko „Skill Pack existiert bereits" → überall als geplant/future markiert. WP-111 muss das MVP-Design innerhalb dieser Grenzen halten.

## Recommendation

**GO WITH NOTES** — Governance sauber geschaffen; bewusste Note: kein aktives Skill Pack; WP-111 liefert das MVP-Design innerhalb der Policy.

## Compact Context Summary

Foundation 0.8 (scope-locked, Agent Enablement & Context Economy). **WP-110 done:** Skill Security Policy als **ADR-0032 (Accepted)** + operatives `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (DE/EN, Option A). Fail closed; erlaubt nur docs-only/read-only-Vorschläge; verboten: autonome Git-/Release-/Tag-Aktionen, Netzwerk, Secrets, Scripts im MVP, Drittanbieter-Import, Gate-/Human-Gate-Umgehung. Human Maintainer finaler Owner; Gate + Neutralität Pflicht. Kein Skill Pack erstellt. Release-blocking done: 108/109/110. Nächster Schritt WP-111 (Skills MVP Design). WP-112 optional. Nächste freie ADR-Nummer **0033**. Kein Release, kein v1.0.
