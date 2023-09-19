import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QDateEdit
from datetime import date

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt QDateEdit')
        #self.setMinimumWidth(300)

        layoutPadre = QFormLayout()
        self.setLayout(layoutPadre)

        # Creamos nuestro QDateEdit
        self.date_Edit = QDateEdit(self)
        self.date_Edit.editingFinished.connect(self.actualizacion)

        self.resultado_label = QLabel('', self)

        layoutPadre.addRow('Fecha: ', self.date_Edit)
        layoutPadre.addRow(self.resultado_label)

        self.show()

    def actualizacion(self):
        valor = self.date_Edit.date()
        print(type(valor))
        self.resultado_label.setTex(str(valor.toPyDate()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPadre()
    sys.exit(app.exec())