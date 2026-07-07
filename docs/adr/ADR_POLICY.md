# ADR Policy

## DE – Zweck

Diese Policy regelt minimal und verbindlich, wann das Nova Development Framework (NDF) eine Architecture Decision Record (ADR) braucht, wo sie liegt, wie sie nummeriert wird und wer entscheidet. Sie ist das Ergebnis von **NDF-WP-086 (Foundation 0.6, Governance Hardening)** — die Entscheidung, die laut Foundation-0.5-Sonderregel nicht erneut verschoben werden durfte. Ergebnis: **Minimal ADR Policy adopted.**

## EN – Purpose

This policy minimally and bindingly regulates when the Nova Development Framework (NDF) needs an architecture decision record (ADR), where it lives, how it is numbered, and who decides. It is the result of **NDF-WP-086 (Foundation 0.6, governance hardening)** — the decision that, per the binding Foundation 0.5 special rule, could not be deferred again. Outcome: **minimal ADR policy adopted.**

## DE – Status

**Accepted** (NDF-WP-086, 2026-07-07). Diese Policy ist bewusst minimal: Sie kodifiziert die seit WP-033 dokumentierte, gelebte Praxis und erfindet keine neue Governance-Struktur. Sie muss sich in künftigen Work Packages bewähren; Änderungen nur per neuer ADR oder ausdrücklichem Work Package.

## EN – Status

**Accepted** (NDF-WP-086, 2026-07-07). Deliberately minimal: it codifies the practice documented since WP-033 and invents no new governance structure. It must prove itself in future work packages; changes only via a new ADR or an explicit work package.

## DE – Wann ist eine ADR erforderlich?

Eine ADR ist erforderlich bei Entscheidungen mit dauerhafter Wirkung über mehrere Work Packages hinweg:

- Architektur- oder Governance-Entscheidungen mit Wirkung über mehrere Work Packages
- Sicherheits- oder Destructive-Action-Patterns
- Release-/Versionierungsregeln (z. B. eine künftige v1.x-Kompatibilitätszusage)
- Public-Quality-Gate- oder Neutralitätsregeln
- Rollen-/Workflow-Invarianten (Nova (ChatGPT) → Implementation Agent → Human Maintainer)
- Entscheidungen, die v1.0-Reife oder Kompatibilität beeinflussen

## EN – When is an ADR Required?

An ADR is required for decisions with lasting effect across work packages: architecture or governance decisions spanning multiple work packages; security or destructive-action patterns; release/versioning rules (e.g. a future v1.x compatibility promise); public quality gate or neutrality rules; role/workflow invariants; decisions affecting v1.0 maturity or compatibility.

## DE – Wann reicht eine Work-Package-Notiz?

Eine WP-Note (`project-brain/WP_*_NOTES.md`) reicht bei:

- reinem Statusupdate
- kleiner Dokumentationskorrektur
- Umsetzung innerhalb eines bereits entschiedenen Patterns
- einmaligem Release-Prep-Schritt
- Review-Ergebnis ohne dauerhafte Policy-Wirkung

Faustregel: Wirkt die Entscheidung über das aktuelle WP hinaus als Regel → ADR. Beschreibt sie nur, was in diesem WP passiert ist → WP-Note.

## EN – When is a Work Package Note Enough?

A work package note suffices for pure status updates, small documentation fixes, implementation within an already-decided pattern, one-off release prep steps, and review results without lasting policy effect. Rule of thumb: if the decision acts as a rule beyond the current work package → ADR; if it only describes what happened in this work package → note.

## DE – Ablageort und Nummerierung

- **Neue ADRs entstehen ausschließlich in `docs/adr/`** im Muster `docs/adr/ADR-XXXX-short-title.md`.
- Vierstellige Nummer; die nächste freie Nummer ergibt sich aus der höchsten vorhandenen Nummer **über beide Ordner hinweg** (aktuell: **ADR-0031**).
- Kurzer, neutraler, kleingeschriebener Titel mit Bindestrichen.
- Keine privaten Projekt-/Personennamen im Dateinamen oder Inhalt, keine Secret-Begriffe, keine echten Domains.
- `adr/` (Repo-Wurzel) bleibt **eingefrorener Altbestand** der Foundation-0.1-Kernentscheidungen (ADR-0001–0026) — dort entsteht nichts Neues.

## EN – Location and Numbering

New ADRs are created exclusively in `docs/adr/` as `ADR-XXXX-short-title.md`; four-digit number, next free number derived from the highest existing number **across both folders** (currently **ADR-0031**); short neutral lowercase-hyphen title; no private names, secret terms, or real domains. The root `adr/` folder stays the **frozen legacy** of Foundation 0.1 core decisions — nothing new is created there.

## DE – ADR-Statuswerte / EN – ADR Status Values

```text
Proposed | Accepted | Superseded | Rejected | Deprecated
```

