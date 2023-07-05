"""
Crear un programa que tenga:
- Una ventana
- Tamaño fijo
- Ventana no redimensionable
- Un Menu
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados de la pantalla home
- Opcion de salir
"""
from tkinter import *

ventana = Tk()
ventana.geometry('600x500')
ventana.title('Programa con Tkinter')

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Crearemos un submenu.
archivo = Menu(mi_menu, tearoff= 0)
archivo.add_command(label='Nuevo archivo de texto')
archivo.add_command(label='Nuevo archivo')
archivo.add_command(label='Nueva ventana')

editar = Menu(mi_menu, tearoff = 0)
editar.add_command(label='Deshacer')
editar.add_command(label='Rehacer')
editar.add_separator()
editar.add_command(label='Cortar')
# Submenu para editar
subEditar = Menu(editar, tearoff= 0)
subEditar.add_command(label='Buscar')
subEditar.add_command(label='Remplazar')

editar.add_cascade(label='Configuracion', menu= subEditar)
editar.add_command(label='Pegar')

seleccion = Menu(mi_menu, tearoff = 0)
seleccion.add_command(label='Seleccionar todo')
seleccion.add_command(label='Expandir seleccion')
seleccion.add_command(label='Reducir Seleccion')

mi_menu.add_cascade(label='Archivo', menu=archivo)
mi_menu.add_cascade(label='Editar', menu = editar)
mi_menu.add_cascade(label='Seleccion', menu = seleccion)


ventana.mainloop()