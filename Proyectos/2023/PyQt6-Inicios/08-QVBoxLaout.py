import sys 
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton

class VentanaDaniel(QWidget):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("PyQt6 QVBoxLayout - Verticalmente")
        #self.setGeometry(100,100,100,300)

        layoutPadre = QVBoxLayout()
        self.setLayout(layoutPadre)

        nombreBotones = ['Daniel', 'Pipe', 'Edgar', 'Pato']
        buttons = [QPushButton(nombreBoton) for nombreBoton in nombreBotones]

        for Boton in buttons:
            layoutPadre.addWidget(Boton)

        self.show()


if __name__ in '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDaniel()
    sys.exit(app.exec())