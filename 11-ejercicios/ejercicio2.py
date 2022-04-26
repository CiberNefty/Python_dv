"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar While y For.
"""
listanumeros = []
entrada=""
contador = 0
"""
while contador in range(4):
    entrada = input("Ingrese numero a la lista: ")
    listanumeros.append(entrada)
    contador += 1
print(listanumeros)

listanumeros1 = []
for i in range(4):
    entrada1 = input("Ingrese valor a la lista: ")
    listanumeros1.append(entrada1)

print(listanumeros1)"""
# ------------------------------
# Ejercicio por CIV

coleccion = []
x = 0
while x < 120:
    coleccion.append(f"Elementos-{x}")
    print("Mostrando el: " + coleccion[x])
    x += 1
print(coleccion[64])
"""
coleccion = []
for contador1 in range(0,120):
    coleccion.append(f"Elemento-{contador1}")
    print("Mostrando el: "+ coleccion[contador1])

print(coleccion[115]) # Si queremos sacar una posicion en concreto
"""