# Foundation 0.5 Scope Lock

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.5 verbindlich ein (NDF-WP-072). Es macht aus dem Planungs-Draft (NDF-WP-071) die verbindliche Einstufung: release-blocking, optional, deferred. Änderungen nur noch über die Änderungsregeln unten.

## EN – Purpose

This document bindingly freezes the Foundation 0.5 scope (NDF-WP-072), turning the planning draft (NDF-WP-071) into the binding classification: release-blocking, optional, deferred. Changes only via the change rules below.

## DE – Status

**Scope locked** (NDF-WP-072, 2026-07-06). Foundation 0.5 ist geplant und gelockt, **nicht released**. NDF ist kein v1.0 und behauptet keine v1.0-Reife.

## EN – Status

**Scope locked** (NDF-WP-072, 2026-07-06). Foundation 0.5 is planned and locked, **not released**. NDF is not v1.0 and claims no v1.0 maturity.

## DE – Eingefrorenes Zielbild

**Foundation 0.5 – External Validation & 1.0 Path Hardening.** Je ein Kern-Deliverable pro Titel-Hälfte: der unabhängige Adapter-Validierungslauf (Vorbereitung WP-073 + Durchführung WP-074) gegen den dokumentierten Selbstvalidierungs-Bias, und der v1.0-Kriterien-Entwurf (WP-079) als Messlatte — nicht als Versprechen.

## EN – Locked Target

**Foundation 0.5 – External Validation & 1.0 Path Hardening.** One core deliverable per title half: the independent adapter validation run (preparation WP-073 + execution WP-074) against the documented self-validation bias, and the v1.0 criteria draft (WP-079) as a yardstick — not a promise.

## DE – Release-blocking Scope

Nur diese WPs blockieren den Release `v0.5.0-foundation`:

| WP | Titel | Begründung |
|---|---|---|
| NDF-WP-072 | Scope Lock | Gate — abgeschlossen mit diesem Dokument |
| NDF-WP-073 | Independent Adapter Validation Preparation | Kern External Validation; selbstständig erfüllbar (Testleitfaden, neutrales Setup, Erfolgskriterien, Feedback-Format), unabhängig davon, ob der Run gelingt |
| NDF-WP-074 | Independent Adapter Validation Run | Kern External Validation — **mit Downgrade-Ventil** (siehe unten), weil die Durchführung personenabhängig ist |
| NDF-WP-079 | v1.0 Readiness Criteria Draft | Kern 1.0 Path Hardening; nur Entwurf, kein v1.0-Claim |
| NDF-WP-081 | Release Readiness Review | Gate; entscheidet zugleich über das WP-074-Ventil |
| NDF-WP-082 | Release Prep | Gate |

## EN – Release-blocking Scope

Only WP-072 (this gate), WP-073 (validation preparation, self-contained), WP-074 (validation run, with downgrade valve), WP-079 (v1.0 criteria draft), WP-081 (readiness review, also decides the valve) and WP-082 (release prep) block the `v0.5.0-foundation` release.

## DE – Optionaler Scope

Should-have, blockiert nie; Unerledigtes wird ehrlich in Release Notes und Translation-Status-Matrix geführt:

