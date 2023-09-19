import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QComboBox, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox")
        self.setGeometry(100, 100, 300, 100)

        # Creamos nuestra caja contenedora
        layotuPadre = QVBoxLayout()
        self.setLayout(layotuPadre)


        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())