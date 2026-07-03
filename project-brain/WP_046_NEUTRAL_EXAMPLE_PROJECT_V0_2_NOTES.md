# Project Brain – WP-046 Neutral Example Project v0.2 Notes

## Zweck

`examples/neutral-example-project/` enthält **SampleProject** — ein fiktives, neutrales Pre-Adoption-Fixture für die praktische Adapter-Validierung (NDF-WP-047). Kein echtes Produkt, keine lauffähige Software, keine echten Namen/Domains/Secrets (nur `SampleProject`, `example-owner`, `example.local`, `EXAMPLE_SECRET_PLACEHOLDER`).

## Erstellte Dateien (13)

README (bilingual, Zweck + WP-047-Nutzung) · PROJECT_BRIEF (Intake-Input) · CURRENT_STATE (Lücken/Schulden) · REQUIREMENTS (inkl. Security + DE/EN) · ARCHITECTURE_OVERVIEW (bewusst unvollständig) · SECURITY_NOTES (inkl. harmlosem Destructive-Fall „Notiz löschen") · ROADMAP (unklare Prioritäten) · RISKS (7 Risiken) · MOCK_REPOSITORY_TREE (fiktive Repo-Struktur mit Auffälligkeiten) · sample-docs/ (3 bewusst unvollständige Doku-Dateien mit Fixture-Hinweis) · expected-adapter-output/README (Erwartungsdefinition für WP-047)

## Design-Entscheidungen

- **Abgrenzung zu `minimal-ndf-project`:** dieses zeigt Post-Adoption, das neue Fixture Pre-Adoption — bewusst getrennt, wechselseitig referenziert; kein Ausbau des Bestands nötig (Abweichung vom WP-044-Queue-Text, im Queue-Eintrag korrigiert).
- **Eingebaute Findings:** Port-Widerspruch (README 3000 vs. Deployment 8080), zwei Destructive-Kandidaten (Notiz-Löschung, `reset-db.sh`), doppelte Konfigquellen, rote CI, geteilter Admin, Secret-per-Chat-Antipattern — genug Substanz für alle Adapter-Phasen.
- **Fixture-Hinweise** in den „unvollständigen" Dateien, damit niemand sie für echte NDF-Doku hält.
- Erwartungen definieren die **Bewertung des Adapters** (Abweichung = Finding über den Adapter, nicht über das Fixture).

## Nutzung durch WP-047

Intake mit PROJECT_BRIEF → Read-only Review über alle Fixture-Dateien → Baseline-Artefakte erzeugen → gegen expected-adapter-output bewerten → Adapter-Findings an Nova (ChatGPT); Scope-Lock-Findings-Regel beachten.

## Bekannte Grenzen

1. Nur Doku-Fixture — kein echter Code, daher testet WP-047 die Analyse-/Doku-Phasen, nicht z. B. echtes `git status` im Zielprojekt.
2. Bewusst klein gehalten; sehr große Projekte (Monorepos, viele Teams) bildet es nicht ab.
3. DE-lastig mit bilingualem README — passt zur fiktiven Teamsituation, ist im Fixture selbst dokumentiert.

## Nächstes empfohlenes WP

NDF-WP-047 – Project Adapter Practical Validation (parallel weiterhin möglich: NDF-WP-052).
