# Project Brain – WP-100 v1.x Compatibility Policy Notes

## Summary

Die release-blocking Foundation-0.7-Entscheidung zur v1.x Compatibility Policy ist getroffen: **Option A — ADR-0031 angenommen** (`docs/adr/ADR-0031-v1x-compatibility-policy.md`, Status Accepted). Governance-Rahmen für v1.x-Kompatibilität; die aktive volle Zusage tritt erst mit v1.0 in Kraft. Damit ist das letzte klar `not met` v1.0-blocking-Kriterium auf `met with notes` gehoben — ohne v1.0-Claim.

## Inputs reviewed

0.7-Scope-Lock (ADR-0031 bevorzugt), ADR-Policy (ADR für Governance-/Versionierungsentscheidungen erforderlich; ADR-0031 nächste freie Nummer über beide Ordner), v1.0-Draft (Kriterium `not met`), ADR-README (Kollisions-Historie). ADR-0031 war frei (docs/adr bis 0030, adr/ bis 0026).

## Decision: ADR-0031 or policy-only

**ADR-0031** (Option A). Begründung: Kompatibilitäts-/Versionierungsregeln haben dauerhafte Governance-Wirkung und betreffen künftige Releases + v1.0-Readiness — genau der Fall, für den die ADR-Policy eine ADR verlangt. ADR-0031 ist Source of Truth; kein separates Policy-Dokument (Token-/Doku-Sparsamkeit, wie im Prompt empfohlen).

## Compatibility categories

Stable Candidate · Governed · Experimental · Deprecated · Out of Scope.

## What is governed before v1.0

Stable Candidate (Kern-Rollenmodell, WP-Flow + GO/GO-WITH-NOTES/REWORK/STOP, Public-Neutrality-Invarianten, Maintainer-Release-Kontrolle); Governed (ADR-Policy, Release-Muster, Adapter Conventions, Gate-Erwartungen). Breaking-Change- und Deprecation-Regeln vor v1.0 best-effort mit dokumentiertem Vermerk.

## What is not promised before v1.0

Keine aktive volle v1.x-Kompatibilitätsgarantie; Experimental-Bestandteile ohne Erwartung; Out-of-Scope (private Workflows/Domains/Deployment/Secrets). Aktivierung der vollen Zusage erst im v1.0-Zyklus.

## Impact on Foundation 0.7

WP-100 erfüllt. Blocking Kern: 098/099/100 (done) · 101 · 104 · 105. Nächster inhaltlicher Schritt: WP-101 (Convention Stability Review — prüft, ob Adapter-Konventionen als Stable Candidate belastbar sind).

## Impact on v1.0 path

Kriterium „v1.x-Versionierungs-/Kompatibilitätszusage" `not met` → **`met with notes`** (Rahmen angenommen; aktive Zusage v1.0-tracked). Übersichtstabelle (Kategorie 8) + Path Summary (DE+EN) nachgezogen. Kein v1.0-Claim.

## Files changed

Neu: `docs/adr/ADR-0031-v1x-compatibility-policy.md`, diese Note. Geändert: ADR-README (ADR-0031 eingetragen, nächste Nummer → 0032), v1.0-Draft (Kriterium + Kategorie 8), Path Summary, 0.7-Criteria/Queue/Scope-Lock/Plan (WP-100 done), README (ADR-0031-Link DE/EN), CHANGELOG, NEXT_PHASE_0_7.

## What was not done

Keine aktive v1.x-Zusage, kein v1.0 Scope Lock, keine v1.0-Reife-Behauptung, kein separates Policy-Dokument, keine ADR-Massenmigration, keine Umnummerierung/Änderung alter ADRs, keine privaten Beispiele.

## Risks

ADR-0031 könnte als aktive Zusage missverstanden werden → „Aktivierung erst mit v1.0" mehrfach verankert (ADR, Criteria, Path Summary, README, Changelog). Stable-Candidate-Liste ist Vorschlag → Bestätigung durch WP-101 + v1.0-Zyklus.

## Next step

**NDF-WP-101 – Project Adapter Convention Stability Review.**

## Compact Context Summary

Foundation 0.7 (scope-locked, v1.0 Path Consolidation & Compatibility Governance) läuft; 0.6 released. WP-099: Checklist DE/EN = Option B (optional, kein Blocker). **WP-100: v1.x Compatibility Policy als ADR-0031 angenommen** — 5 Kompatibilitätskategorien, Breaking-/Deprecation-Regeln, volle Zusage erst mit v1.0; v1.0-Kriterium jetzt `met with notes`. Offener blocking Kern: WP-101 (Convention Stability), dann WP-104/105. Nächste freie ADR-Nummer: 0032. Kein v1.0, kein Release. ADR-0031 = Source of Truth, kein separates Policy-Dokument.
