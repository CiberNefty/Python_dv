import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class ventanaMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt6 QHBoxLayout')
        self.setGeometry(100, 100, 400, 100)

        # Creamos nuestro layout
        layoutPadre = QHBoxLayout()
        self.setLayout(layoutPadre)
        
        #layoutPadre.addStretch()
        # Creamos los botones y añadimos los temas a nuestro layout
        titulos = ['Yes', 'No', 'Cancelado']
        botonPadre = [QPushButton(titulo) for titulo in titulos]
        
        for botonHijo in botonPadre:
            layoutPadre.addWidget(botonHijo)

        layoutPadre.setSpacing(0)
        layoutPadre.setContentsMargins(150, 50, 150, 50)
        """layoutPadre.addWidget(botonPadre[0])
        layoutPadre.addWidget(botonPadre[1])"""
        
        """layoutPadre.setStretchFactor(botonPadre[0], 1)
        #layoutPadre.setSpacing(20)
        layoutPadre.setStretchFactor(botonPadre[1], 0)
        layoutPadre.setStretchFactor(botonPadre[2], 1)"""

        # Añadimos un espaciador en el LayoutPadre
        #layoutPadre.addStretch()

        """layoutPadre.addWidget(botonPadre[2])"""

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ventanaMain()
    sys.exit(app.exec())

"""
Resumen
Se utiliza para dividir el widget principal en cuadros horizontales y colocarlos secuencialmente de izquierda a derecha.QHBoxLayout
    * Utilice el método del objeto para agregar un espaciador horizontal al diseño para alinear los widgets secundarios a la izquierda, derecha o centro.addStretch()QHBoxLayout
    * Utilice el método del objeto para establecer el factor de estiramiento de un widget secundario.setStretchFactor()QHBoxLayout
    * Utilice el método del objeto para establecer los espacios entre los widgets secundarios.setSpacing()QHBoxLayout
    * Utilice el método del objeto para establecer los márgenes izquierdo, superior, derecho e inferior.setContentsMargins()QHBoxLayout
"""