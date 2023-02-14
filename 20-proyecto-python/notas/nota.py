# Aqui vamos a crear nuestra clase para crear diferentes tipos de notas y reutilizar este codigo.
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    
    def __init__(self,usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id # Este seria el usuario identificado.
        self.titulo = titulo # Es el titulo que rellena el usuario.
        self.descripcion = descripcion # Que es la descripcion que el usuario nos meta.
 
    def guardar(self): # Este seria el metodo que sirve para guardar en la base de datos.
        # Creamos una variable sql
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        #Ejecucion de la consulta.
        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount(), self ]