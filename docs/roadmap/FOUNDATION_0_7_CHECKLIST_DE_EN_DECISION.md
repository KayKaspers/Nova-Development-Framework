# Foundation 0.7 Checklist DE/EN Decision

## DE – Zweck

Dieses Dokument trifft die verbindliche Foundation-0.7-Entscheidung zum wiederholt offenen Thema **Checklist DE/EN** (NDF-WP-099). Ergebnis: **Option B — optional mit finaler Begründung.** Damit endet das stille Mitführen dieses Themas als ungelöster Foundation-Kandidat.

## EN – Purpose

This document makes the binding Foundation 0.7 decision on the recurring **Checklist DE/EN** topic (NDF-WP-099). Outcome: **Option B — keep optional with an explicit final rationale.** This ends the silent carry-over of the topic as an unresolved foundation candidate.

## DE – Ausgangslage

Das Thema „Checklist DE/EN" wird seit Foundation 0.4 mitgeführt: WP-061 (0.4, optional), WP-075 (0.5, optional), WP-091 (0.6, optional — „zweimal offen"). In jedem Release blieb es optional und wurde nicht umgesetzt. Foundation 0.7 (Scope Lock, WP-098) verbietet ein viertes stilles Verschieben und verlangt in WP-099 eine A/B/C-Entscheidung.

## EN – Background

The "Checklist DE/EN" topic has been carried since Foundation 0.4: WP-061 (0.4), WP-075 (0.5), WP-091 (0.6) — optional each time, never implemented. Foundation 0.7 (scope lock, WP-098) forbids a fourth silent deferral and requires an A/B/C decision in WP-099.

## DE – Scope-Lock-Anforderung

Aus `FOUNDATION_0_7_SCOPE_LOCK.md`: WP-099 muss **genau einen** Weg wählen — **A)** priorisieren (release-blocking), **B)** optional mit expliziter finaler Begründung, **C)** aus dem Foundation-Pfad streichen. Verboten: stilles Verschieben, viertes leises Weiterschleppen, unklares „später".

## EN – Scope Lock Requirement

Per the scope lock: WP-099 must pick **exactly one** path — (A) prioritize as release-blocking, (B) keep optional with an explicit final rationale, (C) drop from the foundation path. Forbidden: silent deferral, a fourth quiet carry-over, an unclear "later".

## DE – Inventur vorhandener Checklisten

| Dokument(e) | Zweck | DE/EN-Abdeckung | Release-Relevanz | v1.0-Relevanz | Lücken-Schwere |
|---|---|---|---|---|---|
| `docs/release/FOUNDATION_0_1..0_6_GO_NO_GO_CHECKLIST.md` | Release-Freigabe | **vollständig DE/EN** (je Release bilingual erstellt) | hoch | mittel | none |
| `framework/checklists/PUBLIC_QUALITY_GATE_CHECKLIST.md` | Neutralitäts-Ritual | DE/EN-Zweck + gemischte Punktliste | mittel | mittel | low |
| `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md` | Adapter-Ausführung | EN-Zweck + DE-Bezug + überwiegend DE-Punkte | mittel (Adoption) | mittel | low–medium |
| `framework/checklists/WORK_PACKAGE_TYPE_CHECKLIST.md`, `AUDIT_PRIVACY`, `OWNER_ONLY_FLOW`, `DESTRUCTIVE_*` (Zweckblock) | Governance/Security | bilingualer Zweck-Block (WP-039), Punktlisten gemischt | mittel | mittel | low |
| `framework/checklists/AGENT_ENDPOINT_DESTRUCTIVE_CHECKLIST.md`, `BACKUP_DELETE_SAFETY_CHECKLIST.md` | tiefe Security-/Destructive-Checks | keine expliziten DE/EN-Marker; überwiegend einsprachig | niedrig (Fach-Tiefe, kein Erstkontakt) | niedrig | info |
| `framework/toolkit/checklists/`, `framework/project-starter/checklists/`, `framework/templates/RELEASE_CHECKLIST_TEMPLATE.md` | Toolkit/Templates | gemischt | niedrig | niedrig | info |
| `docs/i18n/TRANSLATION_STATUS.md` | ehrliche i18n-Matrix | führt `framework/checklists/` als „mixed" | — | — | none (bereits ehrlich dokumentiert) |

