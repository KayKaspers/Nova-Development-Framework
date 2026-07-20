# Skills Real-use and Context Efficiency Review

> Work Package: `NDF-WP-151` — Skills Real-use and Context Efficiency Review
> Type: review-only / docs-only (measurement & decision preparation, no implementation)
> Sprachstatus / Language status: EN mit deutschen Kernaussagen. / English with German key statements.

## 1. Status / Ergebnis

**GO WITH NOTES – skills real-use and context efficiency review completed.** WP-151 wurde von „Skills Real-use Review" zu **„Skills Real-use and Context Efficiency Review"** präzisiert (öffentlich reconciled). Kernfrage: *Wie muss NDF verändert werden, damit mehrere aufeinanderfolgende Work Packages und Reviews mit Claude bearbeitet werden können, ohne dass nach wenigen Prompts das Nutzungslimit erreicht wird?* Ergebnis: Das Problem ist real und teilweise belegt; die Antwort ist ein **additives Lean-/Budget-/Handoff-Modell**, kein Umbau. Entscheidungsvorlage für WP-152 liegt vor (Empfehlung: **GO mit reduziertem, additivem Scope + project-local Pilot**). Keine neuen Skills, keine Skill-Entfernung/-Umbenennung, kein v1.1 Scope Lock, kein Release Prep. ADR-0031/0032 unverändert.

## 2. A – Repository-Reconciliation

**Autoritativ:** lokale Git-Daten (Tags `v1.0.0` → `9dcadc1` annotated, `v1.0.0-rc.1` → `4beab84`; HEAD `ebf716c`), `CHANGELOG.md` (inkl. `[1.0.0]` und `[Unreleased] – v1.1 Planning`), [V1_1_PLAN.md](../../roadmap/V1_1_PLAN.md), [V1_0_PATH_SUMMARY.md](../../roadmap/V1_0_PATH_SUMMARY.md), Context Pack / Next Phase, `.claude/skills/README.md` (38 Skills), ADR-0031/0032.

**Befunde:**

| Dokument | Befund | Maßnahme |
|---|---|---|
| `README.md` | **veraltet:** Status endete bei „Foundation 0.9 scope-locked … nicht released, kein v1.0"; zweimal „NDF ist bewusst noch kein v1.0"; Workflow-Zeile verwies auf „geplantes Skills-MVP (Design)" | **minimal korrigiert** (0.9 released, v1.0.0 final, v1.x aktiv, 38 Skills, v1.1 planning, WP-151 neuer Titel) |
| `CHANGELOG.md` | `[Unreleased]` vorhanden (WP-150), aber die drei committeten CoreOps-Adoptionen (A/B/C) fehlten (waren dort Forbidden Files) | **minimal ergänzt** (eine kompakte Adoptions-Zeile + WP-151-Zeile) |
| `V1_1_PLAN.md` | WP-151 unter altem Titel „Skills Real-use Review" | **minimal präzisiert** (neuer Titel + Context-Efficiency-Scope) |
| Context Pack / Next Phase | Next Step unter altem WP-151-Titel | **minimal reconciled** |
| `V1_0_PATH_SUMMARY.md` | konsistent bis WP-149/150; kein WP-151-Fehler | keine Änderung nötig |
| Skills README / ADR-0031 / ADR-0032 | konsistent (38 Skills; ADRs unverändert) | keine Änderung |

Zusätzlich konsistent, aber erwähnenswert: die drei CoreOps-Adoptions-Commits (`1ebffa6`, `e894c6f`, `ebf716c`) liegen nach WP-150 und sind additive docs-only Governance (Prompt-Safety-Baseline, Skill-Provenance/Integrity-Lock, Decision/Status- + Framework-Tailoring-Guidance).

## 3. B – Aktuelles Token-/Kontextproblem

**Belegte Ursachen** (aus realen v1.0-/Adoptions-Sessions dieses Repos):

