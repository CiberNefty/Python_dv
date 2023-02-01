import usuarios.usuario as modelo # Aqui le estamos dando un alias ya que es el modelo

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
        mail = input('Introduce email: ')
        password = input('Introduce tu contraseña: ')