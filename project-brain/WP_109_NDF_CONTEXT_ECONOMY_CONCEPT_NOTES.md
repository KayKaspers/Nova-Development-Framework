# Project Brain – WP-109 NDF Context Economy Concept Notes

## Summary

Erstes inhaltliches Foundation-0.8-Deliverable erstellt: **NDF Context Economy** als offizielles, public-neutrales NDF-Arbeitsprinzip (`docs/agent-workflows/NDF_CONTEXT_ECONOMY.md`, DE/EN). Nur Konzept + Regeln — konkrete Templates/Prompt-Mode-Vorlagen folgen in WP-113, Skills in WP-111/112. Kein Skill Pack/Script/`.claude/skills`. Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

0.8 Scope Lock/Plan/Queue/Criteria, NEXT_PHASE_0_8, WP-108-Brain-Notiz; README, CHANGELOG, V1_0_PATH_SUMMARY, ADR-0031. Gezielte Greps (Context Economy/Compact Context Summary/Context Pack/Prompt Mode/Nova) — Begriffe bisher nur in den 0.8-Dokumenten. Gate strict/self-test grün, Working Tree sauber (WP-108 `dd4f050`).

## Concept document

`docs/agent-workflows/NDF_CONTEXT_ECONOMY.md` (neuer Ordner `docs/agent-workflows/`): Zweck, Definition, Grundprinzipien (Context Economy ≠ weniger Sorgfalt/Security/Review/Gate/Doku), Kontext-Schichten, Compact Context Summary, Context Packs, Prompt Modes, Rollenmodell, Sicherheits-/Neutralitätsgrenzen, was nicht reduziert werden darf, Anwendung in WPs, Beziehung zu Claude Skills, Beziehung zu Foundation 0.8, Nicht-Ziele, nächste Schritte.

## Context layers

Fünf Schichten (je Zweck/Quellen/einschließen/nicht einschließen/Spar-Effekt/Leitplanke): L1 Durable Rules, L2 Phase Context, L3 Work Package Context, L4 Evidence Context, L5 Output Summary. Leitplanken verhindern Kürzen von Security/Neutralität/Evidenz/harten Grenzen.

## Compact Context Summary

Verbindlich als offizieller Handover-Baustein am WP-Ende definiert: 5–10 Zeilen; letzter WP-Status, Entscheidung/Ergebnis, nächste Aktion, Notes/Risiken; keine privaten Daten; keine Chain-of-Thought; Teil der Rückmeldung an Nova; in Context Packs übernehmbar. Neutrales Mini-Beispiel enthalten (nur öffentliche NDF-Platzhalter WP-XXX/WP-YYY).

## Context Packs

Nur konzeptionell (Templates in WP-113). Soll-Inhalt: Phasenstatus, letztes/nächstes WP, blocking/optional/deferred WPs, relevante ADRs, Notes/Limitations, Sicherheitsgrenzen, Quelldateien, kompakte Kontext-Historie. Nicht-Inhalt: private Daten, Secrets, Roh-Chatlogs, Chain-of-Thought, riesige Kopien, externe Skill-Inhalte, ungeprüfter Drittanbieter-Text. Mögliche Dateinamen nur als Konzept genannt, **nicht erstellt**.

## Prompt Modes

Drei Größen konzeptionell (Templates in WP-113): **Full** (Scope Lock, ADR, Release Prep/Readiness, Security Policy, gefährliche/irreversible/governance-relevante Entscheidungen), **Standard** (normale WPs, Doku-Reviews, kleine Updates), **Short** (standardisierte Folgearbeit nach Context Pack, kleine Update-WPs, wiederkehrende Checks). Grenze: Short **nie** für Security Policy/ADR/Scope Lock/Release/destructive/Git-Write-Release-Tag/unklare Anforderungen.

## Relationship to Claude Skills

Skills = späteres Enablement; **kein Skill in diesem WP**. Skills lagern Standardregeln aus, dürfen keine autonomen Schreib-/Release-Aktionen ermöglichen, müssen Skill Security Policy (WP-110) respektieren; MVP Design WP-111, Implementierung WP-112 optional. MVP-Skill-Set nur referenziert (nicht aktiv).

## Safety boundaries

Gate + Neutralität Pflicht; keine Secrets/privaten Daten/Roh-Chat/Chain-of-Thought/Drittanbieter-Skill-Import; keine autonome Commit-/Push-/Tag-/Release-Aktion; Human Maintainer finale Kontrolle; Short Prompts umgehen keine Sicherheitsprüfungen; Token-Sparen entfernt nie erforderliche Evidenz.

## Foundation 0.8 updates

WP-109 in Queue/Criteria/Plan als erledigt markiert; WP-110 (Skill Security Policy / ADR-0032) als nächster release-blocking Schritt; WP-112 bleibt optional. README (DE/EN): Link auf Context Economy im Standard-Workflow. CHANGELOG: WP-109-Zeile. NEXT_PHASE_0_8: WP-110 als nächster Schritt.

## What was not done

Keine Skills/`.claude/skills`/Cursor-Rules/Workflows/Scripts; keine Context-Pack-Datei; keine Prompt-Templates (WP-113); kein ADR-0032 (WP-110); kein Commit/Push/Tag/Release; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt.

## Risks

Gering: Abgrenzung zu WP-113 (Templates) und WP-111 (Skills) muss sauber bleiben — im Dokument mehrfach explizit als „Konzept, Templates/Skills später" markiert. „Short Prompt" könnte als Sicherheits-Shortcut missverstanden werden → ausdrückliche Verbotsliste. Kein weiteres Risiko.

## Recommendation

**GO WITH NOTES** — Konzept sauber und neutral; bewusste Note: konkrete Templates/Prompt-Mode-Vorlagen bleiben WP-113 vorbehalten, Skills WP-111/112.

## Compact Context Summary

Foundation 0.8 (scope-locked, Agent Enablement & Context Economy). **WP-109 done:** `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md` (DE/EN) definiert Context Economy als NDF-Prinzip — 5 Kontext-Schichten (Durable Rules/Phase/WP/Evidence/Output Summary), Compact Context Summary als verbindlicher Handover (5–10 Zeilen, keine CoT/privaten Daten), Context Packs + Full/Standard/Short Prompt Modes nur konzeptionell (Templates in WP-113), Beziehung zu Skills (WP-111/112), Sicherheitsgrenzen (keine autonome Git-/Release-Aktion, Gate Pflicht). Kein Skill Pack erstellt. Release-blocking done: 108/109. Nächster Schritt WP-110 (Skill Security Policy / ADR-0032). WP-112 optional. Nächste freie ADR-Nummer 0032. Kein Release, kein v1.0.
