import usuarios.usuario as modelo # Aqui le estamos dando un alias ya que es el modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk! Vamos a registrarte en el sistema...")
        
        nombre = input('Cual es tu nombre?: ')
        apellidos = input('Cuales son tus apellidos?: ')
        mail = input('Introduce email: ')
        password = input('Introduce tu contraseña: ')
        # Listo ahora tenemos que crear nuestro objeto que va a enviar los valores a nuestro modulo usuario
        usuario = modelo.Usuario(nombre, apellidos, mail, password)
        # Ahora tengo que registrar a mi usuario en la BD a los valores que le he pasado al objeto usuario.
        registroUdb = usuario.registrar()

        if registroUdb[0] >= 1: # Esta comprobacion esta evaluando lo que retorna el metodo registrar.
            print(f"\nPerfecto {registroUdb[1].nombre}  te has registrado con el email {registroUdb[1].mail}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nVale! Identificate en el sistema...")
        
        try:
            mail = input('Introduce email: ')
            password = input('Introduce tu contraseña: ')

            usuario = modelo.Usuario('','', mail, password)
            login = usuario.identificar()

            # Comprobar si el login es correcto
            if mail == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto! intentalo mas tarde!.")        

    def proximasAcciones(self, usario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == 'crear':
            hazEl.crear(usario)
            self.proximasAcciones(usario)
        elif accion == 'mostrar':
            hazEl.mostrar(usario)
            self.proximasAcciones(usario)

        elif accion == 'eliminar':
            hazEl.borrar(usario)
            self.proximasAcciones(usario)
        
        elif accion == 'salir':
            print(f'ok {usario[1]}, hasta pronto!')
            exit ()
    