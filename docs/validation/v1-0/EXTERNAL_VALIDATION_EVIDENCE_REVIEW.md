# External Validation Evidence Review

## DE – Titel

Review der externen/neutralen Validierungs-Evidenz für den v1.0-Pfad — Bewertung von Gap G-13 (NDF-WP-140, Skill-assisted Full Prompt Mode).

## DE – Status / Ergebnis

**GO WITH NOTES.** **G-13 → Partially closed / remains tracked for RC.** Es existiert echte, unabhängige und neutrale Validierungs-Evidenz (zwei unabhängige Läufe, beide PASS WITH NOTES, keine Blocker/High-Findings), aber mit dokumentierter Begrenzung der Schrittbeleg-Tiefe. **RC-Fähigkeit: RC can proceed with notes** — ein RC darf mit dokumentierter Evidenz-Note vorbereitet werden; ein **v1.0 final** braucht tiefere Evidenz oder eine ausdrücklich dokumentierte Grenze. Keine neue externe Evidenz erfunden. Foundation 0.9 bleibt released/published, **nicht v1.0**, kein RC, keine volle v1.x-Zusage. ADR-0031/0032 unverändert.

## EN – Status / Result

**GO WITH NOTES.** **G-13 → Partially closed / remains tracked for RC.** Genuine independent and neutral validation evidence exists (two independent runs, both PASS WITH NOTES, no blockers/high findings) but with a documented per-step depth limitation. **RC capability: RC can proceed with notes** — an RC may be prepared with a documented evidence note; a **v1.0 final** needs deeper evidence or an explicitly documented boundary. No new external evidence invented. Foundation 0.9 stays released/published, **not v1.0**, no RC, no full v1.x promise. ADR-0031/0032 unchanged.

## DE – Scope

Bewertung von G-13: welche externe/neutralere Validierung existiert, wie belastbar sie ist, ob sie für einen v1.0 RC reicht, ob vor RC/v1.0-final zusätzliche Validierung nötig ist, G-13-Status, und die Vorbereitung der WP-141-Entscheidung. **Nicht im Scope:** neue externe Validierung durchführen, private Projekte/Reviewer-Identitäten als Evidenz, v1.0-Aktivierung/RC, neue/geänderte Skills, Scripts, Netzwerk, Commit/Push/Tag/Release.

## EN – Scope

Assessment of G-13: which external/neutral validation exists, how robust it is, whether it suffices for a v1.0 RC, whether additional validation is needed before RC/v1.0-final, the G-13 status, and preparing the WP-141 decision. Out of scope: performing new external validation, private projects/reviewer identities as evidence, v1.0 activation/RC, new/changed skills, scripts, network, commit/push/tag/release.

## DE – Input Summary

Ausgewertet (read-only, im Repo vorhanden): die zwei unabhängigen Läufe unter `docs/validation/project-adapter/independent-runs/` (2026-07-06 privater Referenzkontext, WP-074; 2026-07-07 öffentliche SampleProject-Runbook-Validierung, WP-088), die [SampleProject Adapter Validation](../project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md) (WP-047, Selbstvalidierung), der Konventions-Stabilitäts-Review (WP-101), die 0.9-Reviews (WP-122/123/126), die Skills-Validationen (WP-129/137/138), der [v1.0 Gap Review](V1_0_GAP_REVIEW_AND_SCOPE_LOCK.md) (WP-139), der [v1.0 Readiness Criteria Draft](../../release/V1_0_READINESS_CRITERIA_DRAFT.md) und die [v1.0 Path Summary](../../roadmap/V1_0_PATH_SUMMARY.md). **Keine erfundene Evidenz; nicht belegte Bereiche werden nicht als geprüft behauptet.**

## EN – Input Summary

Reviewed read-only from the repo: the two independent runs (2026-07-06 private reference, WP-074; 2026-07-07 public SampleProject runbook, WP-088), the SampleProject adapter validation (WP-047, self-validation), the convention stability review (WP-101), the 0.9 reviews (WP-122/123/126), the skills validations (WP-129/137/138), the v1.0 gap review (WP-139), the criteria draft, and the path summary. No invented evidence; unevidenced areas are not claimed as reviewed.

## DE – Evidence-Matrix

