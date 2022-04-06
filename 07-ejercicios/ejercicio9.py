"""
Ejercicio 9.
Hacer un programa que pida numeros al usuario 
indefinidamente hasta meter el numero 111
"""
numero = 0

while numero != 111:
    numero = int(input("Ingresa un numero: "))
    if numero == 111:
        print("Fin.") 
        break
    else: 
        print(numero)
#-----------------------------------
contador=1
m = str(0)
while contador < 100:
    numero = int(input("Introduce un numero: "))

    if numero == 111: 
        break
    else:
        m = m + ", "+str(numero)
        print(f"has eintroducido : {m}")