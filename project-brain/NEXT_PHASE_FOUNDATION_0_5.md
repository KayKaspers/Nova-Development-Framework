# Project Brain – Next Phase Foundation 0.5

> **Status:** Scope locked (NDF-WP-072, 2026-07-06) — verbindlich: `docs/roadmap/FOUNDATION_0_5_SCOPE_LOCK.md`. Nächster Schritt: WP-073 (Validation Preparation), parallel/danach WP-079 (v1.0 Criteria Draft). Kein Release, kein v1.0.

## Zielbild

**Foundation 0.5 – External Validation & 1.0 Path Hardening.** Nach Adoptionsbeweis (0.3) und Adoption Hardening (0.4) schließt 0.5 die zwei strukturellen Lücken: den Selbstvalidierungs-Bias (Adapter bisher nur durch die eigene Rollenkette validiert, offene Grenze aus WP-047) und die fehlende Messlatte Richtung v1.0.

## Wichtigste Kandidaten

- **Blocking-Kandidaten:** WP-072 Scope Lock → WP-073 Independent Validation Preparation ‖ WP-079 v1.0 Criteria Draft → WP-074 Independent Validation Run (mit Downgrade-Ventil über WP-081) → WP-081/082 Release-Strecke.
- **Optional:** WP-075 Checklist DE/EN, WP-076 ADR Policy Plan, WP-077 Academy Entry, WP-078 Gate Maintenance (alle aus 0.4 übernommen).
- **Deferred:** WP-080 Docs Export / Website Concept.

## Risiken

1. WP-074 hängt an der Verfügbarkeit einer unbeteiligten Person → Ventil im Scope Lock festschreiben (analog WP-060-Ventil in 0.4).
2. v1.0 Criteria Draft darf nicht als Release-Ankündigung wirken → überall als Entwurf markieren.
3. Vier 0.4-Reste verleiten zu Scope Creep → bleiben optional, blocking Kern klein.

## Nächster Schritt

**Update (WP-072):** Scope Lock ist beschlossen — Release-blocking sind nur 072, 073, 074 (mit präzisem 8-Bedingungen-Downgrade-Ventil über WP-081), 079, 081, 082; 075–078 optional (076 mit Priorisieren-oder-Streichen-Regel für 0.6); 080 deferred. Verbindlich: `docs/roadmap/FOUNDATION_0_5_SCOPE_LOCK.md`

**Update (WP-073/WP-079):** Beide inhaltlichen Kern-WPs sind erledigt — Validierungsvorbereitung (`docs/validation/project-adapter/`) und v1.0-Kriterien-Entwurf (`docs/release/V1_0_READINESS_CRITERIA_DRAFT.md` + `docs/roadmap/V1_0_PATH_SUMMARY.md`; Draft, kein v1.0-Claim).

**Update (WP-074):** Unabhängiger Lauf durchgeführt — neutralisierter Review eines privaten Referenzkontexts, **PASS WITH NOTES**, keine Blocker; Ventil nicht benötigt (`docs/validation/project-adapter/independent-runs/2026-07-06-private-reference-validation/`). Alle inhaltlichen blocking WPs sind damit erledigt.

**Update (WP-081):** Release Readiness Review abgeschlossen — **GO WITH NOTES**, keine Blocker (`docs/release/FOUNDATION_0_5_RELEASE_READINESS_REVIEW.md`).

**Update (WP-082):** Release Prep abgeschlossen — Release Notes (inkl. aller Known Limitations), Go/No-Go-Checkliste (20 Punkte), Tagging-Guide; Changelog auf `[0.5.0-foundation]` („tag pending"), README auf „vorbereitet". **Nächster Schritt (manuell, Human Maintainer):** Go/No-Go durchgehen → Tag `v0.5.0-foundation` → GitHub Pre-Release → danach Post-Release-Cleanup-WP. WP-076-Regel und öffentlicher Fixture-Lauf gehören in die 0.6-Planung. Kein Release bis zum Tagging, kein v1.0.
