"""
Ejercicio 7.
Hacer un programa que muestre todos los numeros impares 
entre dos numero que decida el usuario.
"""
numero1 = int(input("Ingresa primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))
"""
pared =str(0)
for contador in range (numero1, (numero2+1)):
    if contador % 2 == 1:
        pared = pared + ", "+str(contador)
print(pared)
"""
#EJEMPLO por victor
if numero1 < numero2:
    for x in range (numero1,(numero2+1)):
        if x%2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")
else: 
    print(f"El numero {numero1} tiene que ser menor al numero {numero2}")