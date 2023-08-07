import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout)

class ventantaPrincipal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ponemos un valor en neustro titulo
        self.setWindowTitle('Qt Singlas & Slots - Señales y Ranuras')

        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)

        # Creamos un widget button y lo conectamos con un evento o señal de clicked
        button = QPushButton('¡Click Me!')
        button.clicked.connect(self.boton_cliqueo)

        layout = QVBoxLayout()
        
        layout.addWidget(button)
        layout.addWidget(label)
        layout.addWidget(line_edit)


        self.setLayout(layout)
        
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