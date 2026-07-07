# Project Brain – WP-086 ADR Policy Decision Notes

## Ausgangslage

ADR-Policy zweimal verschoben (0.4/WP-063, 0.5/WP-076). Die 0.5-Sonderregel und der 0.6-Scope-Lock machten WP-086 release-blocking mit hartem Entscheidungszwang: **A) Minimal-Policy annehmen** oder **B) ehrlich streichen** — „später" in jeder Form unzulässig.

## Bestandsaufnahme

Zwei ADR-Orte existieren und werden aktiv genutzt: `adr/` (Repo-Wurzel, Foundation-0.1-Kernentscheidungen 0001–0026, eingefroren) und `docs/adr/` (thematische ADRs 0027–0030 + früher Altbestand 0001–0005 mit dokumentierter Nummernkollision; nächste freie Nummer 0031 — alles seit WP-033 dokumentiert). NDF nutzt ADRs also bereits; es fehlte nur die verbindliche Regel.

## Entscheidung

**Option A: Minimal ADR Policy adopted** (`docs/adr/ADR_POLICY.md`, Status Accepted, 2026-07-07).

Begründung: (1) ADRs sind gelebte Praxis — eine Policy kodifiziert, statt zu erfinden; (2) Governance Hardening ist 0.6-Kernziel; (3) schließt das offene v1.0-Kriterium; (4) minimal gehalten (nur Wann/Wo/Wie/Wer) — wartbar für das Ein-Personen-Modell; (5) besser als Streichen, weil die Alternative (nur WP-Notes) dauerhafte Regeln von Umsetzungsverläufen nicht trennen könnte. Option B wurde geprüft und verworfen — nicht aus Bequemlichkeit, sondern weil A tragfähig ist.

## Kerninhalte der Policy

ADR erforderlich bei dauerhafter Wirkung über WPs hinaus (Architektur/Governance, Security-Patterns, Release-/Versionierungsregeln, Gate-/Neutralitätsregeln, Rollen-Invarianten, v1.0-relevante Entscheidungen); WP-Note reicht für Statusupdates/Einmalschritte/Umsetzung entschiedener Muster. Neue ADRs **nur** in `docs/adr/` als `ADR-XXXX-short-title.md`, Nummer fortlaufend **über beide Ordner** (nächste: 0031 — löst die Kollisionsfrage für die Zukunft); `adr/` bleibt eingefroren. Status: Proposed/Accepted/Superseded/Rejected/Deprecated (+ Deferred nur für inhaltliche ADRs, nie für Policy-Entscheidungen). Rollen: Nova empfiehlt/reviewt, Agent entwirft auf Anweisung, Maintainer entscheidet. Angenommene ADRs werden per Supersede ersetzt, nicht umgeschrieben.

## Massenmigrations-Schutz

Dreifach verankert: Pflichtformulierung „keine Massenmigration" in der Policy (Altbestand bleibt gültiger historischer Nachweis), Nummernkollision ausdrücklich als dokumentierter Altbestand bestätigt (README-Update statt Konsolidierungs-Versprechen), ADR-Massenmigration bleibt im 0.6-Scope-Lock deferred. In diesem WP wurde kein einziger Alt-ADR verschoben oder umgeschrieben.

## Erstellte/geänderte Dateien

Neu: `docs/adr/ADR_POLICY.md`, `docs/adr/ADR_TEMPLATE.md`, diese Note. Geändert: `docs/adr/README.md` (Einstieg + Kollisions-Entscheidung), v1.0-Draft (Kategorie 10 → `met with notes`), Path Summary, 0.6-Criteria (WP-086 abgehakt), 0.6-Queue/Scope-Lock/Plan (WP-086 entschieden), README (ADR-Policy-Link DE/EN mit „kein v1.0"), CHANGELOG, NEXT_PHASE_0_6.

## Auswirkungen auf v1.0-Kriterien

Kategorie 10 (ADR/Decision Structure): `not met` → **`met with notes`** — Notes: Massenmigration bleibt deferred, die Policy muss sich in künftigen WPs bewähren. Kein v1.0-Claim; Path Summary entsprechend aktualisiert.

## Bewusst nicht getan

Keine Migration/Umbenennung bestehender ADRs, kein Umbau des eingefrorenen `adr/`-Ordners, keine neue ADR-0031 (kein akuter Anlass — die nächste echte Entscheidung nutzt das Template), keine Governance-Struktur über das Minimum hinaus, kein v1.0 Scope Lock.

## Risiken

1. Policy könnte totes Papier werden → v1.0-Note „muss sich bewähren"; WP-094 sollte prüfen, ob sie bei anstehenden Entscheidungen tatsächlich genutzt wird.
2. Verwechslung Template/Policy-Pflicht → Faustregel in der Policy (Regel über WP hinaus = ADR).
3. Alt-Kollisionen könnten Leser verwirren → README erklärt sie jetzt als entschiedenen Altbestand.

## Nächste WP

**NDF-WP-088 – Public SampleProject Runbook Validation Run** (WP-087 nur bei Bedarf; Maintainer-Outreach früh starten), danach WP-089.
