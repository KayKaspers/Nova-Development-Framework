# Foundation 0.9 Release Readiness Review

## DE – Status / Ergebnis

Review-Gate (NDF-WP-127, Full Prompt Mode) vor der Release-Vorbereitung von voraussichtlich `v0.9.0-foundation`. **Decision: GO WITH NOTES.** Foundation 0.9 ist bereit für **NDF-WP-128 – Release Prep**; alle release-blocking WPs vor WP-127 sind erfüllt und nachgewiesen, keine Blocker. Foundation 0.9 ist **nicht released**, **nicht v1.0**, **kein v1.0 Release Candidate**; die volle v1.x-Kompatibilitätszusage ist **nicht aktiv**. Es existiert **kein aktives Claude Skills Pack**.

## EN – Status / Result

Review gate (NDF-WP-127, Full Prompt Mode) before the release preparation of presumably `v0.9.0-foundation`. **Decision: GO WITH NOTES.** Foundation 0.9 is ready for **NDF-WP-128 – Release Prep**; all release-blocking WPs before WP-127 are complete and evidenced, no blockers. Foundation 0.9 is **not released**, **not v1.0**, **no v1.0 release candidate**; the full v1.x compatibility promise is **not active**. **No active Claude Skills Pack** exists.

## DE – Geprüfter Scope

Scope Lock (NDF-WP-121) eingehalten: Adoption, Validation & Optional Enablement, validation-first; blocking Kern 121/122/123/124/126/127/128; optional/conditional 125/129/130/131/132; WP-133 nur Post-Release-Kandidat. Kein Scope Creep; WP-125 wurde von WP-124 empfohlen, aber **nicht aktiviert**; WP-129 nicht aktiviert; keine 0.8-Optional-WPs (112/116/117/118) still reaktiviert. Keine falschen Haken in den Release Criteria; 0.9 nirgends als released, v1.0 nirgends als erreicht dargestellt.

## EN – Reviewed Scope

Scope lock honored: validation-first; blocking core 121/122/123/124/126/127/128; optional/conditional 125/129/130/131/132; WP-133 post-release candidate only. No scope creep; WP-125 recommended by WP-124 but **not activated**; WP-129 not activated; no 0.8 optional WPs silently reopened. No false checkmarks; 0.9 nowhere claimed as released, v1.0 nowhere claimed as reached.

## DE – Reviewed Inputs / EN – Reviewed Inputs

Scope Lock, Plan, WP-Queue, 0.9-Release-Criteria, NEXT_PHASE_0_9, Context Pack 0.9; die fünf Evidenz-Dokumente: [Adoption Review](../validation/context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md) (WP-122), [Prompt Modes & Context Pack Validation](../validation/context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md) (WP-123), [Skills MVP Implementation Decision](../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md) (WP-124), [Adoption Evidence & v1.0 Path Review](../validation/foundation-0-9/ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md) (WP-126); ADR-0031/ADR-0032 + ADR-Index; Agent-Workflow-Dokumente (Context Economy, Prompt Modes, Skill Security Policy, Skills MVP Design); README, CHANGELOG, V1_0_PATH_SUMMARY. Quality Gate strict/self-test; Dateisystem-/Artefakt-Prüfung; `git status`/`git diff` zur Selbstprüfung.

## DE – Release Criteria Check / EN – Release Criteria Check

