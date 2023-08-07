import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget): # Esta es la clase padre que hereda de metodos de la clase QWidget

    # CREAMOS CONSTRUCTOR
    def __init__(self):
        # Vamos a inicializar el contructor de la clase Qwidget utilizando el comando SUPER
        super().__init__()
        self.inicializarUI() # Este es un metodo que se ejecutara con nuestro constructor

    def inicializarUI(self):
        # En esta parte definimos nuestro UI
        self.setGeometry(100,100,250,250) # Definir las dimenciones de la ventana. recibiendo 4 parametros (X,Y, ancho, largo)
        self.setWindowTitle("Mi primemr ventana con PYQT6") # Metodo para darle un titulo a la ventana.
        self.show() # Metodo para darle inicio a la ventana es parecido al mainloop de TK

# Ejecutamos la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)    # Aca instanciamos la clase QApplication # El argumento sys.argv nos permite  pasarle por consola parametros a la app
    ventana = VentanaVacia() # Aca instanciamos nuestra clae padre 
    sys.exit(app.exec())