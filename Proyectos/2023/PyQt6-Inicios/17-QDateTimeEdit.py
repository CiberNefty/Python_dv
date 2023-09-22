import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QDateTimeEdit

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QDateTimeEdit')
        #self.setGeometry(100,100,200,100)
        self.setMinimumWidth(200)

        layoutPadre_form = QFormLayout()
        self.setLayout(layoutPadre_form)

        self.fecha_tiempo_editable = QDateTimeEdit(self, calendarPopup = True)
        self.fecha_tiempo_editable.dateTimeChanged.connect(self.tiempo)

        self.resultado_tiempo_editable = QLabel('',self)

        layoutPadre_form.addRow('Date: ', self.fecha_tiempo_editable)
        layoutPadre_form.addRow(self.resultado_tiempo_editable)

        self.show()

    def tiempo(self):
        valorRecogido = self.fecha_tiempo_editable.dateTime()
        self.resultado_tiempo_editable.setText(valorRecogido.toString("yyyy-MM-dd HH:mm"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())