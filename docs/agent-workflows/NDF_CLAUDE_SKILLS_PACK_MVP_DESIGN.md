# NDF Claude Skills Pack MVP Design

## DE – Zweck

Dieses Dokument entwirft das **NDF Claude Skills Pack MVP** als public-neutrales, sicheres Design (NDF-WP-111). Es dokumentiert Zweck, Trigger, Grenzen und erwartete Outputs von sechs MVP-Skills und wendet die [Skill Security Policy](NDF_SKILL_SECURITY_POLICY.md) (ADR-0032) und die [Context Economy](NDF_CONTEXT_ECONOMY.md) an. Es ist **nur Design** — es entstehen **keine aktiven Skills**.

## EN – Purpose

This document designs the **NDF Claude Skills Pack MVP** as a public-neutral, safe design (NDF-WP-111). It documents the purpose, triggers, limits, and expected outputs of six MVP skills and applies the [Skill Security Policy](NDF_SKILL_SECURITY_POLICY.md) (ADR-0032) and [Context Economy](NDF_CONTEXT_ECONOMY.md). It is **design only** — **no active skills** are created.

## DE – Status

**Design only (NDF-WP-111, 2026-07-08).** Dieses Dokument erstellt **kein** aktives Claude Skills Pack, **keine** `.claude/skills`, **keine** `SKILL.md`, **keine** Skill-Scripts; es erlaubt **keine** autonomen Commit-/Push-/Tag-/Release-Aktionen. Foundation 0.8 ist scope-locked, **nicht released**, **nicht v1.0**. WP-112 (Implementierung) bleibt optional und wird durch dieses WP nicht aktiviert.

## EN – Status

**Design only (NDF-WP-111, 2026-07-08).** This document creates **no** active Claude Skills Pack, **no** `.claude/skills`, **no** `SKILL.md`, **no** skill scripts; it allows **no** autonomous commit/push/tag/release actions. Foundation 0.8 is scope-locked, **not released**, **not v1.0**. WP-112 (implementation) stays optional and is not activated by this WP.

## DE – Design-Grundsätze

- **Klein und fokussiert:** genau sechs Skills, jeder mit einem klaren Zweck.
- **Docs-only zuerst:** Skills liefern Vorschläge/Struktur, keine ausgeführten Aktionen.
- **Fail closed:** was nicht ausdrücklich erlaubt ist, ist verboten.
- **Additiv:** Skills operationalisieren bestehende NDF-Prinzipien, ohne sie zu ändern.
- **Human-first:** jede Entscheidung/Ausführung bleibt beim Human Maintainer.

## EN – Design Principles

Small and focused (exactly six skills, each with one clear purpose); docs-only first (skills provide suggestions/structure, not executed actions); fail closed (whatever is not explicitly allowed is forbidden); additive (skills operationalize existing NDF principles without changing them); human-first (every decision/execution stays with the human maintainer).

## DE – Sicherheitsbasis

Verbindlich gemäß [ADR-0032](../adr/ADR-0032-skill-security-policy.md): fail closed; docs-only/read-only-orientiert; keine Scripts im MVP; keine Netzwerkzugriffe; keine Secrets; keine privaten Projektdaten; kein Drittanbieter-Skill-Import; keine autonomen Git-/Release-/Tag-Aktionen; Human Maintainer finale Kontrolle; Public Quality Gate und Public Neutrality Pflicht; Rückmeldung an Nova und Compact Context Summary unterstützt.

## EN – Security Baseline

Binding per ADR-0032: fail closed; docs-only/read-only-oriented; no scripts in the MVP; no network access; no secrets; no private project data; no third-party skill import; no autonomous git/release/tag actions; human maintainer final control; public quality gate and public neutrality mandatory; Report to Nova and Compact Context Summary supported.

## DE – MVP-Skill-Set

Genau sechs Skills (keine weiteren, keine optionalen hochgezogen):

1. `ndf-token-economy`
2. `ndf-feedback-to-nova`
3. `ndf-work-package-runner`
4. `ndf-public-neutrality-guard`
5. `ndf-release-safety`
6. `ndf-adr-governance`