Strength: **strong** · **moderate** · **limited** · **weak**. Decision: **counts for v1.0** · **counts with notes** · **insufficient** · **N/A**.

| ID | Evidence Source | Type | Scope | Strength | Limitations | Public-Neutrality | v1.0-Relevanz | Decision |
|---|---|---|---|---|---|---|---|---|
| E-01 | 2026-07-07 Public SampleProject Runbook Validation (WP-088) | independent | öffentlicher Fixture-/Runbook-Pfad | **moderate** | Schrittbeleg-Tiefe begrenzt (PSV-001); Gesamturteil positiv, Einzelschritte „not provided" | neutral (Fixture öffentlich, keine Identität) | hoch (Kern-External-Validation) | **counts with notes** |
| E-02 | 2026-07-06 Private Reference Validation (WP-074) | independent | Struktur/Doku/Sicherheitsmuster | **limited** | summarisch/neutralisiert; privater Referenzkontext (IAV-002); Runbook-Detail nicht belegt | neutralisiert (keine Namen/Domains/Secrets) | mittel (unabhängige Außensicht) | **counts with notes** |
| E-03 | SampleProject Adapter Validation (WP-047) | neutral sample | Adapter gegen neutrales Fixture | moderate | Selbstvalidierung; kein echter Code im Fixture; Monorepo/>10-Teams nicht abgedeckt | neutral | mittel | counts with notes |
| E-04 | Convention Stability Review (WP-101) | release/governance | Konventions-Stabilität über 4 Releases | **strong** | reine Stabilitätsaussage, keine externe Nutzersicht | neutral | mittel–hoch | counts for v1.0 |
| E-05 | Public Quality Gate Maintenance Review (WP-089) | release/governance | Denylist-/Gate-Wirksamkeit | **strong** | betrifft Neutralität, nicht Adoption | neutral (Secret-Name only) | mittel | counts for v1.0 |
| E-06 | Context Economy Adoption Review (WP-122) | adoption | interne Adoption der 0.9-Artefakte | moderate | interne Sicht | neutral | mittel (Arbeitsweise) | counts with notes |
| E-07 | Prompt Modes & Context Pack Validation (WP-123) | internal | Prompt-Modes/Context-Packs | moderate | Selbstvalidierung | neutral | mittel | counts with notes |
| E-08 | Skill Real-use Validation (WP-138) | internal | Skill-Pack Prompt-Kompression | moderate | strukturell/erfahrungsbasiert, keine Token-Instrumentierung | neutral | mittel (Arbeitsweise) | counts with notes |
| E-09 | Adoption Evidence & v1.0 Path Review (WP-126) | internal | Zusammenführung 0.9-Evidence | moderate | konsolidiert, keine neue externe Evidenz | neutral | mittel | counts with notes |

**Zusammenfassung:** strong 2 (E-04, E-05) · moderate 5 · limited 1 (E-02) · weak 0 · insufficient 0. **Wichtigste Evidence:** E-01 (öffentlicher unabhängiger Runbook-Lauf) + E-04 (Konventions-Stabilität). **Wichtigste Limits:** Schrittbeleg-Tiefe (E-01/E-02) und Selbstvalidierungsanteil (E-03/E-07/E-08).

## EN – Evidence Matrix

The table rates nine evidence sources by type, scope, strength (strong/moderate/limited/weak), limitations, public-neutrality, v1.0 relevance, and decision (counts for v1.0 / counts with notes / insufficient / N/A). Summary: 2 strong (convention stability, gate maintenance), 5 moderate, 1 limited (private reference run), none weak/insufficient. Strongest adoption-facing evidence: the public independent runbook run (E-01); key limits: per-step evidence depth and the self-validation share.

## DE – G-13-Bewertung

**G-13 – External Validation Evidence Depth → Partially closed / remains tracked for RC.**

- **Begründung:** Es gibt **zwei echte unabhängige Läufe** (E-01 öffentlich, E-02 privat-neutralisiert), beide PASS WITH NOTES ohne Blocker/High-Findings — das ist mehr als „open" und belegt eine reale Außensicht. Aber die **Schrittbeleg-Tiefe** bleibt begrenzt (PSV-001/IAV-001) und ein Lauf war privat-kontextuell — daher **nicht** „Closed".
- **Vor RC nötig:** nein (RC can proceed with notes; s. u.). **Vor v1.0 final nötig:** ja — entweder ein tieferer, schrittbelegter öffentlicher Lauf **oder** eine ausdrücklich dokumentierte Grenze im finalen v1.0 Scope Lock.
- **Keine erfundene Evidenz:** die Begrenzung wird ehrlich als tracked geführt.

