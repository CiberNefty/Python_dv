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

        # 2° Creamos un de verificacion Triestatal
        """En la práctica, se utiliza una casilla de verificación triestatal para dar al usuario la opción de no marcar ni desmarcar la casilla de verificación."""
        self.checkBoxTristatal = QCheckBox('Un CheckBox Tristatal', self)
        self.checkBoxTristatal.setTristate(True)

        # Agregamos los objetos al layout
        gridLayoutPadre.addWidget(self.checkBox1, 0,0,1,2, Qt.AlignmentFlag.AlignCenter)
        gridLayoutPadre.addWidget(Boton1, 1,0, Qt.AlignmentFlag.AlignJustify)
        gridLayoutPadre.addWidget(Boton2, 1,1, Qt.AlignmentFlag.AlignJustify)
        gridLayoutPadre.addWidget(self.checkBoxTristatal, 2,0,2,0, Qt.AlignmentFlag.AlignCenter)

        self.show()

    def chekiado(self): # CUando solo colocamos una self solo envia un valor.
        self.checkBox1.setChecked(True)

    def noChekiado(self):
        self.checkBox1.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheck_Stados()
    sys.exit(app.exec())


"""
Resumen
 - Utilice la clase para crear un widget de casilla de verificación. 'QCheckbox'
 - La señal se emite cuando la casilla de verificación está marcada o desmarcada. 'stateChanged'
 - Utilice el método or para activar o desactivar una casilla de verificación mediante programación. 'setChecked()' 'setState()'
 - Utilice el método para crear una casilla de verificación triestatal. 'setTristate()'
"""