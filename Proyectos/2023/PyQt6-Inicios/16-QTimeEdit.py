import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QTimeEdit

class clasePadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QTimeEdit")
        self.setGeometry(200,200,0,0)
        #elf.setMinimumWidth(200)

        formLayoutPadre = QFormLayout()
        self.setLayout(formLayoutPadre)

        self.tiempoEditable = QTimeEdit(self)
        self.tiempoEditable.editingFinished.connect(self.tiempo)

        self.resultado_tiempo = QLabel('',self)

        formLayoutPadre.addRow('Tiempo', self.tiempoEditable)
        formLayoutPadre.addRow(self.resultado_tiempo)

        self.show()

    def tiempo(self):
        valor_recibido = self.tiempoEditable.time()
        self.resultado_tiempo.setText(str(valor_recibido.toPyTime()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = clasePadre()
    sys.exit(app.exec())