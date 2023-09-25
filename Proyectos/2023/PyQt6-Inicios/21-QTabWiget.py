import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QGridLayout, QTabWidget, QDateEdit, QPushButton, QFormLayout
from PyQt6.QtCore import Qt

class ventanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QTabWidget 1.1")
        self.setGeometry(100,100,355,100)

        # Creamos Nuestra hoja Principal
        Layoutpadre = QGridLayout()
        self.setLayout(Layoutpadre)

        # Grupo de Pestañas 1
        tab = QTabWidget(self, movable=True, tabsCloseable=True) # para mover pestañas con (movable=True) para boton cerrar pestañas (tabsCloseble=True)
        # tab.setMovable(True) # Para mover la petaña de un lado a hotro horizontal
        #tab.setTabsClosable(True) # Para boton de cerrar pestañas
        
        # Cramos primero nuestras pestaña 1 del grupo de pestañas 1
        # Panel de informacion persona
        pagina_personal = QWidget(self)
        layoutPagePerson = QFormLayout()
        pagina_personal.setLayout(layoutPagePerson)
        
        # Agregamos objetos a el estilo de la hoja (pestaña 1 - QGridLayout) (QFormLayout)
        layoutPagePerson.addRow('Nombres: ', QLineEdit(self))
        layoutPagePerson.addRow('Apellidos: ', QLineEdit(self))
        layoutPagePerson.addRow('DOB: ', QDateEdit(self))
        
        # Cramos primero nuestras pestaña 2
        # Panel de informacion de contacto
        pagina_contacto = QWidget(self)
        layoutPageContact = QFormLayout()
        pagina_contacto.setLayout(layoutPageContact)
        
        # Agregamos objetos a el estilo de la hoja (pestaña 2 - QGridLayout) (QFormLayout)
        layoutPageContact.addRow('Numero Telefonico: ', QLineEdit(self))
        layoutPageContact.addRow('Contacto de informacion: ', QLineEdit(self))

        # Añadimos al tab (grupo de pestañas) cada pagina contenedora de widgets y su nombre
        tab.addTab(pagina_personal, 'Informacion Personal')
        tab.addTab(pagina_contacto, 'Informacion de Contacto')

        # Añadimos los paneles de paginas a la clase de objeto de QTabWidget (Grupo de pestañas 1)        
        Layoutpadre.addWidget(tab, 0,0,2, 1)
        Layoutpadre.addWidget(QPushButton('Guardar'), 2,0,
                              alignment= Qt.AlignmentFlag.AlignLeft)
        Layoutpadre.addWidget(QPushButton('Cancel'), 2,0,
                              alignment= Qt.AlignmentFlag.AlignRight)
        

        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaPadre()
    sys.exit(app.exec())
