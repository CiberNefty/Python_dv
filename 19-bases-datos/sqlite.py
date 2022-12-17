"""
Le llamamos a asi a nuestro fichero por que vamos a trabajar con sql lite.

Dentro de Python viene un Motos de DB ligero basado en SQL que se llama sqlite
y ya viene instalado dentro del lenguaje, es decir, no tenemos que estar instalando ningun modulo ni nada
simplemente el modulo ya viene, esa DB se guarda en un archivo, vamos a conectarnos en la DB."""

# CONECXION DB
# Lo primero que toca hacer es importar el modulo
# Importar Modulo.

import sqlite3

# CONECXION
conexion = sqlite3.connect('pruebasqlite.db')

#Lo primero que tenemos que tener para crear una tabla, es que tenemos que crear un cursor,
# El cursos lo que me va a permitir es ejecutar las consultas.

# CREAR CURSOR
cursor = conexion.cursor() # De esta manera puedo ejecutar consultas.

# CREATE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, " + # Aqui en sqlite el auto_increment va todo pegado (AUTOINCREMENT)
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
#"CONSTRAINT producto_pkey PRIMARY KEY (producto)"+
");")

"""Evidenteme no me genera error, pero para que quede guardado tengo que hacer un commit."""
# GUARDAR CAMBIOS
conexion.commit()

# INSERRT DATOS
#cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto','Descripcion de mi producto',540);")
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto','Descripcion de mi producto',540);")
conexion.commit()

# Lesctura Listar Datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

"""for producto in productos:
    print(producto[1]) # Aqui accedemos como si fuera una lista, nos motrara la primera columna.
"""
for producto in productos:
    print("id: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ",producto[3])
    print('\n')

# Sacar primer registro de la table.
cursor.execute("SELECT id, titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# Tenemos que cerrar la conexion por que si no la cerramos el fichero se quedara abierto y no se guardaran los cambios en el fichero.
# CERRAR CONECXION
conexion.close()

