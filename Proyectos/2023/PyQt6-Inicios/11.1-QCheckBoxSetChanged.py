import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox, QPushButton
from PyQt6.QtCore import Qt

class VentanaQCheck_Stados (QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Metodo Que permite cambiar de estado (TRUE or FALSE)')
        self.setGeometry(100,100,100,100)

        # Creamos nuestro caja de guardado (GridLayout)
        gridLayoutPadre = QGridLayout()
        self.setLayout(gridLayoutPadre)
    
        # Creamos un checBox
        self.checkBox1 = QCheckBox('Cambio de estado', self)

        # Creamos dos botones que nos serviran para cambiar de estado (TRUE or FALSE)
        Boton1 = QPushButton('CheckearBoton', self)
        # Vamos a darle una bandera y llevarla a una señal
        Boton1.clicked.connect(self.chekiado)

        Boton2 = QPushButton('Quitar Checkeable', self)
        Boton2.clicked.connect(self.noChekiado)

        # Agregamos los objetos al layout
        gridLayoutPadre.addWidget(self.checkBox1, 0,0,0,2, Qt.AlignmentFlag.AlignCenter)
        gridLayoutPadre.addWidget(Boton1, 1,0, Qt.AlignmentFlag.AlignJustify)
        gridLayoutPadre.addWidget(Boton2, 1,1, Qt.AlignmentFlag.AlignJustify)

        self.show()

    def chekiado(self): # CUando solo colocamos una self solo envia un valor.
        self.checkBox1.setChecked(True)

    def noChekiado(self):
        self.checkBox1.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheck_Stados()
    sys.exit(app.exec())