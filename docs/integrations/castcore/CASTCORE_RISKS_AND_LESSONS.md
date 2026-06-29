# CastCore Risks and Lessons Learned

## Risiko 1 – docs-status.json Instabilität

### Problem

Wenn `docs-status.json` ein generiertes Datum enthält, kann CI fehlschlagen, obwohl fachlich nichts kaputt ist.

### NDF-Lesson

Generierte Dateien müssen deterministisch sein oder bewusst aus CI-Diffs herausgehalten werden.

## Risiko 2 – FFmpeg-Binary-Abhängigkeit in Tests

### Problem

Tests können instabil werden, wenn sie eine echte lokale ffmpeg/ffprobe-Binary erwarten.

### NDF-Lesson

Tests sollen externe Systemabhängigkeiten mocken, wenn die eigentliche Logik ohne echte Binary prüfbar ist.

## Risiko 3 – Docker Build-Gate zu spät

### Problem

Wenn FFmpeg-Versionen erst zur Laufzeit auffallen, wird der Fehler spät sichtbar.

### NDF-Lesson

Kritische Runtime-Abhängigkeiten sollten im Docker-Build oder CI-Gate validiert werden.

## Risiko 4 – Suite wächst schneller als Dokumentation

### Problem

CastCore kann durch viele Module schnell schwer nachvollziehbar werden.

### NDF-Lesson

Project Brain, Capability Matrix und Work Package Queue müssen früh gepflegt werden.

## Risiko 5 – KI-Arbeit ohne kleine Work Packages

### Problem

Große Claude-Prompts können zu schwer prüfbaren Änderungen führen.

### NDF-Lesson

Claude bekommt kleine, abgegrenzte Arbeitspakete mit Rückmeldung an Nova.
