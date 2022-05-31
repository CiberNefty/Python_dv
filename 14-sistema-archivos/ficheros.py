from io import open
import pathlib

# Abir archivo
ruta = str(pathlib.Path().absolute()) +"/fichero_texto."
archivo = open(ruta, "a+")

# Escribir dentro de un archivo
archivo.write("*****SOY UN TEXTO metido desde python******\n")

# cerrar archivo
archivo.close()

# Abir archivo
ruta = str(pathlib.Path().absolute()) +"/fichero_texto."
archivo_lectura = open(ruta, "r+")

# Leer contenido
#contenido = archivo_lectura.read()
 #print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines() # Vamo a leer las lineas
archivo_lectura.close()

"""for frase in lista:
    if not frase.isnumeric():
        print("- "+frase.upper())"""

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    print("- "+frase.center(100))