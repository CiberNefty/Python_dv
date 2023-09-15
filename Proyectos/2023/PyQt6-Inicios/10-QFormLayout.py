import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton

class Ventana1(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QFormLayout')
        #self.setGeometry(100,100,100,100)

        layoutPadre = QFormLayout()
        self.setLayout(layoutPadre)
        
        layoutPadre.addRow('Name: ', QLineEdit(self, placeholderText='Escribe tu Nombre'))
        layoutPadre.addRow('Email: ', QLineEdit(self))
        layoutPadre.addRow('Password: ', QLineEdit(self, echoMode = QLineEdit.EchoMode.Password))
        layoutPadre.addRow('Confirm Password: ', QLineEdit(self, echoMode = QLineEdit.EchoMode.Password))
        layoutPadre.addRow('Phone: ', QLineEdit(self))

        layoutPadre.addRow(QPushButton('Sign Up'))


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana1()
    sys.exit(app.exec())