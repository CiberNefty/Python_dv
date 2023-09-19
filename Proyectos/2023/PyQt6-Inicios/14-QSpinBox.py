import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QSpinBox, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QSpinBox')
        self.setMinimumWidth(300)

        # Creamos caja contendedora
        layoutPadre = QVBoxLayout()
        self.setLayout(layoutPadre)

        # Creamos nuestro SpinBox
        spinBox_amount = QSpinBox(
            minimum = 1, maximum = 50, value= 20, prefix = '$'
        )
        # Creamos una conexion con el metodo valueChanged.connect
        spinBox_amount.valueChanged.connect(self.funcionActualizacion)

        self.resultado = QLabel('',self)

        # Agregamos los objetos al layout
        layoutPadre.addWidget(spinBox_amount)
        layoutPadre.addWidget(self.resultado)

        self.show()

    def funcionActualizacion(self, valor):
        self.resultado.setText(f'Valor acutal: {valor}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPadre()
    sys.exit(app.exec())