1. **WP-Prompts tragen den vollen stabilen Rahmen jedes Mal neu:** Rollenmodell, harte Grenzen, Git-/Netz-/Secret-Regeln, Neutralitätsregeln, Rückmelde-Template und Compact-Context-Summary-Template werden pro Prompt wiederholt — obwohl sie seit WP-134 skill-getragen sein sollten. Reale WP-Prompts dieser Phase (140–151, Adoptions) waren durchgehend Full-Prompts mit vollständigen Wiederholungen.
2. **Rückmeldungen sind sehr lang:** das verbindliche Rückmelde-Format (15–17 Abschnitte + Compact Context Summary) erzeugt pro WP mehrere tausend Wörter Ausgabe — auch bei kleinen WPs und sogar bei Blocked-Reports.
3. **Status-Dokumente wachsen additiv:** Context Pack, Next Phase, Path Summary und WP-Queue akkumulieren Historie; jede „minimale" Fortschreibung liest und schreibt lange Absätze.
4. **Session-Limits wurden real erreicht:** in dieser Entwicklungsphase gab es mehrfach Modell-/Limit-Unterbrechungen mit Resume-Prompts (dokumentierte Resume-WPs) — der Schmerz ist kein Konstrukt.

**Plausible Hypothesen** (konsistent, aber nicht einzeln gemessen):

- 38 Skill-Beschreibungen erzeugen Kontextkosten, wenn sie als „aktiv nutzen"-Liste in Prompts stehen (10–15 Skills pro Prompt aufgezählt), statt selektiv referenziert zu werden.
- Review-Prompts wiederholen Kontext, den die Rückmeldung des Vor-WPs bereits enthielt (doppelte Übertragung Prompt ↔ Rückmeldung).
- Es fehlt ein leichtes Handoff-Artefakt: Fortsetzungen laden faktisch die Chat-Historie oder große Status-Dokumente statt eines kleinen Wiederaufnahme-Blocks.
- Dauerhafter, aktueller und aufgabenspezifischer Kontext sind konzeptionell getrennt (Context Economy Layer 1–5), aber die realen Prompts trennen sie nicht — sie liefern alles zusammen.

**Noch zu messende Ursachen:** tatsächlicher Token-Anteil der Skill-Aufzählungen; tatsächlicher Anteil der Rückmelde-Templates am Sessionverbrauch; Kompressionsverlust-Risiko bei kürzeren Rückmeldungen; realer Effekt eines Handoff-Blocks auf Folge-Sessions.

## 4. C – Mess- und Evidenzmodell

Acht Messfälle; je Fall werden bewertet: Promptgröße, geladener Kontext, referenzierte vs. vollständig gelesene Dateien, wiederholte Standardtexte, Anzahl aktiv genutzter Skills, Rückfragen, Informationsverlust, Reviewqualität, Wiederaufnahmefähigkeit.

| # | Messfall | Baseline-Beobachtung (qualitativ, aus realen Sessions) |
|---|---|---|
| M1 | neues kleines WP | Prompt groß trotz kleinem Scope (voller Rahmen); 0–2 Dateien nötig, aber Standardtexte dominieren |
| M2 | großes WP in bestehendem Projekt | Prompt + viele Dateien; Full-Read statt gezielter Abschnitte |
| M3 | Fortsetzung nach Unterbrechung | Resume-Prompt wiederholt den Original-Prompt fast vollständig |
| M4 | Implementierungsrückmeldung | 15+ Pflichtabschnitte, auch bei kleinen Diffs |
| M5 | Nova-Review | Review-Prompt dupliziert die vorige Rückmeldung |
| M6 | Scope-Change | neuer Full-Prompt statt Delta |
| M7 | Fehlerkorrektur | voller Rahmen für punktuelle Korrektur |
| M8 | projektübergreifende Übergabe | zwei Repos read-only + voller Rahmen (real: Adoptions-WPs) |

**Baseline:** der heutige Full-Prompt-Stil (WP-140…151) je Fall. **Zielkorridor:** M1/M3/M7 sollen mit einem Lean-Prompt (Kernelemente + Referenzen) auskommen; M4-Rückmeldungen sollen für kleine WPs auf einen Kurzreport + Compact Context Summary schrumpfen. **Mindestverbesserung:** eine normale WP-Kette (Prompt → Umsetzung → Rückmeldung → Review) soll spürbar mehr als zwei Durchläufe pro Session erlauben; qualitativ: „mehrere WPs pro Session statt 1–2". **Abbruchkriterien:** steigende Rückfragen, Scope-Fehler, übersehene Invarianten, Gate-/Neutralitätsfehler. **Qualitätsgrenzen:** Sicherheits-/Neutralitäts-/Evidenzgehalt darf nie der Kompression geopfert werden (Context-Economy-Grundsatz). Keine schein-präzisen Token-Zahlen ohne Messung.

