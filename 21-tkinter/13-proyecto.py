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
ventana.geometry('400x400')
ventana.title('Programa Tkinter - Python DV')
ventana.resizable(0,0) # O puede ser  (FALSE,FALSE)

# PANTALLAS
# van hacer metodos el los cuales me mostrara otro tipo de pantallas
def home(): 
    home_label.config(
        foreground= 'white',
        background= 'Black',
        font= ('Arial', 20),
        padx=157,
        pady=15
    )
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas.
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add(): 
    # Encabezado
    add_label.config(
        foreground= 'white',
        background= 'Black',
        font= ('Arial', 20),
        padx=70,
        pady=15
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario
    add_name_label.grid(row=1, column=0, padx= 5, pady=5, sticky= E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx= 5, pady=5, sticky= E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W) 
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=N)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=('Consolas', 12),
        padx=15, pady=15
    )

    add_separator.grid(row=4)
    
    boton.grid(row=5, column=1, sticky= N)
    boton.config(
        padx=15, pady=5,
        background='Green',
        fg='white'
    )
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
        padx=105,
        pady=15
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas.
    home_label.grid_remove()
    add_label.grid_remove()

    return True

# Variablees Importantes
name_data = StringVar()
price_data = StringVar()

# Definimos campos de pantalla (INICIO)
home_label = Label(ventana, text='INICIO')

# Definimos campos de pantalla (ADD)
add_label = Label(ventana, text='AÑADIR PRODUCTO')
    # Campos del fomulario
add_name_label= Label(ventana, text='Nombre :')
add_name_entry= Entry(ventana, textvariable= name_data)

add_price_label= Label(ventana, text='Precio :')
add_price_entry= Entry(ventana, textvariable= price_data)

add_description_label= Label(ventana, text='Descripcion :')
add_description_entry= Text(ventana)

add_separator= Label(ventana)

boton = Button(ventana, text='Guardar')

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