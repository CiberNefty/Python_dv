# Aqui vamos a crear nuestra clase para crear diferentes tipos de notas y reutilizar este codigo.
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    
    def __init__(self,usuario_id, titulo = "", descripcion = ""):
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

    def listar(self):
        # Este metodo se encargara de hacer un select a la DB

        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall() # Sacaremos todos los datos que nos muestre esa cosulta

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%';"

        cursor.execute(sql)
        database.commit()

        # Devolvemos la cantidad de filas afectadas
        return [cursor.rowcount(), self]