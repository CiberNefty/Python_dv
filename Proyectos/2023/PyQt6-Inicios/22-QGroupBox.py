import sys
from PyQt6.QtWidgets import QWidget, QApplication, QGroupBox, QFormLayout, QPushButton, QLineEdit, QDateEdit

class clasePadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QGroupBox')
        #self.setGeometry(100,100,200,200)
        
        # creamos nuestro layou principal donde va ir guardado el groupBox1
        layout_padre = QFormLayout()
        self.setLayout(layout_padre)

        # Creamos nuestro Cuadro de Grupo QgroupBox para INFORMACION DE PERSONAS
        person_groupbox = QGroupBox('Informacion Personal')
        form_layout = QFormLayout()
        person_groupbox.setLayout(form_layout)

        form_layout.addRow('Nombres: ', QLineEdit(person_groupbox))
        form_layout.addRow('Apellidos: ', QLineEdit(person_groupbox))
        form_layout.addRow('DOB', QDateEdit())

        # Creamos nuestro Cuadro de Grupo QgroupBox para CONTACTOS
        contacto_groupbox = QGroupBox('Contacto de Informacion')
        form_layout = QFormLayout()
        contacto_groupbox.setLayout(form_layout)

        form_layout.addRow('Numero Telefonico: ', QLineEdit(contacto_groupbox))
        form_layout.addRow('Correo Electronico: ', QLineEdit(contacto_groupbox))

        layout_padre.addRow(person_groupbox)
        layout_padre.addRow(contacto_groupbox)
        layout_padre.addRow(QPushButton('SAVE'))


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = clasePadre()
    sys.exit(app.exec())