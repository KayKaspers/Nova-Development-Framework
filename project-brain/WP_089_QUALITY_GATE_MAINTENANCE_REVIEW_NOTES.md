# Project Brain – WP-089 Quality Gate Maintenance Review Notes

## Ausgangslage nach WP-088

Beide inhaltlichen 0.6-Kerne erledigt (086 ADR, 088 öffentliche Validierung); WP-089 war der letzte inhaltliche release-blocking Baustein — erstes Gate-Wartungsreview seit v0.2 (WP-052), inkl. des seit 0.4 offenen Prüfpunkts CI-Denylist-Wirksamkeit.

## Geprüfte Artefakte

`scripts/check_public_quality.py` (v0.2, unverändert seit WP-052), `.github/workflows/public-quality-gate.yml`, `docs/repository/PUBLIC_QUALITY_GATE.md`, lokale Läufe (strict + self-test) und ein kontrollierter synthetischer Lokaltest.

## Ergebnis

**Gate in gutem Zustand, keine Blocker.** Alle 10 Script-Prüfpunkte grün (tracked/untracked-Erkennung, strict, self-test, duale Denylist-Quellen, sichere Ausgaben, neutrale Meldungen, klare Exit-Codes, Windows-Praxis, keine CI-Risiken). CI-Verdrahtung sauber: eigener Self-Test-Schritt + Strict-Schritt mit Secret via `env`, Fallback kommentiert (fehlende Denylist = Notice).

## Evidence-Level

**strong** — Kernbeleg war der synthetische Lokaltest (Regeln eingehalten: nur synthetisches Test-Token, temporäre Dateien, vollständiges Cleanup, kein privates Muster dokumentiert): gitignorierte Lokaldatei mit einem synthetic test token + temporäre untracked Datei → Gate **FAILED (exit 1)** mit Treffern in der neuen untracked **und** einer getrackten Datei, plus Root-Hygiene-WARNING als Bonus → nach Cleanup wieder **passed (exit 0)**. Damit sind Denylist-Konsum, New-file-Scan und Fail-Verhalten bewiesen; CI referenziert dasselbe Script mit demselben Env-Mechanismus.

## WP-090-Entscheidung

**A) WP-090 not needed** — die CI-Denylist-Wirksamkeitsbewertung wurde ausreichend in WP-089 erbracht. So in Criteria, Queue, Scope Lock und Review-Dokument festgehalten.

## Findings

QGM-001 (info): Evidence strong, alles grün. QGM-002 (info): synthetische Testbegriffe stehen in getrackten Notes — kollidieren nur, wenn jemand sie auf die echte Denylist setzt (kein Handlungsbedarf). QGM-003 (low, non-blocking): Bei echtem Treffer druckt der Gate den gefundenen Begriff im ERROR — in CI-Logs sichtbar; der Begriff wäre dann aber ohnehin schon in der Repo-Datei öffentlich. Operative Erwartung: Verstoß sofort beheben. → Known-Limitation-Kandidat für WP-094/095.

## Auswirkungen auf Foundation 0.6

WP-089 erfüllt; **alle inhaltlichen blocking WPs sind damit done** — offen nur noch die Release-Strecke WP-094 → WP-095. 0.6 bleibt unreleased.

## Auswirkungen auf v1.0-Kriterien

Kategorie 7 (Gate & Neutralität) bleibt `met` und ist jetzt inkl. CI-Wirksamkeitsnachweis bestätigt; der bisherige „WP-078 empfohlen"-Hinweis im Draft ist durch den WP-089-Verweis ersetzt. Kein v1.0-Claim.

## Bewusst nicht getan

Keine Script-/CI-Änderungen (keine nötig — keine Bugs gefunden), keine neuen Gate-Regeln, keine dauerhaften Testbegriffe (Testdateien vollständig entfernt, per `git status` verifiziert), kein README-Update (Gate-Doku verlinkt den Review; Top-Level-Link wäre Rauschen).

## Risiken

1. QGM-003 (CI-Log-Echo bei echtem Treffer) — dokumentierte operative Erwartung, non-blocking.
2. Optionaler Maintainer-Spot-Check bleibt sinnvoll: Im CI-Log eines aktuellen Push-Laufs darf die „No custom neutrality denylist configured."-Notice nicht erscheinen (Secret aktiv). Kein Artefakt nötig.

## Nächste WP

**NDF-WP-094 – Foundation 0.6 Release Readiness Review**, danach WP-095 (Release Prep).
