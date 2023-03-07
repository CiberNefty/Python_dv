from tkinter import *
from tkinter import messagebox as MessageBox # Este modulo sirve para crear alertas.
ventana =Tk()
ventana.config(bd=70)


def sacarAlerta():
# Como crear alertas
    MessageBox.showinfo('¡Alerta! Info', 'Soy Daniel Vera')
    #MessageBox.showerror('¡Alerta! Error', 'Soy Daniel Vera')
    #MessageBox.showwarning('¡Alerta! Warning', 'Soy Daniel Vera')

Button(ventana, text='Mostrar alerta!', command=sacarAlerta).pack() # Aqui estamos utilizando el comando que reconocera como metodo y colocamos el nombre de nuestra funcion sin los parentesis por que se ejecuta solo sin yo llamarlo.

def salir(nombre):
    resultado = MessageBox.askquestion('Salir', '¿Quieres continuar ejecutando la aplicacion?')

    if resultado != 'yes':
        MessageBox.showinfo('Good Bay', f'Adios {nombre}')
        ventana.destroy() # este metodo me permite cerrar la ventana.

Button(ventana, text='Salir', command= lambda: salir('Daniel Vera')).pack() # Cuando yo utilizo la funcion lambda en un comando se refiere es que caundo haga click en ell boton se ejecute la funcion.
ventana.mainloop()