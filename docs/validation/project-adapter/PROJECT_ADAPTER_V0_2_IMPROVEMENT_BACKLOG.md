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

## Mögliche Folge-WPs

- „Project Adapter Conventions Polish" (docs-only; Punkte 1–3) — vor NDF-WP-054 empfohlen.
- Punkte 4–5 als Sammel-WP nach 0.3 oder huckepack im Conventions-Polish.
- Punkt 6 nach 0.3 (externe Mitwirkung nötig).
