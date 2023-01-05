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

# Ya que tenemos la conexsion podemos crear la DB con nuestro cursor para crear nuestras consultas.
cursor = database.cursor()
#Crear db
"""cursor.execute("CREATE DATABASE IF NOT EXISTS master_python_db") # Al ejecutar desde aqui podemos visualizar en phpMyadmin que se puede visualizar.

# Como puedo comprobar desde codigo que una db existe.
cursor.execute("SHOW DATABASES")

# Ahora mismo dentro de nuestro cursor tenemos todos los datos de nuestra db
# como sacar todas nuestras db's

for bd in cursor:
    print(bd)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculos PRIMARY KEY (id)
);
""")

# Comprobar que tablas hay.
cursor.execute("SHOW TABLES")
# print(cursor.fetchall())
for table in cursor:
    print(table)

# INSERTAR DATOS
#cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra', 18500)")
coches = [
    ('Seat','Ibiza', 5000),
    ('Reanult','Clio', 15000),
    ('Chevrolet','Onix', 6000),
    ('Ford','Ranger', 5000)
]
cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s);", coches)
# Recordar que toca guardar los datos ya que si no hacemos el commit no se nos guardara nada de lo que escribamos aquí.
# cursor.commit() # Recordemos que el atributo lo tiene es la db 
"Guardar cambios en la db que tiene nuestro cursor."
database.commit()