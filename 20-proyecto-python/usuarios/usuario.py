""" Este es un modelo va a contener una clase que me va a permitir crear los usuarios
y que cada uno obtenga valores diferente y ademas me va a permitir reutilizar y tener 
mas limpio mi codigo por que creare un objeto usuario que va a tener muchos metodos utilez.
"""
import mysql.connector
import datetime

database = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    database="proyectonotas_python"
)
#Verificamos si funciona la coneccion 
#print(database)

cursor = database.cursor(buffered=True) # Este buffered me va a permitir hacer muchas consultas usanndo el mismo cursor

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
    # Lo primero que haremos es crear una variable sql para guardar la consulta.
        sql = 'INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,%s);'
    # Los porcentajes eese(%s) nos sirve para sustituir datos que tengamos en una tapla.
        usuario = (self.nombre, self.apellidos, self.mail, self.password, fecha)
        cursor.execute(sql, usuario)
        database.commit()
        
        # Vamos a devolver una lista de la cantidad de registros que se han modificado.
        return [cursor.rowcount, self]
        # Listo toca probarlo, ahora nos vamos al modulo acciones y tengo que importar el modelo de usuario que esta en el dicho paquete usuarios 


    def identificar(self):
    # Este metodo nos devolvera el objeto usuario que estemos identificando, en base a los datos que tenemos en las propiedades.
        return self.nombre