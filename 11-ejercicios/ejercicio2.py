"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar While y For.
"""
listanumeros = []
entrada=""
contador = 0

while contador in range(4):
    entrada = input("Ingrese numero a la lista: ")
    listanumeros.append(entrada)
    contador += 1
print(listanumeros)

listanumeros1 = []
for i in range(4):
    entrada1 = input("Ingrese valor a la lista: ")
    listanumeros1.append(entrada1)

print(listanumeros1)