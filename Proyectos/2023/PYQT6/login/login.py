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
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Mi Login")
        self.generar_formulario() # Va a tener toda la logica que nos genera la contraseña los botones toda la parte visual en este metodo
        self.show()

    def generar_formulario(self):
        # Esto es una variable de instancia gracias a el metodo self que va hacer accesible en toda la clase
        self.is_logged = False # Como el usuario no esta logiado el va a inicializar el formulario
        
        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont("Arial", 10))
        # Vamos a situar o colocar en alguna posicion (x,y)
        user_label.move(20,54)

        # Campo donde el usuario digita la informacion y de paso vamos a colocar esta variable como instacia
        self.user_imput = QLineEdit(self)
        self.user_imput.resize(250,24)
        self.user_imput.move(90,50)

        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont("Arial", 10))
        # Vamos a situar o colocar en alguna posicion (x,y)
        password_label.move(20,86)

        # Campo donde el usuario digita la informacion y de paso vamos a colocar esta variable como instacia
        self.password_imput = QLineEdit(self)
        self.password_imput.resize(250,24)
        self.password_imput.move(90,82)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec()) # inicamos la aplicacion