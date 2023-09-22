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

"""
tiene los siguientes métodos y propiedades útiles:QDateTimeEdit

Propiedad	Descripción
date()	Devuelve el valor de fecha mostrado por el widget. El tipo de devolución es . Para convertirlo en un objeto, utilice el método de la clase.QDatedatetime.datetoPyDate()QDate
time()	Devuelve la hora mostrada por el widget. El valor devuelto tiene el tipo de . Utilice el método para convertirlo en un objeto de Python.QTimetoPyTime()datetime.time
dateTime()	Devuelve el valor de fecha y hora que muestra el widget. El tipo de devolución es .QDateTime
minimumDate	La fecha más temprana que puede establecer el usuario.
maximumDate	La última fecha que puede establecer el usuario.
minimumTime	La hora más temprana que puede establecer el usuario.
maximumTime	La última hora que puede establecer el usuario.
minimumDateTime	La fecha y hora más tempranas que puede establecer el usuario.
maximumDateTime	La última fecha y hora que puede establecer el usuario.
calendarPopup	Mostrar una ventana emergente de calendario si es True.
displayFormat	es una cadena que da formato a la fecha mostrada en el widget.
"""