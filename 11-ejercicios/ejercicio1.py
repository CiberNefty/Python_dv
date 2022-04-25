"""
Ejercicio1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla.
- Hacer funcion que recorra listas de numeros y devuelva un string.
- Ordenarla y mostrarla.
- Mostrar su longitud.
- Buscar algun elemento (que el usuario pida por teclado)
"""
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
    print("no existe valor en la lista.")
