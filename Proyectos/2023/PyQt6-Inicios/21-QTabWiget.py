import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QGridLayout, QTabWidget, QDateEdit, QPushButton
from PyQt6.QtCore import Qt

class ventanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QTabWidget 1.1")
        #self.setGeometry(100,100,100,100)

        # Creamos Nuestra hoja Principal
        Layoutpadre = QGridLayout()
        self.setLayout(Layoutpadre)

        # Grupo de Pestañas 1
        
         
        # Cramos primero nuestras pestaña 1 del grupo de pestañas 1
        

        
        # Agregamos objetos de escrituras a el estilo de la hoja (pestaña) (Gridlayout)
        
        

        # Cramos primero nuestras pestaña 2
              
        
        

        # Añadimos los grupos de pestañas a la hoja principal 1
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaPadre()
    sys.exit(app.exec())
