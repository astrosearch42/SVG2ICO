# SVG2ICO

SVG2ICO is a small Windows desktop application that converts one or more SVG
files into ICO files. It uses Qt for the graphical interface and Pillow for
the ICO export.

## Features

- Select multiple SVG files in one operation.
- Render each SVG at 256 x 256 pixels with transparency preserved.
- Create ICO files containing 16, 24, 32, 48, 64, 128, and 256 pixel sizes.
- Save each ICO file next to its source SVG file.
- Use the bundled SVG artwork for the application and window icon.

## Requirements

- Windows
- Python 3.13 or newer

## Install the dependencies

From the project root, create and activate the virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

## Run from source

```powershell
python .\src\svg2ico\SVG2ICO.py
```

You can also use the package entry point after installing the project:

```powershell
svg2ico
```

## Build the Windows executable

From the project root, after installing the dependencies, run:

```powershell
.\scripts\build_exe.ps1
```

The script uses the project virtual environment and resolves all paths from
the repository root. PyInstaller embeds `icon\svg2ico.svg` for the Qt window
icon and uses `icon\svg2ico.ico` as the Windows executable icon. The resulting
file is written to `dist\SVG2ICO.exe`.

## Usage

1. Click **Open SVG** and select one or more SVG files.
2. Click **Convert to ICO**.
3. Find the generated ICO files in the same folders as their source SVG files.
