import sys
from  PyQt6.QtWidgets import (QDialog, 
QLabel, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont
class RegistrarUsuarioView(QDialog):
    def  __init__(self):
        super().__init__()
        self.setModal(True) # Esto es para que cuando se ejecute esta ventana no se pueda ejecutar alguna otra que este en segundo plano
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Registrar Ventana")

        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 40)

        password_1_label = QLabel(self)
        password_1_label.setText('Password: ')
        password_1_label.setFont(QFont('Arial', 10))
        password_1_label.move(20, 74)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250, 24)
        self.password_1_input.move(90, 70)
        self.password_1_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        password_2_label = QLabel(self)
        password_2_label.setText('Password: ')
        password_2_label.setFont(QFont('Arial', 10))
        password_2_label.move(20, 104)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250, 24)
        self.password_2_input.move(90, 100)
        self.password_2_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        create_Button = QPushButton(self)
        create_Button.setText('¡CREAR!')
        create_Button.resize(145, 34)
        create_Button.move(20, 170)
        create_Button.clicked.connect(self.crear_usuario)

        cancel_Button = QPushButton(self)
        cancel_Button.setText('¡CANCELAR!')
        cancel_Button.resize(145, 34)
        cancel_Button.move(170, 170)
        cancel_Button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        # Para cerrar la ventana con la opcion close()
        self.close()

    def crear_usuario(self):
        #vamos a crear a los usuario dandole una ruta en especifico
        user_path = 'usuarios.txt'

        # Vamos a obtener la informacion que el usuario haya digitado en los campos de texto
        usuario = self.user_input.text() # Obtenemos el valor con text()
        password1 = self.password_1_input.text()
        password2 = self.password_2_input.text() # Extraer el texo

        """ VERIFICAR QUE LA INFORMACION ES COHERENTE """
        if password1 == '' or password2 == '' or usuario == '':
            QMessageBox.warning(self,'ERROR',
            'Por favor ingrese datos validos, sin dejar campos de texto en blanco.',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        elif password1 != password2:
            QMessageBox.warning(self,'ERROR',
            'Las contraseñas no coinciden.',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        else:
            try:
                # Primero abrimos el archivo para escribir en él.
                with open(user_path, 'a+') as f:
                    f.write(f'{usuario}, {password1}\n')
                QMessageBox.information(self, 'CREACION EXITOSA',
                'Usuario creado correctamente',
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.close()
            except FileNotFoundError as e: 
                # Herrorres que se pueden presentar
                QMessageBox.warning(self,
                'ERROR',
                f'La base de datos de usuario no existe: {e}',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        
            
        