import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QSlider')
        #self.setGeometry(100,100,200,100)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())