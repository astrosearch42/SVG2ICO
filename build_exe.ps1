python -m PyInstaller `
  --noconfirm `
  --clean `
  --onefile `
  --windowed `
  --name SVG2ICO `
  --icon icon\svg2ico.ico `
  --add-data "icon\svg2ico.svg;icon" `
  SVG2ICO.py