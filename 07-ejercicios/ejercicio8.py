"""
Ejercicio 8.
Realizar un programa que me pregunte cuando pociento
va hacer a un numero que digie. Ejemplo;
¿Cuanto es X por ciento de X numero?
                20% de 150 
"""
numero1 = float(input("Ingresa El primer numero como porcentaje: "))
numero2 = float(input("Ingresa El segundo numero: "))

if numero1 > 0.01:
    print(f"El procentaje de {numero1} de {numero2} es: {(numero1 * numero2)/100}%")