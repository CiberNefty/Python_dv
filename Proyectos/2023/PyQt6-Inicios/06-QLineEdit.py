import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont

class Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt6 QLineEdition')
        self.setGeometry(100,100,300,200)
        
        self.show()
        

if '__name__' == '__main__':
    app = QApplication(sys.argv)
    ventana = Main()
    sys.exit(app.exec())