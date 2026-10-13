$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "uv is required to build SVG2ICO. Install it from https://docs.astral.sh/uv/"
}

Push-Location $projectRoot
try {
uv run python -m PyInstaller `
  --noconfirm `
  --clean `
  --onefile `
  --windowed `
  --name SVG2ICO `
  --icon (Join-Path $projectRoot "icon\svg2ico.ico") `
  --add-data "$(Join-Path $projectRoot 'icon\svg2ico.svg');icon" `
  --distpath (Join-Path $projectRoot "dist") `
  --workpath (Join-Path $projectRoot "build") `
  --specpath $projectRoot `
  (Join-Path $projectRoot "src\svg2ico\SVG2ICO.py")
}
finally {
    Pop-Location
}

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller failed with exit code $LASTEXITCODE"
}