## EN – MVP Skill Set

Exactly six skills (no more, no optional ones pulled up): `ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`.

## DE – Skill-Spezifikationen

### 1. `ndf-token-economy`

- **Zweck:** Context Economy anwenden, Kontext reduzieren, Compact Context Summary und Context-Pack-Nutzung unterstützen.
- **Wann nutzen:** lange WP-Zusammenhänge verdichten; Handover vorbereiten.
- **Wann nicht:** wenn Sicherheits-/Evidenz-Kontext betroffen ist und Kürzen ihn entfernen würde.
- **Erlaubte Inputs:** öffentliche Repo-Inhalte, bereits vorhandener WP-Kontext.
- **Verbotene Inputs:** private Chat-Historie, Secrets, private Projektdaten.
- **Erlaubte Outputs:** sichere Status-Summaries, Compact Context Summary, Empfehlung zur Context-Pack-Nutzung.
- **Verbotene Outputs:** Chain-of-Thought, gekürzte Evidenz, entfernte Sicherheitsgrenzen.
- **Pflichtprüfungen:** Public Quality Gate respektieren; Evidenz erhalten.
- **Pflicht-Handover:** Compact Context Summary.
- **Security Notes:** Token-Sparen darf keine Sicherheitsprüfung ersetzen.
- **Bezug:** [NDF_CONTEXT_ECONOMY.md](NDF_CONTEXT_ECONOMY.md).

### 2. `ndf-feedback-to-nova`

- **Zweck:** Rückmeldung an Nova standardisieren.
- **Wann nutzen:** am WP-Ende die strukturierte Rückmeldung vorbereiten.
- **Wann nicht:** um ein negatives Ergebnis zu beschönigen.
- **Erlaubte Inputs:** WP-Ergebnis, Gate-Status, bekannte Notes.
- **Verbotene Inputs:** private Daten, Secrets.
- **Erlaubte Outputs:** feste Abschnittsstruktur, GO/GO WITH NOTES/REWORK/STOP-Vorschlag, Compact Context Summary, Risiken/nächste Schritte.
- **Verbotene Outputs:** verschwiegene Gate-Fehler, ersetzte Maintainer-Entscheidung.
- **Pflichtprüfungen:** Gate-Ergebnis ehrlich abbilden.
- **Pflicht-Handover:** Rückmeldung an Nova + Compact Context Summary.
- **Security Notes:** ersetzt keine Human-Maintainer-Entscheidung.
- **Bezug:** Workflow-/Review-Dokumentation.

### 3. `ndf-work-package-runner`

- **Zweck:** standardisierte Work-Package-Ausführung unterstützen.
- **Wann nutzen:** WP-Schritte strukturieren, relevante Dateien identifizieren.
- **Wann nicht:** für Governance-/Release-/destruktive Entscheidungen ohne Full-Prompt-Kontext.
- **Erlaubte Inputs:** WP-Prompt, betroffene öffentliche Dateien.
- **Verbotene Inputs:** private Projektlogik, Secrets.
- **Erlaubte Outputs:** strukturierte WP-Schritte, Datei-Identifikation, Statusupdate-Vorschläge, Wiederholung harter Grenzen.
- **Verbotene Outputs:** autonome Commits/Pushes/Tags/Releases, eigenständige Scope-Erweiterung, destruktive Aktionen.
- **Pflichtprüfungen:** harte Grenzen des WP respektieren; Gate.
- **Pflicht-Handover:** Rückmeldung an Nova + Compact Context Summary.
- **Security Notes:** löst keine Git-/Release-Aktionen aus.
- **Bezug:** Work-Package-Standards, [Context Economy](NDF_CONTEXT_ECONOMY.md).

### 4. `ndf-public-neutrality-guard`

