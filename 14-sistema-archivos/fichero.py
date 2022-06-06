from io import open
import pathlib # para encontrar archivos en rutas
import shutil # Este modulo podemos acceder a diferentes funciones para copiar archivos, renombrar archivos entre otras cosas.

# Abrir archivo
ruta = str(pathlib.Path().absolute())+'/fichero_txt1.txt'
archivo = open(ruta, 'a+')

# Escribir dentro de un archivo
archivo.write("***** ***** SOY Un TExto  metido desde python ****\n")

# Cerrrar el archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute())+'/fichero_txt1.txt'
archivo_lectura = open(ruta, 'r')

# Leer contenido del archivo
#contenido = archivo_lectura.read()
#print(elemento)

# Leer contenido y guardar en una lista 
lista = archivo_lectura.readlines()
archivo_lectura.close()

"""for  frase in lista:
    if not frase.isnumeric():
        print('- '+frase.upper())"""

'''for  frase in lista:
    lista_frase= frase.split() # El split nos sirve para que una frase se conviertan en una lista
    print(lista_frase)
    #print('- '+frase.upper())'''

for  frase in lista:
    #lista_frase= frase.split() # El split nos sirve para que una frase se conviertan en una lista
    #print(lista_frase)
    print('- '+frase.center(150)) # El center me sirva para centrar texto o contenido

# Copiar archivo
"""ruta_original = str(pathlib.Path().absolute())+'/fichero_txt1.txt'
ruta_nueva = str(pathlib.Path().absolute())+'/fichero_copiado.txt'
ruta_alternativa = '../07-ejercicios/fichero_copiado88.txt' # Si quiero que este archivo se copie en otra carpeta dentro del proyecto principal

shutil.copyfile(ruta_original, ruta_nueva) # Tenemos que coger el archivo de la ruta que este actualmente y copiarlo a otra ruta que queramos
"""

# Mover archivo o renombrar
"""ruta_original = str(pathlib.Path().absolute())+'/fichero_copiado.txt'
ruta_nueva = str(pathlib.Path().absolute())+'/fichero_copiado__NUEVA.txt'

shutil.move(ruta_original, ruta_nueva) # Utilizamos un metodo de shutil que se llama move, ha esta funcion le paso dos parametros la ruta original y la ruta nueva
"""
# Eliminar archivo
"""import os

ruta_nueva = str(pathlib.Path().absolute())+'/fichero_copiado__NUEVA.txt'
os.remove(ruta_nueva)
"""
# Comprobar si existe
import os.path # Este modulo nos permite comprobar si existe un directorio
#print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "/fichero_txt1.txt"
ruta_comprobar = './fichero.py'

if os.path.isfile(ruta_comprobar): # podemos comprobar si un fichero existe o no
    print('El archivo existe')
else:
    print('El archivo no existe')