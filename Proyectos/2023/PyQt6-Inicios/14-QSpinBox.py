import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QSpinBox, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QSpinBox')
        self.setMinimumWidth(300)

        # Creamos caja contendedora
        layoutPadre = QVBoxLayout()
        self.setLayout(layoutPadre)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPadre()
    sys.exit(app.exec())