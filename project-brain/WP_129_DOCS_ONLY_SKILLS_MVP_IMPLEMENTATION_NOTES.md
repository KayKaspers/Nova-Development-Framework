# NDF-WP-129 – Docs-only Skills MVP Implementation (Notes)

## Ziel

Das docs-only Skills MVP aus WP-125 mit engem Scope umsetzen: genau die vier empfohlenen MVP-Skills als reine Markdown-`SKILL.md` plus Index, ADR-0032-konform, fail-closed, ohne Scripts/Netz/Secrets/private Daten/Git-Release-Aktionen. Ziel ist Prompt-Kompression ohne Schwächung der NDF-Governance.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-125 committet `9fa85a8`, Working Tree sauber). Kein Blocker.

## Aktivierungs-/Scope-Hinweis

Der Human Maintainer hat WP-129 ausdrücklich mit dem Scope „genau die vier MVP-Skills als docs-only Skill Pack, keine Extended Skills, keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen" aktiviert. Bis WP-128/WP-133 galt „keine `.claude/skills`, keine `SKILL.md`"; dieser Scope wird mit WP-129 **ausdrücklich und ausschließlich** für diese vier Skills geändert.

## Implementierte Skills (genau vier)

1. `ndf-work-package-runner` — WP-Rahmen: Rolle, Guardrails, Self-Check, Abschlussstruktur, Prompt-Mode-Respekt.
2. `ndf-compact-context-summary-runner` — Enforcement-Punkt für Rückmeldung an Nova + Compact Context Summary.
3. `ndf-public-neutrality-guard` — Neutralitäts-/Secret-Namensregel-Reminder; **kein** CI-Gate.
4. `ndf-context-pack-maintainer` — Context Pack konsistent/kurz halten; erfindet keinen Status.

## Angelegte Dateien

- `.claude/skills/README.md` (Index)
- `.claude/skills/ndf-work-package-runner/SKILL.md`
- `.claude/skills/ndf-compact-context-summary-runner/SKILL.md`
- `.claude/skills/ndf-public-neutrality-guard/SKILL.md`
- `.claude/skills/ndf-context-pack-maintainer/SKILL.md`
- `docs/validation/foundation-0-9/DOCS_ONLY_SKILLS_MVP_VALIDATION.md`
- `project-brain/WP_129_DOCS_ONLY_SKILLS_MVP_IMPLEMENTATION_NOTES.md` (diese Notiz)

## Aktualisierte Statusdokumente

- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md` (WP-129-Zeile: erledigt, implemented as docs-only MVP)
- `docs/roadmap/FOUNDATION_0_9_PLAN.md` (dokumentarischer Hinweis WP-129)
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md` (Next → Skill-/Prompt-Compression-Validation)
- `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md` (Last/Next WP, History, Next Prompt Recommendation, Deferred-Note)
- `CHANGELOG.md` (WP-129-Zeile)

## Jede SKILL.md enthält

Title, Purpose, When to use, Required inputs, Expected outputs, Allowed actions, Forbidden actions, Fail-closed behavior, Public-neutrality requirements, ADR-0032 safety boundaries, Human-maintainer-only boundaries, Output contract, Compact-Context-Summary/Rückmeldung-an-Nova-Bezug. Keine Chain-of-Thought, keine privaten Daten, keine Secret-Werte.

## Validierung

Docs-only: ja · genau vier MVP-Skills: ja · keine Extended Skills: ja · keine Scripts: ja · kein Netzwerk: ja · keine Secrets (nur Name): ja · keine privaten Daten: ja · keine Git-/Release-Aktionen: ja · ADR-0032: unverändert bindend · Public Neutrality: Gate grün. Details: [Validation](../docs/validation/foundation-0-9/DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (18-Punkte-Matrix).

## Token-Economy-Einschätzung

Qualitativ hoch–sehr hoch: Rolle, Guardrails, Neutralitäts-/Secret-Regeln, Abschlussformat, Rückmeldung an Nova, Compact Context Summary und Self-Check wandern aus dem Prompt in die Skills. Realer Vorher/Nachher-Nachweis steht aus (DSK-001) → Folge-WP.

## Risiken / offene Punkte

- DSK-001: Prompt-Ersparnis noch nicht empirisch gemessen (Folge-WP).
- Scope Creep: Nur vier Skills; Extended bewusst nicht implementiert.
- Neutralitäts-Fehldeutung: Guard ≠ Gate-Runner; realer Gate maßgeblich.
- Skills sind additiv; keine Governance-Änderung, keine Aktivierung von WP-130/131/132.

## Nächster empfohlener Schritt

**Skill-/Prompt-Compression-Validation** (realer Vorher/Nachher-Prompt-Overhead an einem echten WP) — oder, falls Repo-Konvention näher, **v1.0 Gap Review**. WP-130/131/132 bleiben optional/nicht aktiviert. Nächste freie ADR-Nummer: 0033.