| ID | Criterion | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Foundation 0.9 Scope gelockt (validation-first) | Met | `FOUNDATION_0_9_SCOPE_LOCK.md` (WP-121) |
| 2 | Alle release-blocking WPs vor WP-127 abgeschlossen | Met | 121/122/123/124/126 done, in Criteria abgehakt |
| 3 | WP-121–126 mit Notes korrekt berücksichtigt | Met | Notes in diesem Review übernommen (Known Notes) |
| 4 | Keine offenen Blocker aus den Review-Matrizen | Met | 16-Punkte- (WP-122), 28-Punkte- (WP-123), 24-Punkte- (WP-124), 28-Punkte-Matrix (WP-126): keine „Not met"/Blocker |
| 5 | Known Notes korrekt übernommen | Met | siehe Abschnitt Known Notes |
| 6 | 0.9 nicht als v1.0 / RC / volle v1.x-Zusage dargestellt | Met | Kontroll-Greps sauber; nur Negationen/Abgrenzungen |
| 7 | ADR-0031 und ADR-0032 unverändert respektiert | Met | beide Accepted, unverändert; nächste freie Nummer ADR-0033 |
| 8 | Kein aktives Skill Pack existiert oder wird aktiviert | Met | kein `.claude`, keine `SKILL.md`, keine Skill-Scripts (Artefakt-Prüfung) |
| 9 | WP-125 bleibt optional/conditional | Met | von WP-124 empfohlen, nicht aktiviert; Human-Maintainer-Wunsch nötig |
| 10 | WP-129 bleibt optional/nicht aktiviert | Met | Scope Lock + WP-124-Entscheidung (Option B) |
| 11 | Short-Prompt-Ersteinsatz-Note erhalten | Met with notes | PMV-003: Definition valide, praktischer Ersteinsatz steht aus — Note für WP-128-Release-Notes |
| 12 | Externe Validierungs-Evidenz-Tiefe bleibt v1.0-tracked | Met with notes | evidence-quality note (aus WP-088) unverändert getrackt, nicht künstlich geschlossen |
| 13 | WP-128 als nächster Schritt empfehlbar | Met | keine Blocker; Release Prep kann starten |
| 14 | WP-133 erst nach manuellem Release relevant | Met | Post-Release-Kandidat, nicht vorgezogen |
| 15 | Keine Release-/Tag-/Push-/GitHub-Aktion durch Claude nötig/erlaubt | Met | dieses WP ist docs-only; Grenzen eingehalten |
| 16 | Human Maintainer allein für Commit/Push/Tag/Release | Met | Invariante in allen 0.9-Dokumenten |
| 17 | Public Neutrality eingehalten | Met | Gate strict/self-test grün; Neutralitäts-Greps sauber |
| 18 | Foundation 0.9 bereit für Release Prep | Met | Gesamtergebnis dieses Reviews |

## DE – Work Package Completion Check / EN – Work Package Completion Check

| WP | Status | Ergebnis / Result |
|---|---|---|
| NDF-WP-121 Scope Lock | ✅ done | validation-first; WP-124 blocking-Entscheidung, WP-125 optional/conditional, WP-129 optional/nicht aktiviert |
| NDF-WP-122 Context Economy Adoption Review | ✅ done | **GO WITH NOTES** — 16-Punkte-Matrix (14 Met, 2 Met with notes) |
| NDF-WP-123 Prompt Modes & Context Pack Validation | ✅ done | **GO WITH NOTES** — 28-Punkte-Matrix (27 Met, 1 Met with notes); Short Prompt sicher begrenzt |
| NDF-WP-124 Skills MVP Implementation Decision | ✅ done | **Option B — Blueprint-first, implementation-not-activated** (24-Punkte-Matrix) |
| NDF-WP-126 Adoption Evidence & v1.0 Path Review | ✅ done | **GO WITH NOTES** — 28-Punkte-Matrix; v1.0-Pfad gestärkt, nicht geschlossen |
| NDF-WP-127 Release Readiness Review | ✅ mit diesem Dokument / with this document | — |
| NDF-WP-128 Release Prep | ⬜ offen / open | nächster Schritt nach GO / next step after GO |
| NDF-WP-133 Post-Release Cleanup | ⬜ Kandidat | erst nach manuellem Release relevant |

## DE – Known Notes / EN – Known Notes

Alle non-blocking, für die WP-128-Release-Notes zu übernehmen:

