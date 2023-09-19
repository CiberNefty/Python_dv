import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class VentanaQCheckBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QCheckBox')
        #self.setGeometry(100,100,100,100)

        layoutPadre = QGridLayout()
        self.setLayout(layoutPadre)

        # Creamos nuestro checkBox
        checkBox1 = QCheckBox('Ya estoy aqui', self)
        checkBox1.stateChanged.connect(self.on_checkbox_changed) # Estado de cambio metodo (stateChange) con una señal.

        # Agregamos nuestro checkBox a nuestro gridlayout y lo posicionamos y le damos un aliniamiento.
        layoutPadre.addWidget(checkBox1, 0,0, Qt.AlignmentFlag.AlignBottom)
        

        self.show()

    def on_checkbox_changed(self, checkBox1):
        estado = Qt.CheckState(checkBox1)
        
        if estado == Qt.CheckState.Checked:
            print("Checkiado - Comprobado")
        elif estado == Qt.CheckState.Unchecked:
            print("Unchecked - Desenfrenado - No comprobado")
        elif estado == Qt.CheckState.PartiallyChecked: # Esta condicion no me la evalua porque no veo que utilice mas de dos checkpoints
            print("PartiallyChecked - Pacialmente comprobado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaQCheckBox()
    sys.exit(app.exec())