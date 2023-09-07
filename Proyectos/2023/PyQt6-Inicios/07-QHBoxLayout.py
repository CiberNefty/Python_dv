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

        """layoutPadre.addWidget(botonPadre[0])
        layoutPadre.addWidget(botonPadre[1])"""
        layoutPadre.setStretchFactor(botonPadre[0], 2)
        layoutPadre.setStretchFactor(botonPadre[1], 2)
        layoutPadre.setStretchFactor(botonPadre[2], 1)
        # Añadimos un espaciador en el LayoutPadre
        #layoutPadre.addStretch()

        """layoutPadre.addWidget(botonPadre[2])"""

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ventanaMain()
    sys.exit(app.exec())