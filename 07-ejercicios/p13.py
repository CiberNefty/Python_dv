# 13. Programa para determinar cuál es mayor entre 2 números cualquiera ingresados por el usuario
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 == numero2:
    print("Los numero son iguales")
elif numero1 > numero2:
    print("El numero {} es mayor que {}".format(numero1, numero2))
else:
    print(f"El numero {numero2} es mayor que {numero1}")