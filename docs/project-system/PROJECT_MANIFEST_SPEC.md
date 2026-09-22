# Project Manifest Specification / Projekt-Manifest-Spezifikation

> Kanonisches Format / Canonical format: Seit Foundation 0.4 ([`PROJECT_ADAPTER_CONVENTIONS.md`](../project-starter/PROJECT_ADAPTER_CONVENTIONS.md), NDF-WP-059) ist `PROJECT_MANIFEST.md` (Markdown) das kanonische, öffentlich reviewbare Manifestformat; ein YAML- oder JSON-Block **innerhalb** dieser Markdown-Datei ist erlaubt, ist aber nicht die alleinige Wahrheit. Diese Spezifikation beschreibt den **empfohlenen Feldsatz** für diesen eingebetteten Block. Eigenständige `.yaml`-Manifest-Dateien, die NDF als Vorlage/Beispiel ausliefert, stellen denselben Feldsatz dar, sind aber selbst **nicht** das kanonische Artefakt — sie dienen als Datenquelle bzw. als Inhalt des eingebetteten Blocks. / Since Foundation 0.4 ([`PROJECT_ADAPTER_CONVENTIONS.md`](../project-starter/PROJECT_ADAPTER_CONVENTIONS.md), NDF-WP-059), `PROJECT_MANIFEST.md` (Markdown) is the canonical, publicly reviewable manifest format; a YAML or JSON block **inside** that Markdown file is allowed but is not the sole source of truth. This specification describes the **recommended field set** for that embedded block. Standalone `.yaml` manifest files shipped by NDF as templates/examples represent the same field set but are themselves **not** the canonical artifact — they serve as a data source, or as the content of the embedded block.

## DE

### Zweck

Das Project Manifest ist die Identitätskarte eines Projekts.

Es ist maschinenlesbar und menschenlesbar.

### Empfohlenes Format (Inhalt des eingebetteten YAML-Blocks)

```yaml
name: SampleProject
slug: sample-project
owner: <project-owner>
architecture_lead: Nova
implementation_assistant: Claude
repository: ""
status: active
ndf_level: 1
primary_language: ""
secondary_languages: []
deployment:
  - docker
quality_targets:
  documentation: required
  tests: required
  security: required
  ci: required
```

### Pflichtfelder

- name
- slug
- owner
- status
- ndf_level
- repository

Ein Pflichtfeld muss als Schlüssel vorhanden sein; sein Wert darf gemäß der Adapter-Konventionen `unknown`, `not evidenced`, `n/a` oder `open decision` sein, wenn er aus den Eingaben nicht belegbar ist. Ein solcher Wert macht das Manifest nicht ungültig — er markiert ein offenes Feld, kein Format-Problem. Ein Pflichtfeld darf nicht vollständig fehlen (kein Schlüssel) und sein Wert wird nie geraten.

### Statuswerte

- idea
- active
- paused
- maintenance
- archived

### NDF-Level

- 0: nicht angebunden
- 1: Basisanbindung
- 2: Standards aktiv
- 3: Quality Gates aktiv
- 4: Health Score aktiv
- 5: vollständig NDF-konform

Die Stufen sind kumulativ: eine höhere Stufe setzt voraus, dass die Merkmale der niedrigeren Stufen ebenfalls zutreffen (z. B. setzt `health_score: true` auf Stufe 4 voraus, dass Quality Gates aus Stufe 3 bereits aktiv sind).

## EN

### Purpose

The Project Manifest is a project's identity card.

It is machine-readable and human-readable.

### Recommended Format (content of the embedded YAML block)

```yaml
name: SampleProject
slug: sample-project
owner: <project-owner>
architecture_lead: Nova
implementation_assistant: Claude
repository: ""
status: active
ndf_level: 1
primary_language: ""
secondary_languages: []
deployment:
  - docker
quality_targets:
  documentation: required
  tests: required
  security: required
  ci: required
```

### Mandatory Fields

- name
- slug
- owner
- status
- ndf_level
- repository

A mandatory field must be present as a key; per the adapter conventions its value may be `unknown`, `not evidenced`, `n/a`, or `open decision` when it cannot be evidenced from the inputs. Such a value does not make the manifest invalid — it marks an open field, not a format problem. A mandatory field must not be missing entirely (no key), and its value is never guessed.

### Status Values

- idea
- active
- paused
- maintenance
- archived

### NDF Level

- 0: not connected
- 1: basic connection
- 2: standards active
- 3: quality gates active
- 4: health score active
- 5: fully NDF-conformant

The levels are cumulative: a higher level presumes the traits of the lower levels also hold (e.g. `health_score: true` at level 4 presumes quality gates from level 3 are already active).
