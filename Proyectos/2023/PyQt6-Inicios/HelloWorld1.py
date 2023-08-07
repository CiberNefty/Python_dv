import sys
from PyQt6.QtWidgets import QApplication, QWidget

## POO - OOP (Programacion Orientada a Objetos)
class ventanaPrincipal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #set the window title
        self.setWindowTitle('Hello World OOP')

        # show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create object the main window
    ventana = ventanaPrincipal()
    # Iniciamos el evento loop
    sys.exit(app.exec())