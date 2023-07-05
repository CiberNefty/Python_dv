"""
Crear un programa que tenga:
(hecho) - Una ventana
(hecho) - Tamaño fijo
(hecho) - Ventana no redimensionable [funcion: resizable()]
(hecho) - Un Menu (Inicio, Añadir, Informacion, Salir)
(hecho) - Opcion de salir
(hecho) - Diferentes pantallas [Ocultar pantallas con la función grid_remove()]
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados de la pantalla home

"""
from tkinter import *

# Definimos ventana
ventana = Tk()
ventana.geometry('500x500')
ventana.title('Programa Tkinter - Python DV')
ventana.resizable(False,False) # O puede ser  (0,0)

# PANTALLAS
# van hacer metodos el los cuales me mostrara otro tipo de pantallas
def home(): 
    home_label.config(
        foreground= 'white',
        background= 'Black',
        font= ('Arial', 20,'bold'),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas.
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add(): 
    add_label.config(
        foreground= 'white',
        background= 'Black',
        font= ('Arial', 20,'bold'),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)

    # Ocultar otras pantallas.
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True


def info():
    info_label.config(
        foreground= 'white',
        background= 'Black',
        font= ('Arial', 20,'bold'),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas.
    home_label.grid_remove()
    add_label.grid_remove()

    return True

# Definimos campos de pantalla (INICIO)
home_label = Label(ventana, text='INICIO')

# Definimos campos de pantalla (ADD)
add_label = Label(ventana, text='AÑADIR PRODUCTO')

# Definimos campos de pantalla (INFO)
info_label = Label(ventana, text='INFORMACION')
data_label = Label(ventana, text='Creado por Daniel Vera en 06-2023')


# Cargamos la pantalla de inicio
home()

# Definimos el Menu superior
menu_Padre = Menu(ventana)
menu_Padre.add_cascade(label='Inicio', command=home)
menu_Padre.add_cascade(label='Añadir', command= add)
menu_Padre.add_cascade(label='Información', command= info)
menu_Padre.add_command(label='Salir', command = quit)

# Cargar Menu
ventana.config(menu = menu_Padre)

# Cargamos ventana para que abra.
ventana.mainloop()