## EN – G-13 Assessment

**G-13 → Partially closed / remains tracked for RC.** Two genuine independent runs exist (public + private-neutralized), both PASS WITH NOTES with no blockers/high findings — more than "open" — but per-step depth stays limited and one run was private-context, so not "closed." Not needed before RC (RC can proceed with notes); needed before v1.0 final — either a deeper, step-evidenced public run or an explicitly documented boundary in the final v1.0 scope lock. No invented evidence; the limit is honestly tracked.

## DE – RC-Fähigkeit

**RC can proceed with notes.** Begründung:

- Ein `v1.0.0-rc.1` ist ausdrücklich ein **Kandidat**, kein finaler Vertrauensanspruch; er darf selbst als **Validierungsvehikel** dienen (öffentlicher RC → Feedback → v1.0-final-Entscheidung).
- Die vorhandene Evidenz (E-01/E-04/E-05 + Notes) trägt einen RC mit dokumentierter Evidence-Note.
- **v1.0 final muss stärker sein als der RC:** tiefere externe Evidenz **oder** eine klar dokumentierte, akzeptierte Grenze.
- **Risiko öffentliche Glaubwürdigkeit:** gering bei ehrlicher Note im RC-Text („External-Validation-Tiefe begrenzt, tracked"); hoch nur, wenn ein RC v1.0-Reife behaupten würde — das ist ausgeschlossen.
- **Public Neutrality:** gewahrt (keine Reviewer-Identitäten/privaten Namen).

## EN – RC Capability

**RC can proceed with notes.** A `v1.0.0-rc.1` is explicitly a candidate, not a final trust claim, and may itself serve as a validation vehicle (public RC → feedback → v1.0-final decision); the existing evidence carries an RC with a documented note; v1.0 final must be stronger (deeper external evidence or a clearly documented, accepted boundary); public-credibility risk is low with an honest RC note and high only if an RC claimed v1.0 maturity (excluded); public neutrality preserved.

## DE – Empfohlene zusätzliche Validierung

| Option | Ziel | Aufwand | Nutzen | Risiko | Vor RC nötig | Vor v1.0 final nötig |
|---|---|---|---|---|---|---|
| Neutraler SampleProject-Re-Run mit Schrittbelegen | E-01-Tiefe erhöhen (sechs Schritte belegt) | mittel | hoch | gering | optional | **ja (oder dokumentierte Grenze)** |
| Zweiter unabhängiger Review-Lauf (öffentliches Fixture) | zweite Außensicht, ggf. andere Sprache | mittel–hoch | hoch | gering | optional | empfohlen |
| v1.0 RC dry-run (öffentlich) | RC als Validierungsvehikel | mittel | hoch | gering | **ja (empfohlen)** | ja |
| Project Adapter validation (zweiter Fixture-Typ) | Grenze „nur Fixture ohne Code" adressieren | hoch | mittel | gering | nein | optional (sonst Non-Goal) |
| Prompt-Mode-Validierung mit frischem Sample | Prompt-Entscheidungslogik-Randbestand prüfen | gering | mittel | gering | nein | optional |
| Public-neutral reproducibility checklist | reproduzierbarer Selbst-/Fremd-Check ohne Identität | gering | mittel | gering | optional | empfohlen |
| External reviewer checklist (ohne Identität im Public NDF) | strukturierte Fremd-Rückmeldung neutral erfassen | gering | mittel | gering | optional | empfohlen |

**Kernempfehlung:** vor **RC** genügt eine ehrliche Evidence-Note + optional der RC-dry-run; vor **v1.0 final** ist ein schrittbelegter öffentlicher Lauf **oder** eine dokumentierte akzeptierte Grenze nötig.

## EN – Recommended Additional Validation

The table lists options (neutral SampleProject re-run with per-step evidence, second independent run, public v1.0 RC dry-run, second-fixture adapter validation, fresh prompt-mode validation, public-neutral reproducibility checklist, external reviewer checklist without identity) with goal, effort, benefit, risk, and pre-RC / pre-v1.0-final necessity. Core recommendation: before an RC, an honest evidence note (+ optional RC dry-run) suffices; before v1.0 final, a step-evidenced public run or a documented accepted boundary is required.

## DE – Entscheidung für WP-141

**Empfehlung: WP-141 bleibt `v1.0 Release Criteria Finalization`.** G-13 blockiert die Kriterien-Finalisierung **nicht** — im Gegenteil, die Finalisierung sollte die G-13-Evidence-Note und die „vor v1.0 final"-Anforderung **verbindlich verankern** (Kriterium „External Validation" mit Schwelle für RC vs. final). Ein separater Validierungslauf wird **nicht** als blockierendes WP-141 vorgeschaltet; er wird als **empfohlener Schritt vor v1.0 final** (bzw. als öffentlicher RC-dry-run) in die Kriterien aufgenommen.

