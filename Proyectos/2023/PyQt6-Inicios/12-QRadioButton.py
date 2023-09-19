import sys
from PyQt6.QtWidgets import QWidget, QApplication, QRadioButton

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QRadioButton")
        self.setGeometry(100, 100, 300, 100)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())