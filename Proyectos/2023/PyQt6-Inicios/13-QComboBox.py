import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QComboBox, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QComboBox')
        self.setMinimumWidth(300)

        # Creamos caja contendedora
        layoutPadre = QVBoxLayout()
        self.setLayout(layoutPadre)

        labeltitle = QLabel('Selecciona Plataforma', self)
        # create a combobox
        self.cb_platform = QComboBox(self)
        self.cb_platform.addItem('AWS EDUCATE')
        self.cb_platform.addItem('UDEMY')
        self.cb_platform.addItem('UNIVESITY OF TOLIMA')
        self.cb_platform.addItem('PLATZI')

        self.cb_platform.activated.connect(self.update)

        self.resultado = QLabel('', self)

        layoutPadre.addWidget(labeltitle)
        layoutPadre.addWidget(self.cb_platform)
        layoutPadre.addWidget(self.resultado)

        # show the window
        self.show()

    def update(self):
        self.resultado.setText(
            f'You selected {self.cb_platform.currentText()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPadre()
    sys.exit(app.exec())

"""
Después de crear un cuadro combinado, debe rellenar sus opciones mediante:

 + addItem() - toma una etiqueta de cadena y un valor de datos y lo agrega al final de la lista.
 + insertItem() - funciona como el método, excepto que toma un índice para el primer argumento y agrega el elemento de ese índice a la lista.addItem()
   Además, puede pasar una lista de opciones al método or a la vez.addItems()insertItems()

Para obtener los elementos seleccionados actualmente, puede utilizar uno de los métodos siguientes:

 * currentData() - devuelve el elemento seleccionado actualmente.
 * currentIndex() - devuelve el índice del elemento seleccionado actualmente.
 * currentText() - devuelve el texto del elemento seleccionado actualmente.
 * Opcionalmente, un cuadro combinado permite introducir texto si establece su propiedad editable en. 'True'

La propiedad permite establecer si el cuadro combinado debe insertar elementos introducidos en la lista. 'insertPolicy'
"""