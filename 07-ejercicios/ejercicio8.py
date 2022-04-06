"""
Ejercicio 8.
Realizar un programa que me pregunte cuando pociento
va hacer a un numero que digie. Ejemplo;
¿Cuanto es X por ciento de X numero?
                20% de 150 
"""
numero1 = float(input("Ingresa El numero: "))
numero2 = float(input(f"Ingresa El porcentaje para sacar de {numero1}: "))

if numero1 > 0.01:
    print(f"El {numero2}% de {numero1} es: {(numero2 * numero1)/100}")
#---------------------------------------------
# Ejercico por Vic
numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero}?:"))

operacion = (numero * (porcentaje/100))
print(f"El {porcentaje}% de {numero} es: {operacion}")