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

# VAmos a combinar una lista con los diccionarios una, espcie de lista multidimensional.

# Lista con diccionarios
# Esta variable va hacer una lista, dentro de esta lista podemos 
# tener varios diccionarios, van hacer varios pequeños conjuntos 
# de datos  pero que tienen un indice asociativo o indice alfanumerico
# que me permite seleccionar un diccionario.
# Entonces dentro de nuestra lista definimos diccionarios. 
contactos = [
    {
        'nombre': 'Josfino',
        'email': 'Josfino@gmail.com',
    },
    {
        'nombre': 'Luis',
        'email': 'Luis@gmail.com',
    },
    {
        'nombre': 'Salvador',
        'email': 'Salvador@gmail.com',
    }
]

# ACCEDER A UN INDICE
print(contactos[0]['nombre']) # Aqui ingresa a nuestra lista mandamos a llamar al indice de la lista y luego llamamos a la clave del diccionario

# MODIFICAR EL VALOR
contactos[0]['nombre'] = 'Josefiñito'

# MOSTRAR EL LISTADO COMPLETO 
print("\nLISTADO DE CONTACTOS:")
print("------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("---------------------------------------")

print("\nesta es la lista como se ve nomalmente\n"+str(contactos))