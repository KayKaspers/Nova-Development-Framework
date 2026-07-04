# Initial Work Package Queue (Template)

Erste Work Package Queue nach der Adapter-Ausführung.

**Hinweis zu den IDs:** `XY-WP-xxx` ist ein **Platzhalter-Präfix**. Für echte Projekte ein eigenes, neutrales Präfix aus dem Projektnamen wählen (2–4 Buchstaben), z. B. `XY-WP-001`. Nicht das Framework-Präfix `NDF-WP` verwenden. (Das frühere Beispiel `SP-WP` kollidierte mit „SampleProject" und wurde in WP-059 ersetzt.)

| ID | Titel | Typ | Priorität | Status | Hinweis |
|---|---|---|---|---|---|
| XY-WP-001 | Project System Baseline | project-adapter | P1 | ready | NDF-Artefakte anlegen (docs-only) |
| XY-WP-002 | Documentation Stability Review | review-only | P1 | ready | Doku-Lücken erfassen, nichts ändern |
| XY-WP-003 | Security Baseline Review | security-baseline | P1 | ready | Findings ohne Code-Fixes |
| XY-WP-004 | Health Score Initialization | health-score-update | P2 | draft | nach XY-WP-002/003 mit Evidenz |
| XY-WP-005 | First Safe Improvement | docs-only oder code-fix | P2 | draft | kleinster sinnvoller Schritt aus den Reviews |

## Regeln

- Jedes WP hat genau einen primären Typ (`framework/standards/WORK_PACKAGE_TYPES.md`).
- Das erste umgesetzte WP muss klein und sicher sein — kein Feature, nichts Destruktives.
- Destruktive Funktionen laufen ausschließlich über `destructive-blueprint` → `destructive-implementation`.
- Jedes WP endet mit einer Rückmeldung an Nova und Maintainer-Review vor dem Commit.
