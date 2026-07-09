# NDF Skills MVP Implementation Decision

## DE – Zweck

Dokumentierte Entscheidung (NDF-WP-124, Full Prompt Mode), ob und wie eine spätere docs-only Skills-MVP-Implementierung im NDF weiterverfolgt werden soll. Geprüft wurden das [Skills MVP Design](NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md) (WP-111) gegen [ADR-0032](../adr/ADR-0032-skill-security-policy.md) / die [Skill Security Policy](NDF_SKILL_SECURITY_POLICY.md) sowie die Adoption- (WP-122) und Validation-Evidence (WP-123). **Dieses WP entscheidet nur — es implementiert nichts.**

## EN – Purpose

Documented decision (NDF-WP-124, Full Prompt Mode) on whether and how a later docs-only skills MVP implementation should be pursued in NDF. The skills MVP design (WP-111) was checked against ADR-0032 / the skill security policy, together with the adoption (WP-122) and validation evidence (WP-123). **This WP decides only — it implements nothing.**

## DE – Status

Foundation 0.9 ist scope-locked (NDF-WP-121), **nicht released**, **nicht v1.0**, validation-first. Artefakt-Prüfung bestätigt: kein aktives Skill Pack, kein `.claude`-Verzeichnis, keine `SKILL.md`, keine neuen Skill-Scripts. Dieses WP erstellt keine Skills, keine `.claude/skills`, keine Scripts.

## EN – Status

Foundation 0.9 is scope-locked (NDF-WP-121), **not released**, **not v1.0**, validation-first. Artifact check confirms: no active skill pack, no `.claude` directory, no `SKILL.md`, no new skill scripts. This WP creates no skills, `.claude/skills`, or scripts.

## DE – Entscheidung

**Option B – Blueprint-first, implementation-not-activated.**

- **WP-125 (Skills MVP Implementation Blueprint) darf als optionaler / bedingter Blueprint-Schritt empfohlen werden.** Es bleibt optional/conditional und wird durch diese Entscheidung **nicht** aktiviert — der Human Maintainer entscheidet separat, ob WP-125 überhaupt gestartet wird.
- **WP-129 (Docs-only Skills MVP Implementation) bleibt optional, nicht release-blocking und wird durch diese Entscheidung nicht aktiviert.**
- Es wird **kein** aktives Claude Skills Pack erstellt; **kein** `.claude/skills`-Verzeichnis; **keine** `SKILL.md`-Dateien; **keine** Skill-Scripts.
- Jede künftige Implementierung erfordert einen **ausdrücklichen Human-Maintainer-Scope-Change** und muss **ADR-0032** einhalten.
- Der nächste release-blocking Schritt bleibt **NDF-WP-126 – Adoption Evidence and v1.0 Path Review**.

## EN – Decision

**Option B – Blueprint-first, implementation-not-activated.** WP-125 may be recommended as an optional / conditional blueprint step; it stays optional/conditional and is **not** activated by this decision — the Human Maintainer decides separately whether WP-125 is started at all. WP-129 remains optional, not release-blocking, and not activated by this decision. No active Claude Skills Pack is created; no `.claude/skills` directory; no `SKILL.md` files; no skill scripts. Any future implementation requires an explicit Human Maintainer scope change and must comply with ADR-0032. The next release-blocking step stays **NDF-WP-126 – Adoption Evidence and v1.0 Path Review**.

## DE – Entscheidungsoptionen

Geprüft wurden vier Optionen:

- **Option A – Defer Skills Implementation:** keine WP-125-/WP-129-Empfehlung; Skills bleiben Design-only. *Verworfen:* zu konservativ — die Evidenz (vollständiges ADR-0032-konformes Design, positive Adoption/Validation) rechtfertigt den nächsten Vorbereitungsschritt.
- **Option B – Blueprint-first, implementation-not-activated:** **gewählt** (Begründung unten).
- **Option C – Recommend later docs-only Implementation path:** verworfen — würde eine Implementierung vorab empfehlen, bevor ein Blueprint existiert; das ginge über die Evidenz hinaus und erhöhte das Scope-Creep-Risiko ohne Nutzen.
- **Option D – Stop Skills path:** verworfen — es gibt keine Sicherheits-, Neutralitäts- oder Governance-Blocker; ADR-0032 und die Policy sind klar und bindend.

## EN – Decision Options

Four options were evaluated: **A (defer)** — rejected as overly conservative given the evidence; **B (blueprint-first)** — **chosen** (rationale below); **C (recommend later implementation path)** — rejected because it would pre-endorse implementation before a blueprint exists, exceeding the evidence and raising scope-creep risk without benefit; **D (stop)** — rejected because no security, neutrality, or governance blockers exist.

## DE – Begründung

