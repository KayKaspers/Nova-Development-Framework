# Project Brain – WP-124 Optional Skills MVP Implementation Decision Notes

## Summary

Governance-Entscheidung zum Skills-Pfad im Full Prompt Mode getroffen: **Option B — Blueprint-first, implementation-not-activated** (`docs/agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md`, DE/EN). WP-125 wird als optionaler/bedingter Blueprint-Schritt empfohlen, aber **nicht aktiviert**; WP-129 bleibt optional und nicht aktiviert; ADR-0032 unverändert bindend. 24-Punkte-Decision-Matrix (23 Met, 1 Met with notes), keine Blocker. Kein aktives Skill Pack. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

0.9 Scope Lock/Plan/Queue/Criteria, NEXT_PHASE_0_9, Context Pack 0.9, WP-121/122/123-Brain-Notizen; Adoption Review (WP-122) + Validation (WP-123); Context Economy, Prompt Modes, Skill Security Policy, Skills MVP Design; ADR-0031/0032/README; README, CHANGELOG, V1_0_PATH_SUMMARY. Artefakt-Prüfung: kein `.claude`, keine `SKILL.md`, keine neuen Skill-Scripts (4 Repo-Scripts = Altbestand). Gate strict/self-test grün, Working Tree sauber (WP-123 `a229f90`).

## Decision result

**GO WITH NOTES** — Entscheidung sauber; Notes: WP-125/WP-129 bleiben bewusst optional und Human-Maintainer-abhängig.

## Decision option selected

**Option B — Blueprint-first, implementation-not-activated.** A verworfen (zu konservativ angesichts der Evidenz); C verworfen (würde Implementierung vorab empfehlen, bevor ein Blueprint existiert — über die Evidenz hinaus); D verworfen (keine Blocker vorhanden).

## Decision matrix summary

