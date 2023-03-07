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
ventana.config(bd=25)

num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

Label(ventana, text="Primer Numero: ").pack()
Entry(ventana, textvariable=num1).pack()

Label(ventana, text="Segundo Numero: ").pack()
Entry(ventana, textvariable=num2).pack()

Button(ventana, text='Suma', command=lambda:suma(num1, num2)).pack(anchor=NW)
Button(ventana, text='Restar').pack(anchor=NE)
Button(ventana, text='Multiplicar').pack(anchor=SW)
Button(ventana, text='Dividir').pack(anchor=SE)

ventana.mainloop()