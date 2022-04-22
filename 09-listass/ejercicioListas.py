# EJERCICIO 1
# Crear diferentes listas, una que contenga Marcas de automoviles, 
# otra que contenga un rango de numeros, otra que este definida  con su List()
# otra que contenga entre srt-int-float

marcasAutos = ["Chevebrolet", "Renault",'Mercedez','Tesla','Audi']
numeros = [1,2,3,4,5,6,7]
numeros1 = list(range(11))
diferentes = [1,'jose',23,'Estefany',22.23, list(range(111,122))]
#print(diferentes)

# EJERCICIO 2 
# Acceder a la lista de cada uno a de las listas que creamos anteriormente
"""
print(marcasAutos[-2]) # Acedemos desde atras nos delvolvera Tesla
print(numeros[3:]) # Accedemos desde un comienzo hasta todos los valores que siguen.
print(numeros1[3:9]) # Accedemmos a los valores que estan en ese rango guardados.
print(diferentes[:]) # Accedemos a todos los valores.
"""
# EJERCICIO 3
# Modificar cada una de las listas creadas

marcasAutos[3] = 'Hiunday' # Aqui modificamos varias listas.
marcasAutos[2] = 'Bmw'
numeros[3] = 9
numeros1[6] = 18
diferentes[5] = 'Lisa'

# EJERCICIO 4
# Añadir elemtentos a las listas
marcasAutos.append("Nissan")
marcasAutos.append("Dodge")
numeros.append(9) # Aqui vemos que se puede colocar valores iguales
numeros1.append(44) # Deja agregar valores a un rango.
diferentes.append('Josefina')

# EJERCICIO 5
# recorrer con un bucle for la lista de marcasAutos
"""
for i in marcasAutos:
    print(f"{marcasAutos.index(i)}. {i}")

for e in numeros1:
    print(f"{numeros1.index(e)}. --{e}")    
"""
# EJERCICIO 6
# Crear Listas vacia y agregar valores hasta que se escriba stop, con while 
ciclas = []
nuevacicla=''
while nuevacicla != 'stop':
    #nuevacicla = input("Ingrese marca de cicla: ")

    if nuevacicla != 'stop':
        ciclas.append(nuevacicla)
    
for nuevacicla in ciclas:
    intr =(f"{ciclas.index(nuevacicla)+1}. {nuevacicla}")

# EJERCICIO 7
# Crear una lista con una coleccion de nombre, apellidos, cumpleaños,estatura, para cada usuario minimo 4.
contactos = [
    [
        'Santiago',
        'Vera',
        'Febrero 22'
    ],
    [
        'Felipe',
        'Vera',
        'Febrero 22'
    ],
    [
        'Andrea',
        'Jimenez',
        'Junio 15'
    ],
    [
        'Melisa',
        'Ortega',
        'Agosto 9'
    ]

]
for contacto in contactos:
    for elemento in contacto:
         print(elemento)
