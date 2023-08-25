import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QPushButton, QWidget)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

"""BOTON DE ALTERNACIA (TRUE - FALSE)"""
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("BOTON DE ALTERNACIA")
        self.setGeometry(200,100, 200,100)

        buton = QPushButton('Toggle Me')
        buton.setIcon(QIcon('python-logo.png'))
        buton.setFixedSize(100,30)
        buton.setCheckable(True)
        buton.clicked.connect(self.on_toggle)

        contendor = QVBoxLayout()
        contendor.addWidget(buton)
        self.setLayout(contendor)
        

        self.show()

    def on_toggle(self, clicked):
        print('Estoy clickeado')

if __name__ == '__main__':
    app= QApplication(sys.argv)
    ventanaMain = MainWindow()
    sys.exit(app.exec())