# NDF Skill Security Policy

## DE – Zweck

Dieses Dokument ist das operative Regelwerk der **NDF Skill Security Policy** — die praktische Sicherheitsregel für alle NDF-bezogenen Claude Skills. Die zugrunde liegende Governance-Entscheidung steht in [ADR-0032](../adr/ADR-0032-skill-security-policy.md). WP-111 (MVP Design) und optional WP-112 (Implementation) referenzieren dieses Dokument.

## EN – Purpose

This document is the operative rule set of the **NDF Skill Security Policy** — the practical security rule for all NDF-related Claude skills. The underlying governance decision lives in [ADR-0032](../adr/ADR-0032-skill-security-policy.md). WP-111 (MVP design) and optionally WP-112 (implementation) reference this document.

## DE – Status

**Accepted (NDF-WP-110, 2026-07-08).** Gilt für alle künftigen NDF-Skills, auch während WP-112 optional bleibt. Es wird in diesem WP **kein Skill Pack, keine `.claude/skills`, kein Script** erstellt.

## EN – Status

**Accepted (NDF-WP-110, 2026-07-08).** Applies to all future NDF skills, even while WP-112 stays optional. **No skill pack, `.claude/skills`, or script** is created in this WP.

## DE – Grundsatz: Fail Closed

Was nicht ausdrücklich erlaubt ist, ist verboten. Im Zweifel gilt: verbieten und an den Human Maintainer eskalieren. Sicherheit hat Vorrang vor Bequemlichkeit und vor Token-Ersparnis.

## EN – Principle: Fail Closed

Whatever is not explicitly allowed is forbidden. When in doubt: forbid and escalate to the human maintainer. Safety takes precedence over convenience and over token savings.

## DE – Erlaubter Skill-Scope

Erlaubt sind ausschließlich **docs-only, read-only-orientierte** Hilfen: Struktur-/Textvorschläge für Work-Package-Arbeit; Formulierungshilfe für die Rückmeldung an Nova und die Compact Context Summary; Neutralitäts-/Checklisten-Erinnerungen; Zusammenfassen bereits vorhandener öffentlicher Repo-Inhalte. Skill-Ausgaben sind **Vorschläge** — der Human Maintainer entscheidet und führt aus.

## EN – Allowed Skill Scope

Only **docs-only, read-only-oriented** aids are allowed: structure/text suggestions for work-package work; wording help for the Report to Nova and the Compact Context Summary; neutrality/checklist reminders; summarizing already-present public repo content. Skill outputs are **suggestions** — the human maintainer decides and executes.

## DE – Verbotene Fähigkeiten

Verboten (sofern nicht später durch ausdrückliche ADR-/Scope-Entscheidung eng begrenzt erlaubt): autonome Commits/Pushes/Tags/Releases; GitHub-Release-Erstellung/-Änderung; Netzwerkzugriffe; Secret-Verarbeitung; private Projektlogik; Drittanbieter-Skill-Import; Scripts im Skill-MVP; destruktive Aktionen; Umgehung des Public Quality Gate; Umgehung der Rückmeldung an Nova; Umgehung der Human-Maintainer-Gates.

## EN – Forbidden Capabilities

Forbidden (unless later narrowly allowed by an explicit ADR/scope decision): autonomous commits/pushes/tags/releases; GitHub release creation/modification; network access; secret processing; private project logic; third-party skill import; scripts in the skill MVP; destructive actions; bypassing the public quality gate; bypassing the Report to Nova; bypassing the human-maintainer gates.

## DE – Human-Maintainer-Gates

Der Human Maintainer bleibt finaler Owner: GO / GO WITH NOTES / REWORK / STOP, Commit, Push, Tag, Release. Skills treffen keine irreversiblen Entscheidungen und lösen keine Git-/Release-Aktionen aus. Klarstellung (NDF-WP-153): Nova (ChatGPT) gibt als Review-Rolle Review-Verdikte (GO / GO WITH NOTES / REWORK / STOP / BLOCKED) ab — Bewertungen, keine Annahme; die finale normative Entscheidung (Annahme, Scope-Änderung, ADR-Annahme) und alle Git-/Release-Aktionen bleiben beim Human Maintainer (`NOVA_REVIEW != HUMAN_ACCEPTANCE`).

## EN – Human Maintainer Gates

