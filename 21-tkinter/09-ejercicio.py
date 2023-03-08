"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operacion
- Mostrar el resultado
"""
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title = "Ejercicio completo con Tkinter | DV"
ventana.geometry('400x400')
ventana.config(bd=25)

num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

# Vamos a crear un Frame (marco) para que todo este guardado en él.
marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief= SOLID # Esto es un borde solido
)
marco.pack(side=TOP, anchor=CENTER)

Label(ventana, text="Primer Numero: ").pack()
Entry(ventana, textvariable=num1).pack()

Label(ventana, text="Segundo Numero: ").pack()
Entry(ventana, textvariable=num2).pack()

label1 = Label(ventana, text="").pack()

Button(ventana, text='Suma').pack(side='left')
Button(ventana, text='Restar').pack(side='left')
Button(ventana, text='Multiplicar').pack(side='left')
Button(ventana, text='Dividir').pack(side='left')

ventana.mainloop()