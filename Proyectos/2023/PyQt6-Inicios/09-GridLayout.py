import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout, QLineEdit
# Para obtener el valor o (metodo) de aliniamiento toca importar el QtCore
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Grid Layout')
        #self.setGeometry(100, 100, 100, 300)

        layoutPadre_Grid = QGridLayout()
        self.setLayout(layoutPadre_Grid)

        # USUARIO
        """user_input = QLineEdit(self,
            placeholderText = 'Escribe tu nombre aquí...',
            clearButtonEnabled = True
        )"""

        layoutPadre_Grid.addWidget(QLabel('Usuario: '),0,0)
        layoutPadre_Grid.addWidget(QLineEdit(self, 
            placeholderText = 'Escribe tu usuario...',
            clearButtonEnabled = True),
            0,1)
        
        # CONTRASEÑA
        contraseña_label = QLabel('Contraseña: ')
        layoutPadre_Grid.addWidget(contraseña_label, 1,0)
        layoutPadre_Grid.addWidget(QLineEdit(
            self, placeholderText = '*****************',
            echoMode = QLineEdit.EchoMode.Password,
            clearButtonEnabled = True
        ),1,1) # Position the QlineEdit

        # Botones
        """boton1 = QPushButton()
        boton1.setText("Boton 1ds")
        #boton1.setFixedSize(100,30)
        #boton1.setIcon('') # Toca volver a retomar la libreria de IO
        boton1.setStyleSheet('QPushButton{background-color: GREY}')

        layoutPadre_Grid.addWidget(boton1, 3,0, 2,0, Qt.AlignmentFlag.AlignBottom)"""
        layoutPadre_Grid.addWidget(QPushButton('Iniciar'), 2,0,
                                    Qt.AlignmentFlag.AlignHCenter)
        botonCerrar = QPushButton()
        botonCerrar.setText('Cerrar')
        botonCerrar.setStyleSheet('QPushButton{background-color:red}')
        botonCerrar.clicked.connect(self.cerrar_ventana)

        layoutPadre_Grid.addWidget(botonCerrar, 2,1,
                                   alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.show()

    def cerrar_ventana(self, clicked):
        print("Cerrar")
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())