import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QPushButton, QInputDialog, QMessageBox, QLabel
)
# from PyQt6.QtCore import Qt
import sys


class GestorArchivos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Archivos (CRUD)")
        self.setGeometry(200, 100, 600, 450)
        self.ruta_carpeta = os.path.expanduser("~/Downloads")  # Ruta fija

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Etiqueta de la ruta actual
        self.label_ruta = QLabel(f"Carpeta: {self.ruta_carpeta}")
        self.label_ruta.setStyleSheet("font-weight: bold;")
        main_layout.addWidget(self.label_ruta)

        # Lista de archivos
        self.lista_archivos = QListWidget()
        main_layout.addWidget(self.lista_archivos)

        # Botones CRUD
        botones_layout = QHBoxLayout()

        btn_crear = QPushButton("➕ Crear")
        btn_crear.clicked.connect(self.crear_archivo)

        btn_renombrar = QPushButton("✏️ Renombrar")
        btn_renombrar.clicked.connect(self.renombrar_archivo)

        btn_eliminar = QPushButton("🗑️ Eliminar")
        btn_eliminar.clicked.connect(self.eliminar_archivo)

        botones_layout.addWidget(btn_crear)
        botones_layout.addWidget(btn_renombrar)
        botones_layout.addWidget(btn_eliminar)

        main_layout.addLayout(botones_layout)

        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_archivos.clear()
        try:
            archivos = sorted(os.listdir(self.ruta_carpeta))
            for archivo in archivos:
                self.lista_archivos.addItem(archivo)
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"No se puede acceder a la carpeta:\n{e}")

    def crear_archivo(self):
        nombre, ok = QInputDialog.getText(
            self,
            "Crear Archivo o Carpeta",
            "Nombre (agrega '/' al final para carpeta):")
        if ok and nombre:
            ruta_nueva = os.path.join(self.ruta_carpeta, nombre)
            try:
                if nombre.endswith("/"):
                    os.mkdir(ruta_nueva)
                else:
                    with open(ruta_nueva, "w") as f:
                        f.write("")  # crea archivo vacío
                self.actualizar_lista()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo crear:\n{e}")

    def renombrar_archivo(self):
        seleccionado = self.lista_archivos.currentItem()
        if seleccionado:
            nombre_actual = seleccionado.text()
            nuevo_nombre, ok = QInputDialog.getText(
                self, "Renombrar", f"Nuevo nombre para: {nombre_actual}")
            if ok and nuevo_nombre:
                ruta_actual = os.path.join(self.ruta_carpeta, nombre_actual)
                ruta_nueva = os.path.join(self.ruta_carpeta, nuevo_nombre)
                try:
                    os.rename(ruta_actual, ruta_nueva)
                    self.actualizar_lista()
                except Exception as e:
                    QMessageBox.critical(
                        self, "Error", f"No se pudo renombrar:\n{e}")

    def eliminar_archivo(self):
        seleccionado = self.lista_archivos.currentItem()
        if seleccionado:
            nombre = seleccionado.text()
            ruta = os.path.join(self.ruta_carpeta, nombre)
            confirmar = QMessageBox.question(
                self, "Eliminar", f"¿Estás seguro de eliminar '{nombre}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirmar == QMessageBox.StandardButton.Yes:
                try:
                    if os.path.isdir(ruta):
                        os.rmdir(ruta)
                    else:
                        os.remove(ruta)
                    self.actualizar_lista()
                except Exception as e:
                    QMessageBox.critical(
                        self, "Error", f"No se pudo eliminar:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorArchivos()
    ventana.show()
    sys.exit(app.exec())
