""" 
LISTAS (arras)
Son condicionales o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos ysar un indice numerico.
"""

peilcula = "Batman"

# Definir Lista
peliculas = ["Batman", "Spiderman","El señor de los anillos"]
cantantes = list(('2pac','Daniel Vera','Amy winhouse'))
years = list(range(2020,2050))
variada= ["Vic",34, 34,3, True,"Texto"], 

"""
print(peliculas)
print(cantantes)
print(years)
print(variada) """
#---------------------------------

# Indice

#Acceder a un indice de la lista
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# Modificar
pelicula = "Otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"
print(peliculas)
#-------------------------------

# Añadir elemento a lista
cantantes.append("Kase O")
cantantes.append("Enrique Iglesias")

print(cantantes)
#------------------------------
# Como recorrer elementos de una lista para utilizarlos con el bucle for

# Recorrer  Lista
#print("\n*******LISTADO PELICULAS*******")
"""
for pelicula in peliculas: # Mientras quede en el elementos de pelicula ve iterDO y ve guardando cada uno de los elemento en pelicula.
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") """

# Agregando elementos a mi listado para ir sacandolos
"""
nueva_peliicula = ""
while nueva_peliicula != "parar":
    nueva_peliicula = input("Introduce la nueva pelucula: ")

    if nueva_peliicula != "parar":
        peliculas.append(nueva_peliicula)

print("\n*******LISTADO PELICULAS*******")
for pelicula in peliculas: # Mientras quede en el elementos de pelicula ve iterDO y ve guardando cada uno de los elemento en pelicula.
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") """
#----------------------------
# Listas MULTIDIMENSIONALES
# Es una lista que contiene una lista dentro de otra lista
print("\n*******LISTADO DE CONTACTOS*******")
contactos = [
    [
        'Daniel',
        'daniel@daniel.com'
    ],
    [
        'Pipe',
        'pipe@pipe.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]
"""
for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n") """

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+elemento)
        else:
            print("Email: "+elemento)
    print("\n")
#print(contactos[1][1]) # Aquí accedemos a nuestra sublista o subdimencion.
