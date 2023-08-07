import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, # se encarga de recibir todos los eventos que pasen en la ventana
    QLabel, # Para mostrar los Label en la ventana y tambien para mostrar imagenes
    QWidget, # Permite generar la ventana
    QLineEdit, # Nos permite generar los campos para ingresar información
    QPushButton, # Nos permite generar bonotes
    QMessageBox, # Nos permite interactuar con ventanas emergentes
    QCheckBox)
from PyQt6.QtGui import QFont, QPixmap # Con esta calse qpixmap vamos a introducir imagenes en nuestra app

class Login(QWidget):
    def __init__(self):
        super.__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Mi Login")
        self.generar_formulario() # Va a tener toda la logica que nos genera la contraseña los botones toda la parte visual en este metodo
        self.show()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec()) # inicamos la aplicacion