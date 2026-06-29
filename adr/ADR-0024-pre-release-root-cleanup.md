# ADR-0024: Pre-Release Root Cleanup

## Status

Accepted

## Kontext

Während der Foundation-Aufbauphase wurden viele Pakete importiert. Dadurch liegen historische Import-Anleitungen und Paket-Changelogs im Repository-Root.

Für einen öffentlichen Foundation-Release soll der Root übersichtlich und professionell wirken.

## Entscheidung

Vor Foundation 0.1 wird ein Pre-Release Cleanup durchgeführt:

- Root-README wird wieder zur allgemeinen Framework-Startseite.
- Import-Anleitungen werden nach `docs/import-history/` verschoben.
- Paket-Changelogs werden nach `docs/release/history/` verschoben.
- Alte Übersichtsdokumente werden nach `docs/import-history/legacy-overviews/` verschoben.
- Der zentrale Changelog bleibt `CHANGELOG.md`.

## Konsequenzen

- Das Repository wirkt sauberer.
- Historie bleibt erhalten.
- Der Release kann professioneller veröffentlicht werden.
- Es werden keine großen fachlichen Umstrukturierungen kurz vor Release durchgeführt.
