"Vamos hacer una practica hacerca de los posicionamientos de los elementos de una pantalla"

from tkinter import *

ventana = Tk()
#ventana.geometry('700x500')

# Vamos a intentar cargar varios textos con el objeto label.
texto = Label(ventana, text = 'Bienvenido a mi programa')#.pack()
# Manipular texto. en el orden que queramos.
texto.config(
            fg='white', # Color de texto.
            bg= '#000000',# Fondo de texto,
            padx=50, # Margen en X
            pady=20, # Margen en Y
            font=('Consola', 30)# Es el tipado de fuente de letra.
)
# PAra mostrar mi texto tengo que empaquetarlo
#texto.pack() # Esto es para directamente me lo cargue en la ventana.
texto.pack(side=TOP, fill=X, expand=YES) # TOP - RIGHT - LEFT - BOTTOM


texto = Label(ventana, text = 'Soy Daniel Vera')
texto.config(
    #width=10,
    height=3,
    bg='Orange',
    font=('Arial', 18),
    padx=10, # Margen en X
    pady=20, # Margen en Y
    cursor='spider' # cada vez que me pare encima de este objeto me cambiara el cursor
)
#texto.pack(side = TOP, expand= True)
texto.pack(side = TOP, fill= X ,expand= YES)


texto = Label(ventana, text = 'Basico 1')
texto.config(
    #width=10,
    height=3,
    bg='#FFCEEF',
    font=('Arial', 18),
    padx=10, # Margen en X
    pady=20, # Margen en Y
    cursor='Circle' 
)
texto.pack(side=LEFT, expand= YES, fill = X)

texto = Label(ventana, text = 'Basico 2')
texto.config(
    #width=10,
    height=3,
    bg='#BBFBF3',
    font=('Arial', 18),
    padx=10, # Margen en X
    pady=20, # Margen en Y
    cursor='Circle' 
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = 'Basico 3')
texto.config(
    #width=10,
    height=3,
    bg='#F8FBBB',
    font=('Arial', 18),
    padx=10, # Margen en X
    pady=20, # Margen en Y
    cursor='Spider' 
)
texto.pack(side=LEFT, fill=X, expand=YES)

# Ahora cargamos el mainloop para que se muestre.
ventana.mainloop()