- Foundation 0.9 ist **nicht v1.0** und **kein v1.0 Release Candidate**.
- Die **volle v1.x-Kompatibilitätszusage ist nicht aktiv** (erst mit einem künftigen v1.0-Release; ADR-0031).
- Es gibt **kein aktives Claude Skills Pack**; das Skills-MVP existiert nur als Design.
- **WP-125 bleibt optional/conditional** (von WP-124 empfohlen, Start nur auf ausdrücklichen Human-Maintainer-Wunsch).
- **WP-129 bleibt optional und nicht aktiviert** (separater Human-Maintainer-Scope-Change nötig).
- Der **Short Prompt Mode hat in 0.9 noch keinen praktischen Ersteinsatz** (PMV-003; Definition valide, Beobachtungspunkt).
- Die **externe Validierungs-Evidenz-Tiefe bleibt v1.0-tracked** (evidence-quality note, nicht künstlich geschlossen).
- **WP-133 ist erst nach dem manuellen Release relevant.**
- **Commit/Push/Tag/Release bleiben Human-Maintainer-Aufgabe.**

## DE – ADR / Governance Check

ADR-0031 (v1.x Compatibility Policy) und ADR-0032 (Skill Security Policy) sind Accepted und unverändert; keine ADRs umnummeriert, keine Massenmigration; nächste freie Nummer **ADR-0033** (konsistent im ADR-Index). Change-Control-Regeln des Scope Locks eingehalten: kein neues release-blocking WP, keine stille Scope-Erweiterung, keine Release Prep vor WP-127.

## EN – ADR / Governance Check

ADR-0031 and ADR-0032 are Accepted and unchanged; no renumbering, no mass migration; next free number ADR-0033 (consistent in the ADR index). Scope-lock change-control rules honored.

## DE – Skills / Optional Enablement Check

Artefakt-Prüfung bestätigt: **kein `.claude`-Verzeichnis, keine `.claude/skills`, keine `SKILL.md`, keine neuen Skill-Scripts** (die vier Repo-Scripts sind legitimer Altbestand). WP-124 hat Option B entschieden — die Reihenfolge Entscheidung → ggf. Blueprint (WP-125) → ggf. separate Aktivierung (WP-129) ist verbindlich dokumentiert; nichts davon wurde durch WP-127 aktiviert. ADR-0032 (fail closed) bleibt bindend.

## EN – Skills / Optional Enablement Check

Artifact check confirms: no `.claude` directory, no `.claude/skills`, no `SKILL.md`, no new skill scripts. WP-124 decided Option B — the order decision → possibly blueprint (WP-125) → possibly separate activation (WP-129) is bindingly documented; none of it was activated by WP-127. ADR-0032 (fail closed) stays binding.

## DE – Prompt Modes / Context Economy Check

Adoption (WP-122) und Detail-Validierung (WP-123) positiv: Compact Context Summary als durchgängiger Handover, Context Packs (Template + 0.8-Baseline + 0.9-aktuell) konsistent, Prompt Modes klar begrenzt; Short Prompt mit expliziter Verbotsliste und ohne Gate-/Human-Review-Bypass. Der 0.9-Zyklus selbst nutzte die Modi korrekt (WP-121/124/126/127 Full, WP-122/123 Standard). Note: Short-Prompt-Ersteinsatz steht aus (PMV-003).

## EN – Prompt Modes / Context Economy Check

Adoption (WP-122) and detailed validation (WP-123) positive: Compact Context Summary as consistent handover, context packs consistent, prompt modes clearly bounded; Short Prompt with an explicit forbidden list and no gate/human-review bypass. The 0.9 cycle itself used the modes correctly. Note: first practical Short Prompt use pending (PMV-003).

## DE – v1.0 Path Check