The human maintainer stays final owner: GO / GO WITH NOTES / REWORK / STOP, commit, push, tag, release. Skills make no irreversible decisions and trigger no git/release actions. Clarification (NDF-WP-153): Nova (ChatGPT), as the review role, issues review verdicts (GO / GO WITH NOTES / REWORK / STOP / BLOCKED) — evaluations, not acceptance; the final normative decision (acceptance, scope change, ADR acceptance) and all git/release actions stay with the human maintainer (`NOVA_REVIEW != HUMAN_ACCEPTANCE`).

## DE – Public Quality Gate

Der Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante. Skills dürfen ihn weder umgehen noch abschalten; Skill-erzeugte Dateien unterliegen ihm wie alle anderen.

## EN – Public Quality Gate

The public quality gate v0.2 stays a mandatory invariant. Skills must not bypass or disable it; skill-generated files are subject to it like all others.

## DE – Public Neutrality

Skills führen keine privaten Projekt-/Personennamen, Reviewer-Identitäten, Kontaktwege oder echten Domains ein. Der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden; der Wert oder einzelne Denylist-Begriffe niemals.

## EN – Public Neutrality

Skills introduce no private project/person names, reviewer identities, contacts, or real domains. Naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed; its value or individual denylist terms never.

## DE – Secrets und private Daten

Skills verarbeiten, speichern oder dokumentieren keine Secrets und keine privaten Projektdaten. Keine Roh-Chat-Historie, keine Chain-of-Thought.

## EN – Secrets and Private Data

Skills process, store, or document no secrets and no private project data. No raw chat history, no chain-of-thought.

## DE – Drittanbieter-Skills

Kein ungeprüfter Import von Drittanbieter-Skills oder externen Skill-Inhalten; keine Übernahme externer Branding-/Autorenhinweise.

## EN – Third-Party Skills

No unreviewed import of third-party skills or external skill content; no adoption of external branding/author notices.

## DE – Scripts und Tool-Nutzung

Skills sind zunächst **docs-only**. Scripts sind verboten, bis eine spätere ausdrückliche ADR-/Scope-Entscheidung sie eng begrenzt erlaubt (mit definierten Grenzen, Review und Human-Maintainer-Freigabe).

## EN – Scripts and Tool Use

Skills are **docs-only first**. Scripts are forbidden until a later explicit ADR/scope decision narrowly allows them (with defined limits, review, and human-maintainer approval).

## DE – Netzwerkzugriffe

Netzwerkzugriffe durch Skills sind verboten.

## EN – Network Access

Network access by skills is forbidden.

## DE – Git- und Release-Aktionen

Git-Schreibaktionen (commit/push/branch/tag) und Release-/Tag-Aktionen durch Skills sind verboten. Sie bleiben ausschließlich beim Human Maintainer.

## EN – Git and Release Actions

Git write actions (commit/push/branch/tag) and release/tag actions by skills are forbidden. They remain exclusively with the human maintainer.

## DE – Destruktive Aktionen

Destruktive oder irreversible Aktionen durch Skills sind verboten. Für gefährliche Funktionen gilt weiterhin das NDF-Muster destructive-blueprint → destructive-implementation unter menschlicher Freigabe — nie durch einen Skill ausgelöst.

## EN – Destructive Actions

Destructive or irreversible actions by skills are forbidden. Dangerous functionality still follows the NDF pattern destructive-blueprint → destructive-implementation under human approval — never triggered by a skill.

## DE – Beziehung zu Context Economy

Context Economy ([NDF_CONTEXT_ECONOMY.md](NDF_CONTEXT_ECONOMY.md)) reduziert unnötigen Kontext, **nicht** Sicherheit. Short Prompts und Token-Sparen dürfen keine Sicherheitsprüfung, keine erforderliche Evidenz und kein Human-Maintainer-Gate ersetzen oder umgehen.

## EN – Relationship to Context Economy

Context economy reduces unnecessary context, **not** safety. Short prompts and token saving must not replace or bypass a safety check, required evidence, or a human-maintainer gate.

## DE – Rückmeldung an Nova und Compact Context Summary

Jeder WP-bezogene Skill unterstützt die Rückmeldung an Nova (ChatGPT) und die Compact Context Summary und darf sie nicht umgehen oder verkürzen, wo sie erforderlich sind.

## EN – Rückmeldung an Nova and Compact Context Summary

Every work-package-related skill supports the Report to Nova (ChatGPT) and the Compact Context Summary and must not bypass or shorten them where they are required.

## DE – Ausgabevorrang: aktiver Prompt vor Skill (NDF-WP-153)

