# para trabajar con los directorios tengo que utilizar el modulo os
import os, shutil

# Crear carpeta 
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print("Ya existe el directorio")

# Copiar
"""ruta_original = './mi_carpeta' # Aquí le pasamos la ruta original
ruta_nueva = './mi_carpeta_COPIADA' # Aquí le pasamos la ruta nueva

#shutil.copyfile(ruta_original, ruta_nueva) # la funcion copyfile no nos sirve toca la funcion copytree
shutil.copytree(ruta_original, ruta_nueva)
"""
# Eliminar carpeta
"""
os.rmdir('./mi_carpeta_COPIADA')
""" 