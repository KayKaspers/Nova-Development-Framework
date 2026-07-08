# Project Brain – WP-099 Checklist DE/EN Decision Notes

## Summary

Verbindliche Foundation-0.7-Entscheidung zum Dauerläufer Checklist DE/EN getroffen: **Option B — optional mit finaler Begründung.** Kein Foundation-Release-Blocker, kein Auto-Carry mehr, kein Folge-WP. Der stille Weiterschleppung-Zyklus (seit 0.4) ist damit beendet.

## Inputs reviewed

0.7-Scope-Lock (WP-099-Korridor A/B/C, kein stilles Verschieben), Thema-Historie (WP-061/0.4 → WP-075/0.5 → WP-091/0.6, jeweils optional/unerledigt), tatsächliche Checklisten im Repo, Translation-Status-Matrix.

## Checklist inventory

- **Release-Go/No-Go-Checklisten (0.1–0.6):** vollständig DE/EN (je Release bilingual erstellt) — die release-kritischen Checklisten sind schon zweisprachig.
- **`framework/checklists/` (10 Stück):** seit WP-039 bilinguale Zweck-Blöcke; Punktlisten gemischt, aber funktional nutzbar (Zweck/Grenzen/Entscheidungswerte erschlossen). Stichprobe bestätigt: PROJECT_ADAPTER (EN-Zweck + DE-Punkte), PUBLIC_QUALITY_GATE (DE/EN-Zweck + gemischte Punkte).
- **2 rein einsprachige:** AGENT_ENDPOINT_DESTRUCTIVE, BACKUP_DELETE_SAFETY — tiefe Security-/Destructive-Werkzeuge, kein Erstkontakt-Material.
- **`TRANSLATION_STATUS.md`:** führt `framework/checklists/` bereits ehrlich als „mixed".
- Lücken-Schwere insgesamt: **low–medium, keine High-/Blocker-Lücke.**

## Options considered

A (priorisieren) verworfen — keine release-relevante Lücke, Voll-Übersetzung wäre Scope Creep weg von WP-100/101. C (streichen) verworfen — Punktlisten-DE/EN hat echten kleinen Wert, bleibt legitimer i18n-Backlog. **B gewählt** — passt zum Befund und beendet den Auto-Carry.

## Decision A/B/C

**B — optional mit finaler Begründung.**

## Rationale

Release-Checklisten schon DE/EN; operative Checklisten mit bilingualen Zweck-Blöcken; ehrliche Matrix vorhanden; einsprachige Reste sind Fach-Tiefe, kein Erstkontakt. Externe Nutzbarkeit gewährleistet, 0.7 nicht releasegefährdet. Das eigentliche Governance-Problem war der wiederholte Auto-Carry — B beendet ihn, ohne einen ehrlichen i18n-Backlog-Punkt zu verstecken.

## Impact on Foundation 0.7

Checklist DE/EN blockiert 0.7 nicht (war nie blocking). Blocking Kern unverändert: 098/099 (done)/100/101/104/105. Nächster inhaltlicher Schritt: WP-100.

## Impact on v1.0 path

Kein direktes v1.0-Kriterium; der v1.0-Draft führt „vollständige Zweisprachigkeit" bereits als **nicht erforderlich** — Entscheidung konsistent. Keine v1.0-Kriterien abgehakt.

## Follow-up handling

Kein Folge-WP nötig. Spätere Punktlisten-DE/EN-Arbeit nur über bewussten neuen Scope (Nova-Review + Maintainer-Freigabe), nicht als Auto-Carry. Reststand bleibt in der Matrix geführt.

## What was not done

Keine Voll-Übersetzung, keine große i18n-/Checklist-Umsetzung, kein neuer blocking WP, keine 0.7-/v1.0-Behauptung, keine Änderung an den Checklisten-Inhalten selbst.

## Risks

Gering: Falls ein rein englischsprachiger Nutzer die gemischten Punktlisten doch als Hürde meldet, kann über bewussten neuen Scope ein i18n-WP nachgezogen werden — das ist ehrlich in Matrix und Entscheidung dokumentiert.

## Next step

**NDF-WP-100 – v1.x Compatibility Policy Decision / ADR-0031 Preparation.**
