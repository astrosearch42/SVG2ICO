$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    throw "The project virtual environment was not found at $python"
}

& $python -m PyInstaller `
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

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller failed with exit code $LASTEXITCODE"
}