# Project Brain – WP-085 Foundation 0.6 Scope Lock Notes

## Ausgangslage nach WP-084

Foundation 0.6 geplant (Adoption Confidence & Governance Hardening), 12 Kandidaten mit vorläufigen Empfehlungen. Konsistenzprüfung sauber: 0.6 nirgends als released, v1.0 nirgends behauptet, alle sechs WP-083-Kandidaten übernommen, kein Scope Creep.

## Finale Scope-Entscheidung

Nova-Empfehlung kritisch geprüft und **unverändert übernommen** (deckt sich mit der WP-084-Empfehlung; kleiner Kern nach 0.4/0.5-Muster):

- **Release-blocking:** 085 (Gate, done), 086 (ADR Decision), 088 (Public Validation Run, mit Ventil), 089 (Gate Maintenance inkl. CI-Denylist-Bewertung), 094 (Readiness, entscheidet Ventil), 095 (Release Prep).
- **Optional:** 087 (nur falls nötig — skipped, wenn 088 mit WP-073-Unterlagen startet), 090 (merged/conditional in 089), 091 (Checklist DE/EN), 092 (Academy), 093 (v1.x Policy Draft, v1.0-tracked).
- **Deferred:** Website, volle i18n, ADR-Massenmigration, v1.0-RC, großer Rewrite, App-Features.

## ADR-Policy-Entscheidungspflicht (WP-086)

Release-blocking mit hartem Entscheidungszwang gemäß 0.5-Sonderregel: Zulässig sind nur **A) Minimal-Policy angenommen** oder **B) ehrlich gestrichen mit Begründung** (schließt dann das offene v1.0-Kriterium als „dokumentiert gestrichen"); C) REWORK/STOP nur, wenn beides unmöglich. „Defer again"/„later" ist in jeder Formulierung unzulässig.

## WP-088-Ventil

8-Bedingungen-Ventil über WP-094 (0.5-Muster übernommen und angepasst): tatsächlich versucht/nachvollziehbar vorbereitet; ausführbarer öffentlicher Plan; Hinderungsgrund neutral dokumentiert; nicht durch kleine Doku-Korrekturen lösbar; keine privaten Daten im Pfad; Known Limitation in Release Notes; bleibt v1.0-tracked; Maintainer-Bestätigung im Go/No-Go. **Plus Missbrauchsklausel:** kein Überspringen unbequemer Arbeit — ist WP-088 mit vertretbarem Aufwand möglich, bleibt es blocking. Ventil gilt nur für 088.

## WP-090-Entscheidung

**Merged/conditional:** CI-Denylist-Wirksamkeitsnachweis ist Teil von WP-089; WP-090 wird nur eigenständig, wenn WP-089 ein separates Nachweis-Artefakt ausdrücklich für nötig erklärt.

## Änderungsregeln

Dreistufig im Scope Lock verankert: erlaubt (kleine Doku-/Link-/Status-Korrekturen, Gate-Fixes, Review-Fixes) / nur mit expliziter Nova-+Maintainer-Entscheidung (neue blocking WPs, Downgrades außerhalb des Ventils, neue Dokumentfamilien, Tooling/CI, Ventil-Änderungen) / verboten (stilles ADR-Verschieben, v1.0-RC, Release Prep vor WP-094, Agent-Tagging).

## v1.0-Abgrenzung

Durchgängig: 0.6 „reduziert v1.0-Unsicherheit", mehr nicht — auch bei Erfolg von 086/088/093 keine v1.0-Behauptung; v1.0 nur über späteren eigenen Zyklus.

## Nächste WP

**NDF-WP-086 – ADR Policy Decision** (parallel sinnvoll: WP-088-Vorbereitungsbedarf prüfen oder WP-089).
