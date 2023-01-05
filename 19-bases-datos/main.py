""" Vamos a importar el modulo de mysql de python"""
import mysql.connector

# Conexsion
"""database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)"""
database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="master_python_db" # Acomparacion de como esta arriba esta instruccion nos sirver como si estuvieramos realizando un (USE) a alguna base de datos.
)

# Como saber si la conexion ha sido correcta?
#print(database)

# Ya que tenemos la conexsion podemos crear la DB con nuestro cursor.
cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python_db") # Al ejecutar desde aqui podemos visualizar en phpMyadmin que se puede visualizar.

# Como puedo comprobar desde codigo que una db existe.
cursor.execute("SHOW DATABASES")

# Ahora mismo dentro de nuestro cursor tenemos todos los datos de nuestra db
# como sacar todas nuestras db's

for bd in cursor:
    print(bd)