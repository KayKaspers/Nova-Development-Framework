# Public Quality Gate Maintenance Review

## DE – Zweck

Wartungsreview des Public Quality Gate v0.2 (NDF-WP-089, Foundation 0.6 — Governance Hardening): Zustand von Script, Strict-Mode, Self-Test, New-file-Scan, Custom-Denylist-/Secret-Integration und CI-Verdrahtung — inklusive der Entscheidung, ob ein separates CI-Denylist-Nachweis-Artefakt (NDF-WP-090) nötig ist.

## EN – Purpose

Maintenance review of the public quality gate v0.2 (NDF-WP-089, Foundation 0.6 — governance hardening): state of the script, strict mode, self-test, new-file scan, custom denylist / secret integration, and CI wiring — including the decision whether a separate CI denylist proof artifact (NDF-WP-090) is needed.

## DE – Status

**Review abgeschlossen am 2026-07-07. Ergebnis: Gate in gutem Zustand, keine Blocker. Evidence-Level: strong. Entscheidung: WP-090 not needed.** Foundation 0.6 ist nicht released; kein v1.0-Claim.

## EN – Status

**Review completed on 2026-07-07. Result: gate in good shape, no blockers. Evidence level: strong. Decision: WP-090 not needed.** Foundation 0.6 is not released; no v1.0 claim.

## DE – Geprüfter Umfang

`scripts/check_public_quality.py` (v0.2, seit WP-052 unverändert), `.github/workflows/public-quality-gate.yml`, zentrale Doku `docs/repository/PUBLIC_QUALITY_GATE.md`, lokales Laufverhalten unter Windows, plus ein kontrollierter synthetischer Lokaltest. Keine Script- oder CI-Änderungen (Review-only).

## EN – Reviewed Scope

The gate script (v0.2, unchanged since WP-052), the CI workflow, the central documentation, local behavior on Windows, plus a controlled synthetic local test. No script or CI changes (review-only).

## DE – Script-Verhalten

Geprüft, ohne Änderungen:

