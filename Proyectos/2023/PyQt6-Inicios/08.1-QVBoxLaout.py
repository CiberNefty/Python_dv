import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

class Ventana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt6 QVBoxLayout - Verticalmente")
        self.setGeometry(100,100, 300, 200)

        # Creamos el layout para alajor los objetos
        layoutPadre = QVBoxLayout()
        self.setLayout(layoutPadre)

        # Creamos los "Botones" (de objeto Label)
        label1 =QLabel()
        label1.setStyleSheet('QLabel {background-color: YELLOW}')
        label2 =QLabel()
        label2.setStyleSheet('QLabel {background-color: BLUe}')
        label3 =QLabel()
        label3.setStyleSheet('QLabel {background-color: RED}')


        # Añadimos los widget en el layout.
        layoutPadre.addWidget(label1)
        layoutPadre.addStretch() # Utlizando los metodoss de StrechFacto no sirve este espaciador.
        layoutPadre.addWidget(label2)
        layoutPadre.addSpacing(15)
        layoutPadre.addWidget(label3)
        
        # Asisgnar proporcianalmente el tamaño a un widget.
        layoutPadre.setStretchFactor(label1, 3)
        layoutPadre.setStretchFactor(label2, 2)
        layoutPadre.setStretchFactor(label3, 1)

        # Configuracion de margenes
        layoutPadre.setContentsMargins(10,10,10,20)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())


"""
Resumen
 * Utilice PyQt para dividir el widget principal en cuadros verticales y colocar los widgets secundarios secuencialmente de arriba a abajo.QVBoxLayout
 * Utilice el método del objeto para agregar un espaciador vertical al diseño para alinear los widgets en la parte superior, inferior o central.addStretch()QVBoxLayout
 * Utilice el método del objeto para establecer un factor de estiramiento para un widget en el diseño.setStretchFactor()QVBoxLayout
 * Utilice el método del objeto para establecer los espacios entre los widgets secundarios.setSpacing()QVBoxLayout
 * Utilice el método del objeto para establecer los márgenes izquierdo, superior, derecho e inferior del contenido.setContentsMargins()
"""