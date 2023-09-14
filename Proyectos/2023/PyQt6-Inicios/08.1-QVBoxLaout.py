import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

class Ventana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt6 QVBoxLayout - Verticalmente")
        self.setGeometry(100,100, 300, 200)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())