## 5. D – Kontextklassen

| Klasse | Zweck | existiert? | Datei/Lücke | Empfehlung | Risiko bei Überkompression |
|---|---|---|---|---|---|
| 1 Dauerhafter Framework-Kontext | invariante Regeln (Rollen, Grenzen, Gate, ADRs) | **teilweise** | Prompt-Blocks + Skills vorhanden, aber Prompts wiederholen sie trotzdem | nur **referenzieren** (Router-Prinzip), nicht wiederholen | Invarianten aus dem Blick → Verstöße |
| 2 Projektkontext | was das Projekt ist (Ziel, Module, Schlüsseldateien) | **teilweise** | Project Profile/Adapter; kein kompaktes `PROJECT_MAP` | optionales PROJECT_MAP für Consumer-Projekte (project-local) | falsche Architektur-Annahmen |
| 3 Aktueller Projektstatus | wo das Projekt gerade steht | **teilweise** | Context Pack + Next Phase — aber groß/monolithisch, historienlastig | kleines `CURRENT_STATE` (≤ 1 Seite) als Extrakt | veralteter Status → falscher Einstieg |
| 4 Aufgabenkontext | das konkrete WP | ja | WP-Prompt | auf 8 Kernelemente reduzieren (→ G) | fehlende harte Grenzen |
| 5 Übergabekontext | Wiederaufnahme ohne Chat-Historie | **Lücke** | Compact Context Summary existiert, ist aber Ausgabe-, nicht Wiederaufnahme-orientiert | minimales `SESSION_HANDOFF`-Format (→ H) | verlorene Entscheidungen/Blocker |
| 6 Evidenzkontext | Nachweise für Review | **teilweise** | Gate-Output/Greps ad hoc | kompaktes Evidence Pack im Rückmelde-Kurzformat | fehlende Belege → blindes Review |

## 6. E – Context Budgets B0–B4

| Budget | WP-Arten | Projektkontext | Dateien | Governance im Prompt | Rückmeldung | Reviewtiefe | Eskalation |
|---|---|---|---|---|---|---|---|
| **B0 Micro** | Tippfehler, Statuszeile, 1-Datei-Korrektur | CURRENT_STATE-Zeile | ≤ 2 | nur Referenz | 5–10 Zeilen + Summary | Stichprobe | bei jeder Unklarheit → B1/B2 |
| **B1 Lean** | normale docs-/kleine code-WPs, Fortsetzungen, Fixes | CURRENT_STATE + 1 Kontextabsatz | ≤ 5 relevant, ≤ 3 voll gelesen | Referenz + WP-spezifische Sonderregeln | Kurzreport (Status, Dateien, Tests, Risiken, Next) + Summary | gezielt | Scope unklar/kritisch → B2 |
| **B2 Standard** | mittlere Features/Reviews | + Project-Map-Ausschnitt | ≤ 10 | Referenz + relevante Invarianten sichtbar | Standard-Rückmeldung | normal | Kritikalität → B3 |
| **B3 Extended** | Architektur, Release-Readiness, ADR-nahe Arbeit | volle Phase-Docs gezielt | nach Bedarf, begründet | volle relevante Governance | volles Format | tief | Governance-Konflikt → B4/STOP |
| **B4 Exceptional** | Release/Scope-Lock/Security-Sonderfälle | maximal nötig | begründet je Datei | vollständig | vollständig | maximal | **kein Standard**; regelmäßiger B4-Bedarf ⇒ WP splitten/neu scopen |

**Regel:** B4 darf kein Standard werden. Wenn ein WP regelmäßig B4 braucht, muss es gesplittet oder neu scoped werden.

## 7. F – Prompt-Modi

