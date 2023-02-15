# Tkinter
# Es un modulo para crear interfaces graficas de usuario.

 # Importamos todo de tkinter
from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana.
ventana.title("Interfaz Grafica con Python y Tkinter")

# Icono de la Ventana.
ventana.iconbitmap('./21-tkinter/imagenes/python_icon.ico')

# Cambio en el tamaño de la venta
ventana.geometry('750x450')

# Bloquear el tamaño de la venta.
ventana.resizable(0,0)

# Arrancar y mostrar la ventana hasta que se cierre (es impotante que este metodo sea el ultimo)
ventana.mainloop()