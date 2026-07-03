# Project Brain – WP-035 Prompt Index & i18n Notes

## Was wurde gemacht?

- **Adapter-Prompt-Pfad entschieden:** `framework/prompts/project-adapter/` ist der einzige Adapter-Prompt-Ordner. Der v0.1-Prompt `CREATE_PROJECT_ADAPTER.md` wurde per `git mv` dorthin migriert (Frontmatter-Kategorie angepasst), der alte Ordner `project-adapters/` ist entfernt. Verweise (Prompt-Index, Prompt-Library-Overview, WP-034-Notes) aktualisiert.
- **Prompt-Index aktualisiert:** v0.2 mit allen drei Adapter-Prompts (Intake v0.2, Baseline v0.2, Kurzform v0.1 legacy) und DE/EN-Hinweiszeile.
- **DE/EN-Standard eingeführt:** `docs/i18n/DE_EN_LANGUAGE_STANDARD.md` — bilingual verfasst, definiert Formate (DE/EN-Sektionen oder `.de.md`/`.en.md`), geschützte englische Schlüsselwörter, schrittweise Umstellung ab Foundation 0.2 (0.1 bleibt frozen).
- **Translation Status Matrix eingeführt:** `docs/i18n/TRANSLATION_STATUS.md` — 16 Bereiche grob bewertet, Prioritätenliste für die Umstellung.
- README um `## Language / Sprache` ergänzt; Sprachstatus-Hinweis in Adapter-Guide und Adapter-Helper.

## Kernentscheidungen

- Keine Big-Bang-Übersetzung: Umstellung pro Work Package entlang der Prioritätenliste.
- Foundation-0.1-Altbestand (`adr/`, Import-/Release-History) bleibt sprachlich frozen.
- Sprachstatus-Hinweise nur in Einstiegsdokumenten, nicht in Templates (kein Lärm).

## Nächste empfohlene WPs

1. README DE-Spiegelung (höchste i18n-Priorität)
2. `docs/workflow/` EN-Fassung
3. Adapter-Praxistest (aus WP-034 offen)
4. ADR Consolidation (aus WP-033 offen)
