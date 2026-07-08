# ADR-0031: v1.x Compatibility Policy

## Status

Accepted

## Date

2026-07-08

## Context

Der v1.0 Readiness Criteria Draft (NDF-WP-079) führt die **v1.x-Versionierungs-/Kompatibilitätszusage** als klar `not met` blocking-Kriterium — die bewusste Lücke „Was verspricht v1.x an Kompatibilität?". Foundation 0.7 (Scope Lock, NDF-WP-098) macht die Entscheidung dazu release-blocking (NDF-WP-100) und benennt ADR-0031 als bevorzugten Pfad, weil Kompatibilitäts-, Release- und Versionierungsregeln dauerhafte Governance-Wirkung haben und laut ADR-Policy (`ADR_POLICY.md`) einer ADR bedürfen.

Diese ADR definiert den **Governance-Rahmen** für v1.x-Kompatibilität. Sie macht NDF **nicht** v1.0-reif und aktiviert **keine** vollständige v1.x-Kompatibilitätszusage. Foundation 0.7 bleibt ein Foundation-Pre-Release; die volle v1.x-Zusage tritt erst mit einem späteren v1.0-Release in Kraft.

## Decision

NDF nimmt eine **v1.x Compatibility Policy** als Governance-Rahmen an: eine Kategorisierung öffentlicher NDF-Bestandteile nach Kompatibilitätsstatus, Regeln für Breaking Changes und Deprecations, sowie eine klare Aktivierungsschwelle (volle Zusage erst ab v1.0). Diese ADR ist die Source of Truth; ein separates Policy-Dokument wird nicht erstellt.

## Compatibility Policy

### Before v1.0

Vor v1.0 gilt **keine** verbindliche Kompatibilitätsgarantie. Foundation-Releases sind Pre-Releases; Struktur, Konventionen und Prompts können sich additiv oder verändernd weiterentwickeln. Diese Policy legt fest, **wie** Kompatibilität künftig regiert wird — sie verspricht sie noch nicht. Bestehende Foundation-Tags (v0.1–v0.6) bleiben eingefroren.

### Compatibility Categories

Öffentliche NDF-Bestandteile werden einer von fünf Kategorien zugeordnet:

- **Stable Candidate** — voraussichtlich stabil, Kandidat für die v1.x-Zusage; Änderungen nur mit Breaking-Change-Regel.
- **Governed** — durch dokumentierte Governance (ADR/Policy) geregelt; Änderungen laufen über den jeweiligen Governance-Pfad.
- **Experimental** — bewusst offen/vorläufig; keine Kompatibilitätserwartung.
- **Deprecated** — nur mit ausdrücklichem Deprecation-Vermerk; Nachfolger benannt.
- **Out of Scope** — nicht Teil der öffentlichen NDF-Kompatibilität (private/projektspezifische Inhalte, Secrets, Domains).

### Stable Candidate

Voraussichtlich stabil, Kandidaten für die v1.x-Zusage (Bestätigung erfolgt ausschließlich im v1.0-Zyklus, u. a. gestützt auf die Convention Stability Review NDF-WP-101):

- Kern-Rollenmodell (Nova (ChatGPT) → Implementation Agent → Human Maintainer)
- Work-Package-Flow und der Review-Entscheidungswert GO / GO WITH NOTES / REWORK / STOP
- Public-Neutrality-Invarianten (keine privaten Bezüge, new-file neutrality check)
- Human-Maintainer-Release-Kontrolle (nur der Mensch committet/taggt/released)

### Governed

Durch dokumentierte Governance geregelt; Änderungen über den jeweiligen Pfad:

- ADR-Policy (`ADR_POLICY.md`)
- Release-Vorbereitungsmuster (Planning → Scope Lock → Readiness → Prep → manueller Tag → Cleanup)
- Project Adapter Conventions (`PROJECT_ADAPTER_CONVENTIONS.md`)
- Public-Quality-Gate-Erwartungen (v0.2, WP-089 Evidence strong)

### Experimental

Bewusst offen; keine Kompatibilitätserwartung:

- optionale Academy-Materialien
- Konzepte ohne Umsetzung (Docs Export / Website)
- nicht gelockte künftige Phasen-Kandidaten
- frühe Context-Economy-Artefakte

