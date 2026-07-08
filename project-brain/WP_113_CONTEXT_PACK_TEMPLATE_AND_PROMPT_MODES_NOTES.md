# Project Brain – WP-113 Context Pack Template and Prompt Modes Notes

## Summary

Konkrete Context-Economy-Vorlagen erstellt: **Prompt Modes** (`docs/agent-workflows/NDF_PROMPT_MODES.md`, Full/Standard/Short mit Auswahl- und Verbotsregeln), **Context Pack Template** (`project-brain/CONTEXT_PACK_TEMPLATE.md`, inkl. Rückmeldung-an-Nova-Struktur) und ein erstes **Foundation-0.8 Context Pack** (`project-brain/CONTEXT_PACK_FOUNDATION_0_8.md`) als aktuelle Anwendung. Setzt WP-109 praktisch um, ADR-0032-konform. **Keine aktiven Skills.** Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

0.8 Scope Lock/Plan/Queue/Criteria, Context Economy (WP-109), Skill Security Policy + ADR-0032 (WP-110), Skills MVP Design (WP-111), NEXT_PHASE_0_8, WP-109/110/111-Brain-Notizen, README, CHANGELOG. Gate strict/self-test grün, Working Tree sauber (WP-111 `af6979c`).

## Prompt Modes

`NDF_PROMPT_MODES.md` (DE/EN, Accepted): **Full** (Scope Lock, ADR, Security Policy, Release Readiness/Prep, gefährliche/governance-relevante Entscheidungen), **Standard** (normale WPs, Doku-Reviews, kleine Updates), **Short** (standardisierte Folgearbeit mit aktuellem Context Pack). Auswahlregeln + Verbotsliste (Short nie für Security Policy/ADR/Scope Lock/Release/destructive/Git-Write/Tag-Release/unklare Anforderungen). Grundprinzip: Modus bestimmt Kontextmenge, nie Sorgfalt; im Zweifel größerer Modus. Keine Chain-of-Thought.

## Context Pack Template

`CONTEXT_PACK_TEMPLATE.md`: Status/Scope/Phase/Phasenstatus/letztes+nächstes WP/blocking+optional+deferred WPs/relevante ADRs/Sicherheitsgrenzen/Notes/Quelldateien/Compact Context History/Next Prompt Recommendation/What-Must-Not-Be-Claimed/What-Must-Not-Be-Included/Update Rules. Regeln: nur geprüfte öffentliche Repo-Inhalte; keine privaten Daten/Secrets/Roh-Chatlogs/Chain-of-Thought/externen Skill-Inhalte/riesigen Kopien; ersetzt nicht Datei-Prüfung/Gate/Human-Review.

## Foundation 0.8 Context Pack

`CONTEXT_PACK_FOUNDATION_0_8.md` als erste echte Anwendung: 0.7 released, 0.8 scope-locked/nicht released/nicht v1.0; release-blocking 108-111/113 done, 114/115 open; WP-112 optional not activated, 116/117/118 optional; ADR-0031+0032 Accepted, nächste 0033; Sicherheitsgrenzen (fail closed, docs-only, keine autonomen Git-/Release-Aktionen, Human-Kontrolle); Compact Context History (WP-109..113); Next Prompt Recommendation Full für WP-114. Nur öffentliche NDF-Daten.

## Rückmeldung an Nova structure

In das Context Pack Template integriert (kein Extra-Dokument): Standardabschnitte Zusammenfassung / Geänderte Dateien / Entscheidung-Ergebnis / Quality Gate / Public Neutrality / Risiken / Empfehlung an Nova / Commit-Message / Compact Context Summary. Kompakt, ohne Chain-of-Thought.

## Security boundaries

Public Quality Gate + Public Neutrality in jedem Modus Pflicht; kein Modus umgeht Human-Maintainer-Gate; keine Secrets/privaten Daten/echten Domains; Secret-Name nennbar, Wert nie; keine Chain-of-Thought; Short Prompt setzt aktuellen Context Pack voraus und überspringt keine Sicherheitsprüfung.

## Relationship to Context Economy

Setzt WP-109 praktisch um: die dort konzeptionell eingeführten Prompt Modes und Context Packs sind jetzt konkrete, nutzbare Vorlagen; Compact Context Summary aus WP-109 fließt als Context-Pack-Input (Compact Context History) ein.

## Relationship to ADR-0032

Prompt Modes und Context Packs sind Dokumentationsregeln, keine Skills. Ein späterer `ndf-token-economy`-Skill könnte die Modus-Auswahl unterstützen, muss aber die Skill Security Policy einhalten. Kein Skill in diesem WP.

## Foundation 0.8 updates

WP-113 in Queue/Criteria/Plan als erledigt; **WP-114 (Release Readiness Review) als nächster release-blocking Schritt**; WP-112 optional. README (DE/EN): Link auf Prompt Modes im Workflow-Abschnitt. CHANGELOG: WP-113-Zeile. NEXT_PHASE_0_8 aktualisiert (inkl. Korrektur einer veralteten ADR-Nummer 0032→0033).

## What was not done

Keine aktiven Skills/`.claude/skills`/`SKILL.md`/Scripts/Cursor-Rules/Workflows/Netzwerk-Tools; keine WP-112-Aktivierung; keine Release Prep/Readiness; kein Commit/Push/Tag/Release; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt; keine Chain-of-Thought/Roh-Chatlogs im Context Pack.

## Risks

Gering: Risiko „Short Prompt als Sicherheits-Shortcut" → explizite Verbotsliste + „im Zweifel größerer Modus" + Gate/Human-Gate in jedem Modus Pflicht. Risiko „Context Pack veraltet" → Update Rules (nach jedem WP aktualisieren) + „ersetzt keine Datei-Prüfung". Alle inhaltlichen 0.8-WPs damit done; WP-114 prüft Release Readiness.

## Recommendation

**GO WITH NOTES** — Vorlagen sauber, neutral und policy-konform; bewusste Note: Foundation 0.8 bleibt unreleased, WP-114 muss Release Readiness prüfen; kein aktives Skill Pack.

## Compact Context Summary

Foundation 0.8 (scope-locked, Agent Enablement & Context Economy). **WP-113 done:** `NDF_PROMPT_MODES.md` (Full/Standard/Short + Verbotsliste), `CONTEXT_PACK_TEMPLATE.md` (inkl. Rückmeldung-an-Nova-Struktur) und `CONTEXT_PACK_FOUNDATION_0_8.md` (erste Anwendung). Setzt Context Economy (WP-109) praktisch um; ADR-0032-konform; keine Chain-of-Thought, keine aktiven Skills. **Alle inhaltlichen release-blocking WPs (108/109/110/111/113) done**; WP-112 optional nicht aktiviert. Nächster Schritt WP-114 (Release Readiness Review, Full Prompt Mode empfohlen), dann WP-115. Nächste freie ADR-Nummer 0033. Kein Release, kein v1.0.