WP-126 hat die Evidence korrekt und ohne Überhöhung eingeordnet: Foundation 0.9 **stärkt** den v1.0-Pfad (Arbeitsweise/Effizienz — Adoption-, Validation- und Decision-Evidence), **schließt ihn aber nicht**. Offene v1.0-Punkte bleiben sichtbar (u. a. externe Validierungs-Evidenz-Tiefe). Kein 0.9-Dokument stellt v1.0 als erreicht, einen RC oder eine aktive volle v1.x-Zusage dar; V1_0_PATH_SUMMARY ist entsprechend fortgeschrieben.

## EN – v1.0 Path Check

WP-126 classified the evidence correctly and without inflation: Foundation 0.9 **strengthens** the v1.0 path (way of working / efficiency) but does **not** complete it. Open v1.0 items stay visible (incl. external validation evidence depth). No 0.9 document presents v1.0 as reached, an RC, or an active full v1.x promise.

## DE – Public Neutrality Check

Public Quality Gate `--strict` und `--self-test` grün; new-file neutrality check aktiv — die in diesem Review erzeugten Dateien wurden mitgescannt. Keine privaten Projekt-/Personennamen, Reviewer-Identitäten, Kontaktwege, echten Domains, Secret-Werte oder privaten Suchmuster; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` wird nur als Name genannt. „chain-of-thought"/„raw chat" kommen ausschließlich als Verbot vor.

## EN – Public Neutrality Check

Public quality gate strict and self-test green; new-file neutrality check active — files created by this review were scanned. No private names, reviewer identities, contacts, real domains, secret values, or private search patterns; the secret name is mentioned as a name only. "chain-of-thought"/"raw chat" appear only as prohibitions.

## DE – Risk / Open Notes

- **Keine Blocker.** Alle Notes sind non-blocking und bewusst (siehe Known Notes).
- WP-128 muss die Known Notes vollständig in die Release Notes übernehmen und Go/No-Go-Checkliste + Tagging-Guide erstellen.
- Der optionale WP-125-Blueprint bleibt jederzeit auf Human-Maintainer-Wunsch startbar, ist aber für die 0.9-Releasefähigkeit nicht erforderlich; sein Auslassen aktiviert WP-129 nicht.
- Context-Pack-Pflege nach jedem WP beibehalten (CPV-002, bisher eingehalten).

## EN – Risk / Open Notes

**No blockers.** All notes are non-blocking and deliberate. WP-128 must carry the known notes into the release notes and create the go/no-go checklist + tagging guide. The optional WP-125 blueprint stays startable on human-maintainer request but is not required for 0.9 release readiness; skipping it does not activate WP-129. Keep context-pack maintenance after each WP (CPV-002).

## DE – Decision / EN – Decision

```text
Decision: GO WITH NOTES
```

Foundation 0.9 ist bereit für die Release-Vorbereitung. Die Prüfung trägt dieses Ergebnis ehrlich: alle fünf inhaltlichen blocking WPs sind mit dokumentierten Matrizen abgeschlossen, keine Matrix enthält „Not met"- oder Blocker-Einträge, alle Invarianten (Gate, Neutralität, Human-Gates, ADR-Grenzen, Skill-Nichtaktivierung) sind verifiziert. / Foundation 0.9 is ready for release preparation; the review honestly supports this result.

## DE – Recommendation for Next Step

**NDF-WP-128 – Foundation 0.9 Release Prep** (Full Prompt Mode; empfohlenes Modell Claude Opus 4.8): Release Notes inkl. aller Known Notes, Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für voraussichtlich `v0.9.0-foundation`. Danach manuell (Human Maintainer): Go/No-Go, Tag, GitHub Pre-Release; anschließend WP-133 Post-Release Cleanup.

## EN – Recommendation for Next Step

**NDF-WP-128 – Foundation 0.9 Release Prep** (Full Prompt Mode; recommended model Claude Opus 4.8): release notes incl. all known notes, criteria completion, go/no-go checklist, tagging guide for presumably `v0.9.0-foundation`. Then manually (Human Maintainer): go/no-go, tag, GitHub pre-release; afterwards WP-133 post-release cleanup.
