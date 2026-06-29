$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$dist = Join-Path (Split-Path -Parent $root) "chainops-dashboard-ui-kit-v1.0.0.zip"
$staging = Join-Path $env:TEMP "chainops-ui-kit-pack"

if (Test-Path $staging) {
  Remove-Item -Recurse -Force $staging
}

New-Item -ItemType Directory -Force -Path $staging | Out-Null

$items = @(
  "preview",
  "assets",
  "design-tokens",
  "cover",
  "docs",
  "figma",
  "exports",
  "tools",
  "README.md",
  "package.json"
)

foreach ($item in $items) {
  Copy-Item -Recurse -Force (Join-Path $root $item) (Join-Path $staging $item)
}

if (Test-Path $dist) {
  Remove-Item -Force $dist
}

Compress-Archive -Path (Join-Path $staging "*") -DestinationPath $dist -Force
Remove-Item -Recurse -Force $staging

Write-Host "Gumroad package created:"
Write-Host $dist
