"""
SET es un tipo de dato, para tener una coleccion de valores, 
pero no tiene ni indice ni orden.

definimos el set con llaves {}
"""
personas = { # Los set me ordenan los valores en desorden.
    "Daniele",
    "Manolo",
    "Wendy"
}

# AGREGAR UN ELEMENTO A MI SET.
personas.add('Paquito')

# ELEMINAR UN ELEMENTO DEL SET CON REMOVE
personas.remove('Manolo')

# COMPROBAR EL TIPO DE DATO
print(type(personas))

print(personas)