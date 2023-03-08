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
marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief= SOLID # Esto es un borde solido
)
marco.pack(side=TOP, anchor=CENTER) 
# Cuando metamos el formulario se va a deformar entonces tenemos que utlizar pack_propagate con valor de False para que no se deforme.
# Entonce para meter el formulario en el Frame toca es en vez de ejecutar los label y los button en la ventana toca es meterlos al frame (marco).
marco.pack_propagate(False)

Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=num1, justify='center').pack()

Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=num2,justify='center').pack()

label1 = Label(marco, text="").pack()

Button(marco, text='Suma').pack(side='left',fill=X, expand=YES)
Button(marco, text='Restar').pack(side='left',fill=X, expand=YES)
Button(marco, text='Multiplicar').pack(side='left',fill=X, expand=YES)
Button(marco, text='Dividir').pack(side='left',fill=X, expand=YES)

ventana.mainloop()