- **Zweck:** Public Neutrality und private-data-freie Dokumentation unterstützen.
- **Wann nutzen:** vor Übergabe/Commit an Neutralitätsregeln erinnern.
- **Wann nicht:** als Ersatz für den Public Quality Gate.
- **Erlaubte Inputs:** öffentliche Textentwürfe.
- **Verbotene Inputs:** Secret-Werte, private Denylist-Begriffe.
- **Erlaubte Outputs:** Neutralitäts-Erinnerungen, Bevorzugung öffentlicher NDF-Begriffe, gate-konforme Formulierungsvorschläge.
- **Verbotene Outputs:** dokumentierte Secrets/Denylist-Begriffe, private Projektlogik.
- **Pflichtprüfungen:** Public Quality Gate bleibt maßgeblich (Skill ersetzt ihn nicht).
- **Pflicht-Handover:** Hinweis, dass der Gate final entscheidet.
- **Security Notes:** kennt/dokumentiert keine Secret-Werte; `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name.
- **Bezug:** Public-Quality-Gate-Dokumentation.

### 5. `ndf-release-safety`

- **Zweck:** Release-Safety und Human-Maintainer-Gates unterstützen.
- **Wann nutzen:** Release-Prep-Checklisten und Go/No-Go-Struktur vorbereiten.
- **Wann nicht:** um Tag/Release auszulösen.
- **Erlaubte Inputs:** Release-Notes-Entwürfe, Kriterien.
- **Verbotene Inputs:** GitHub-Schreib-Credentials, Secrets.
- **Erlaubte Outputs:** strukturierte Checklisten, manuelle Go/No-Go-Schritte, Tagging-Guide als Dokumentation, Wiederholung der No-Auto-Release-Grenzen.
- **Verbotene Outputs:** Tag-Erstellung/-Push, GitHub-Release-Erstellung/-Änderung, automatisch gesetzter Release-Titel, ersetzte Maintainer-Freigabe.
- **Pflichtprüfungen:** „nur Human Maintainer taggt/releast" wiederholen.
- **Pflicht-Handover:** Hinweis auf manuelle Human-Maintainer-Schritte.
- **Security Notes:** löst nie eine Release-/Tag-Aktion aus.
- **Bezug:** Release-Prep-/Tagging-Guide-Muster.

### 6. `ndf-adr-governance`

- **Zweck:** ADR-Policy und Governance-Entscheidungen unterstützen.
- **Wann nutzen:** prüfen, ob eine ADR nötig ist; ADR-Struktur vorschlagen.
- **Wann nicht:** um eine ADR autonom als Accepted zu finalisieren.
- **Erlaubte Inputs:** ADR-Policy, bestehende ADRs (öffentlich).
- **Verbotene Inputs:** private Governance-Daten.
- **Erlaubte Outputs:** ADR-Bedarfsprüfung, konzeptionelle Nummernprüfung, Strukturvorschlag, Supersede-vs-Rewrite-Erinnerung.
- **Verbotene Outputs:** autonome Accepted-Entscheidung, Umnummerierung alter ADRs, ADR-Massenmigration, Finalisierung ohne Human-Maintainer-Review.
- **Pflichtprüfungen:** ADR-Policy respektieren; nächste freie Nummer über beide Ordner.
- **Pflicht-Handover:** Vorschlag zur Human-Maintainer-Entscheidung.
- **Security Notes:** ersetzt keine Governance-Freigabe.
- **Bezug:** `docs/adr/ADR_POLICY.md`, `docs/adr/README.md`.

## EN – Skill Specifications

Each of the six MVP skills is specified with: skill name; purpose; when to use / when not to use; allowed vs forbidden inputs; allowed vs forbidden outputs; required checks; required handover output; security notes; relationship to other NDF docs — as detailed in the German section above. In summary: `ndf-token-economy` condenses context and produces Compact Context Summaries without removing safety/evidence; `ndf-feedback-to-nova` standardizes the Report to Nova without hiding gate failures; `ndf-work-package-runner` structures WP execution without autonomous git/release actions; `ndf-public-neutrality-guard` reminds of neutrality without knowing secrets or replacing the gate; `ndf-release-safety` structures release prep without triggering tags/releases; `ndf-adr-governance` supports ADR decisions without autonomously accepting or renumbering ADRs.

## DE – Skill Review Matrix

| Skill | Primärer Zweck | Trigger | Erlaubte Outputs | Verbotene Outputs | Pflicht-Security-Checks | Pflicht-Handover | MVP-Status |
|---|---|---|---|---|---|---|---|
| `ndf-token-economy` | Kontext verdichten | langer WP-Kontext | Status-Summary, Compact Context Summary | Chain-of-Thought, gekürzte Evidenz | Gate, Evidenz erhalten | Compact Context Summary | MVP (Design) |
| `ndf-feedback-to-nova` | Rückmeldung standardisieren | WP-Ende | Abschnittsstruktur, GO/…/STOP-Vorschlag | verschwiegene Gate-Fehler | Gate ehrlich | Rückmeldung an Nova + Summary | MVP (Design) |
| `ndf-work-package-runner` | WP-Ausführung strukturieren | WP-Start | WP-Schritte, Datei-Identifikation | autonome Git-/Release-Aktion | harte Grenzen, Gate | Rückmeldung an Nova + Summary | MVP (Design) |
| `ndf-public-neutrality-guard` | Neutralität sichern | vor Übergabe/Commit | Neutralitäts-Erinnerung | dokumentierte Secrets/Denylist | Gate bleibt maßgeblich | Gate-Hinweis | MVP (Design) |
| `ndf-release-safety` | Release-Safety | Release Prep | Checkliste, Go/No-Go-Struktur | Tag/Release-Aktion | „nur Human Maintainer" | manuelle Schritte | MVP (Design) |
| `ndf-adr-governance` | ADR-Governance | ADR-Bedarf | ADR-Bedarfsprüfung, Strukturvorschlag | autonome Accepted-Entscheidung | ADR-Policy | Human-Maintainer-Vorschlag | MVP (Design) |

## EN – Skill Review Matrix

The table above (Skill / primary purpose / trigger / allowed outputs / forbidden outputs / required security checks / required handover / MVP status) applies verbatim; all six skills are at **MVP status: Design** — none is active.

## DE – Gemeinsame Skill-Regeln

Alle MVP-Skills müssen: docs-only sein; keine Scripts enthalten; keine Netzwerkzugriffe enthalten; keine Secrets verarbeiten; keine privaten Projektdaten enthalten; keine Drittanbieter-Skill-Inhalte kopieren; keine Git-Schreibaktionen auslösen; keine Release-/Tag-Aktionen auslösen; keine destruktiven Aktionen auslösen; Public Quality Gate respektieren; Public Neutrality respektieren; Human-Maintainer-Gates respektieren; Rückmeldung an Nova unterstützen; Compact Context Summary unterstützen.

## EN – Shared Skill Rules

All MVP skills must: be docs-only; contain no scripts; contain no network access; process no secrets; contain no private project data; copy no third-party skill content; trigger no git write actions; trigger no release/tag actions; trigger no destructive actions; respect the public quality gate; respect public neutrality; respect the human-maintainer gates; support the Report to Nova; support the Compact Context Summary.

## DE – Verbotene Fähigkeiten

Für alle Skills verboten (gemäß ADR-0032): autonome Commits/Pushes/Tags/Releases; GitHub-Release-Erstellung/-Änderung; Netzwerkzugriffe; Secret-Verarbeitung; private Projektlogik; Drittanbieter-Skill-Import; Scripts im MVP; destruktive Aktionen; Umgehung von Gate / Rückmeldung an Nova / Human-Gates.

## EN – Forbidden Capabilities

Forbidden for all skills (per ADR-0032): autonomous commits/pushes/tags/releases; GitHub release creation/modification; network access; secret processing; private project logic; third-party skill import; scripts in the MVP; destructive actions; bypassing the gate / Report to Nova / human gates.

## DE – Human-Maintainer-Gates

Alle Skill-Outputs sind Vorschläge. Der Human Maintainer entscheidet GO / GO WITH NOTES / REWORK / STOP, committet, pusht, taggt und veröffentlicht. Kein Skill trifft eine irreversible Entscheidung.

## EN – Human Maintainer Gates

All skill outputs are suggestions. The human maintainer decides GO / GO WITH NOTES / REWORK / STOP, commits, pushes, tags, and releases. No skill makes an irreversible decision.

## DE – Beziehung zu Context Economy

Das MVP operationalisiert die Context Economy (WP-109): `ndf-token-economy` und `ndf-feedback-to-nova` erzeugen die Compact Context Summary und verdichten Kontext, ohne Sicherheit/Evidenz zu reduzieren. Prompt Modes und Context-Pack-Templates bleiben WP-113 vorbehalten.

## EN – Relationship to Context Economy

The MVP operationalizes context economy (WP-109): `ndf-token-economy` and `ndf-feedback-to-nova` produce the Compact Context Summary and condense context without reducing safety/evidence. Prompt modes and context-pack templates remain for WP-113.

## DE – Beziehung zu ADR-0032

Jeder Skill hält die Skill Security Policy ein: fail closed, docs-only, keine autonomen Aktionen. `ndf-public-neutrality-guard` und `ndf-release-safety` spiegeln die Policy direkt in ihren Grenzen; `ndf-adr-governance` respektiert die ADR-Policy und finalisiert nichts ohne Human-Maintainer-Review.

## EN – Relationship to ADR-0032

Every skill complies with the skill security policy: fail closed, docs-only, no autonomous actions. `ndf-public-neutrality-guard` and `ndf-release-safety` mirror the policy directly in their limits; `ndf-adr-governance` respects the ADR policy and finalizes nothing without human-maintainer review.

## DE – Beziehung zu WP-112

WP-112 (Implementation) **bleibt optional. WP-111 aktiviert WP-112 nicht.** WP-112 darf das MVP nur implementieren, wenn es ausdrücklich per Human-Maintainer-Scope-Change freigegeben wird; es muss docs-only bleiben, sofern nicht eine spätere ADR-/Scope-Entscheidung mehr erlaubt; es darf keine Scripts, Netzwerkzugriffe, Git-Schreibaktionen, Release-/Tag-Aktionen, Secrets oder privaten Projektdaten hinzufügen. Keine stille Aktivierung.

## EN – Relationship to WP-112

WP-112 (implementation) **stays optional. WP-111 does not activate WP-112.** WP-112 may implement the MVP only if explicitly approved by a human-maintainer scope change; it must stay docs-only unless a later ADR/scope decision allows more; it may not add scripts, network access, git write actions, release/tag actions, secrets, or private project data. No silent activation.

## DE – Nicht-MVP / spätere Kandidaten

Nur als Future/Optional (nicht im MVP, nicht erstellt): `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`.

## EN – Non-MVP / Later Candidates

Future/optional only (not in the MVP, not created): `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`.

## DE – Nicht-Ziele

Kein aktives Claude Skills Pack; keine `.claude/skills`; keine `SKILL.md`; keine Skill-Scripts; keine Cursor Rules; keine Workflows; keine Netzwerk-Tools; keine autonomen Git-/Release-Aktionen; kein v1.0-Claim; keine aktive volle v1.x-Kompatibilitätszusage; keine WP-112-Aktivierung.

## EN – Non-Goals

No active Claude Skills Pack; no `.claude/skills`; no `SKILL.md`; no skill scripts; no Cursor rules; no workflows; no network tools; no autonomous git/release actions; no v1.0 claim; no active full v1.x compatibility promise; no WP-112 activation.

## DE – Nächste Schritte

**NDF-WP-113 – NDF Context Pack Template and Prompt Modes.** Danach optional WP-112 (Implementation, nur per Human-Maintainer-Scope-Change), dann Readiness (WP-114) und Release Prep (WP-115).

## EN – Next Steps

**NDF-WP-113 – NDF Context Pack Template and Prompt Modes.** Then optionally WP-112 (implementation, only via human-maintainer scope change), then readiness (WP-114) and release prep (WP-115).
