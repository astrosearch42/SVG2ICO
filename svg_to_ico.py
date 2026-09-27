from __future__ import annotations

import io
import sys
from pathlib import Path

from PIL import Image
from PySide6.QtCore import QByteArray, QBuffer, QIODevice, Qt
from PySide6.QtGui import QIcon, QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QListWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


ICON_SIZES = (16, 24, 32, 48, 64, 128, 256)


def resource_path(relative_path: str) -> Path:
    bundle_path = getattr(sys, "_MEIPASS", None)
    base_path = Path(bundle_path) if bundle_path else Path(__file__).resolve().parent
    return base_path / relative_path


APP_ICON_PATH = resource_path("icon/app_icon.svg")


def svg_to_image(svg_path: Path) -> Image.Image:
    renderer = QSvgRenderer(str(svg_path))
    if not renderer.isValid():
        raise ValueError(f"SVG invalide : {svg_path.name}")

    image = QImage(256, 256, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    renderer.render(painter)
    painter.end()

    png_data = QByteArray()
    buffer = QBuffer(png_data)
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    if not image.save(buffer, "PNG"):
        buffer.close()
        raise RuntimeError(f"Impossible de rasteriser : {svg_path.name}")
    buffer.close()

    return Image.open(io.BytesIO(bytes(png_data))).convert("RGBA")


def convert_svg_to_ico(svg_path: Path) -> Path:
    image = svg_to_image(svg_path)
    output_path = svg_path.with_suffix(".ico")
    image.save(output_path, format="ICO", sizes=[(size, size) for size in ICON_SIZES])
    return output_path


class SvgToIcoWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.svg_paths: list[Path] = []
        self.setWindowTitle("SVG vers ICO")
        self.setWindowIcon(QIcon(str(APP_ICON_PATH)))
        self.setMinimumWidth(460)

        self.open_button = QPushButton("Ouvrir SVG")
        self.convert_button = QPushButton("Convertir en ICO")
        self.convert_button.setEnabled(False)
        self.files_list = QListWidget()
        self.status_label = QLabel("Aucun fichier sélectionné")
        self.status_label.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.open_button)
        layout.addWidget(self.files_list)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.status_label)

        self.open_button.clicked.connect(self.open_svg_files)
        self.convert_button.clicked.connect(self.convert_files)

    def open_svg_files(self) -> None:
        selected_files, _ = QFileDialog.getOpenFileNames(
            self,
            "Choisir un ou plusieurs fichiers SVG",
            "",
            "Fichiers SVG (*.svg)",
        )
        if not selected_files:
            return

        self.svg_paths = [Path(file) for file in selected_files]
        self.files_list.clear()
        self.files_list.addItems([str(path) for path in self.svg_paths])
        self.convert_button.setEnabled(True)
        self.status_label.setText(f"{len(self.svg_paths)} fichier(s) prêt(s) à convertir")

    def convert_files(self) -> None:
        converted: list[str] = []
        errors: list[str] = []
        for svg_path in self.svg_paths:
            try:
                output_path = convert_svg_to_ico(svg_path)
                converted.append(output_path.name)
            except (OSError, RuntimeError, ValueError) as error:
                errors.append(str(error))

        if errors:
            message = "\n".join(errors)
            if converted:
                message = f"Convertis : {', '.join(converted)}\n\nErreurs :\n{message}"
            QMessageBox.warning(self, "Conversion terminée avec erreurs", message)
        else:
            QMessageBox.information(
                self,
                "Conversion terminée",
                f"{len(converted)} fichier(s) ICO enregistré(s) dans le dossier des SVG.",
            )
        self.status_label.setText(
            f"{len(converted)} conversion(s) terminée(s)"
            + (f", {len(errors)} erreur(s)" if errors else "")
        )


def main() -> int:
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(APP_ICON_PATH)))
    window = SvgToIcoWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())