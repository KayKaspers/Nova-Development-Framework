# ADR-0032: Skill Security Policy

## Status

Accepted

## Date

2026-07-08

## Context

Foundation 0.8 (Scope Lock, NDF-WP-108) macht **Agent Enablement & Context Economy** zum Thema und benennt eine **Skill Security Policy** als release-blocking (NDF-WP-110), mit ADR-0032 als bevorzugtem Pfad. NDF plant ein kleines, public-neutrales Claude Skills Pack (MVP-Design in WP-111, Implementierung optional in WP-112). Bevor Skills existieren, braucht NDF verbindliche Sicherheitsgrenzen, damit Skills die bestehenden Invarianten (Human-Maintainer-Kontrolle, Public Quality Gate, Public Neutrality) niemals aushöhlen.

Diese ADR ist die **Governance-Entscheidung**. Das operative Regelwerk steht im separaten Dokument `docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md` (Option A), das WP-111 und optional WP-112 referenzieren.

## Decision

NDF nimmt eine **Skill Security Policy** nach dem **Fail-Closed-Prinzip** an: Was nicht ausdrücklich erlaubt ist, ist verboten. Skills unterstützen NDF-Abläufe, ersetzen aber niemals die Human-Maintainer-Kontrolle und lösen keine autonomen Git-/Release-/Netzwerk-/Secret-Aktionen aus. Die Policy gilt für alle NDF-bezogenen Skills — auch für künftige, während WP-112 optional bleibt.

## Skill Security Policy

### Fail-Closed Principle

Wenn eine Fähigkeit nicht ausdrücklich in „Allowed Skill Scope" erlaubt ist, ist sie verboten. Im Zweifel: verbieten, an den Human Maintainer eskalieren.

### Allowed Skill Scope

Erlaubt sind ausschließlich **docs-only, read-only-orientierte** Hilfen: Struktur-/Textvorschläge für Work-Package-Arbeit, Formulierungshilfe für die Rückmeldung an Nova und die Compact Context Summary, Neutralitäts-/Checklisten-Erinnerungen, Zusammenfassen bereits vorhandener öffentlicher Repo-Inhalte. Skill-Ausgaben sind Vorschläge — der Human Maintainer entscheidet und führt aus.

### Forbidden Skill Capabilities

Verboten (sofern nicht später durch eine ausdrückliche ADR-/Scope-Entscheidung eng begrenzt erlaubt): autonome Commits, Pushes, Tags, Releases; GitHub-Release-Erstellung/-Änderung; Netzwerkzugriffe; Secret-Verarbeitung; private Projektlogik; Drittanbieter-Skill-Import; Scripts im Skill-MVP; destruktive Aktionen; Umgehung des Public Quality Gate; Umgehung der Rückmeldung an Nova; Umgehung der Human-Maintainer-Gates.

### Human Maintainer Gates

Der Human Maintainer bleibt finaler Owner: Er entscheidet GO / GO WITH NOTES / REWORK / STOP, committet, pusht, taggt und veröffentlicht. Skills treffen keine irreversiblen Entscheidungen.

### Public Quality Gate

Der Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante. Skills dürfen ihn weder umgehen noch abschalten; Skill-erzeugte Dateien unterliegen ihm wie alle anderen.

### Public Neutrality

Skills dürfen keine privaten Projekt-/Personennamen, Reviewer-Identitäten, Kontaktwege oder echten Domains einführen. Der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden; der Wert oder einzelne Denylist-Begriffe niemals.

### Secrets and Private Data

Skills verarbeiten, speichern oder dokumentieren keine Secrets und keine privaten Projektdaten. Keine Roh-Chat-Historie, keine Chain-of-Thought.

### Third-Party Skills

Kein ungeprüfter Import von Drittanbieter-Skills oder externen Skill-Inhalten; keine Übernahme externer Branding-/Autorenhinweise.

### Scripts and Tool Use

Skills sind zunächst **docs-only**. Scripts sind verboten, bis eine spätere ausdrückliche ADR-/Scope-Entscheidung sie eng begrenzt erlaubt (mit definierten Grenzen, Review und Human-Maintainer-Freigabe).

### Network Access

Netzwerkzugriffe durch Skills sind verboten.

### Git and Release Actions

Git-Schreibaktionen (commit/push/branch/tag) und Release-/Tag-Aktionen durch Skills sind verboten. Diese Aktionen bleiben ausschließlich beim Human Maintainer.

### Destructive Actions

Destruktive oder irreversible Aktionen durch Skills sind verboten. Für gefährliche Funktionen gilt weiterhin das NDF-Muster destructive-blueprint → destructive-implementation unter menschlicher Freigabe — nie durch einen Skill ausgelöst.

### Context Economy Relationship

Context Economy (WP-109) reduziert unnötigen Kontext, **nicht** Sicherheit. Short Prompts und Token-Sparen dürfen keine Sicherheitsprüfung, keine erforderliche Evidenz und kein Human-Maintainer-Gate ersetzen oder umgehen.

### Rückmeldung an Nova and Compact Context Summary

Jeder WP-bezogene Skill unterstützt die Rückmeldung an Nova (ChatGPT) und die Compact Context Summary und darf sie nicht umgehen oder verkürzen, wo sie erforderlich sind.

### Change Control

Erweiterungen des erlaubten Scopes (z. B. begrenzte Scripts) erfordern eine neue ausdrückliche ADR-/Scope-Entscheidung mit Human-Maintainer-Freigabe. Keine stille Ausweitung.

## Consequences

NDF hat verbindliche Skill-Sicherheitsgrenzen, bevor Skills existieren. WP-111 (MVP Design) und optional WP-112 (Implementation) bauen auf dieser Policy auf. Die Human-Maintainer-Kontrolle, das Public Quality Gate und die Public Neutrality bleiben unangetastet. Die Policy ist bewusst restriktiv (fail closed) und kann später nur per ausdrücklicher Governance-Entscheidung gelockert werden.

## Non-Goals

Diese ADR erstellt **kein** aktives Claude Skills Pack. Sie erlaubt **keine** Skill-Scripts, **keine** netzwerkfähigen Skills und **keine** autonomen Commit-/Push-/Tag-/Release-Aktionen. Sie ersetzt **nicht** die Human-Maintainer-Kontrolle und macht Foundation 0.8 **nicht** zu einem v1.0-Release; sie aktiviert **keine** volle v1.x-Kompatibilitätszusage.

## Follow-ups

- NDF-WP-111 – NDF Claude Skills Pack MVP Design (referenziert diese Policy).
- NDF-WP-112 – NDF Claude Skills Pack MVP Implementation (optional; nur per Human-Maintainer-Scope-Change hochstufbar).
- Nächste freie ADR-Nummer: ADR-0033.