1. **Das Design ist tragfähig, aber es ist ein Design.** Das Skills MVP Design (WP-111) spezifiziert sechs Skills mit Zweck, Grenzen und Review Matrix — es spezifiziert jedoch nicht das konkrete Datei-Layout, die exakten Regeltexte pro Skill oder den Review-/Abnahmeprozess einer Implementierung. Genau diese Lücke schließt ein Blueprint (WP-125).
2. **Implementierung ohne Blueprint wäre unnötiges Risiko.** ADR-0032 ist fail closed; eine direkte Implementierung müsste Sicherheitsentscheidungen implizit treffen, die ein Blueprint explizit und reviewbar macht.
3. **Die Evidenz trägt den Blueprint-Schritt, nicht mehr.** Adoption (WP-122) und Validation (WP-123) belegen, dass die Context-Economy-Grundlagen funktionieren — sie belegen nicht, dass eine Implementierung jetzt nötig ist. Note: der Short Prompt Mode hat noch keinen praktischen Ersteinsatz (PMV-003); auch das spricht für Vorbereitung statt Umsetzung.
4. **Human-Maintainer-Kontrolle bleibt vollständig.** Option B verschiebt keine Entscheidungsmacht: WP-125 startet nur auf ausdrücklichen Wunsch des Human Maintainers, WP-129 bleibt zusätzlich hinter einem separaten Scope-Change-Gate.

## EN – Rationale

(1) The design is sound but is a design — it does not specify the concrete file layout, the exact per-skill rule texts, or the review/acceptance process of an implementation; a blueprint (WP-125) closes exactly this gap. (2) Implementation without a blueprint would create unnecessary risk — ADR-0032 is fail closed, and a direct implementation would make security decisions implicitly that a blueprint makes explicit and reviewable. (3) The evidence supports the blueprint step, not more — adoption (WP-122) and validation (WP-123) prove the context economy foundations work, not that implementation is needed now; the Short Prompt Mode also lacks its first practical use (PMV-003). (4) Human maintainer control stays complete — WP-125 starts only on explicit request, and WP-129 additionally stays behind a separate scope-change gate.

## DE – Decision Matrix / EN – Decision Matrix

| # | Kriterium / Criterion | Status | Nachweis / Evidence |
|---|---|---|---|
| 1 | ADR-0032 allows docs-only, fail-closed skill enablement in principle | **Met** | „Allowed Skill Scope": docs-only/read-only-Vorschläge |
| 2 | ADR-0032 forbids autonomous commit/push/tag/release | **Met** | „Forbidden Skill Capabilities" + „Git and Release Actions" |
| 3 | ADR-0032 forbids network access for MVP skills | **Met** | „Network Access": verboten |
| 4 | ADR-0032 forbids secret processing | **Met** | „Secrets and Private Data" |
| 5 | ADR-0032 forbids private project data | **Met** | „Secrets and Private Data" + Public Neutrality |
| 6 | Skills MVP Design exists and is design-only | **Met** | `NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md`, Pflichtstatus „Design only" |
| 7 | Design does not require scripts for MVP | **Met** | Shared Skill Rules: „keine Scripts" |
| 8 | Design does not require network access | **Met** | Shared Skill Rules: „keine Netzwerkzugriffe" |
| 9 | Design does not require third-party skill import | **Met** | Shared Skill Rules + Non-Goals |
| 10 | Context Economy adoption evidence supports possible future enablement | **Met** | WP-122: GO WITH NOTES, 16-Punkte-Matrix |
| 11 | Prompt Modes / Context Pack validation supports safe handover usage | **Met** | WP-123: GO WITH NOTES, 28-Punkte-Matrix |
| 12 | No active Claude Skills Pack exists | **Met** | Artefakt-Prüfung dieses WP |
| 13 | No `.claude/skills` exists | **Met** | kein `.claude`-Verzeichnis |
| 14 | No `SKILL.md` exists | **Met** | keine getrackte `SKILL.md` |
| 15 | WP-129 is optional and not activated | **Met** | Scope Lock (WP-121) + diese Entscheidung |
| 16 | WP-125 can be useful as blueprint before implementation | **Met** | schließt die Design→Implementierungs-Lücke (Layout, Regeltexte, Review-Prozess) |
| 17 | Implementation without blueprint would create unnecessary risk | **Met** | fail-closed-Prinzip verlangt explizite, reviewbare Sicherheitsentscheidungen |
| 18 | Implementation without Human Maintainer scope change is forbidden | **Met** | Scope Lock Change Control + ADR-0032 |
| 19 | Public Quality Gate remains mandatory | **Met** | strict/self-test grün; Invariante in allen Docs |
| 20 | Human Maintainer final control remains mandatory | **Met** | ADR-0032 „Human Maintainer Gates" |
| 21 | v1.0 is not claimed | **Met** | Kontroll-Greps sauber |
| 22 | Full v1.x compatibility promise is not active | **Met** | ADR-0031: aktiv erst mit v1.0 |
| 23 | Evidence is sufficient to make a decision | **Met** | Design + Policy + Adoption + Validation liegen vollständig vor |
| 24 | Evidence is sufficient for WP-126 to summarize later | **Met with notes** | Entscheidung dokumentiert; Zusammenführung folgt in WP-126 |

