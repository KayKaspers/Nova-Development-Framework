# Project Adapter v0.2 – Improvement Backlog (aus NDF-WP-047)

Abgeleitet aus der praktischen Validierung am SampleProject-Fixture. Keine Umsetzung in WP-047 — nur Klassifizierung.

## Release-blocking für Foundation 0.3

**Keine.** Alle Punkte sind Konventions-/Doku-Verbesserungen; der Adoptionsbeweis steht.

## Should-have (empfohlen vor dem 0.3-Release, kleines docs-only-WP)

| # | Verbesserung | Beleg aus der Validierung |
|---|---|---|
| 1 | **Manifest-Formatkonvention klären:** wann `PROJECT_MANIFEST.yaml` (Zielprojekt) vs. Markdown (Doku/Validierung); Guide + Template angleichen | Validierung musste .md mit YAML-Block improvisieren |
| 2 | **Health-Score-Template erweitern:** Kategorien „Operations/Backup" und „i18n" ergänzen (oder als optionale Zusatzkategorien dokumentieren) | beide mussten ad hoc ergänzt werden |
| 3 | **Output-Pfad-Konvention dokumentieren:** Zielprojekt (`project-system/…`) vs. Validierungs-/Demo-Lauf (`adapter-validation-output/`) im Guide definieren | Pfad musste erfunden werden |

## Later

| # | Verbesserung | Beleg |
|---|---|---|
| 4 | **Queue-Template-Präfix entschärfen:** Beispielpräfix von `SP-WP` auf z. B. `XY-WP` ändern, damit es nicht mit „SampleProject" kollidiert und die Eigenpräfix-Regel klarer wird | Kollision in dieser Validierung |
| 5 | **First-Safe-WP-Template ergänzen** (`framework/templates/project-adapter/FIRST_SAFE_WORK_PACKAGE_TEMPLATE.md`) | Datei musste frei formuliert werden |
| 6 | **Unabhängiger Testlauf:** Adapter durch einen nicht am Bau beteiligten Nutzer/Agent durchspielen lassen | Selbstvalidierungs-Bias dieser Runde |

## Status (Update NDF-WP-059, Foundation 0.4)

- **Punkte 1–3 (should-have): addressed.** In WP-059 umgesetzt über `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` (Manifest-Konvention, Health-Score-Kategorien, Output-Pfad-Konvention) sowie aktualisierte Templates (Health Score, Output Structure, Review Report) und Checkliste.
- **Punkt 4 (Präfix-Beispiel): addressed.** Queue-Template nutzt jetzt das Platzhalter-Präfix `XY-WP` statt `SP-WP`.
- **Punkt 5 (First-Safe-WP-Template): addressed.** `framework/templates/project-adapter/FIRST_SAFE_WORK_PACKAGE_TEMPLATE.md` erstellt.
- **Punkt 6 (unabhängiger Testlauf): weiterhin later** — Foundation 0.4 deferred candidate (NDF-WP-064, nur wenn Unbeteiligte verfügbar).

Die WP-047-Validierung selbst bleibt historisch **PASS WITH NOTES**; diese Konventionen sind Folgearbeit daraus.
