"""
Ejercicio 7.
Hacer un programa que muestre todos los numeros impares 
entre dos numero que decida el usuario.
"""
numero1 = int(input("Ingresa primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))
pared =str(0)
for contador in range (numero1, (numero2+1)):
    if contador % 2 == 1:
        pared = pared + ", "+str(contador)
print(pared)
        