Verworfen (mit Begründung): `WP-141 Additional External Validation Run` (nicht blockierend nötig; kann parallel/RC-getrieben laufen); `WP-141 RC Dry-run Validation` (sinnvoll, aber besser **nach** Kriterien-Lock als Teil des RC-Pfads); `WP-141 Neutral Sample Validation Refresh` (wertvoll, aber pre-v1.0-final, nicht pre-criteria).

## EN – WP-141 Decision

**Recommendation: WP-141 stays `v1.0 Release Criteria Finalization`.** G-13 does not block criteria finalization; rather, finalization should **bindingly anchor** the G-13 evidence note and the "before v1.0 final" requirement (an external-validation criterion with an RC-vs-final threshold). A separate validation run is not front-loaded as a blocking WP-141; it is captured as a recommended pre-v1.0-final step (or a public RC dry-run) within the criteria. Alternatives (additional-run / RC-dry-run / sample-refresh as WP-141) were rejected with rationale.

## DE – Security / ADR-0031 / ADR-0032 Bewertung

ADR-0031 und ADR-0032 bleiben bindend und unverändert; keine v1.0-Aktivierung/RC; volle v1.x-Zusage erst mit v1.0. Kein Skill geändert/erstellt; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine Reviewer-Identitäten/privaten Projektnamen/Domains. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name. Nächste freie ADR-Nummer: 0033.

## EN – Security / ADR-0031 / ADR-0032 Assessment

ADR-0031/0032 stay binding and unchanged; no v1.0 activation/RC; full v1.x promise only at v1.0. No skill changed/created; no scripts/network/secrets/private data/git-release actions; no reviewer identities/private names/domains; secret name only as a name. Next free ADR number: 0033.

## DE – Risks / Open Notes

- **G-13 bleibt der zentrale v1.0-final-Vorbehalt** (tracked, kein Blocker für RC).
- **Selbstvalidierungsanteil:** mehrere Evidence-Quellen sind intern; die Außensicht ruht auf zwei Läufen mit Tiefe-Note.
- **Ein-Personen-Engpass** begrenzt zusätzliche unabhängige Läufe (dokumentiertes Risiko).
- **Kein Zeitplan**; keine erfundene Evidenz; Grenzen ehrlich geführt.

## EN – Risks / Open Notes

G-13 remains the central v1.0-final caveat (tracked, not an RC blocker); a self-validation share persists (external view rests on two runs with a depth note); the single-person bottleneck limits additional independent runs (documented risk); no schedule; no invented evidence; limits honestly tracked.

## DE – Decision

**GO WITH NOTES.** G-13 Partially closed / remains tracked for RC; RC can proceed with notes; v1.0 final braucht tiefere Evidenz oder dokumentierte Grenze; keine erfundene externe Evidenz; keine v1.0-Aktivierung/RC; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. **Nächster empfohlener WP: WP-141 – v1.0 Release Criteria Finalization** (verankert die G-13-Evidence-Schwelle).

## EN – Decision

**GO WITH NOTES.** G-13 partially closed / tracked for RC; RC can proceed with notes; v1.0 final needs deeper evidence or a documented boundary; no invented external evidence; no v1.0 activation/RC; ADR-0031/0032 unchanged; Foundation 0.9 stays not v1.0. Next recommended WP: WP-141 – v1.0 Release Criteria Finalization (anchoring the G-13 evidence threshold).
