import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout, QHBoxLayout

class ventanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QTabWidget")
        #self.setGeometry(100,100,100,100)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaPadre()
    sys.exit(app.exec())