Generische Skill-Ausgabeverträge überschreiben nicht das ausdrücklich vorgegebene Rückgabeformat des aktiven, autorisierten Prompts; bei Konflikt gilt das Prompt-Format. Höherrangige normative Pflichtinhalte (z. B. Rückmeldung an Nova, Compact Context Summary, Human-Maintainer-Gates) bleiben bindend und werden in die Struktur des Prompts eingepasst. Ein Skill ersetzt oder schwächt den aktiven Ausführungsvertrag nie stillschweigend; ein echter normativer Konflikt wird gemeldet und fail-closed behandelt. Siehe [Execution Contract](../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md). Diese Klarstellung ändert weder den Skill-Scope (öffentlich/privat) noch Netzwerk-, Script- oder Secret-Regeln noch ADR-0032.

## EN – Output Precedence: Active Prompt over Skill (NDF-WP-153)

Generic skill output contracts do not override the explicit return format of the active authorised prompt; on conflict, the prompt's format wins. Higher normative requirements (e.g. the Report to Nova, the Compact Context Summary, human-maintainer gates) stay binding and are fitted into the prompt's structure. A skill never silently replaces or weakens the active execution contract; a real normative conflict is reported and fails closed. See the [Execution Contract](../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md). This clarification changes neither the skill scope (public/private) nor the network, script, or secret rules, nor ADR-0032.

## DE – Skill-Provenance und Integritäts-Lock

Für importierte oder lokal bereitgestellte Skills gilt zusätzlich die [Skill Provenance and Integrity Lock Governance](NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md): **lokale Verfügbarkeit ist kein Vertrauen**; unbekannte, veränderte oder provenance-unverifizierte Skill-Dateien werden für normative/sicherheitsrelevante Nutzung **fail-closed** behandelt; Skill-Import und -Update stehen unter einem Human-Maintainer-Gate; die technische Ausführung bleibt weiterhin separat und (docs-only) ausgeschlossen. Zusätzlich: der Status `verified` kann zunächst durch eine **dokumentierte manuelle Prüfung** belegt werden; automatische Verifikation oder Durchsetzung wird **noch nicht** behauptet; bestehende Projekte ohne historischen Lock benötigen einen **kontrollierten Migrationsstatus** (nicht automatisch als verifiziert behandeln); neue oder veränderte normative bzw. sicherheitsrelevante Skills bleiben ohne Verifikation fail-closed. Dieses Dokument dupliziert die Provenance-/Lock-Governance nicht — es verweist darauf.

## EN – Skill Provenance and Integrity Lock

For imported or locally provided skills, the [Skill Provenance and Integrity Lock Governance](NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md) additionally applies: **local availability is not trust**; unknown, modified, or provenance-unverified skill files **fail closed** for normative/security-sensitive use; skill import and update stay under a Human-Maintainer gate; technical execution remains separate and (docs-only) excluded. Additionally: the status `verified` may initially be established through a **documented manual check**; automated verification or enforcement is **not yet** claimed; existing projects without a historical lock require a **controlled migration state** (not treated as verified automatically); new or changed normative/security-sensitive skills stay fail-closed without verification. This document does not duplicate the provenance/lock governance — it references it.

## DE – Change Control

Erweiterungen des erlaubten Scopes (z. B. begrenzte Scripts) erfordern eine neue ausdrückliche ADR-/Scope-Entscheidung mit Human-Maintainer-Freigabe. Keine stille Ausweitung. Diese Policy ist über [ADR-0032](../adr/ADR-0032-skill-security-policy.md) governed.

## EN – Change Control

Extensions of the allowed scope (e.g., limited scripts) require a new explicit ADR/scope decision with human-maintainer approval. No silent expansion. This policy is governed via ADR-0032.

## DE – Nicht-Ziele

Kein aktives Claude Skills Pack; keine Skill-Scripts; keine netzwerkfähigen Skills; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Ersatz der Human-Maintainer-Kontrolle; kein v1.0-Release; keine aktive volle v1.x-Kompatibilitätszusage.

## EN – Non-Goals

No active Claude Skills Pack; no skill scripts; no network-enabled skills; no autonomous commit/push/tag/release actions; no replacement of human-maintainer control; no v1.0 release; no active full v1.x compatibility promise.

## DE – Nächste Schritte

**NDF-WP-111 – NDF Claude Skills Pack MVP Design** (referenziert diese Policy). Danach optional WP-112 (Implementation), WP-113 (Context Pack Template & Prompt Modes).

## EN – Next Steps

**NDF-WP-111 – NDF Claude Skills Pack MVP Design** (references this policy). Then optionally WP-112 (implementation), WP-113 (context pack template & prompt modes).
