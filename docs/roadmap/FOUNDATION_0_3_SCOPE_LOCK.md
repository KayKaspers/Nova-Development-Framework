# Foundation 0.3 Scope Lock

> Beschlossen in NDF-WP-045 (2026-07-03). Ab jetzt gilt: Der Release-blocking Scope von Foundation 0.3 ist eingefroren. / Decided in NDF-WP-045; the release-blocking scope of Foundation 0.3 is frozen from now on.

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.3 verbindlich ein. Es verhindert das unkontrollierte Scope-Wachstum, das Foundation 0.2 erlebt hat, und definiert, was den Release `v0.3.0-foundation` blockiert, was optional ist und was bewusst nach 0.3 verschoben wird.

## EN – Purpose

This document freezes the Foundation 0.3 scope. It prevents the uncontrolled scope growth Foundation 0.2 experienced and defines what blocks the `v0.3.0-foundation` release, what is optional, and what is deliberately deferred beyond 0.3.

## DE – Scope-Entscheidung

Foundation 0.3 bleibt ein **Adoption Release**: Der einzige Release-Kernbeweis ist, dass ein externer Nutzer NDF anhand des neutralen Beispielprojekts praktisch übernehmen kann. Alles andere ist Unterstützung dieses Beweises (Quality Gate v0.2) oder Qualitätsverbesserung (i18n, Academy, ADR-Policy) — Letzteres blockiert den Release nicht, solange der Reststand ehrlich dokumentiert ist. Foundation 0.3 ist ausdrücklich **kein v1.0**.

## EN – Scope Decision

Foundation 0.3 stays an **adoption release**: the only release-defining proof is that an external user can practically adopt NDF using the neutral example project. Everything else either supports that proof (quality gate v0.2) or improves quality (i18n, academy, ADR policy) — the latter does not block the release as long as the remaining state is honestly documented. Foundation 0.3 is explicitly **not v1.0**.

## DE – Release-blocking Scope

| WP | Titel | Warum blocking |
|---|---|---|
| NDF-WP-045 | Foundation 0.3 Scope Lock | dieses Gate — ohne eingefrorenen Scope kein kontrollierter Release |
| NDF-WP-046 | Neutral Example Project v0.2 | ohne realistisches Zielprojekt kein Adoptionsbeweis |
| NDF-WP-047 | Project Adapter Practical Validation | der Kernbeweis von 0.3 |
| NDF-WP-052 | Public Quality Gate v0.2 | schützt die Neutralitäts-Invarianten inkl. der in 0.2 gefundenen Fehlerklassen |
| NDF-WP-054 | Foundation 0.3 Release Readiness Review | ehrliches Release-Gate |
| NDF-WP-055 | Foundation 0.3 Release Prep | Release Notes, Go/No-Go, Tagging-Vorbereitung |

## EN – Release-blocking Scope

The six work packages above (scope lock, neutral example project v0.2, adapter practical validation, quality gate v0.2, release readiness review, release prep). Deliberately small: the adoption proof plus its safety net plus the release track.

## DE – Optionaler Scope

| WP | Titel | Regel |
|---|---|---|
| NDF-WP-048 | Prompt Library Full DE/EN Pass | should-have; Reststand muss in der Translation-Status-Matrix ehrlich dokumentiert sein |
| NDF-WP-049 | Checklist Library Full DE/EN Pass | should-have; gleiche Regel |
| NDF-WP-050 | Academy Band 1 DE/EN Entry Pass | should-have; nur Einstiegskapitel, keine Vollübersetzung |
| NDF-WP-051 | ADR Structure Consolidation Plan | should-have; nur Policy/Plan, keine Migration |

Optionale WPs dürfen den Release **nicht** blockieren. Werden sie nicht fertig, werden sie in den Release Notes als bekannte Einschränkung genannt und nach 0.3 verschoben.

## EN – Optional Scope

WP-048/049/050/051 are should-have. Optional work packages must **not** block the release; if unfinished, they are listed as known limitations in the release notes and deferred beyond 0.3.

