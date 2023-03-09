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

def sumar():
    # Como es un stringvar tengo que usar el metodo set y de hay paso la operacion que vaya hacer.
    resultado.set(float(num1.get()) + float(num2.get())) # Con esto sacamos los numeros que hay en num1 y num2 con get luego como de texto String los convertimos en algun nuemero.
    mostrarResultado()

def restar():
    resultado.set(float(num1.get()) - float(num2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(num1.get()) * float(num2.get()))
    mostrarResultado()

def division():
    resultado.set(float(num1.get()) / float(num2.get()))
    mostrarResultado()

def mostrarResultado():
    MessageBox.showinfo('Resultado', f'EL resultado de la operacion es: {resultado.get()}')
    num1.set("") # Cuando se ejecute este metodo al utilizar el set le estamos danto un valor de nada, entonces nos da el mensaje y cambia los valores a nada.
    num2.set("")

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

label1 = Label(marco, text="").pack() # Este la label nos da un espacio.

Button(marco, text='Suma', command = sumar).pack(side='left',fill=X, expand=YES)
Button(marco, text='Restar', command= restar).pack(side='left',fill=X, expand=YES)
Button(marco, text='Multiplicar', command = multiplicar).pack(side='left',fill=X, expand=YES)
Button(marco, text='Dividir', command= division).pack(side='left',fill=X, expand=YES)

ventana.mainloop()