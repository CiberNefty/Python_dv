import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QGridLayout, QTabWidget, QDateEdit, QPushButton
from PyQt6.QtCore import Qt

class ventanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QTabWidget")
        #self.setGeometry(100,100,100,100)

        # Creamos Nuestra hoja Principal
        LayoutMain = QHBoxLayout()
        self.setLayout(LayoutMain)

        # Grupo de Pestañas 1
        tab = QTabWidget()
        LayoutMain.addWidget(tab)
         
        # Cramos primero nuestras pestaña 1 del grupo de pestañas 1
        page1 = QWidget(tab) # Contenedor
        page_layoutGrid1 = QGridLayout()
        page1.setLayout(page_layoutGrid1)
        
        # Agregamos objetos de escrituras a el estilo de la hoja (pestaña) (Gridlayout)
        page_layoutGrid1.addWidget(QLineEdit(page1),0,0, Qt.AlignmentFlag.AlignCenter)
        

        # Cramos primero nuestras pestaña 2
        page2 = QWidget(tab)
        page_layoutGrid2 = QGridLayout()
        page2.setLayout(page_layoutGrid2)        
        
        # Grupo de Pestañas 2
        tab1 = QTabWidget()
        LayoutMain.addWidget(tab1)

        # Cramos primero nuestras pestaña 1
        page3 = QWidget(tab1)
        page_layoutGrid3 = QGridLayout()
        page3.setLayout(page_layoutGrid3)

        # Cramos primero nuestras pestaña 2
        page4 =QWidget(tab1)
        page_layoutGrid4 = QGridLayout()
        page4.setLayout(page_layoutGrid4)

        # Añadimos los grupos de pestañas a la hoja principal 1
        tab.addTab(page1, 'Hoja 1')
        tab.addTab(page2, 'Hoja 2')
        tab1.addTab(page3, 'Hoja 3')
        tab1.addTab(page4, 'Hoja 4')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaPadre()
    sys.exit(app.exec())