**Kernbefund:** Die release-kritischen Go/No-Go-Checklisten sind vollständig zweisprachig. Die operativen `framework/checklists/` haben seit WP-039 bilinguale Zweck-Blöcke; die Punktlisten sind gemischt, aber funktional nutzbar (ein zweisprachiger Nutzer versteht Zweck, Grenzen, Entscheidungswerte). **Keine High-/Blocker-Lücke.** Der Reststand ist in der Translation-Status-Matrix bereits ehrlich als „mixed" geführt.

## EN – Inventory of Existing Checklists

See the table above. **Key finding:** the release-critical go/no-go checklists are fully bilingual; the operational `framework/checklists/` have bilingual purpose blocks since WP-039, with mixed but functionally usable item lists (a bilingual user understands purpose, limits, decision values). **No high/blocker gap.** The remaining state is already tracked honestly as "mixed" in the translation status matrix.

## DE – Bewertete Optionen

- **A) Priorisieren** — nur bei release-relevanter Lücke. Die Inventur zeigt **keine** solche Lücke: Release-Checklisten sind DE/EN, operative Checklisten haben bilinguale Zweck-Blöcke. Eine Voll-Übersetzung aller Punktlisten wäre Scope Creep weg vom gesperrten 0.7-Kern (WP-100/101). → **verworfen.**
- **B) Optional mit finaler Begründung** — passt zum Befund: Verbesserungen sind sinnvoll, aber nicht release-blocking; der 0.7-Kern bleibt auf Compatibility Governance/Convention Stability fokussiert; der Reststand wird ehrlich in der Matrix geführt und nicht mehr automatisch als ungelöster Foundation-Blocker weitergeschleppt. → **gewählt.**
- **C) Streichen** — zu hart: Die Voll-Übersetzung der Punktlisten hat für einen rein englischsprachigen Nutzer echten (wenn auch kleinen) Wert und bleibt ein legitimer i18n-Backlog-Punkt. Streichen würde diesen ehrlichen Reststand verstecken. → **verworfen.**

## EN – Options Considered

(A) Prioritize — only for a release-relevant gap; the inventory shows none, and full item-list translation would be scope creep away from the locked 0.7 core → rejected. (B) Keep optional with final rationale — matches the finding: improvements are worthwhile but not release-blocking, the remaining state is tracked honestly and no longer auto-carried → chosen. (C) Drop — too hard: full item-list translation has real (if small) value for an English-only user and stays a legitimate i18n backlog item → rejected.

## DE – Entscheidung

**Option B — Checklist DE/EN bleibt optional mit finaler Begründung.** Die vollständige DE/EN-Übersetzung der operativen Checklisten-Punktlisten ist **kein Foundation-Release-Blocker** und wird **nicht länger automatisch als ungelöster Foundation-Kandidat weitergetragen**. Der Reststand bleibt ehrlich in `docs/i18n/TRANSLATION_STATUS.md` als „mixed" geführt. Eine spätere Hochstufung ist nur über einen **bewussten neuen Scope** (Nova-(ChatGPT)-Review + Human-Maintainer-Freigabe) möglich, nicht durch stilles Auto-Übernehmen in Foundation 0.8.

## EN – Decision

**Option B — Checklist DE/EN stays optional with a final rationale.** Full DE/EN translation of the operational checklist item lists is **not a foundation release blocker** and is **no longer automatically carried as an unresolved foundation candidate**. The remaining state stays honestly tracked in `docs/i18n/TRANSLATION_STATUS.md` as "mixed". A later upgrade is only possible via a **deliberate new scope** (Nova (ChatGPT) review + human-maintainer approval), not by silent auto-carry into Foundation 0.8.

