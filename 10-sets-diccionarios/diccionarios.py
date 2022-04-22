"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.


Es parecido a una lista de datos, almacena conjunto de datos
pero en ves de tener indices numericos tiene indices ALFANNUMERICOS.
"""

persona = {
    "nombre": "Daniel",
    "apellidos": "Vera",
    "instagram": "@_ds.va_"
}

print(persona)

# COMPROBAR TIPO DE DATOS
print(type(persona))

# ACCEDER A DIFERENTES INDICES EN EL DICCIONARIO.
print(persona["apellidos"])
print(persona["instagram"])
print(persona["nombre"])
