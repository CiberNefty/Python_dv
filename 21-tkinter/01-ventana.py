# Tkinter
# Es un modulo para crear interfaces graficas de usuario.

 # Importamos todo de tkinter
from tkinter import *
import os.path

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana.
ventana.title("Interfaz Grafica con Python y Tkinter")

# Comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/python_icon.ico')

# Comprobar si existe un archivo no desde if
if not os.path.isfile(ruta_icono): # si no encuentra esta ruta quiero que me cargue una ruta alternativa...
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/python_icon.ico')

# Icono de la Ventana.
#ventana.iconbitmap('./21-tkinter/imagenes/python_icon.ico')
ventana.iconbitmap(ruta_icono)

# Mostrar texto en el programa
texto = Label(ventana,text= ruta_icono )
texto.pack() # Esto es para empaquetar el texto en la ventana de la ruta de la imagen}

# Cambio en el tamaño de la venta
ventana.geometry('750x450')

# Bloquear el tamaño de la venta.
ventana.resizable(0,0)

# Arrancar y mostrar la ventana hasta que se cierre (es impotante que este metodo sea el ultimo)
ventana.mainloop()

"""------------------------"""
""" SI ejecutamos el programa desde consola y no! desde visual studio codo nos arrojara un erro, informandonos que no encontrara algunos
 archivos, en este ejemplo desde consola no reconoce y no carga las imagenes de iconos, entonces lo que toca hacer es devolverse desede
 una carpeta antes y ejecutarla comun icorriente ejemplo"""
 # No ejecuta de esta manera desde consola
 #/Desktop/Proyectos/Master-python/21-tkinter/py 01-ventana.py

 # EJecutra desde consola
# Desktop/Proyectos/Master-python/py 21-tkinter/01-ventana.py

""" PAra que nos funciones desde las dos formar hay que utilizar una libreria que ya utilizamos anteriormente en la carpeta 14-sistemas-archivos
 para eso tenemos que utilizar la libreria os.path"""