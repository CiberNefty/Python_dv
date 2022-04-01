"""
Ejercicio2 
Escribir un script que nos muestre por pantalla todos los numeros pares 
del 1 al 120
"""

num1= 0
num = str(0)
for num1 in range(0,121):
    if num1 % 2 == 0:
        num = num + ", "+ str(num1)
        
print(num)

print("---------------------------------------")


for contador in range(1,121):
    if contador %2 == 0:
        print(contador, " Es par.")
    """else:
        print(f"{contador} es impart")"""