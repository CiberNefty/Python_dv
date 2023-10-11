import sys
from PyQt6.QtWidgets import QWidget, QApplication

class clasePadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QGroupBox')
        self.setGeometry(100,100,100,100)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = clasePadre()
    sys.exit(app.exec())