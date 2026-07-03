# DE/EN-Sprachstandard / DE/EN Language Standard

## DE

### Ziel

Das Nova Development Framework soll vollständig zweisprachig (Deutsch/Englisch) nutzbar sein. Öffentliche Nutzer sollen NDF auf Englisch verstehen können; die deutsche Fassung bleibt gleichwertig erhalten.

### Grundsatz

Neue öffentliche NDF-Dokumente sind entweder **bilingual** oder besitzen eine **klare Sprachzuordnung** (dokumentiert in `docs/i18n/TRANSLATION_STATUS.md`).

### Bevorzugtes Format für zentrale Dokumente

```text
# Deutscher Titel / English Title

## DE

Deutscher Inhalt.

## EN

English content.
```

### Parallele Dateien

Für längere Dokumentation sind parallele Dateien erlaubt:

```text
DOCUMENT.de.md
DOCUMENT.en.md
```

### Prompts

- Framework-Prompts dürfen zweisprachig geführt werden, wenn sie öffentlich als NDF-Prompts dienen.
- Claude-/Implementation-Agent-Prompts müssen mindestens eine klare Rückmeldung-an-Nova-Struktur enthalten; langfristig DE/EN.

### Technische Schlüsselwörter

Diese Begriffe bleiben englisch und werden nicht übersetzt:

- Work Package
- Project Brain
- Health Score
- Implementation Agent
- Maintainer
- Security

### Regeln

1. Keine privaten Projekt- oder Personenbezüge in Übersetzungen.
2. Übersetzungen erhalten die Bedeutung — keine erzwungene Wörtlichkeit.
3. Foundation 0.1 bleibt frozen; die DE/EN-Umstellung erfolgt über Foundation 0.2 und spätere Releases.
4. Umstellung schrittweise pro Work Package, priorisiert nach `TRANSLATION_STATUS.md` — keine Big-Bang-Übersetzung.

## EN

### Goal

The Nova Development Framework shall be fully usable in both German and English. Public users must be able to understand NDF in English; the German version remains equally maintained.

### Principle

New public NDF documents are either **bilingual** or have a **clear language assignment** (tracked in `docs/i18n/TRANSLATION_STATUS.md`).

### Preferred format for central documents

```text
# Deutscher Titel / English Title

## DE

German content.

## EN

English content.
```

### Parallel files

For longer documentation, parallel files are allowed:

```text
DOCUMENT.de.md
DOCUMENT.en.md
```

### Prompts

- Framework prompts may be bilingual when they serve as public NDF prompts.
- Claude / Implementation Agent prompts must at least contain a clear feedback-to-Nova structure; bilingual DE/EN in the long term.

### Technical keywords

These terms stay in English and are never translated:

- Work Package
- Project Brain
- Health Score
- Implementation Agent
- Maintainer
- Security

### Rules

1. No private project or person references in translations.
2. Translations preserve meaning — no forced literalness.
3. Foundation 0.1 stays frozen; the DE/EN transition happens through Foundation 0.2 and later releases.
4. Transition is incremental per work package, prioritized via `TRANSLATION_STATUS.md` — no big-bang translation.
