# noinspection PyUnresolvedReferences, PyTypeChecker

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora CreativeTech")
        self.setGeometry(100, 100, 350, 500)
        self.load_styles()
        self.create_ui()

    def load_styles(self):
        """Carga los estilos desde styles.qss"""
        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

    def create_ui(self):
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Arial", 24))
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3, "operator"),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3, "operator"),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3, "operator"),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2, "clear"), ('+', 3, 3, "operator"),
            ('=', 4, 0, 1, 4, "equal")
        ]

        for button_data in buttons:
            text, row, col, *extra = button_data
            span = extra[:2] if len(extra) > 1 else (1, 1)
            button_type = extra[2] if len(extra) > 2 else None

            button = QPushButton(text)
            button.setFixedHeight(60)
            if button_type:
                button.setObjectName(button_type)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col, *span)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender().text()
        if sender == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        elif sender == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + sender)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())