## DE – Evidence Summary

Geprüft wurden: das vollständige Skills MVP Design (sechs Skills, Review Matrix, Shared Rules, WP-112/129-Grenze), ADR-0032 + operatives Policy-Dokument (fail closed, Verbotsliste, Human-Gates), das Adoption Review (WP-122: Context Economy praktisch adoptiert) und die Detail-Validierung (WP-123: Prompt Modes/Context Packs valide). Artefakt-Prüfung: kein aktives Skill Pack, keine `.claude/skills`, keine `SKILL.md`, keine neuen Skill-Scripts (die vier Repo-Scripts sind legitimer Altbestand). Das Design benötigt für das MVP weder Scripts noch Netzwerk noch Drittanbieter-Inhalte — es ist vollständig innerhalb der ADR-0032-Grenzen umsetzbar.

## EN – Evidence Summary

Reviewed: the complete skills MVP design (six skills, review matrix, shared rules, WP-112/129 boundary), ADR-0032 + the operative policy document (fail closed, forbidden list, human gates), the adoption review (WP-122) and the detailed validation (WP-123). Artifact check: no active skill pack, no `.claude/skills`, no `SKILL.md`, no new skill scripts (the four repo scripts are legitimate pre-existing tooling). The design requires neither scripts nor network nor third-party content for the MVP — it is fully implementable within the ADR-0032 boundaries.

## DE – Verhältnis zu ADR-0032

ADR-0032 bleibt **bindend und unverändert**: fail closed; nur docs-only/read-only-Hilfen erlaubt; autonome Commit-/Push-/Tag-/Release-Aktionen, Netzwerkzugriffe, Secret-Verarbeitung, private Projektlogik, Drittanbieter-Import, Scripts im MVP und destruktive Aktionen verboten. Diese Entscheidung erweitert den erlaubten Scope **nicht** — sie bestätigt nur, dass ein Blueprint innerhalb dieser Grenzen sinnvoll wäre. Eine Lockerung erfordert weiterhin eine neue ausdrückliche ADR-/Scope-Entscheidung.

## EN – Relationship to ADR-0032

ADR-0032 stays **binding and unchanged**. This decision does **not** extend the allowed scope — it only confirms that a blueprint within these boundaries would be worthwhile. Any relaxation still requires a new explicit ADR/scope decision.

## DE – Verhältnis zu WP-125

**WP-125 wird als optionaler / bedingter Blueprint-Schritt empfohlen** — nicht release-blocking, nicht automatisch aktiviert. Falls der Human Maintainer WP-125 später ausdrücklich startet, ist es ein **Blueprint-only-WP**: konkretes Datei-Layout, exakte Regeltexte pro Skill, Review-/Abnahmeprozess — **keine Implementierung**, keine `.claude/skills`, keine `SKILL.md`, keine Scripts. Der reguläre release-blocking Pfad läuft ohne WP-125 weiter zu WP-126.

## EN – Relationship to WP-125

**WP-125 is recommended as an optional / conditional blueprint step** — not release-blocking, not automatically activated. If the Human Maintainer later explicitly starts WP-125, it is a **blueprint-only WP**: concrete file layout, exact per-skill rule texts, review/acceptance process — **no implementation**, no `.claude/skills`, no `SKILL.md`, no scripts. The regular release-blocking path continues to WP-126 without WP-125.

## DE – Verhältnis zu WP-129

**WP-129 bleibt optional, nicht release-blocking und wird durch diese Entscheidung nicht aktiviert.** Es darf erst nach einer ausdrücklichen Human-Maintainer-Entscheidung gestartet werden — sinnvollerweise nach einem abgeschlossenen WP-125-Blueprint — und muss docs-only bleiben, sofern nicht eine spätere ADR-/Scope-Entscheidung dies ändert. Reihenfolge bleibt: **Entscheidung (WP-124, dieses WP) → ggf. Blueprint (WP-125) → ggf. separate ausdrückliche Aktivierung (WP-129)**.

## EN – Relationship to WP-129

**WP-129 remains optional, not release-blocking, and not activated by this decision.** It may only be started after an explicit Human Maintainer decision — sensibly after a completed WP-125 blueprint — and must stay docs-only unless a future ADR/scope decision changes this. The order stays: **decision (WP-124, this WP) → possibly blueprint (WP-125) → possibly separate explicit activation (WP-129)**.