24 Kriterien: **23 Met, 1 Met with notes** (#24 — Zusammenfassung folgt in WP-126). Kernpunkte: ADR-0032 erlaubt docs-only fail-closed Enablement grundsätzlich und verbietet autonome Git-/Netz-/Secret-Aktionen; das MVP-Design ist design-only und braucht weder Scripts noch Netz noch Drittanbieter-Inhalte; Adoption/Validation-Evidence positiv; keine aktiven Skill-Artefakte; WP-129 nicht aktiviert; Implementierung ohne Blueprint = unnötiges Risiko; Implementierung ohne Human-Maintainer-Scope-Change verboten.

## Evidence summary

Design (WP-111, 6 Skills + Review Matrix, ADR-0032-konform), Policy (ADR-0032 + operatives Dokument, fail closed), Adoption (WP-122: 16-Punkte-Matrix positiv), Validation (WP-123: 28-Punkte-Matrix positiv, PMV-003 Short-Prompt-Ersteinsatz offen). Artefakt-Prüfung sauber.

## Relationship to ADR-0032

Bindend und unverändert; diese Entscheidung erweitert den erlaubten Scope nicht — sie bestätigt nur, dass ein Blueprint innerhalb der Grenzen sinnvoll wäre. Lockerung nur per neuer ADR-/Scope-Entscheidung.

## Relationship to WP-125

Als optionaler/bedingter Blueprint-Schritt **empfohlen, nicht aktiviert**; Start nur auf ausdrücklichen Human-Maintainer-Wunsch (dann Full Prompt Mode). Blueprint-only: Datei-Layout, exakte Regeltexte pro Skill, Review-/Abnahmeprozess — keine Implementierung, keine `.claude/skills`/`SKILL.md`/Scripts. Der release-blocking Pfad läuft ohne WP-125 zu WP-126 weiter.

## Relationship to WP-129

Optional, nicht release-blocking, **nicht durch WP-124 aktiviert**; Start erst nach ausdrücklicher Human-Maintainer-Entscheidung (sinnvoll nach WP-125-Blueprint); docs-only, sofern keine spätere ADR-/Scope-Entscheidung anderes erlaubt. Reihenfolge: Entscheidung (124) → ggf. Blueprint (125) → ggf. separate Aktivierung (129).

## Security boundaries

Unverändert aus ADR-0032: keine `.claude/skills`/`SKILL.md`/Skill-Scripts in WP-124; keine Netzwerkzugriffe/Secret-Verarbeitung/privaten Daten; keine autonomen Git-/Release-/Tag-Aktionen; kein Drittanbieter-Import; Gate + Neutralität Pflicht.

## Human Maintainer gates

Human-Maintainer-only: Start von WP-125; Aktivierung von WP-129; jede ADR-0032-Lockerung; GO/GO WITH NOTES/REWORK/STOP; Commit/Push/Tag/Release. Weder Nova (ChatGPT) noch der Implementation Agent aktivieren Enablement-Schritte.

## Findings

SKD-001 (Strength) ADR-0032 liefert klare fail-closed-Grenzen; SKD-002 (Strength) MVP-Design ist mit docs-only Blueprinting kompatibel (keine Scripts/Netz/Drittanbieter nötig); SKD-003 (Note) WP-125 sollte jeder Implementierung vorausgehen; SKD-004 (Note) WP-129 bleibt optional/nicht aktiviert; SKD-005 (Risk) Scope-Creep-Risiko bei Implementierung ohne Human-Maintainer-Scope-Change — mehrfach abgesichert (WP-Reihenfolge, Change Control, ADR-0032). Keine Decision Blocker.

## Foundation 0.9 updates

WP-124 in Queue/Criteria/Plan als Option B erledigt (Plan-Doppelung aus dem Edit direkt bereinigt); WP-125 in Queue als „empfohlen aber nicht aktiviert" präzisiert; **WP-126 als nächster release-blocking Schritt**. NEXT_PHASE_0_9 + Context Pack 0.9 aktualisiert (WP-124 done, WP-126 next, History ergänzt, Next Prompt Recommendation Standard für WP-126 / Full falls WP-125 gewählt). CHANGELOG: WP-124-Zeile. README bewusst unverändert (internes Entscheidungsdokument, über 0.9-Queue erreichbar).

## What was not done

Keine Skills/`.claude/skills`/`SKILL.md`/Skill-Scripts erstellt; WP-125/129 nicht aktiviert; keine 0.8-Optional-WPs reaktiviert; ADR-0032 nicht geändert; kein Commit/Push/Tag/Release; kein v1.0-Claim; keine Chain-of-Thought dokumentiert; Foundation 0.9 nirgends als released dargestellt.

## Risks

SKD-005 (Scope Creep) mehrfach abgesichert; Fehlinterpretation „empfohlen = aktiviert" durch explizite Nicht-Aktivierungs-Aussagen in Dokument/Queue/Context Pack ausgeschlossen; Blueprint-Verfall bei langem Nicht-Start non-blocking (Design versioniert, würde vor Blueprint erneut geprüft).

## Recommendation

**GO WITH NOTES** — Option B sauber entschieden und dokumentiert; bewusste Notes: WP-125 optional/Human-Maintainer-abhängig, WP-129 nicht aktiviert, release-blocking Pfad geht mit WP-126 weiter.

## Compact Context Summary

Foundation 0.9 (scope-locked, validation-first). **WP-124 Optional Skills MVP Implementation Decision: Option B — Blueprint-first, implementation-not-activated** (24-Punkte-Matrix, 23 Met / 1 Met with notes, keine Blocker). WP-125 als optionaler Blueprint empfohlen aber **nicht aktiviert** (Human-Maintainer-Wunsch nötig, dann Full Prompt Mode); WP-129 optional, **nicht aktiviert**; ADR-0032 unverändert bindend; kein aktives Skill Pack, keine `.claude/skills`/`SKILL.md`/Scripts. Release-blocking done: 121/122/123/124. Nächster Schritt WP-126 (Adoption Evidence & v1.0 Path Review, Standard Prompt Mode). Nächste freie ADR-Nummer 0033. Kein Release, kein v1.0.
