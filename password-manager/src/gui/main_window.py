from PyQt6.QtWidgets import (  # type: ignore
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QTabWidget
)
from src.models.password_manager import PasswordManager


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.password_manager = PasswordManager()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestor de Contraseñas")
        self.setGeometry(100, 100, 420, 300)

        self.tabs = QTabWidget()
        self.tab_save = QWidget()
        self.tab_retrieve = QWidget()

        self.tabs.addTab(self.tab_save, "Guardar")
        self.tabs.addTab(self.tab_retrieve, "Recuperar")

        self.initSaveTab()
        self.initRetrieveTab()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def initSaveTab(self):
        layout = QVBoxLayout()

        self.label_service = QLabel("Servicio:")
        self.entry_service = QLineEdit()
        layout.addWidget(self.label_service)
        layout.addWidget(self.entry_service)

        self.label_username = QLabel("Usuario:")
        self.entry_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.entry_username)

        self.label_password = QLabel("Contraseña:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)

        self.btn_save = QPushButton("Guardar")
        self.btn_save.clicked.connect(self.save_password_ui)
        self.btn_save.setStyleSheet(
            "background-color: #28a745; color: white; font-weight: bold;"
        )
        layout.addWidget(self.btn_save)

        self.tab_save.setLayout(layout)

    def initRetrieveTab(self):
        layout = QVBoxLayout()

        self.label_service_retrieve = QLabel("Servicio:")
        self.entry_service_retrieve = QLineEdit()
        layout.addWidget(self.label_service_retrieve)
        layout.addWidget(self.entry_service_retrieve)

        self.btn_retrieve = QPushButton("Recuperar")
        self.btn_retrieve.clicked.connect(self.retrieve_password_ui)
        self.btn_retrieve.setStyleSheet(
            "background-color: #007bff; color: white; font-weight: bold;"
        )
        layout.addWidget(self.btn_retrieve)

        self.tab_retrieve.setLayout(layout)

    def save_password_ui(self):
        service = self.entry_service.text()
        username = self.entry_username.text()
        password = self.entry_password.text()

        if service and username and password:
            self.password_manager.save_password(service, username, password)
            QMessageBox.information(
                self,
                "Éxito",
                "Contraseña guardada correctamente"
            )
            self.entry_service.clear()
            self.entry_username.clear()
            self.entry_password.clear()
        else:
            QMessageBox.warning(
                self,
                "Error",
                "Todos los campos son obligatorios"
            )

    def retrieve_password_ui(self):
        service = self.entry_service_retrieve.text()
        username, password = self.password_manager.retrieve_password(service)
        if username and password:
            QMessageBox.information(
                self,
                "Credenciales Recuperadas",
                f"Servicio: {service}\nUsuario: {username}\nContraseña:"
                f"{password}"
            )
        else:
            QMessageBox.warning(self, "Error", "No se encontró la contraseña")
