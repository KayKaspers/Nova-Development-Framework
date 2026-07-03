# Translation Status / Übersetzungsstatus

## Zweck / Purpose

Grobe Übersicht, welche Bereiche des NDF bereits DE/EN-tauglich sind und wo Folgearbeit nötig ist. Bewertet werden Bereiche, nicht einzelne Dateien. / Rough overview of which NDF areas are already DE/EN-ready and where follow-up work is needed. Areas are assessed, not individual files.

## Statusklassen / Status classes

| Status | Bedeutung / Meaning |
|---|---|
| `bilingual` | DE und EN vorhanden / both DE and EN present |
| `de-only` | nur Deutsch / German only |
| `en-only` | nur Englisch / English only |
| `mixed` | DE und EN gemischt ohne System / mixed without clear structure |
| `needs-review` | Sprachstatus unklar oder Umstellung geplant / unclear or transition planned |
| `frozen` | Foundation-0.1-Altbestand, bleibt unverändert / frozen 0.1 legacy |

## Statusmatrix / Status matrix

| Bereich / Area | Status | Anmerkung / Note |
|---|---|---|
| `README.md` | bilingual | seit WP-036 vollständig DE/EN gespiegelt / fully DE/EN mirrored since WP-036 |
| `CHANGELOG.md` | en-only | Format beibehalten / keep format |
| `docs/project-starter/` | mixed | v0.2-Guide DE, ältere Flows DE; EN-Fassungen offen |
| `docs/toolkit/` | mixed | Toolkit-Kern EN (Destructive Action Toolkit), Helper DE |
| `docs/workflow/` | mixed | seit WP-037: Rollen-Doku bilingual, NOVA_CHATGPT_ROLE bilingual, Rest DE mit Sprachstatus / roles doc + Nova role doc bilingual since WP-037, rest German with language notes |
| `docs/repository/` | mixed | Quality-Gate-Doku DE, Policies DE/EN gemischt |
| `docs/roadmap/` | mixed | Progress-Dateien DE/EN gemischt; niedrige Priorität / low priority |
| `framework/prompts/` | mixed | Frontmatter EN, Inhalte teils DE; neue Prompts zuerst angleichen |
| `framework/templates/` | mixed | Feldnamen EN, Anleitungen DE; für öffentliche Nutzung EN ergänzen |
| `framework/checklists/` | de-only | EN-Fassungen offen |
| `docs/academy/` | de-only | Lernmaterial; Übersetzung als eigenes WP / translation as its own WP |
| `docs/adr/` | mixed | 0027–0030 EN, frühe thematische DE/EN gemischt |
| `adr/` | frozen | Foundation 0.1, bleibt unverändert / stays unchanged |
| `project-brain/` | mixed | internes Arbeitsgedächtnis; niedrigste Priorität / lowest priority |
| `examples/minimal-ndf-project/` | de-only | Beispielprojekt; EN-Fassung sinnvoll für öffentliche Nutzer |
| `docs/i18n/` | bilingual | dieser Bereich / this area |

## Regeln / Rules

- Foundation-0.1-Altbestand (`adr/`, `docs/import-history/`, `docs/release/history/`) bleibt `frozen`.
- Neue Foundation-0.2-Dokumente starten als `needs-review` oder `mixed`, bis sie bilingual sind.
- Keine Big-Bang-Übersetzung — Umstellung pro Work Package.

## Empfohlene Reihenfolge / Recommended order

1. ~~`README.md` DE-Spiegelung~~ — erledigt in WP-036 / done in WP-036
2. Workflow docs full DE/EN alignment (Kernprozess; teilweise erledigt in WP-037 / partially done in WP-037)
3. `framework/prompts/` + `framework/checklists/` EN (öffentliche Nutzbarkeit)
4. `docs/project-starter/` EN (Adapter/Onboarding)
5. `docs/academy/` EN (eigenes größeres WP)
