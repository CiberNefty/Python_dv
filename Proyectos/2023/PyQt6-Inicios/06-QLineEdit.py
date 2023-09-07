import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QCompleter
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit')
        self.setGeometry(100, 100, 320, 210)

        """CAJA DE TEXTO CON BOTON DE LIMPIAR"""
        cajabusqueda = QLineEdit(
            self,
            placeholderText = 'Escribe aquí',
            clearButtonEnabled = True
        )
        
        """CAJA DE TEXTO EN PASSWORD"""
        password = QLineEdit(self,
            echoMode = QLineEdit.EchoMode.Password,
            clearButtonEnabled = True,
            placeholderText = 'Escribe tu contraseña',
        )

        """CAJA DE TEXTO CON AUTOCOMPLETAR"""
        texto_autocompletar = QCompleter(['Manzana','Pera','Banano','Mora','Limon','Sandia','Naranja','Fresa','Curuva', 'Papaya', 'Mandarina','Durazno','Uva','Melocoton'])

        frutas = QLineEdit(
            self,
            placeholderText='Escribe Frutas'
        )
        frutas.setCompleter(texto_autocompletar)

        """CAJA PARA MAXIMO DE CARACTERES"""
        maximoCaracter = QLineEdit(
            self,
            placeholderText='Limite de 8 caracteres',
            maxLength=8
        )

        layout = QVBoxLayout()
        layout.addWidget(cajabusqueda)
        layout.addWidget(password) # Aqui agregamos nuestra QlineEdit con password
        layout.addWidget(frutas)
        layout.addWidget(maximoCaracter)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())