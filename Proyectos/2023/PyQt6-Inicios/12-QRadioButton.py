import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QRadioButton, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QRadioButton")
        self.setGeometry(100, 100, 300, 100)

        # Creamos nuestra caja contenedora
        layotuPadre = QVBoxLayout()
        self.setLayout(layotuPadre)

        # Creamos un titulo
        tituloPrimario = QLabel('Selecciona una plataforma', self)

        # Creamos unos objetos de tipo QRadioButton
        rb_Mircrosoft = QRadioButton('Mircrosoft', self)
        # Le vamos a crear una bandera y luego la conectamos con una señal
        rb_Mircrosoft.toggled.connect(self.actualizacion)

        rb_Sony = QRadioButton('Sony', self)
        rb_Sony.toggled.connect(self.actualizacion)

        rb_McKensie = QRadioButton('McKensie', self)
        rb_McKensie.toggled.connect(self.actualizacion)

        # Creamos un label para que obtenga el resultado de lo que contenga los radio button.
        #self.resultado_label = QLabel('Tu seleccion es:', self)
        self.resultado_label = QLabel('', self)

        # Agregamos nuestros objetos al layout padre.
        layotuPadre.addWidget(tituloPrimario)
        layotuPadre.addWidget(rb_Mircrosoft)
        layotuPadre.addWidget(rb_Sony)
        layotuPadre.addWidget(rb_McKensie)
        layotuPadre.addWidget(self.resultado_label)
    
        self.show()

    def actualizacion(self):
        # Obtenemos la señal del RadioButton
        rb = self.sender()

        # Validamos si el radio button esta chekeado
        if rb.isChecked(): # Con este metodo isChecked() obtenemos la señal si esta chequeado
            self.resultado_label.setText(f'Tu seleccion es: {rb.text()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())