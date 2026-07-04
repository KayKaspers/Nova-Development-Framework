# Foundation 0.4 Scope Lock

> Beschlossen in NDF-WP-058 (2026-07-04). Ab jetzt gilt: Der Release-blocking Scope von Foundation 0.4 ist eingefroren. / Decided in NDF-WP-058; the release-blocking scope of Foundation 0.4 is frozen from now on.

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.4 verbindlich ein. Es verhindert, dass 0.4 zu groß wird oder unbemerkt Richtung v1.0 wächst, und trennt release-blocking, optional und deferred klar voneinander.

## EN – Purpose

This document freezes the Foundation 0.4 scope. It prevents 0.4 from growing too large or drifting toward v1.0, and clearly separates release-blocking, optional, and deferred work.

## DE – Scope-Entscheidung

Foundation 0.4 bleibt **Adoption Hardening & Public Usability**. Der Titel hat zwei Hälften, und der release-blocking Kern gibt jeder Hälfte genau **ein** konkretes Deliverable: Adoption Hardening = Adapter Conventions Polish (WP-059, an die WP-047-Findings gebunden); Public Usability = Prompt Library DE/EN Priority Pass (WP-060, die meistgenutzten öffentlichen Artefakte). Alles andere ist optional oder deferred. Foundation 0.4 ist ausdrücklich **kein v1.0** und **keine neue Produkt-/Website-Phase**.

## EN – Scope Decision

Foundation 0.4 stays **Adoption Hardening & Public Usability**. The title has two halves, and the release-blocking core gives each half exactly **one** concrete deliverable: adoption hardening = adapter conventions polish (WP-059, tied to the WP-047 findings); public usability = prompt library DE/EN priority pass (WP-060, the most-used public artifacts). Everything else is optional or deferred. Foundation 0.4 is explicitly **not v1.0** and **not a new product/website phase**.

## DE – Release-blocking Scope

| WP | Titel | Warum blocking |
|---|---|---|
| NDF-WP-058 | Foundation 0.4 Scope Lock | dieses Gate — ohne eingefrorenen Scope kein kontrollierter Release |
| NDF-WP-059 | Adapter Conventions Polish | Kern der Adoption Hardening; setzt WP-047-Backlog 1–3 um (Manifest-Format, Health-Score-Kategorien, Output-Pfad) plus Präfix-Beispiel und First-Safe-WP-Template |
| NDF-WP-060 | Prompt Library DE/EN Priority Pass | Kern der Public Usability; die höchstpriorisierte i18n-Lücke. **Eng gefasst:** „Priority Pass" = die meistgenutzten zentralen Prompts, nicht die gesamte Bibliothek |
| NDF-WP-067 | Foundation 0.4 Release Readiness Review | ehrliches Release-Gate |
| NDF-WP-068 | Foundation 0.4 Release Prep | Release Notes, Go/No-Go, Tagging-Vorbereitung |

**Downgrade-Ventil:** Falls WP-060 den definierten Priority-Umfang nicht vollständig erreicht, kann WP-067 (Readiness Review) es mit Begründung auf optional herabstufen — der Reststand muss dann in Release Notes und Translation-Status-Matrix ehrlich dokumentiert sein. So bleibt „Public Usability" im Blick, ohne den Release an einer i18n-Vollständigkeit aufzuhängen.

## EN – Release-blocking Scope

The five work packages above (scope lock, adapter conventions polish, prompt DE/EN priority pass, release readiness review, release prep). **Downgrade valve:** if WP-060 cannot fully reach its defined priority scope, WP-067 may downgrade it to optional with justification, provided the remaining state is documented honestly in the release notes and translation status matrix.

## DE – Optionaler Scope

| WP | Titel | Regel |
|---|---|---|
| NDF-WP-061 | Checklist Library DE/EN Priority Pass | should-have; Reststand ehrlich in der Matrix dokumentieren |
| NDF-WP-062 | Academy Band 1 Entry Pass | should-have; nur Einstiegskapitel, keine Vollübersetzung |
| NDF-WP-063 | ADR Policy & Structure Consolidation Plan | should-have; nur Policy/Plan, keine Migration |
| NDF-WP-066 | Public Quality Gate Maintenance Review | should-have; leichter v0.2-Nachlauf, keine große Härtung |

Optionale WPs dürfen den Release **nicht** blockieren. Sie werden versucht, wenn Kapazität da ist; sonst als bekannte Einschränkung in den Release Notes genannt und nach 0.5 verschoben.

## EN – Optional Scope

WP-061/062/063/066 are should-have and must **not** block the release; attempted if capacity allows, otherwise listed as known limitations and deferred beyond 0.4.

## DE – Deferred Scope