- NDF-WP-075 – Checklist Library DE/EN Priority Pass
- NDF-WP-076 – ADR Policy & Structure Consolidation Plan — **Sonderregel:** bereits zweimal verschoben (0.3/WP-050-Umfeld, 0.4/WP-063). Bleibt WP-076 auch in 0.5 unerledigt, muss WP-081 explizit festhalten: in 0.6 verbindlich priorisieren **oder** ehrlich streichen. Ein drittes stillschweigendes Verschieben ist nicht zulässig.
- NDF-WP-077 – Academy Band 1 Entry Pass
- NDF-WP-078 – Public Quality Gate Maintenance Review — blockiert nicht, solange der Gate grün bleibt; empfohlener Prüfpunkt: verifizieren, dass die CI-Denylist mit gesetztem Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` greift

## EN – Optional Scope

WP-075 (checklist DE/EN), WP-076 (ADR policy plan — special rule: deferred twice already; if unfinished again, WP-081 must record "prioritize bindingly in 0.6 **or** drop honestly", a third silent carry-over is not allowed), WP-077 (academy entry), WP-078 (gate maintenance — never blocking while the gate stays green). Unfinished items are documented honestly.

## DE – Deferred Scope

- NDF-WP-080 – Docs Export / Website Readiness Concept (nur bei Restkapazität; kein Build, keine Pipeline; blocking wäre nicht begründbar — kein 0.5-Kernziel hängt daran)
- Restliche i18n-Flächenübersetzung; vollständige Security-/Gate-Prompt-Übersetzung; ADR-Massenmigration (erst nach WP-076-Policy, frühestens 0.6); der v1.0-Release selbst

## EN – Deferred Scope

WP-080 docs export/website concept (spare capacity only); remaining blanket i18n; full security/gate prompt translation; bulk ADR migration (after the WP-076 policy, 0.6 at the earliest); the v1.0 release itself.

## DE – WP-074 Downgrade-Ventil

WP-074 bleibt release-blocking. WP-081 (Release Readiness Review) darf WP-074 auf **deferred / Known Limitation** herabstufen, wenn **alle** folgenden Bedingungen erfüllt sind:

1. NDF-WP-073 ist vollständig abgeschlossen (Testleitfaden, neutrales Setup, Erfolgskriterien, Feedback-Format liegen reviewt vor).
2. Ein sauberer, sofort ausführbarer unabhängiger Validierungsplan existiert — der Run könnte jederzeit ohne weitere Vorbereitung starten.
3. Mindestens ein realistischer Versuch, eine unbeteiligte Person oder Instanz zu gewinnen, ist dokumentiert (konkret: wer/welcher neutrale Kanal wurde wann mit dem WP-073-Material angefragt, ohne private Namen — neutrale Rollenbezeichnung genügt).
4. Zum Zeitpunkt von WP-081 ist keine unabhängige Person/Instanz in einem vertretbaren Zeitfenster verfügbar.
5. WP-081 begründet die Herabstufung explizit im Review-Dokument.
6. Die 0.5-Release-Notes nennen die fehlende unabhängige Durchführung als Known Limitation.
7. Es wird keine v1.0-Reife behauptet — und der v1.0-Kriterien-Entwurf (WP-079) führt die unabhängige Validierung als offenes v1.0-relevantes Kriterium, damit das Ventil kein Dauerausweg wird.
8. Der Human Maintainer bestätigt die Herabstufung in der Go/No-Go-Entscheidung.

Das Ventil gilt **nur** für WP-074. Es erlaubt keine Aufweichung von WP-073 oder WP-079.

## EN – WP-074 Downgrade Valve

WP-074 stays release-blocking. WP-081 may downgrade it to **deferred / known limitation** only if **all** conditions hold: (1) WP-073 fully complete; (2) a clean, immediately executable independent validation plan exists; (3) at least one realistic, documented attempt to engage an uninvolved person or instance (who/which neutral channel, when, with the WP-073 material — neutral role labels, no private names); (4) no independent person/instance available within a reasonable window at WP-081 time; (5) WP-081 justifies the downgrade explicitly; (6) the 0.5 release notes list the missing independent run as a known limitation; (7) no v1.0 claim — and the WP-079 criteria draft keeps independent validation as an open v1.0-relevant criterion so the valve cannot become a permanent escape; (8) the human maintainer confirms the downgrade in the go/no-go decision. The valve applies **only** to WP-074.

## DE – Änderungsregeln

1. Kein neues release-blocking WP ohne dokumentierte Scope-Lock-Änderung (eigenes kleines Review durch Nova (ChatGPT) + Freigabe durch den Human Maintainer).
2. Herabstufung blocking → optional/deferred: nur über das WP-074-Ventil (oben) oder eine begründete Entscheidung in WP-081.
3. Hochstufung optional → blocking: nur bei kritischem Fund (z. B. Neutralitäts- oder Gate-Problem), dokumentiert im Scope-Lock-Änderungsvermerk.
4. Neue Ideen außerhalb des Korridors gehen als Kandidaten in die 0.6-Planung, nicht in 0.5.
5. Redaktionelle Korrekturen (Tippfehler, Links) sind keine Scope-Änderung.

## EN – Change Rules

No new blocking work package without a documented scope lock change (small Nova (ChatGPT) review + human maintainer approval); downgrades only via the WP-074 valve or a justified WP-081 decision; upgrades only on critical findings; new ideas go to 0.6 planning; editorial fixes are not scope changes.

## DE – Release-Gate-Regeln

- Reihenfolge: 072 → (073 ‖ 079) → 074 → optional/deferred → 081 → 082. Kein inhaltliches WP vor diesem Scope Lock.
- WP-081 und WP-082 bleiben eigene Gates; Tag und GitHub Pre-Release erstellt ausschließlich der Human Maintainer.
- Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) muss durchgehend grün sein.
- Jedes WP endet mit Rückmeldung an Nova (ChatGPT) und GO/GO WITH NOTES/REWORK/STOP.

## EN – Release Gate Rules

Order 072 → (073 ‖ 079) → 074 → optional/deferred → 081 → 082; readiness and release prep stay separate gates; tag and GitHub pre-release are created by the human maintainer only; the public quality gate must stay green throughout; every work package ends with a report to Nova (ChatGPT).

## DE – Nicht-Ziele

Kein v1.0-Release und keine v1.0-Behauptung (auch nicht implizit über WP-079); keine Website/Export-Pipeline/CLI (höchstens Konzept via WP-080); kein DE/EN-Massenprojekt; keine ADR-Massenmigration; kein History-Rewrite; keine Integration realer privater Projekte; keine neuen Großkonzepte ohne Scope-Lock-Änderung.

## EN – Non-Goals

No v1.0 release or claim (not even implicitly via WP-079); no website, export pipeline, or CLI (concept at most); no blanket DE/EN project; no bulk ADR migration; no history rewrite; no integration of real private projects; no new large concepts without a scope lock change.

## DE – Risiken

1. **WP-074-Personenabhängigkeit** — durch das präzise Ventil adressiert; Restrisiko: das Ventil wird zu früh gezogen. Gegenmittel: Bedingungen 2–4 verlangen echten, dokumentierten Versuch, und Bedingung 7 hält das Kriterium für v1.0 offen.
2. **v1.0-Missverständnis über WP-079** — Draft-Markierung überall; Invariante „kein v1.0-Claim" in Kriterien und Gates.
3. **Scope Creep über optionale WPs** — Einstufung ist gelockt; Änderungen nur über die Regeln oben.
4. **WP-076-Dauerschleife** — durch die Sonderregel (priorisieren oder streichen in 0.6) beendet.

## EN – Risks

WP-074 person dependency (addressed by the precise valve; conditions 2–4 require a real documented attempt, condition 7 keeps the criterion open for v1.0); v1.0 misunderstanding via WP-079 (draft markers + invariant); scope creep via optional work packages (locked classification); WP-076 perpetual carry-over (ended by the special rule).

## DE – Nächster Schritt

**NDF-WP-073 – Independent Adapter Validation Preparation** (parallel oder danach: NDF-WP-079 – v1.0 Readiness Criteria Draft). Kein anderes inhaltliches WP vorher.

## EN – Next Step

**NDF-WP-073 – Independent adapter validation preparation** (in parallel or after: NDF-WP-079 – v1.0 readiness criteria draft). No other content work package before these.
