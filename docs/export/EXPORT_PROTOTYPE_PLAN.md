# Export Prototype Plan

## Zweck

Foundation 0.2 soll prüfen, ob Academy- oder Framework-Inhalte aus Markdown nach PDF/DOCX exportierbar sind.

## Ziel

Ein erster Test mit einem kleinen Teil der Academy.

## Empfohlenes Testobjekt

```text
Academy Band 1 – Kapitel 1 bis 3
```

## Mögliche Toolchain

### Option A – Pandoc

Vorteile:

- weit verbreitet
- DOCX und PDF möglich
- gut für Markdown

Nachteile:

- PDF kann zusätzliche Abhängigkeiten brauchen

### Option B – Python docx + Markdown Parser

Vorteile:

- kontrollierbarer DOCX-Export

Nachteile:

- PDF schwieriger

### Option C – MkDocs → PDF Plugin

Vorteile:

- Website und PDF näher zusammen

Nachteile:

- kann komplex werden

## Empfehlung

Für Foundation 0.2:

1. DOCX-Test zuerst.
2. PDF danach.
3. Nur kleines Testkapitel exportieren.
4. Design später verfeinern.

## Mindestziel

- Export-Testplan
- Book Manifest
- Entscheidung für erste Toolchain
- dokumentierte Grenzen
