import sys
from PyQt6.QtWidgets import QWidget, QApplication, QTextEdit, QFormLayout
from PyQt6.QtCore import Qt

class clasePadre (QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt6 - QTextEdit')
        #self.setGeometry(100,100,200,100)
        self.setMinimumWidth(200)

        layoutPadre = QFormLayout()
        self.setLayout(layoutPadre)
        text_edit = QTextEdit()
        layoutPadre.addRow(text_edit)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = clasePadre()
    sys.exit(app.exec())