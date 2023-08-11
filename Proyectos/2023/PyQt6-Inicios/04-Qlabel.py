import sys
from PyQt6.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout


class mainView(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Colocamos un titulo
        self.setWindowTitle("QLABEL")
        # Tamaño de la ventana
        self.setGeometry(100, 100, 320, 210)

        label = QLabel('Esto es un widget Qlabel')
        """label1 = QLabel()
        label1.setText('Estoy utilizando el metodo .setText()')"""

        # Colocaos los WIGEt en la ventana
        layout1 = QVBoxLayout()
        layout1.addWidget(label) # Agregamos nuestro QLabel al QVBoxLayout
        self.setLayout(layout1)

        # Mostramos la ventana
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainView()
    sys.exit(app.exec())


# Obtener el texto de un label
#label1.text()

# Borrar texto de un label
#label1.clear()

"""label2 = QLabel(input('Ingresa texto'))

print(label2)"""