### Deprecated

Aktuell keine deprecated öffentlichen Bestandteile. Deprecation nur mit ausdrücklichem Vermerk (Status `Deprecated` je Artefakt/ADR) und benanntem Nachfolger.

### Out of Scope

Nicht Teil der öffentlichen NDF-Kompatibilität: private projektspezifische Workflows, private Domains, private Deployment-Details, Secrets, projektspezifische Anpassungen außerhalb des öffentlichen NDF.

### Breaking Changes

Vor v1.0: additive Änderung bevorzugt; eine breaking Änderung an einem **Stable Candidate** oder **Governed**-Bestandteil erfordert einen dokumentierten Vermerk (Changelog + ggf. ADR/Supersede) und, falls sinnvoll, eine Migrationsnotiz. Ab v1.0: breaking Änderungen an durch die Zusage abgedeckten Bestandteilen nur mit Major-Version-Wechsel.

### Deprecations

Ein Bestandteil wird zunächst als `Deprecated` markiert (mit Nachfolger und Zeitraum-Hinweis), bevor er entfernt oder ersetzt wird. Kein stilles Entfernen von öffentlich dokumentierten Bestandteilen.

### Migration Notes

Wo eine Änderung Nutzer betrifft, wird eine kurze Migrationsnotiz in Changelog/Release Notes geführt. Vor v1.0 sind Migrationsnotizen best-effort; ab v1.0 verpflichtend für abgedeckte Bestandteile.

### Activation of v1.x Compatibility

Die **volle v1.x-Kompatibilitätszusage** tritt **erst mit einem späteren v1.0-Release** in Kraft — entschieden im eigenen v1.0-Zyklus (Scope Lock → Readiness → Prep → Maintainer-Freigabe). Bis dahin ist diese Policy ein Governance-Rahmen ohne aktive Garantie. Foundation 0.7 aktiviert keine Zusage.

### Public Quality Gate and Neutrality

Der Public Quality Gate v0.2 und die Public-Neutrality-Invarianten gelten unverändert und sind selbst **Stable Candidate**. Kein Kompatibilitäts-Bestandteil darf private Namen, echte Domains, Kontaktwege oder Secret-Werte enthalten (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden).

### Role Boundaries

Nova (ChatGPT) plant und reviewt; der Implementation Agent implementiert nur beauftragte Work Packages; der Human Maintainer bleibt finaler Release-Owner und einziger, der committet, taggt und released. Diese Grenzen sind **Stable Candidate**.

## Consequences

- Das v1.0-Kriterium „v1.x-Versionierungs-/Kompatibilitätszusage definiert" steigt von `not met` auf **`met with notes`**: Der Governance-Rahmen ist angenommen; die **aktive** volle Zusage bleibt v1.0-tracked.
- Künftige Änderungen an Stable-Candidate-/Governed-Bestandteilen laufen über die hier definierten Regeln.
- ADR-0031 ist die Source of Truth; kein separates Policy-Dokument.

## Non-Goals

Keine v1.0-Reife-Behauptung; keine aktive v1.x-Kompatibilitätsgarantie vor v1.0; kein v1.0 Scope Lock; keine ADR-Massenmigration; keine Änderung eingefrorener Tags oder historischer ADRs; keine privaten Beispiele.

## Follow-ups

- NDF-WP-101 (Convention Stability Review) prüft, ob die Adapter-Konventionen als Stable Candidate belastbar sind.
- Der spätere v1.0-Zyklus aktiviert die volle Zusage und bestätigt die Stable-Candidate-Liste.

## Related Work Packages

NDF-WP-079 (v1.0 Readiness Criteria Draft), NDF-WP-093 (v1.x Compatibility Policy Draft candidate), NDF-WP-098 (Foundation 0.7 Scope Lock), NDF-WP-100 (this decision), NDF-WP-101 (Convention Stability Review).

## Public Neutrality Check

Keine privaten Projekt-/Personennamen, keine echten Domains oder Kontaktwege, keine Secret-Werte. Nur neutrale NDF-Rollen- und Governance-Begriffe.
