"""
#Bucle WHILE
Estructura de control que itera o repite la 
ejecucion de una serie de instrucciones tantas veces como sea 
necesario, hasta que deje de cumplirse

contador = 0

while contador:
|   bloque de instrucciones
|   actualizacionn de contador

"""
#Todos los numero del 1 al 100
contador =1
while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador += 1

print("------------------------------------------")
#Mostramos todos los numero del 1 al 100 pero separados por coma
muestrame = str(0)
contador =1
while contador <= 100:
    muestrame = muestrame + ", "+str(contador)
    contador += 1

print(muestrame)

print("------------------------------------------")
#EJEMPLO tabla multiplicar 
print("#### EJEMPLO  TABLA MULTIPLICAR ####")
numero_usuario = int(input("de que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla del {numero_usuario} ###")

contador =1
while contador <= 10:
    print(f"{numero_usuario} X {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("Tabla terminada.")