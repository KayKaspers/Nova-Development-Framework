# NDF Relationship Model

## Zweck

Das Relationship Model beschreibt, wie die Domain-Objekte miteinander verbunden sind.

## Grundbeziehungen

```text
Project besitzt Project Brain
Project besitzt Roadmap
Project besitzt Work Packages
Project erzeugt Releases
Project erzeugt Lessons Learned

Lesson Learned verbessert Best Practice
Best Practice beeinflusst Standard
Standard erzeugt Rules
Rules erzeugen Quality Gates
Quality Gates prüfen Work Packages
Work Packages nutzen Prompts
Prompts nutzen Templates
Templates erzeugen Artifacts
Artifacts dokumentieren Decisions
Decisions werden als ADRs gespeichert
```

## Projektbeziehung

```text
Project
├── Project Brain
├── Modules
├── Capabilities
├── Standards
├── Work Packages
├── Artifacts
├── Releases
└── Lessons Learned
```

## Wissensbeziehung

```text
Knowledge Node
├── kann verweisen auf Standard
├── kann verweisen auf Rule
├── kann verweisen auf ADR
├── kann verweisen auf Prompt
├── kann verweisen auf Template
└── kann verweisen auf Project
```

## Prompt-Beziehung

```text
Prompt
├── basiert auf Prompt Blocks
├── erfüllt Prompt Standard
├── erzeugt Work Package Output
├── fordert Rückmeldung an Nova
└── kann Quality Gates referenzieren
```

## Compliance-Beziehung

```text
Compliance Check
├── prüft Project
├── nutzt Rules
├── nutzt Quality Gates
├── erzeugt Compliance Score
└── empfiehlt Work Packages
```