## DE – Sicherheitsgrenzen

Verbindlich (aus ADR-0032, durch diese Entscheidung unverändert): keine `.claude/skills` in WP-124; keine `SKILL.md` in WP-124; keine Skill-Scripts in WP-124; keine Netzwerkzugriffe; keine Secret-Verarbeitung; keine privaten Projektdaten; keine autonomen Git-/Release-/Tag-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht.

## EN – Security Boundaries

Binding (from ADR-0032, unchanged by this decision): no `.claude/skills` in WP-124; no `SKILL.md` in WP-124; no skill scripts in WP-124; no network access; no secret processing; no private project data; no autonomous git/release/tag actions; no third-party skill import; public quality gate + public neutrality mandatory.

## DE – Human-Maintainer-Gates

Human-Maintainer-only bleiben: der Start von WP-125 (optionaler Blueprint); die Aktivierung von WP-129 (separater Scope-Change); jede Lockerung von ADR-0032 (neue ADR-/Scope-Entscheidung); GO/GO WITH NOTES/REWORK/STOP; Commit, Push, Tag, Release. Weder Nova (ChatGPT) noch der Implementation Agent aktivieren Enablement-Schritte.

## EN – Human Maintainer Gates

Human-maintainer-only: starting WP-125 (optional blueprint); activating WP-129 (separate scope change); any relaxation of ADR-0032 (new ADR/scope decision); GO/GO WITH NOTES/REWORK/STOP; commit, push, tag, release. Neither Nova (ChatGPT) nor the Implementation Agent activates enablement steps.

## DE – Nicht-Ziele

Kein aktives Claude Skills Pack; keine `.claude/skills`; keine `SKILL.md`; keine Skill-Scripts; keine Cursor Rules; keine Workflows; keine Netzwerk-Tools; keine WP-125-/WP-129-Aktivierung durch dieses WP; keine Reaktivierung der 0.8-Optional-WPs (112/116/117/118); kein v1.0-Claim; keine aktive volle v1.x-Kompatibilitätszusage; keine Chain-of-Thought-Dokumentation.

## EN – Non-Goals

No active Claude Skills Pack; no `.claude/skills`; no `SKILL.md`; no skill scripts; no Cursor rules; no workflows; no network tools; no WP-125/WP-129 activation by this WP; no reactivation of the 0.8 optional WPs (112/116/117/118); no v1.0 claim; no active full v1.x compatibility promise; no chain-of-thought documentation.

## DE – Risiken

- **Scope Creep (SKD-005):** Das Hauptrisiko wäre eine Implementierung ohne Human-Maintainer-Scope-Change — durch die klare WP-124→125→129-Reihenfolge, die Change-Control-Regeln des Scope Locks und ADR-0032 mehrfach abgesichert.
- **Fehlinterpretation der Empfehlung:** „WP-125 empfohlen" könnte als „WP-125 aktiviert" gelesen werden — deshalb ist die Nicht-Aktivierung in diesem Dokument, in der Queue und im Context Pack explizit.
- **Blueprint-Verfall:** Falls WP-125 lange nicht gestartet wird, könnte das Design veralten — non-blocking; das Design ist versioniert und würde vor einem Blueprint erneut geprüft.

## EN – Risks

Scope creep (SKD-005) — the main risk would be implementation without a human-maintainer scope change, guarded multiply by the WP-124→125→129 order, the scope lock's change-control rules, and ADR-0032. Misreading the recommendation ("recommended" ≠ "activated") — non-activation is explicit in this document, the queue, and the context pack. Blueprint staleness — non-blocking; the design is versioned and would be re-checked before any blueprint.

## DE – Empfehlung

**GO WITH NOTES.** Entscheidung sauber getroffen (Option B); WP-125 bleibt bewusst optional/Human-Maintainer-abhängig, WP-129 nicht aktiviert; der release-blocking Pfad geht mit WP-126 weiter.

## EN – Recommendation

**GO WITH NOTES.** Decision cleanly made (Option B); WP-125 stays deliberately optional/human-maintainer-dependent, WP-129 not activated; the release-blocking path continues with WP-126.

## DE – Nächster Schritt

**NDF-WP-126 – Adoption Evidence and v1.0 Path Review** (nächster release-blocking Schritt). Optionaler möglicher Zwischenschritt, nur auf ausdrücklichen Human-Maintainer-Wunsch: **NDF-WP-125 – Skills MVP Implementation Blueprint** (Full Prompt Mode wegen Skills-Bezug).

## EN – Next Step

**NDF-WP-126 – Adoption Evidence and v1.0 Path Review** (next release-blocking step). Optional possible interim step, only on explicit Human Maintainer request: **NDF-WP-125 – Skills MVP Implementation Blueprint** (Full Prompt Mode due to skills relevance).