1. **Tracked-Erkennung:** über `git ls-files` — ✅
2. **New/untracked-Erkennung:** über `git ls-files --others --exclude-standard`, standardmäßig aktiv; `--tracked-only` als Opt-out — ✅
3. **Strict Mode:** vorhanden; Warnings werden in strict zu Fehlern gewertet, klare Zählzeile — ✅
4. **Self-Test:** vorhanden; nutzt ausschließlich synthetische Begriffe in temporären Strukturen — ✅
5. **Custom Denylist:** zwei Quellen — Env-Variable `NDF_PUBLIC_NEUTRALITY_DENYLIST` (kommagetrennt) und gitignorierte Lokaldatei `.ndf/public-neutrality-terms.local.txt`; Kopfkommentar verbietet echte Begriffe im Repo ausdrücklich — ✅
6. **Secret-Sicherheit:** Der Denylist-Inhalt wird nie als Liste ausgegeben; nur konkret gefundene Treffer erscheinen als ERROR (siehe Finding QGM-003) — ✅ mit Hinweis
7. **Neutrale Meldungen:** Fehlertexte generisch („denylisted term … found in …") — ✅
8. **Exit Codes:** 0 = passed, 1 = failed; Notices beeinflussen den Exit-Code nicht — ✅
9. **Windows/PowerShell:** über 50+ WP-Läufe dieser Sessions praktisch bewährt (`python`/`py` beide dokumentiert) — ✅
10. **CI-Risiken:** ubuntu-latest + setup-python 3.12, kein Cache-/Versions-Risiko erkennbar — ✅

## EN – Script Behavior

All ten review points pass: tracked and new/untracked detection, strict mode, self-test with synthetic terms only, dual denylist sources (env variable + gitignored local file), no denylist listing in output (only concrete matches, see QGM-003), neutral messages, clear exit codes (0/1, notices never fail), proven Windows usability, no CI risk identified.

## DE – Strict Mode

Baseline-Lauf am Review-Tag: `0 error(s), 0 warning(s), 3 notice(s) [strict mode] — Public quality gate passed.` Notices sind reine INFO (Scan-Modus, lokal keine Denylist konfiguriert) und korrekt non-failing.

## EN – Strict Mode

Baseline run on review day: passed with 0 errors, 0 warnings, 3 INFO notices (scan mode, no local denylist) — notices correctly non-failing.

## DE – Self-Test

`--self-test` → **passed** (lokal am Review-Tag; läuft zusätzlich als eigener CI-Schritt vor dem Strict-Lauf). Deckt u. a. Denylist-Laden, New-file-Erkennung und README-Regeln mit synthetischen Begriffen ab.

## EN – Self-Test

Passed locally on review day; also runs as its own CI step before the strict run. Covers denylist loading, new-file detection, and README rules using synthetic terms.

## DE – New-file Scan

**Per synthetischem Lokaltest bewiesen** (kontrolliert, mit Cleanup): Eine gitignorierte Lokaldatei erhielt ein einzelnes `synthetic test token`; eine temporäre untracked Markdown-Datei mit diesem Token wurde angelegt. Ergebnis: Gate **FAILED (exit 1)** mit ERROR-Treffern **sowohl in der neuen untracked Datei als auch in einer getrackten Datei** (den WP-052-Notes, die die erlaubten synthetischen Testbegriffe dokumentieren) — plus Root-Hygiene-WARNING für die temporäre Root-Datei als Bonus-Bestätigung. Nach Entfernen von Testdatei und Lokaldatei: Gate wieder **passed (exit 0)**. Der neue Run-Ordner aus WP-088 wurde im Baseline-Lauf ebenfalls per new-file check mitgescannt.

## EN – New-file Scan

**Proven via a controlled synthetic local test** (with cleanup): a gitignored local denylist received a single synthetic test token; a temporary untracked markdown file containing it was created. Result: gate **FAILED (exit 1)** with ERROR hits **in both the new untracked file and a tracked file** (the WP-052 notes documenting the allowed synthetic test terms) — plus a root-hygiene WARNING for the temp root file as bonus confirmation. After removing both files: **passed (exit 0)** again.

## DE – Custom Denylist / Secret Integration

CI-Verdrahtung (`.github/workflows/public-quality-gate.yml`):

- Der Workflow referenziert den erwarteten Secret-Namen und übergibt ihn per `env: NDF_PUBLIC_NEUTRALITY_DENYLIST: ${{ secrets.NDF_PUBLIC_NEUTRALITY_DENYLIST }}` direkt an den Strict-Lauf — **ohne den Wert zu loggen oder zu dokumentieren**.
- Fallback ist im Workflow kommentiert und im Script implementiert: Ohne Secret läuft der Gate weiter; die fehlende Denylist ist eine Notice, kein Fehler.
- Lokale Maintainer-Alternative: die gitignorierte Lokaldatei.
- Leerer Secret-Wert: unkritisch (wie „nicht gesetzt" behandelt).
- Der Gate ist auch ohne Secret sinnvoll (Struktur-/Root-/README-/History-Regeln greifen immer).
- Das Secret selbst ist als **vorhanden** verifiziert (WP-070, Human-Maintainer-Bestätigung); sein Wert wurde und wird nie gelesen oder dokumentiert.

Bewertungsgrundlage ausschließlich: configuration evidence, script behavior, safe logging behavior, self-test behavior, documented operational expectation — **nicht** der Secret-Inhalt.

## EN – Custom Denylist / Secret Integration

CI configuration references the expected secret name and passes it into the public quality gate without documenting its value; the fallback (missing denylist = notice, not failure) is commented in the workflow and implemented in the script; the gitignored local file is the maintainer alternative; an empty secret is harmless; the gate is useful even without a secret. The secret's existence was verified in WP-070; its value was never read or documented. Assessment basis: configuration evidence, script behavior, safe logging, self-test behavior, documented operational expectation only.

## DE – CI-Denylist-Wirksamkeitsbewertung

**Evidence-Level: strong.** Begründung gegen die Definition: CI referenziert das erwartete Secret (✅), das Script konsumiert den Custom-Denylist-Input nachweislich (✅, per Lokaltest), strict und self-test laufen in CI als eigene Schritte (✅), der New-file-Scan ist abgedeckt (✅, per Lokaltest inkl. untracked-Erkennung), und der synthetische Lokaltest hat das erwartete Fehlverhalten bewiesen (✅ — FAIL bei Treffer, PASS nach Bereinigung). Zusätzlicher operativer Prüfpunkt für den Maintainer (optional, kein Nachweis-Artefakt nötig): Im CI-Log eines aktuellen Push-Laufs darf die Notice „No custom neutrality denylist configured." **nicht** erscheinen — dann ist das Secret in CI aktiv.

## EN – CI Denylist Effectiveness Assessment

**Evidence level: strong** per the definition: CI references the expected secret; the script demonstrably consumes custom denylist input (local test); strict and self-test run as separate CI steps; the new-file scan is covered (local test incl. untracked detection); the synthetic local test proved the expected failure behavior. Optional operational spot-check for the maintainer: the "No custom neutrality denylist configured." notice must **not** appear in a current CI push log — then the secret is active in CI.

## DE – Findings / EN – Findings

| ID | Severity | Bereich / Area | Finding | Empfehlung / Recommendation |
|---|---|---|---|---|
| QGM-001 | info | Evidence | Alle Prüfbereiche grün; Wirksamkeit per synthetischem Lokaltest belegt (Evidence-Level strong). / All areas green; effectiveness proven via synthetic local test (evidence level strong). | Keine Aktion; Bewertung bei künftigen Gate-Reviews wiederholen. / No action; repeat at future gate reviews. |
| QGM-002 | info | Synthetic terms | Die dokumentierten synthetischen Testbegriffe stehen in getrackten WP-Notes; setzt ein Maintainer einen davon versehentlich auf die echte Denylist, schlägt der Gate auf historischen Notes an. / The documented synthetic test terms live in tracked notes; putting one on the real denylist would flag historical notes. | Kein Handlungsbedarf — echte Denylists enthalten reale private Begriffe, keine synthetischen; Verhalten ist sogar ein nützlicher Selbsttest. / No action needed. |
| QGM-003 | low | CI log exposure | Bei einem echten Treffer druckt der Gate den gefundenen Begriff im ERROR (nötig für Behebbarkeit) — in einem öffentlichen Repo stünde der Begriff dann auch im CI-Log. Der Begriff wäre zu diesem Zeitpunkt aber ohnehin bereits in der Repo-Datei selbst öffentlich; das Log ist sekundär. / On a real hit the gate prints the matched term in the ERROR (needed for fixability) — in a public repo the term would then also appear in the CI log; at that point it is already public in the repo file itself. | Dokumentierte operative Erwartung: Verstoß sofort beheben (Datei bereinigen), dann ist auch das Log-Risiko abgeräumt. Non-blocking. / Documented operational expectation: fix the violation immediately. Non-blocking. |

## DE – Entscheidung zu WP-090

**A) WP-090 not needed** — WP-090 is not needed as a separate work package because WP-089 sufficiently covered the CI denylist effectiveness assessment (Evidence-Level strong, inkl. bewiesenem Fehlverhalten per synthetischem Lokaltest und sauberer CI-Verdrahtung).

## EN – Decision on WP-090

**A) WP-090 not needed** — WP-089 sufficiently covered the CI denylist effectiveness assessment (evidence level strong, including proven failure behavior via a synthetic local test and clean CI wiring).