## DE – Ausdrücklich nicht Teil von Foundation 0.3

- keine v1.0-Reife behaupten
- keine vollständige Academy-Übersetzung erzwingen
- keine Website vollständig bauen
- keine CLI entwickeln
- keine Export-Pipeline implementieren
- keine History-Rewrite-Aktion
- keine privaten Projektbeispiele einführen
- keine ADR-Massenmigration ohne vorher beschlossene Policy
- keine neuen großen Framework-Konzepte ohne Scope-Review
- **NDF-WP-053 (Docs Export / Website Readiness Concept): auf „deferred candidate" herabgestuft** — startet in 0.3 nur, wenn alle Release-blocking WPs abgeschlossen sind und Kapazität übrig ist; sonst Foundation 0.4.

## EN – Explicitly Out of Scope for Foundation 0.3

No v1.0 claims, no forced full academy translation, no complete website, no CLI, no export pipeline implementation, no history rewrite, no private project examples, no bulk ADR migration without a prior policy, no new large framework concepts without a scope review. **NDF-WP-053 is downgraded to a deferred candidate** — it only starts in 0.3 if all release-blocking work packages are complete and capacity remains; otherwise Foundation 0.4.

## DE – Abhängigkeiten

```text
045 (Scope Lock, dieses Gate)
→ 046 → 047                    (Adoptionsbeweis; 052 parallel möglich)
→ 048 / 049 / 050 / 051        (optional, beliebige Reihenfolge)
→ 054 → 055                    (Release-Strecke; startet, sobald alle blocking WPs außer 054/055 fertig sind)
```

Findings aus WP-047 erzeugen kleine Folge-WPs. Diese sind release-blocking **nur**, wenn sie den Adoptionsbeweis selbst betreffen; sonst bekannte Einschränkung.

## EN – Dependencies

Scope lock gates everything; 046→047 is the adoption proof (052 may run in parallel); optional WPs in any order; 054→055 close the release. Findings from WP-047 spawn small follow-ups — release-blocking **only** if they affect the adoption proof itself, otherwise documented as known limitations.

## DE – Änderungsregeln nach Scope Lock

1. Neue Release-blocking WPs erfordern eine ausdrückliche Scope-Lock-Änderung: Nova-(ChatGPT)-Review + Freigabe durch den Human Maintainer + Update dieses Dokuments.
2. Optionale WPs dürfen jederzeit verschoben, aber nicht stillschweigend zu blocking erklärt werden.
3. Herabstufen (blocking → optional) ist nur über WP-054 (Readiness Review) mit Begründung zulässig.
4. Jede Scope-Änderung wird im Project Brain protokolliert.

## EN – Change Rules After Scope Lock

1. New release-blocking work packages require an explicit scope lock change: Nova (ChatGPT) review + human maintainer approval + update of this document.
2. Optional work packages may be deferred at any time but never silently promoted to blocking.
3. Downgrading (blocking → optional) is only allowed via WP-054 (readiness review) with justification.
4. Every scope change is recorded in the project brain.

## DE – Release-Gate-Regeln

`v0.3.0-foundation` darf erst vorbereitet werden (WP-055), wenn:

1. alle sechs Release-blocking WPs abgeschlossen sind (045–047, 052, 054 mit GO/GO WITH NOTES),
2. die Invarianten durchgehend gelten (Public Quality Gate strict grün, keine privaten Bezüge/Suchmuster, Tags 0.1/0.2 unverändert),
3. der Stand der optionalen WPs ehrlich in Release Notes und Translation-Status-Matrix dokumentiert ist.

## EN – Release Gate Rules

`v0.3.0-foundation` may only be prepared (WP-055) once all six release-blocking work packages are complete (045–047, 052, 054 with GO/GO WITH NOTES), the invariants hold throughout (public quality gate strict green, no private references or search patterns, tags 0.1/0.2 untouched), and the state of the optional work packages is honestly documented in the release notes and the translation status matrix.
