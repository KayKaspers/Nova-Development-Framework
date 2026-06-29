# Markdown for Export Standard

## Ziel

Markdown-Dateien sollen so geschrieben werden, dass sie später sauber nach PDF, Word und Website exportiert werden können.

## Regeln

### Überschriften

Nur eine H1 pro Datei:

```markdown
# Kapitelname
```

Danach H2, H3 usw.

### Listen

Kurze Listen bevorzugen.

### Tabellen

Tabellen einfach halten.

### Codeblöcke

Immer Sprache angeben, wenn möglich:

```bash
git status
```

### Bilder

Bilder relativ verlinken:

```markdown
![Beschreibung](../../assets/images/example.png)
```

### Hinweise

Für Infoboxen verwenden wir später ein einheitliches Format:

```markdown
> [!NOTE]
> Hinweistext
```

### Warnungen

```markdown
> [!WARNING]
> Warntext
```

## Vermeiden

- zu tiefe Überschriftenstruktur
- HTML im Markdown
- absolute lokale Pfade
- Screenshots ohne Beschreibung
- Tabellen als Layout-Ersatz
