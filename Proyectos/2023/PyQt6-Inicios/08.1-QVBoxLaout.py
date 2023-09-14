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
        layoutPadre.addStretch()
        layoutPadre.addWidget(label2)
        layoutPadre.addSpacing(15)
        layoutPadre.addWidget(label3)
        
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())