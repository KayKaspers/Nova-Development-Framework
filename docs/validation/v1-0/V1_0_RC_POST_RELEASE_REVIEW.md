# v1.0 RC Post-Release Review

## DE – Titel

Post-Release-Review und Feedback-Triage für `v1.0.0-rc.1` (NDF-WP-144, Skill-assisted Full Prompt Mode).

## DE – Status / Ergebnis

**GO WITH NOTES – RC published and post-release triage started.** Der Tag `v1.0.0-rc.1` existiert (annotated, vom Human Maintainer erstellt) und zeigt auf den RC-Commit `4beab84` (WP-143). RC-01 (Gate) und RC-10 (Changelog/RC-Notes) sind auf dem RC-Commit **read-only bestätigt**. `v1.0.0-rc.1` ist ein Release Candidate, **nicht** final v1.0; **keine volle v1.x-Zusage aktiv**. v1.0 final wird in diesem WP **nicht** aktiviert. Foundation 0.9 bleibt released/published — reconciliation documented. ADR-0031/0032 unverändert.

## EN – Status / Result

**GO WITH NOTES – RC published and post-release triage started.** The tag `v1.0.0-rc.1` exists (annotated, created by the Human Maintainer) and points to the RC commit `4beab84` (WP-143). RC-01 (gate) and RC-10 (changelog/RC notes) are read-only confirmed on the RC commit. `v1.0.0-rc.1` is a release candidate, **not** final v1.0; **no full v1.x promise is active**. v1.0 final is not activated here. Foundation 0.9 stays released/published — reconciliation documented. ADR-0031/0032 unchanged.

## DE – Scope

Dokumentation des veröffentlichten RC-Status; Bestätigung, dass Tag/Release manuell durch den Human Maintainer erfolgten; Nachprüfung RC-01/RC-10; Triage der Known RC Notes; G-13-Final-Weg-Bewertung; Feedback-Triage-Vorbereitung; Empfehlung der nächsten WPs. **Nicht im Scope:** v1.0-Final-Aktivierung, volle v1.x-Zusage, GitHub-Release editieren, neue/geänderte Skills, Scripts, Netzwerk, Commit/Push/Tag/Release durch AI.

## EN – Scope

Documenting the published RC status; confirming tag/release were done manually by the Human Maintainer; re-checking RC-01/RC-10; triaging the known RC notes; assessing the G-13 final path; preparing feedback triage; recommending next WPs. Out of scope: v1.0 final activation, full v1.x promise, editing the GitHub release, new/changed skills, scripts, network, AI commit/push/tag/release.

## DE – RC-Veröffentlichungsstatus

