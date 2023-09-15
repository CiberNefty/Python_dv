import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QLabel, QLineEdit, QPushButton


class VentanaQCheckBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QCheckBox')
        #self.setGeometry(100,100,100,100)

        layoutPadre = QGridLayout()
        self.setLayout(layoutPadre)

        

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheckBox()
    sys.exit(app.exec())