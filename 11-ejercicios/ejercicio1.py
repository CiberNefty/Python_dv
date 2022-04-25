"""
Ejercicio1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
(Hecho)- Recorrer la lista y mostrarla.
(Hecho)- Hacer funcion que recorra listas de numeros y devuelva un string.
(Hecho)- Ordenarla y mostrarla.
(Hecho)- Mostrar su longitud.
(Hecho)- Buscar algun elemento (que el usuario pida por teclado)
""" """
def fun_lista():
    l=""
    for listacontenida in lista:
        #print(f"{fun_lista().index(listacontenida)+1}. {listacontenida}")
        l += str(listacontenida) + "-" 
    return l
lista = [22, 12, 66, 7, 13, 1, 10, 3]
print(fun_lista())
  
lista.sort() 
print("Lista ordenanda:", lista) # Ordenanos la lista
print("Su longitud es de:",len(lista))

evaluar = int(input("Qee valor quieres buscar en esta lista?: "))

if evaluar in lista:
    print("Esta en la posicion:",lista.index(evaluar)+1)
else:
    print("no existe valor en la lista.") """
#-------------------------------
# Ejercicio por CIV

# Crear la lista
numeros = [13, 64,52,73,21,7,91,63]

# Crear funcion que recorrar lista y devuelva string
def mostrarLista(lista1):
    resultado = ""
    for numero in lista1:
        resultado +="Elemento: " + str(numero)
        resultado += "\n"

    return resultado
"""
# Recorrer y mostrar
print("#### RECORRER Y MOSTRAR ####")
for numero in numeros: # Esto significa recorreme  toda la lista de numeros y ve creandome una variable numero en cada iteracion que contenga el elemento que vayamos a  mostrar
    print(numero) """

print(mostrarLista(numeros))
print(mostrarLista(["Dan","Juan","Gabriel"]))

# Ordenar y mostrar
print("#### ORDENAR Y MOSTRAR ####")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar longitud
print("#### MOSTRAR LONGITUD ####")
print(len(numeros))

# Busqueda en la Lista
print("#### Busqueda en la lista ####")

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
     busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducito el {busqueda}")

print(f"### Buscar en la lsita el numero {busqueda} ###")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indice: {search}")