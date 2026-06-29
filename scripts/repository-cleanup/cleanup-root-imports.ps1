param(
    [switch]$Apply
)

$ErrorActionPreference = "Stop"

$RepoRoot = (Get-Location).Path
$ImportDir = Join-Path $RepoRoot "docs\import-history"
$LegacyDir = Join-Path $RepoRoot "docs\import-history\legacy-overviews"
$HistoryDir = Join-Path $RepoRoot "docs\release\history"

$Targets = @(
    $ImportDir,
    $LegacyDir,
    $HistoryDir
)

foreach ($dir in $Targets) {
    if (-not (Test-Path $dir)) {
        if ($Apply) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        Write-Host "DIR  $dir"
    }
}

$Moves = @()

Get-ChildItem -Path $RepoRoot -File -Filter "NDF*IMPORT_ANLEITUNG.md" | ForEach-Object {
    $Moves += [PSCustomObject]@{
        Source = $_.FullName
        Target = Join-Path $ImportDir $_.Name
    }
}

Get-ChildItem -Path $RepoRoot -File -Filter "CHANGELOG_*.md" | ForEach-Object {
    $Moves += [PSCustomObject]@{
        Source = $_.FullName
        Target = Join-Path $HistoryDir $_.Name
    }
}

Get-ChildItem -Path $RepoRoot -File -Filter "NDF*_Uebersicht.docx" | ForEach-Object {
    $Moves += [PSCustomObject]@{
        Source = $_.FullName
        Target = Join-Path $LegacyDir $_.Name
    }
}

Get-ChildItem -Path $RepoRoot -File -Filter "NDF*_Uebersicht.pdf" | ForEach-Object {
    $Moves += [PSCustomObject]@{
        Source = $_.FullName
        Target = Join-Path $LegacyDir $_.Name
    }
}

if ($Moves.Count -eq 0) {
    Write-Host "No matching root import/changelog files found."
    exit 0
}

Write-Host ""
Write-Host "Planned moves:"
Write-Host ""

foreach ($move in $Moves) {
    Write-Host "MOVE"
    Write-Host "  from: $($move.Source)"
    Write-Host "  to:   $($move.Target)"
}

if (-not $Apply) {
    Write-Host ""
    Write-Host "Dry run only. No files moved."
    Write-Host "Run with -Apply to perform the cleanup:"
    Write-Host ".\scripts\repository-cleanup\cleanup-root-imports.ps1 -Apply"
    exit 0
}

Write-Host ""
Write-Host "Applying cleanup..."
Write-Host ""

foreach ($move in $Moves) {
    Move-Item -Path $move.Source -Destination $move.Target -Force
    Write-Host "Moved: $($move.Source)"
}

Write-Host ""
Write-Host "Cleanup complete. Please review changes in GitHub Desktop."