| WP | Titel | Bedingung für Aufnahme in 0.4 |
|---|---|---|
| NDF-WP-064 | Independent Adapter Validation Run | nur wenn eine unbeteiligte Person/Instanz verfügbar ist und alle blocking WPs fertig sind; sonst 0.5 |
| NDF-WP-065 | Docs Export / Website Readiness Concept | nur bei Restkapazität nach allen blocking WPs; sonst 0.5 (bereits aus 0.3 deferred) |

Deferred WPs dürfen den 0.4-Release **nie** blockieren.

## EN – Deferred Scope

WP-064 (independent adapter run — only if an uninvolved party is available and all blocking WPs are done) and WP-065 (docs export/website concept — only with spare capacity, otherwise 0.5). Deferred work packages never block the 0.4 release.

## DE – Ausdrücklich nicht Teil von Foundation 0.4

- keine v1.0-Reife behaupten
- keine vollständige Übersetzung des gesamten Repos erzwingen
- keine vollständige Academy-Überarbeitung erzwingen
- keine Website vollständig bauen
- keine Docs-Export-Pipeline implementieren
- keine CLI entwickeln
- keine History-Rewrite-Aktion
- keine privaten Projektbeispiele einführen
- keine ADR-Massenmigration ohne vorher beschlossene Policy
- keine neuen großen Framework-Konzepte ohne Scope-Review
- keine neuen produktiven Beispielanwendungen implementieren
- keine Release-Automation einführen

## EN – Explicitly Out of Scope for Foundation 0.4

No v1.0 claims; no forced full-repo translation; no forced full academy rework; no complete website; no docs-export pipeline implementation; no CLI; no history rewrite; no private project examples; no bulk ADR migration without a prior policy; no new large framework concepts without a scope review; no new productive example applications; no release automation.

## DE – Abhängigkeiten

```text
058 (Scope Lock, dieses Gate)
→ 059 (Adapter Conventions Polish) ‖ 060 (Prompt DE/EN)     [Kern-Hardening + Usability]
→ 061 / 062 / 063 / 066 (optional, beliebige Reihenfolge)
→ 064 / 065 (deferred, nur bei Bedingungserfüllung)
→ 067 → 068 (Release-Strecke; startet, sobald 059 und 060 fertig sind)
```

Findings aus WP-059/WP-064 erzeugen kleine Folge-WPs. Diese sind release-blocking **nur**, wenn sie die Adoptionshärtung selbst betreffen; sonst bekannte Einschränkung.

## EN – Dependencies

Scope lock gates everything; 059 ‖ 060 form the core; optional WPs in any order; deferred WPs only on condition; 067 → 068 close the release (starting once 059 and 060 are done). Findings from WP-059/WP-064 spawn small follow-ups — release-blocking only if they affect adoption hardening itself.

## DE – Änderungsregeln nach Scope Lock

1. Neue Release-blocking WPs erfordern eine ausdrückliche Scope-Lock-Änderung: Nova-(ChatGPT)-Review + Freigabe durch den Human Maintainer + Update dieses Dokuments.
2. Optionale WPs dürfen jederzeit verschoben, aber nicht stillschweigend zu blocking erklärt werden.
3. Herabstufen (blocking → optional) ist nur über WP-067 (Readiness Review) mit Begründung zulässig — insbesondere das dokumentierte Downgrade-Ventil für WP-060.
4. Jede Scope-Änderung wird im Project Brain protokolliert.

## EN – Change Rules After Scope Lock

1. New release-blocking work packages require an explicit scope lock change: Nova (ChatGPT) review + human maintainer approval + update of this document.
2. Optional work packages may be deferred at any time but never silently promoted to blocking.
3. Downgrading (blocking → optional) is only allowed via WP-067 (readiness review) with justification — including the documented WP-060 downgrade valve.
4. Every scope change is recorded in the project brain.

## DE – Release-Gate-Regeln

`v0.4.0-foundation` darf erst vorbereitet werden (WP-068), wenn:

1. alle Release-blocking WPs abgeschlossen sind (058–060, 067 mit GO/GO WITH NOTES; WP-060 ggf. dokumentiert herabgestuft),
2. die Invarianten durchgehend gelten (Public Quality Gate strict grün, new-file neutrality check aktiv, keine privaten Bezüge/Suchmuster, Tags 0.1–0.3 unverändert),
3. der Stand der optionalen und deferred WPs ehrlich in Release Notes und Translation-Status-Matrix dokumentiert ist.

## EN – Release Gate Rules

`v0.4.0-foundation` may only be prepared (WP-068) once all release-blocking work packages are complete (058–060, 067 with GO/GO WITH NOTES; WP-060 possibly downgraded with documentation), the invariants hold throughout (public quality gate strict green, new-file neutrality check active, no private references or search patterns, tags 0.1–0.3 untouched), and the state of the optional and deferred work packages is honestly documented in the release notes and the translation status matrix.