Optional zusätzlich `Deferred` für einzelne inhaltliche ADRs — **nicht** verwendbar, um Policy-Entscheidungen wie diese hier zu verschieben. / Optionally `Deferred` for individual content ADRs — **never** usable to defer policy decisions like this one.

## DE – Rollen und Entscheidung

- **Nova (ChatGPT):** Planungs-, Architektur- und Review-Rolle — empfiehlt und reviewt ADRs.
- **Implementation Agent:** darf ADR-Inhalte auf Anweisung entwerfen (Status `Proposed`).
- **Human Maintainer:** trifft die finale Entscheidung (`Accepted`/`Rejected`) und behält Repository- und Release-Kontrolle.

## EN – Roles and Decision Ownership

Nova (ChatGPT) recommends and reviews; the Implementation Agent may draft ADR content when instructed (status `Proposed`); the human maintainer makes the final decision and keeps repository and release control.

## DE – Mindestinhalt einer ADR / EN – Minimum ADR Content

Titel + Nummer, Status, Datum, Kontext, Entscheidung, Konsequenzen, betrachtete Alternativen, verbundene Work Packages, Public-Neutrality-Check. Vorlage: [`ADR_TEMPLATE.md`](ADR_TEMPLATE.md). / Title + number, status, date, context, decision, consequences, alternatives considered, related work packages, public neutrality check. Template: `ADR_TEMPLATE.md`.

## DE – Änderung bestehender ADRs

Angenommene ADRs werden nicht inhaltlich umgeschrieben. Eine neue Entscheidung ersetzt die alte per neuer ADR (`Superseded`-Verweis in beide Richtungen). Redaktionelle Korrekturen (Tippfehler, Links) sind erlaubt und brauchen keine neue ADR.

## EN – Changing Existing ADRs

Accepted ADRs are not rewritten. A new decision supersedes the old one via a new ADR (with `Superseded` cross-references). Editorial fixes (typos, links) are allowed without a new ADR.

## DE – Verhältnis zu Work Packages

ADRs und Work Packages ergänzen sich: Ein WP kann eine ADR vorschlagen oder umsetzen; die ADR hält die dauerhafte Regel fest, die WP-Note den Umsetzungsverlauf. Release-blocking Entscheidungen (z. B. Scope Locks) bleiben in ihren etablierten Dokumenten — sie brauchen keine doppelte ADR, solange kein dauerhaftes neues Muster entsteht.

## EN – Relationship to Work Packages

ADRs and work packages complement each other: a work package may propose or implement an ADR; the ADR records the lasting rule, the note records the implementation. Release-blocking decisions (e.g. scope locks) stay in their established documents — no duplicate ADR needed unless a lasting new pattern emerges.

## DE – Keine Massenmigration

Bestehende historische Entscheidungs- und Work-Package-Notizen werden durch diese Policy **nicht** massenhaft migriert. Sie bleiben gültige historische Nachweise, sofern kein späteres ausdrückliches Work Package etwas anderes entscheidet. Das gilt auch für die dokumentierte Nummernüberschneidung zwischen `adr/ADR-0001–0005` und `docs/adr/ADR-0001–0005`: Sie bleibt dokumentierter Altbestand (siehe [`README.md`](README.md)); künftige Nummern kollidieren durch die Regel oben nicht mehr.

## EN – No Mass Migration

Existing historical decision notes and work-package notes are **not** mass-migrated by this policy. They remain valid historical records unless a future explicit work package decides otherwise. This also covers the documented numbering overlap between `adr/ADR-0001–0005` and `docs/adr/ADR-0001–0005`: it stays documented legacy; future numbers no longer collide due to the rule above.

## DE – Public Neutrality

ADRs sind öffentliche Dokumente: keine privaten Projekt-/Personen-/Organisationsnamen, keine echten Domains oder Kontaktwege, keine Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden). Der Public Quality Gate v0.2 (inkl. new-file neutrality check) gilt für jede neue ADR.

## EN – Public Neutrality

ADRs are public documents: no private project/person/organization names, no real domains or contact channels, no secret values (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed). The public quality gate v0.2 (incl. the new-file neutrality check) applies to every new ADR.

## DE – Nicht-Ziele

Keine ADR-Massenmigration; kein Umbau des eingefrorenen `adr/`-Altbestands; keine ADR-Pflicht für jedes WP; keine neue Governance-Bürokratie über das Minimum hinaus; kein v1.0-Claim (diese Policy schließt ein offenes v1.0-Kriterium, behauptet aber keine v1.0-Reife).

## EN – Non-Goals

No ADR mass migration; no rebuild of the frozen root `adr/` legacy; no ADR obligation for every work package; no governance bureaucracy beyond the minimum; no v1.0 claim (this policy closes an open v1.0 criterion but claims no v1.0 maturity).