## DE – Auswirkungen auf Foundation 0.6

WP-089 ist **erfüllt** — der letzte inhaltliche release-blocking Baustein vor der Release-Strecke. Im blocking Scope offen: nur noch WP-094 (Readiness) und WP-095 (Release Prep). QGM-003 geht als non-blocking Hinweis in die Known-Limitation-Kandidaten. Foundation 0.6 bleibt **unreleased**.

## EN – Impact on Foundation 0.6

WP-089 is **fulfilled** — the last content-level release-blocking piece before the release track; only WP-094 and WP-095 remain. QGM-003 feeds the known-limitation candidates as a non-blocking note. Foundation 0.6 remains **unreleased**.

## DE – Auswirkungen auf v1.0

Die v1.0-Kategorie „Public Quality Gate & Neutralität" bleibt `met` und wird durch dieses Review bestätigt — inklusive des bisher offenen Prüfpunkts CI-Denylist-Wirksamkeit (jetzt strong bewertet). **Kein v1.0-Claim.**

## EN – Impact on v1.0

The v1.0 category "public quality gate & neutrality" stays `met` and is confirmed by this review — including the previously open CI denylist effectiveness spot-check (now assessed strong). **No v1.0 claim.**

## DE – Nicht-Ziele

Keine Script-/CI-Änderungen; keine neuen Gate-Regeln; keine dauerhaften Testbegriffe oder privaten Suchmuster; keine Release Prep; kein v1.0 Scope Lock.

## EN – Non-Goals

No script/CI changes; no new gate rules; no permanent test terms or private search patterns; no release prep; no v1.0 scope lock.
