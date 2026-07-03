# Foundation 0.2 – Public Quality Gate Progress

## Ziel

Die öffentliche Neutralität und Repository-Hygiene des NDF automatisch absichern.

## Status

| Baustein | Status |
|---|---|
| Neutralisierung privater Projektnamen (WP-030) | done |
| Neutralisierung Maintainer-Bezüge (WP-031) | done |
| Quality-Gate-Script `scripts/check_public_quality.py` | done |
| Beispiel-Denylist `.ndf/public-neutrality-terms.example.txt` | done |
| GitHub Action `public-quality-gate.yml` | done |
| Dokumentation `docs/repository/PUBLIC_QUALITY_GATE.md` | done |
| GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` setzen | open (manuell) |

## Warum wichtig?

Ohne automatischen Gate wäre die in WP-030/WP-031 erreichte Neutralität nur ein Momentzustand. Der Gate macht sie zu einer dauerhaft geprüften Eigenschaft des Repositories — bei jedem Pull Request und jedem Push auf `main`.

## Nächste Schritte

1. GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` durch den Maintainer setzen.
2. Lokale Denylist aus der Beispieldatei anlegen (`.ndf/public-neutrality-terms.local.txt`).
3. Ersten CI-Lauf auf GitHub beobachten und ggf. Muster nachschärfen.
