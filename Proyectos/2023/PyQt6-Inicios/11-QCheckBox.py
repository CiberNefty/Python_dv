import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class VentanaQCheckBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QCheckBox')
        #self.setGeometry(100,100,100,100)

        layoutPadre = QGridLayout()
        self.setLayout(layoutPadre)

        # Creamos nuestro checkBox
        checkBox1 = QCheckBox('I gree', self)
        # Agregamos nuestro checkBox a nuestro gridlayout y lo posicionamos y le damos un aliniamiento.
        layoutPadre.addWidget(checkBox1, 0,0, Qt.AlignmentFlag.AlignBottom)
        

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheckBox()
    sys.exit(app.exec())