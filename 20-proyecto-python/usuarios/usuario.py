""" Este es un modelo va a contener una clase que me va a permitir crear los usuarios
y que cada uno obtenga valores diferente y ademas me va a permitir reutilizar y tener 
mas limpio mi codigo por que creare un objeto usuario que va a tener muchos metodos utilez.
"""
import mysql.connector

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
    # Este metodo a parte de devolvernos nos mostrara el usuario registrado    
        return self.nombre

    def identificar(self):
    # Este metodo nos devolvera el objeto usuario que estemos identificando, en base a los datos que tenemos en las propiedades.
        return self.nombre