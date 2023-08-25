import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QVBoxLayout,QPushButton,QLabel)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize  # Darle tamaño a nuestro boton
from io import open
import pathlib

class ventanaMain (QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt6 QPushButtons')
        self.setGeometry(100,100, 320, 100)

        button = QPushButton("Delete")
        button.setIcon(QIcon('trash.png'))

        # Le damos un tamaño  nuestro boton
        button.setFixedSize(QSize(100,30))
        

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        

        self.show()

if __name__ == '__main__':
    app= QApplication(sys.argv)
    ventana = ventanaMain()
    sys.exit(app.exec())
