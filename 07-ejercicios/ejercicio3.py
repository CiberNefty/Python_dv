"""
Ejercicio 3. 
Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros 
naturales. Resolver con FOR y WHILE
"""

# WHILE
"""
numero = 1
while numero < 61:
    print(f"{numero} * {numero} = {numero * numero}")
    numero += 1
"""
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f" el cuadrado de {cuadrado} es {contador}")
    contador += 1

# FOR
"""
for contador in range(0,61):
    print(f"{contador} * {contador} = {contador * contador}")
"""
for numeros in range(61):
    cuadrado = numeros * numeros
    print(f"El cuadrado de {numeros} es {cuadrado}")