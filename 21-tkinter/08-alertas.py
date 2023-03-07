from tkinter import *
from tkinter import messagebox as MessageBox # Este modulo sirve para crear alertas.
ventana =Tk()
ventana.config(bd=70)


def sacarAlerta():
# Como crear alertas
    MessageBox.showinfo('Alerta', 'Soy Daniel Vera')

Button(ventana, text='Mostrar alerta!', command=sacarAlerta).pack() # Aqui estamos utilizando el comando que reconocera como metodo y colocamos el nombre de nuestra funcion sin los parentesis por que se ejecuta solo sin yo llamarlo.

ventana.mainloop()