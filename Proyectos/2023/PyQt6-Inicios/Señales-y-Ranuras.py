import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QLineEdit,
    QPushButton,
    QVBoxLayout)

class ventantaPrincipal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ponemos un valor en neustro titulo
        self.setWindowTitle('Qt Singlas & Slots - Señales y Ranuras')

        # Creamos un widget button y lo conectamos con un evento o señal de clicked
        button = QPushButton('¡Click Me!')
        button.clicked.connect(self.boton_cliqueo)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        # Mostramos la ventana
        self.show()


    def boton_cliqueo(self):
        print('Clicked')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Instanciar clase padre
    ventana = ventantaPrincipal()

    # Inicamos nuestro evento
    sys.exit(app.exec())