| Aspekt | Befund (read-only) |
|---|---|
| Tag `v1.0.0-rc.1` vorhanden | **ja** |
| Tag-Typ | **annotated** (`git cat-file -t` → `tag`) |
| Tag-Ziel | RC-Commit `4beab84` (WP-143, „docs(v1): prepare v1.0 rc release") |
| Tag-Erstellung | durch den **Human Maintainer** (Tagger im Tag-Objekt; nicht durch einen AI-Agenten) |
| Release-Typ | Pre-release / Release Candidate (per Tagging-Guide; **nicht** „Latest", nicht final) |
| GitHub-Pre-Release-Publikation | **nicht netzwerk-verifizierbar** (ADR-0032: kein Netzwerk) → als Human-Maintainer-bestätigt behandelt; Tag + Tagging-Guide belegen den manuellen Pfad |
| Final v1.0 | **nein** (nicht aktiviert) |
| Volle v1.x-Zusage | **nicht aktiv** |

**Hinweis:** Die GitHub-Release-Seite selbst wurde nicht abgerufen (kein Netzwerkzugriff). Der annotated Tag und der [Tagging-Guide](../../release/V1_0_RC_1_TAGGING_AND_GITHUB_RELEASE_GUIDE.md) bestätigen den manuellen Human-Maintainer-Release-Pfad.

## EN – RC Publication Status

The annotated tag `v1.0.0-rc.1` (created by the Human Maintainer) points to RC commit `4beab84`; the release type is pre-release/RC per the tagging guide (not "Latest", not final). The GitHub pre-release page itself is not network-verifiable (ADR-0032 no network) and is treated as human-maintainer-confirmed; the annotated tag and tagging guide evidence the manual path. Not final v1.0; no full v1.x promise active.

## DE – RC-01 / RC-10 Nachprüfung

- **RC-01 (Gate auf RC-Commit):** **grün.** `python scripts/check_public_quality.py --strict` (0/0/4) und `--self-test` auf HEAD == Tag-Commit `4beab84` bestätigt.
- **RC-10 (Changelog/RC-Notes):** **sichtbar.** Der `v1.0.0-rc.1`-Eintrag ist im RC-Commit vorhanden; RC als „prepared, pending Human Maintainer release" ehrlich benannt; Known RC Notes (G-13 tracked, ECS-001, „nicht final") sichtbar.

## EN – RC-01 / RC-10 Re-check

RC-01 (gate on RC commit): **green** (strict 0/0/4 + self-test on HEAD == tag commit `4beab84`). RC-10 (changelog/RC notes): **visible** (the `v1.0.0-rc.1` entry is present; RC honestly labeled; known RC notes visible).

## DE – Known RC Notes Triage

| Note ID | Note | Status | Final Impact | Recommended Action |
|---|---|---|---|---|
| G-13 | External Validation Evidence Depth | **requires final action** | vor v1.0 final Weg A oder B nötig | in WP-145 Final Readiness entscheiden (Weg-Empfehlung unten) |
| ECS-001 | Extended-Core-Skill-Real-use-Historie | accepted for RC | breitere Historie stärkt final, kein Blocker | im Betrieb weiter sammeln; optional in Final Readiness bewerten |
| N-01 | keine volle v1.x-Zusage vor final | accepted for RC | volle Zusage bei v1.0 final aktivieren (F-03) | im v1.0-Final-Zyklus aktivieren |
| N-02 | RC ist nicht final | accepted for RC | Kandidaten-Label bis final | beibehalten bis v1.0 final |
| N-03 | Project-Enablement-Skills optional/post-v1.0 | accepted for RC | kein Final-Blocker | post-v1.0 Kandidat |
| N-04 | optionale Governance-Skills optional | accepted for RC | kein Final-Blocker | optional, nur bei Bedarf |
| N-05 | zweiter Fixture-Typ dokumentierte Grenze | accepted for RC | Non-Goal/tracked für v1.0 | als dokumentierte Grenze führen |

**Zusammenfassung:** 1× requires final action (G-13); 6× accepted for RC. Keine Note ist ein Final-Blocker per se, sofern G-13 vor final über Weg A oder B behandelt wird.

## EN – Known RC Notes Triage

The table triages the seven known RC notes: G-13 requires final action (path A or B before final); the other six are accepted for RC (ECS-001 broadens over time; the full v1.x promise activates at final per F-03; RC-not-final label kept; project-enablement/optional-governance skills stay optional; second fixture type stays a documented limit). No note is a final blocker per se, provided G-13 is handled before final.

## DE – G-13 Final-Weg-Bewertung

| Weg | Nutzen | Aufwand | Risiko | Glaubwürdigkeit | v1.0-Final-Tauglichkeit |
|---|---|---|---|---|---|
| A – tieferer öffentlicher neutraler Lauf mit Schrittbelegen | hoch (hebt Evidence auf `met`) | mittel–hoch | gering | hoch | stark |
| B – dokumentierte akzeptierte Grenze / Known Limitation | mittel (Ehrlichkeit) | gering | gering | mittel (transparent) | tragfähig |
| **C – Kombination A + B** | **hoch** | mittel | gering | **hoch** | **stark** |

**Empfehlung: Weg C (Kombination).** Begründung: Ein realistisch dimensionierter, schrittbelegter öffentlicher Neutral-Lauf (A) sollte angestrebt werden, weil er die Evidence am glaubwürdigsten auf `met` hebt; **gleichzeitig** wird eine ehrliche dokumentierte akzeptierte Grenze (B) als **garantierter Fallback** vorbereitet, damit v1.0 final nicht am Ein-Personen-Engpass hängen bleibt. Falls A vor final nicht leistbar ist, trägt B den Final-Pfad transparent. Die Wegwahl bestätigt der Human Maintainer in der Final Readiness (WP-145).

## EN – G-13 Final Path Assessment

The table rates paths A (deeper public step-evidenced run), B (documented accepted boundary), and C (combination) by benefit, effort, risk, credibility, and v1.0-final suitability. **Recommendation: path C (combination)** — pursue a realistically scoped step-evidenced public run (A) as the most credible way to lift the evidence to `met`, while preparing an honest documented accepted boundary (B) as a guaranteed fallback so v1.0 final is not blocked by the single-person bottleneck. The Human Maintainer confirms the path in the final readiness review (WP-145).

## DE – Feedback-Triage

**No external RC feedback captured yet.** Es liegt (read-only, ohne Netzwerkzugriff) kein dokumentiertes externes RC-Feedback im Repository vor. Es wird **kein** Feedback erfunden und **keine** Reviewer-Identität dokumentiert.

| ID | Source Type | Summary | Severity | Action | Public-Neutrality |
|---|---|---|---|---|---|
| — | — | kein externes RC-Feedback bisher erfasst | note | needs review | neutral |

**Empfehlung:** ein **Feedback-Fenster / Review-Schritt** vor der Final Readiness (WP-145) — Rückmeldungen zum RC (public-neutral, ohne Reviewer-Identitäten) sammeln und triagieren. **Kein Zeitplan** wird erfunden.

## EN – Feedback Triage

No external RC feedback captured yet (read-only, no network). No feedback is invented and no reviewer identity is documented. Recommendation: a feedback window / review step before final readiness (WP-145), collecting and triaging RC feedback public-neutrally, with no reviewer identities and no invented schedule.

## DE – Empfohlene nächste WPs

1. **WP-145 – v1.0 Final Readiness Review** (bezieht ein: RC-Feedback-Fenster, G-13-Wegwahl A/B/C durch den Human Maintainer, ECS-001-Stand; ehrlicher Gesamt-Check gegen die Final-Kriterien F-01…F-07).
2. **WP-146 – v1.0 Final Release Prep** (Final Release Notes / Go-No-Go / Tagging-Guide, nur Doku; volle v1.x-Zusage-Aktivierung als dokumentierter Final-Schritt).
3. **Danach:** manueller v1.0-Final-Release durch den Human Maintainer.

**Optional vor WP-145 (nur falls Weg A gewählt):** ein dedizierter **Final External Validation / Neutral Sample Re-Run** (schritt­belegt) — nicht blockierend, da Weg B als Fallback existiert. Kein separater Zwischen-WP wird erzwungen.

## EN – Recommended Next WPs

WP-145 (v1.0 final readiness review — incorporating an RC feedback window, the human-maintainer G-13 path choice A/B/C, ECS-001 status; an honest check against final criteria F-01…F-07) → WP-146 (v1.0 final release prep, docs only; full v1.x promise activation as a documented final step) → manual v1.0 final release by the Human Maintainer. Optional before WP-145 (only if path A is chosen): a dedicated step-evidenced final external validation / neutral sample re-run — non-blocking, since path B is a fallback.

## DE – Security / ADR-0031 / ADR-0032 Bewertung

ADR-0031/0032 unverändert bindend; keine v1.0-Final-Aktivierung; volle v1.x-Zusage erst mit v1.0 final. Kein Commit/Push/Tag/Release durch AI; das GitHub-Release wurde nicht editiert; kein Netzwerkzugriff. Keine Skills geändert/erstellt; keine Scripts/Netz/Secrets/privaten Daten; keine Reviewer-Identitäten/privaten Namen/Domains. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name. Nächste freie ADR-Nummer: 0033.

## EN – Security / ADR-0031 / ADR-0032 Assessment

ADR-0031/0032 stay binding and unchanged; no v1.0 final activation; full v1.x promise only at final. No AI commit/push/tag/release; the GitHub release was not edited; no network access. No skill changes/creations; no scripts/network/secrets/private data; no reviewer identities/private names/domains; secret name only as a name; next free ADR number 0033.

## DE – Risks / Open Notes

- **G-13** ist der einzige „requires final action"-Punkt; Weg C empfohlen (A anstreben, B als garantierter Fallback).
- **Kein RC-Feedback bisher erfasst** — Feedback-Fenster vor Final Readiness empfohlen.
- **GitHub-Publikation nicht netzwerk-verifizierbar** — als Human-Maintainer-bestätigt geführt (annotated Tag als Beleg).
- **Ein-Personen-Engpass** (dokumentiertes Risiko; stützt Weg B als Fallback).
- **Kein Zeitplan; kein v1.0-final-Claim.**

## EN – Risks / Open Notes

G-13 is the only "requires final action" item (path C recommended: pursue A, keep B as a guaranteed fallback); no RC feedback captured yet (feedback window recommended before final readiness); GitHub publication not network-verifiable (treated as human-maintainer-confirmed via the annotated tag); the single-person bottleneck supports path B as a fallback; no schedule; no v1.0-final claim.

## DE – Decision

**GO WITH NOTES – RC published and post-release triage started.** Tag bestätigt (annotated, Human-Maintainer, → `4beab84`); RC-01/RC-10 read-only bestätigt; Known RC Notes triagiert (G-13 requires final action, Weg C empfohlen); kein RC-Feedback bisher; keine v1.0-Final-Aktivierung/volle v1.x-Zusage; ADR-0031/0032 unverändert. **Nächster empfohlener WP: WP-145 – v1.0 Final Readiness Review.**

## EN – Decision

**GO WITH NOTES – RC published and post-release triage started.** Tag confirmed (annotated, human-maintainer, → `4beab84`); RC-01/RC-10 read-only confirmed; known RC notes triaged (G-13 requires final action, path C recommended); no RC feedback yet; no v1.0 final activation/full v1.x promise; ADR-0031/0032 unchanged. Next recommended WP: WP-145 – v1.0 Final Readiness Review.
