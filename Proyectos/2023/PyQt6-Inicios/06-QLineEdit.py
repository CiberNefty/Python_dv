import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit')
        self.setGeometry(100, 100, 320, 210)

        cajabusqueda = QLineEdit(
            self,
            placeholderText = 'Escribe aquí',
            clearButtonEnabled = True
        )

        password = QLineEdit(self,
            echoMode = QLineEdit.EchoMode.Password,
            clearButtonEnabled = True
        )

        layout = QVBoxLayout()
        layout.addWidget(cajabusqueda)
        layout.addWidget(password) # Aqui agregamos nuestra QlineEdit con password

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())