| Modus | Zweck | Pflichtinfos | Verbotene Wiederholungen | Budget | geeignete WPs | Risiken | Rückmeldeformat |
|---|---|---|---|---|---|---|---|
| Full | Governance-/Release-/Security-kritisch | alles Relevante sichtbar | — | B3–B4 | Release, ADR, Scope Lock, Security | Kosten; Scheinsicherheit | voll |
| Standard | mittlere WPs | Ziel/Scope/Invarianten-Auswahl | voller Rollen-/Regeltext | B2 | Features, Reviews | mittlere Kosten | Standard |
| Short (bestehend) | standardisierte Folgearbeit mit Context Pack | WP-ID, Ziel, Pack-Referenz | Rahmentexte | B1 | kleine Updates | Verbotsliste beachten | kurz |
| **Lean (neu, additiv)** | **bevorzugter Normalfall** | 8 Kernelemente (→ G) | Rollenmodell, Standard-Grenzen, Template-Volltexte | B1 | normale docs-/kleine code-WPs, Fixes, Fortsetzungen | Fail-closed-Liste (→ M) beachten | Kurzreport + Summary |
| Handoff (neu, additiv) | Session-Wiederaufnahme | SESSION_HANDOFF-Block (→ H) | alter Chat, Original-Prompt-Volltext | B0–B1 | Fortsetzungen | veralteter Handoff | Kurzreport |
| Review-only (neu, additiv) | Nova-/Maintainer-Review | Evidence Pack + Abnahmekriterien | erneuter Volltext des WP | B1–B2 | Reviews | fehlende Evidenz | Review-Verdikt |
| Fix (neu, additiv) | punktuelle Korrektur | Symptom, Ziel, betroffene Datei(en), Invariante | Rahmen | B0–B1 | Bugfix/Korrektur | verdeckter Scope | Mini-Report |

**Leitentscheidung (bestätigt):** *Lean Mode soll bevorzugter Normalfall werden, sofern keine erhöhte Komplexität oder Kritikalität vorliegt. Full Mode darf nicht allein deshalb verwendet werden, weil er mehr Sicherheit vermittelt* — Sicherheit entsteht aus den Fail-closed-Regeln (→ M), nicht aus Promptlänge. Alle neuen Modi sind **additive Profile** der bestehenden Full/Standard/Short-Semantik (v1.x-kompatibel, keine inkompatible Änderung).

## 8. G – Work-Package-Prompt-Architektur

Normale WP-Prompts lassen sich auf **8 Kernelemente** reduzieren:

```text
1. Ziel   2. Scope   3. relevante Quellen   4. verbindliche Invarianten (nur WP-spezifische)
5. konkrete Aufgabe   6. Abnahmekriterien   7. Non-Goals   8. Rückmeldeformat (Referenz)
```

