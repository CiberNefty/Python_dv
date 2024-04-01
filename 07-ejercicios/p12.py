# 12. Programa para determinar si un número cualquiera ingresado por el usuario es o no positivo
numero=input("Ingrese un numero para validar si es positivo o no!:")

if float(numero) < 0:
    print("El numero es negativo")
else:
    print("El numero es positivo")