## DE – Begründung

Repository-Evidenz: (1) alle Go/No-Go-Checklisten (0.1–0.6) sind vollständig bilingual; (2) die 10 `framework/checklists/` tragen seit WP-039 bilinguale Zweck-Blöcke — Zweck, Grenzen und Entscheidungswerte sind für zweisprachige Nutzer erschlossen; (3) `TRANSLATION_STATUS.md` führt den gemischten Punktlisten-Stand bereits ehrlich; (4) die zwei rein einsprachigen Checklisten sind tiefe Security-/Destructive-Werkzeuge, kein Erstkontakt-Material. Damit ist die externe Nutzbarkeit gewährleistet und Foundation 0.7 nicht releasegefährdet. Der wiederholte Auto-Carry war das eigentliche Governance-Problem — Option B beendet ihn, ohne einen ehrlichen i18n-Backlog-Punkt zu verstecken.

## EN – Rationale

Repository evidence: all go/no-go checklists (0.1–0.6) are fully bilingual; the 10 framework checklists carry bilingual purpose blocks since WP-039; the translation status matrix already tracks the mixed item-list state honestly; the two monolingual checklists are deep security/destructive tools, not first-contact material. External usability is ensured and Foundation 0.7 is not release-endangered. The recurring auto-carry was the actual governance problem — Option B ends it without hiding an honest i18n backlog item.

## DE – Auswirkungen auf Foundation 0.7

Checklist DE/EN **blockiert Foundation 0.7 nicht** und war nie release-blocking. Der release-blocking Kern bleibt unverändert: 098 (done), 099 (mit dieser Entscheidung erledigt), 100, 101, 104, 105. Nächster inhaltlicher Schritt: WP-100.

## EN – Impact on Foundation 0.7

Checklist DE/EN **does not block Foundation 0.7** and was never release-blocking. The blocking core is unchanged: 098 (done), 099 (fulfilled by this decision), 100, 101, 104, 105. Next content step: WP-100.

## DE – Auswirkungen auf den v1.0-Pfad

Kein direktes v1.0-blocking Kriterium. Der v1.0-Draft führt „vollständige Zweisprachigkeit der gesamten Bibliothek" bereits ausdrücklich als **nicht erforderlich** (ehrliche Matrix genügt) — diese Entscheidung ist damit konsistent. Keine v1.0-Kriterien werden hier abgehakt.

## EN – Impact on the v1.0 Path

No direct v1.0 blocking criterion. The v1.0 draft already lists "full bilingualism of the entire library" as explicitly **not required** (an honest matrix suffices) — this decision is consistent with that. No v1.0 criteria are checked off here.

## DE – Folgearbeit

**Kein Folge-WP erforderlich.** Optional und ausschließlich über bewussten neuen Scope: eine spätere Punktlisten-DE/EN-Angleichung als eigenständiges i18n-WP. Bis dahin bleibt der Stand in der Translation-Status-Matrix geführt.

## EN – Follow-up Work

**No follow-up work package required.** Optionally, and only via a deliberate new scope: a later item-list DE/EN alignment as a standalone i18n work package. Until then the state stays tracked in the translation status matrix.

## DE – Nicht-Ziele

Keine große i18n-/Checklist-Umsetzung in diesem WP; keine Voll-Übersetzung der Punktlisten; kein neuer release-blocking WP ohne Scope-Change; keine Foundation-0.7-Release-Behauptung; kein v1.0-Claim.

## EN – Non-Goals

No large i18n/checklist implementation in this work package; no full item-list translation; no new release-blocking work package without a scope change; no Foundation 0.7 release claim; no v1.0 claim.

## DE – Nächster Schritt

**NDF-WP-100 – v1.x Compatibility Policy Decision / ADR-0031 Preparation.**

## EN – Next Step

**NDF-WP-100 – v1.x compatibility policy decision / ADR-0031 preparation.**