- **Nur referenzieren (skill-/dokumentgetragen):** Rollenmodell, Standard-Git-/Netz-/Secret-Grenzen (BLOCK_LIMITS), Neutralitätsregeln, Rückmelde-/Summary-Templates (BLOCK_FEEDBACK), Self-Check-Standard, Skills-first-Regeln.
- **Immer sichtbar bleiben:** WP-ID/Typ, Allowed/Forbidden Files, WP-spezifische Sonderregeln und Abweichungen von Standards, Fail-closed-Trigger des konkreten WP, erwartete Commit-Message.
- **Lean-WP-Prompt:** die 8 Kernelemente auf ≤ 1 Seite, Standards per Ein-Zeilen-Referenz („Es gelten BLOCK_LIMITS/BLOCK_FEEDBACK und die Skills-first-Regeln").
- **Standard/Full bleiben nötig,** wenn Invarianten selbst Gegenstand des WP sind (Governance/Release/Security) oder der Scope unklar/konfliktbehaftet ist.

## 9. H – Session-Handoff-Modell

Minimales Wiederaufnahmeformat (Ziel ≤ ~30 Zeilen), statt Chat-Historie:

```text
Projekt · NDF-Version · Branch/Revision · aktives WP · Scope
erledigt · offen · Entscheidungen · Blocker
relevante Dateien · nicht erneut laden · nächster Auftrag · verbotene Arbeiten
```

**Handoff-Typen:** Implementierungsfortsetzung, Review, Fehlerbehebung, Human-Maintainer-Entscheidung, Übergabe an Nova — gleicher Block, unterschiedlicher „nächster Auftrag".

**Entscheidung:** Weiterverfolgen als **Template + additiver Prompt-Modus („Handoff") + Ausbau der bestehenden Compact Context Summary** (die Summary liefert bereits 80 % der Felder; es fehlen „nicht erneut laden" und „verbotene Arbeiten"). **Kein neuer Skill** (siehe K) und zunächst **project-local Pilot** vor NDF-Core-Verankerung.

## 10. I – Current-State-/Project-Map-Bewertung

| Datei | Zweck | max. Größe | Pflege | Doppelung | Token-Nutzen | Empfehlung |
|---|---|---|---|---|---|---|
| `CURRENT_STATE` | Status-Einstieg (WP, Phase, letzte Entscheidung, Blocker, nächstes Gate) | ~1 Seite | je WP-Abschluss | extrahiert aus Context Pack | **hoch** (ersetzt Volllektüre der Status-Docs) | **empfohlen** (zuerst project-local, dann ggf. NDF-Template) |
| `SESSION_HANDOFF` | Wiederaufnahme | ~30 Zeilen | je Sessionende | Summary-Ausbau | **hoch** (ersetzt Chat-Historie) | **empfohlen** (Template + Modus, → H) |
| `PROJECT_MAP` | Projektüberblick für Consumer-Projekte | 1–2 Seiten | bei Strukturänderung | teils Project Profile | mittel–hoch bei Code-Projekten | empfohlen **project-local/Adapter**, nicht NDF-Core-Pflicht |
| `CONTEXT_INDEX` | „was liegt wo" | ~1 Seite | selten | README-Router kann das leisten | mittel | **nicht separat** — Router-Prinzip in README/Einstieg genügt |
| `ACTIVE_DECISIONS` | offene/aktive Entscheidungen | klein | je Entscheidung | Decision Index/ADRs | gering–mittel | nicht separat; in CURRENT_STATE-Zeile abdecken |
| `ACTIVE_RISKS` | aktive Risiken | klein | je Review | Risk-Abschnitte vorhanden | gering | nicht separat; in CURRENT_STATE-Zeile abdecken |

Nur `CURRENT_STATE` und `SESSION_HANDOFF` ersetzen messbar größeren Kontext; die übrigen wären Pflege-Overhead bzw. Duplikate. **Router-Prinzip** (README/Einstieg kurz + Verweise, keine Historie, keine monolithischen Packs im Startkontext) wird übernommen; Write/Select/Compress/Isolate dient als Analysemodell und deckt sich mit den bestehenden Context-Economy-Layern 1–5.

## 11. J – Skills Real-use Review (38 Skills)

Reale Nutzungsevidenz: die WP-Prompts seit WP-134 referenzieren Skills aktiv; **tatsächlich prozessprägend** waren in den realen Sessions vor allem der WP-Rahmen, die Abschlussformate, die Neutralitätsprüfung und der Changelog-Stil. Klassifikation (Nutzung = reale/absehbare NDF-Core-Frequenz; alle 30 WP-145/146-Skills tragen weiterhin RDS-001/ADS-001 = *nicht ausreichend validiert*):

**Häufig benötigt (4):** `ndf-work-package-runner` · `ndf-compact-context-summary-runner` · `ndf-public-neutrality-guard` · `ndf-changelog-writer` — Triggerqualität gut, Kontextkosten gering, in fast jedem WP real angewendet. Kandidaten für „automatisch laden".

**Gelegentlich benötigt (9):** `ndf-context-pack-maintainer` · `ndf-skill-quality-reviewer` · `ndf-docs-polish-runner` · `ndf-existing-project-analysis-runner` · `ndf-validation-evidence-reviewer` · `ndf-feedback-triage-runner` · `ndf-skill-trigger-quality-reviewer` · `ndf-adr-governance-review` · `ndf-release-safety` — nur explizit referenzieren, nicht default-aktiv.

**Selten benötigt (25):** die übrigen — u. a. `ndf-v1-readiness-review`, `ndf-release-notes-runner`, `ndf-public-release-body-reviewer`, `ndf-readme-quality-reviewer`, `ndf-skill-supply-chain-risk-reviewer`, `ndf-privacy-data-minimization-reviewer`, `ndf-accessibility-reviewer`, `ndf-project-adapter-quality-reviewer`, `ndf-project-brief-runner` sowie die 16 Engineering/Product/UX/Creative-Skills (`architecture-blueprint`, `feature-scope`, `implementation-review`, `test-strategy`, `debugging-root-cause`, `product-discovery`, `ux-flow`, `onboarding-friction`, `behavioral-adoption`, `ethical-growth`, `branding-kit`, `creative-direction`, `naming`, `ui-style-system`, `landing-page-concept`, `content-tone`) — nur explizit referenzieren.

**Überlappend / Merge-Kandidaten (kompatibel, spätere Konsolidierung per ADR-0031-Deprecation-Pfad, nichts wird jetzt entfernt/umbenannt):**
- `behavioral-adoption-reviewer` + `ethical-growth-reviewer` (Ethik-Adoption)
- `branding-kit-runner` + `creative-direction-runner` (+ `naming-runner`) (Creative)
- `public-release-body-reviewer` + `release-notes-runner` (Release-Text)
- `onboarding-friction-reviewer` + `ux-flow-reviewer` (UX-Reibung)
- `content-tone-reviewer` ↔ `docs-polish-runner` (Teil-Overlap)
- `privacy-data-minimization-reviewer` ↔ `public-neutrality-guard` (Teil-Overlap, unterschiedlicher Fokus — getrennt lassen)

**Adapter-Kandidaten (16):** die Engineering/Product/UX/Creative-Familie gehört mittelfristig eher in **Project-Adapter-/project-local-Profile** als in den NDF-Core-Default (projektartabhängig, im Framework-Repo selbst nie genutzt).

**Deprecation-Kandidaten (spätere kompatible Version):** keine sofort; die Merge-Paare oben sind die Vormerkliste (nur additiv/mit Deprecation-Hinweis, nie stilles Entfernen).

**Kernregel (bestätigt):** *NDF besitzt 38 Skills als Bibliothek. Nicht alle 38 dürfen mental oder promptseitig als Default aktiviert werden. Normale WPs nutzen nur wenige passende Skills* — Lean-Prompts nennen ≤ 3–5 Skills; die 4 „häufigen" gelten als impliziter Rahmen.

## 12. K – Neue Skills kritisch geprüft (nicht implementiert)

**`ndf-token-budget-reviewer`:** Aufgabe (Budget wählen/prüfen) ist eine **Tabellen-Lookup-Entscheidung** — besser als B0–B4-Tabelle in einer Guidance/Checkliste (dieses Dokument → ggf. WP-152-Artefakt) plus Eskalationsregel. Kriterium 4 verfehlt (ein weiterer Skill kostet Kontext, die Tabelle ist billiger); Kriterium 3 verfehlt (Prompt-Mode-/Budget-Wahl liegt bereits beim `work-package-runner`-Rahmen). **Empfehlung: nicht als Skill — als Guidance/Template in WP-152.**

**`ndf-session-handoff-runner`:** Aufgabe ist ein **Format**, kein Prozess — der bestehende `ndf-compact-context-summary-runner` deckt die Erzeugung bereits ab; es fehlt nur das erweiterte Feld-Set (→ H). Kriterium 3 verfehlt (bestehender Skill reicht mit Template-Ergänzung); Consumer-Kriterium noch unbelegt (erst Pilot). **Empfehlung: nicht als Skill — als Template + additiver Handoff-Modus; Re-Evaluation nach project-local Pilot.**

Beide erfüllen die 5 Kriterien nicht. **Keine neuen Skills erstellt.**

## 13. L – Verbraucherprojekte (neutral als Archetypen; projektspezifische Details bleiben project-local)

| Archetyp | Sessiongröße (Annahme, sofern nicht belegt) | größter Tokenverbrauch | Prompt-Modus | Budget | Handoff-Typ | project-local |
|---|---|---|---|---|---|---|
| Design-System-Projekt | mittel (Annahme) | Komponenten-/Style-Dateien | Lean/Standard | B1–B2 | Implementierungsfortsetzung | PROJECT_MAP + UI-Skills als Adapter-Profil |
| Operations-Control-Plane-Projekt (**belegt:** realer Cross-Projekt-Intake/Transfer in dieser Phase) | mittel–groß | Governance-/Statusdokumente, Zwei-Repo-Preflights | Lean für Status-WPs, Full nur für Governance | B1–B3 | Übergabe an Nova + Maintainer-Entscheidung | CURRENT_STATE dringend; Handoff-Pilot-Kandidat **Nr. 1** |
| Dokument-Framework-Projekt | klein–mittel (Annahme) | Dokumentkorpus | Lean | B1 | Review | Evidence Pack |
| Voice-/Community-Server-Projekt | mittel (Annahme) | Code + Konfiguration | Standard | B2 | Implementierungsfortsetzung | PROJECT_MAP |
| Streaming-Operations-Projekt | mittel (Annahme) | Code + Betriebsdoku | Standard | B2 | Fehlerbehebung | PROJECT_MAP + Fix-Modus |

Empfehlung: Pilot in **1–2** Projekten (zuerst das Operations-Control-Plane-Projekt — dort existiert reale NDF-Arbeitslast), nicht in allen fünf gleichzeitig.

## 14. M – Fail-Closed-Regeln

Lean Mode / kleines Budget **darf nicht** verwendet werden bei: sicherheitskritischer Architekturentscheidung · Breaking-Change-Prüfung · Release-Gate · Migration · Datenschutz-/Berechtigungsänderung · unklarem Scope · widersprüchlichen Quellen · fehlenden autoritativen Dokumenten · ADR-Änderung · Skill-Security-Änderung · Public-Neutrality-Unsicherheit.

```text
Fehlender Kontext wird sichtbar gemacht, nicht geraten.
Bei Unsicherheit: Budget erhöhen, STOP melden oder Human-Maintainer-Gate auslösen.
```

Das ist konsistent mit den bestehenden Short-Prompt-Verboten und dem Blocked-/No-Change-Report (Adoption A) — Lean erweitert die Short-Logik, ersetzt sie nicht.

## 15. N – Entscheidungsvorlage für WP-152

| Option | Voraussetzungen | Nutzen | Risiken | v1.1-Roadmap-Wirkung | nächster Schritt |
|---|---|---|---|---|---|
| **GO** (eigenes Token-Efficiency-WP) | dieses Review + Human-Maintainer-GO | größte Wirkung: Lean/Handoff/Budgets/CURRENT_STATE additiv verankert | Scope-Creep; Pflegeaufwand | Token-Efficiency-WP wird eingeschoben; External Validation etc. rücken nach (Renumbering durch Nova/Maintainer) | WP-152 als additives docs-only Implementierungs-WP |
| REDUCE | — | geringer Aufwand | Kernproblem (Limits) bleibt weitgehend | Roadmap unverändert | nur Mini-Edits an Prompt-Guidance |
| PILOT PROJECT-LOCAL | 1–2 Pilotprojekte | reale Messdaten vor Core-Änderung | Verzögerung; Framework-Nutzer profitieren später | Roadmap unverändert, Pilot parallel | Handoff/CURRENT_STATE im Operations-Archetyp testen |
| NO-GO | — | kein Aufwand | dokumentiertes Limit-Problem bleibt ungelöst; widerspricht der Evidenz | unverändert | — |

**Empfehlung: GO mit reduziertem, additivem Scope + paralleler project-local Pilot.** Konkret: ein WP-152 „Token Efficiency & Context Budget Baseline" (docs-only, additiv: Lean-/Handoff-/Review-only-/Fix-Profile als Ergänzung der Prompt Modes, B0–B4-Guidance, SESSION_HANDOFF-Template, CURRENT_STATE-Muster, Kurzreport-Rückmeldevariante) — **kein** neuer Skill, **keine** inkompatible Änderung; parallel Pilot im Operations-Archetyp. Die Einschub-Nummerierung (Token Efficiency als neues WP-152, bisherige WP-152…156 rücken zu WP-153…157) entscheidet Nova/Human Maintainer — dieses Review nimmt sie nicht vorweg.

## 16. Do-not-start-Liste

Bis nach dem Human-Maintainer-Gate nicht beginnen: Token Efficiency als Implementierungs-WP · neue Skills · Skill-Entfernung/-Umbenennung · v1.1 Scope Lock · v1.1 Release Prep · Requirements-Engineering-System · neue Governance-Ebene · projektlokale Fachfunktionen im NDF Core · umfangreiche neue Dokumentationsstruktur · automatische Commit-/Push-/Tag-/Release-Aktionen.

## 17. Compatibility / Governance

Alle Empfehlungen sind **additiv** (neue optionale Profile/Templates/Guidance) und bleiben in der v1.x-Kompatibilität (ADR-0031: Non-breaking-Kategorie der V1_1_PLAN-Grenzen). ADR-0032 bleibt unberührt (keine Scripts/Automation/Netz). Prompt Modes werden nicht inkompatibel geändert — Lean/Handoff/Review-only/Fix sind Ergänzungen. Kein v1.1 Scope Lock, kein Release Prep, keine neue NDF-Version durch dieses WP. Öffentliche Neutralität: Consumer-Projekte nur als Archetypen.

## 18. Decision

**GO WITH NOTES – skills real-use and context efficiency review completed.** Nächster empfohlener Schritt: **Human-Maintainer-Entscheidung über die WP-152-Vorlage (Empfehlung: GO additiv-schlank + Pilot)**; danach Renumbering der v1.1-Roadmap durch Nova.
