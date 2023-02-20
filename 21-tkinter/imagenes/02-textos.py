from tkinter import *

ventana = Tk()
ventana.geometry('700x500')

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
texto.pack() # Esto es para directamente me lo cargue en la ventana.

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
texto.pack(anchor=E) # Mover texto

texto = Label(ventana, text = 'Trabajando con Master Python')
texto.config(
    #width=10,
    height=3,
    bg='red',
    font=('Arial', 18),
    padx=10, # Margen en X
    pady=20, # Margen en Y
    cursor='Circle' 
)
texto.pack(anchor=NW)

# Ahora cargamos el mainloop para que se muestre.
ventana.mainloop()