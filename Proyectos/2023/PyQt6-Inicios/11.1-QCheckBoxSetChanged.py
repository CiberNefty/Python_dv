import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox, QPushButton
from PyQt6.QtCore import Qt

class VentanaQCheck_Stados (QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Metodo Que permite cambiar de estado (TRUE or FALSE)')
        self.setGeometry(100,100,100,100)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheck_Stados()
    sys.exit(app.exec())