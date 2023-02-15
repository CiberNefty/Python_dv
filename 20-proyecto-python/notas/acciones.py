import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}! Vamos a crear una nueva nota.")

        # Vamos a sacar los datos que necesito para guardar la nota osea el usuario_id, el titulo, descripción.
        titulo = input('Introduce el titulo de tu nota: ')
        descripción = input('Mete el contenido de tu nota: ')
        
        # Listo ahora tengo que llamar a mi modelo, toca importarlo primero.
        nota = modelo.Nota(usuario[0], titulo, descripción)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n Vale {usuario[1]}!! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n++++++++++++++++++++++++++++++++++++++++")
            print(nota[2])
            print(nota[3])
            print("\n++++++++++++++++++++++++++++++++++++++++")