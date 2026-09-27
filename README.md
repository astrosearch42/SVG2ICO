# SVG 2 ICO

Application de bureau simple pour convertir un ou plusieurs fichiers SVG en fichiers ICO.

## Fonctionnalites

- Selection de plusieurs fichiers SVG.
- Rasterisation en image 256 x 256.
- Export ICO avec les tailles 16, 24, 32, 48, 64, 128 et 256 pixels.
- Interface graphique Qt et icone d'application integree.

## Installation

Python 3.10 ou une version plus recente est recommande.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Lancer l'application

```powershell
python svg_to_ico.py
```

## Creer l'executable Windows

Depuis la racine du projet, apres l'installation des dependances :

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name SVG_2_ICO --icon icon\app_icon.ico --add-data "icon\app_icon.svg;icon" svg_to_ico.py
```

L'executable sera genere dans `dist\SVG_2_ICO.exe`.

L'option `--add-data` embarque le SVG utilise par l'icone de la fenetre. Le fichier ICO fourni a PyInstaller definit l'icone de l'executable Windows.