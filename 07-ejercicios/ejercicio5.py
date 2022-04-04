"""
ejercicio 5.
Hacer un programa que muesttre todos los numeros entre 
dos numero que diga el usuario

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

for num1 in range(num1,num2):
    print(num1)

#####################################
# Horizontal Mente los muestros
num = str(0)
for num1 in range(num1,num2):
    num = num + ", "+str(num1)
    
print(num)    
"""
####################################
# Ejercicio realizado por victor
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

if numero1 < numero2:
    for contador in range(numero1,(numero2+1)):# Aquí le sumamos un numero al rango numero2 para que nos muestre la cantidad exacta.
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")