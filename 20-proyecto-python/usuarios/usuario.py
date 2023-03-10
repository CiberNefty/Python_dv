""" Este es un modelo va a contener una clase que me va a permitir crear los usuarios
y que cada uno obtenga valores diferente y ademas me va a permitir reutilizar y tener 
mas limpio mi codigo por que creare un objeto usuario que va a tener muchos metodos utilez.
"""

import datetime
import hashlib # importamos este modulo para poder cifrar las contraseñas que tengamos en texto plano en el motor de BD
import usuarios.conexion as conexion # Aquí importamos el modulo para poder conectar a la DB 

connect = conexion.conectar() # creamos una objeto para poder utilizar nuestro metodo conectar_db
database = connect[0] # Creamos otro objeto para utilizar el indice que nos devuelve la funcion(metodo) conectar_db()
cursor = connect[1] 

class Usuario:
    def __init__(self,nombre,apellidos,mail,password):
        self.nombre = nombre
        self.apellidos =apellidos
        self.mail = mail
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now() # estamos guardando la fecha completa 
    # Este metodo a parte de devolvernos nos mostrara el usuario registrado    
    # Este sera el metodo de registro de usuarios

    # Cifrar contraseña 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

    # Lo primero que haremos es crear una variable sql para guardar la consulta.
        sql = 'INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,%s);'
    # Los porcentajes eese(%s) nos sirve para sustituir datos que tengamos en una tapla.
        usuario = (self.nombre, self.apellidos, self.mail, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result =[cursor.rowcount, self]
        except:
            result = [0, self]
        # Vamos a devolver una lista de la cantidad de registros que se han modificado.
        
        return result
        # Listo toca probarlo, ahora nos vamos al modulo acciones y tengo que importar el modelo de usuario que esta en el dicho paquete usuarios 


    def identificar(self):
    # Este metodo nos devolvera el objeto usuario que estemos identificando, en base a los datos que tenemos en las propiedades.
       
        # Consulta para comprobar si existe el usuario y luego ciframos la contraseña
        sql = 'SELECT * FROM usuarios WHERE mail = %s AND password = %s'

        # Cifrar contraseña 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta       
        usuario = (self.mail, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone() # el fetchone es para que solo nos devuelva un usuario

        return result
