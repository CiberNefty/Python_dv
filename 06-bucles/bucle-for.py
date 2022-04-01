"""
# FOR
for variable in elemento_iterable (Lista, rango, etc):
    BLOQUE DE ISNTRUSCCIONES
"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el "+str(contador))
    resultado = resultado + contador
    #resultado += contador 
print(f"El resultado es: {resultado}")

#EJEMPLO tablass de multiplicar (que el usuario introduzca un numero para multiplicar)
print("\n################# Ejemplo ##################")

numero_usuario = int(input("De que numero quieres la tabla: "))

if numero_usuario <= 1:
    numero_usuario = 1

print(f"\n### Tabla de multiplicar del numero {numero_usuario} ###")

for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("no se pueden mostrar numeros prohibidos!!")
        break

    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada.")
