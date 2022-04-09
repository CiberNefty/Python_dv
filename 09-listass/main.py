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


