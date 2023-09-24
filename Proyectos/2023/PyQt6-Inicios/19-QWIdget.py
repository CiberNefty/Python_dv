import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout, QHBoxLayout

class ventanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QWidget")
        #self.setGeometry(100,100,100,100)

        layoutPadre = QHBoxLayout()
        self.setLayout(layoutPadre)

        # Panel de personas
        panel_de_personas = QWidget(self) # Creamos un contenedor el cual sera el contenedor principal para agregar objetos a su vez,
        formLayoutHijo = QFormLayout()   # Creamos un formulario para que sea el estilo formullario para nuestro contenedor
        panel_de_personas.setLayout(formLayoutHijo) # Agregamos a l contenedo 0 el formulario
        formLayoutHijo.addRow('Nombres: ', QLineEdit(panel_de_personas)) # Luego dentro de formulario agregamos en cada fila un texto y luego un objeto que va hacer guardado dentro de nuestro contenedor 0
        formLayoutHijo.addRow('Apellidos: ', QLineEdit(panel_de_personas))
        formLayoutHijo.addRow('Fechas de Cumpleaños: ', QLineEdit(panel_de_personas))
        formLayoutHijo.addRow('Correo electronico: ', QLineEdit(panel_de_personas))
        formLayoutHijo.addRow('Numero Telefonico: ', QLineEdit(panel_de_personas))

        # Panel de direcciones
        panel_de_direcciones = QWidget(self)
        formLayoutHijo = QFormLayout()
        panel_de_direcciones.setLayout(formLayoutHijo)
        formLayoutHijo.addRow('Calle: ', QLineEdit(panel_de_direcciones))
        formLayoutHijo.addRow('Ciudad: ', QLineEdit(panel_de_direcciones))
        formLayoutHijo.addRow('Estado/Providencia: ', QLineEdit(panel_de_direcciones))
        formLayoutHijo.addRow('Codigo de estado: ', QLineEdit(panel_de_direcciones))
        formLayoutHijo.addRow('Pais: ', QLineEdit(panel_de_direcciones))

        # Agregar al formulario principañ los dos formularios aparte
        layoutPadre.addWidget(panel_de_personas) # Agregamos a nuestro layout Padre los contenedores principales que contienen los formularios
        layoutPadre.addWidget(panel_de_direcciones) # Agregamos a nuestro layout Padre los contenedores principales que contienen los formularios

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaPadre()
    sys.exit(app.exec())
