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
ventana.geometry('280x250')
ventana.config(bd=15)

# Para que no tenga que capturar los errores en cada funcion puedo hacer lo siguiente:
def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        MessageBox.showerror('Error', 'Introduce bien los datos')

    return result

def sumar():
    # try:
    # Como es un stringvar tengo que usar el metodo set y de hay paso la operacion que vaya hacer.
    # Con esto sacamos los numeros que hay en num1 y num2 con get luego como de texto String los convertimos en algun nuemero.
    resultado.set(convertirFloat(num1.get()) + convertirFloat(num2.get()))
    mostrarResultado()
#    except:
#        MessageBox.showerror('Error','Introduce bien los datos')
#        num1.set("")
#        num2.set("")

def restar():
    resultado.set(convertirFloat(num1.get()) - convertirFloat(num2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convertirFloat(num1.get()) * convertirFloat(num2.get()))
    mostrarResultado()

def division():
    resultado.set(convertirFloat(num1.get()) / convertirFloat(num2.get()))
    mostrarResultado()

def mostrarResultado():
    MessageBox.showinfo(
        'Resultado', f'EL resultado de la operacion es: {resultado.get()}')
    # Cuando se ejecute este metodo al utilizar el set le estamos danto un valor de nada, entonces nos da el mensaje y cambia los valores a nada.
    num1.set("")
    num2.set("")

num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

# Vamos a crear un Frame (marco) para que todo este guardado en él.
marco = Frame(ventana, width=240, height=200)
marco.config(
    padx=10,
    pady=10,
    bd=3,
    relief=SOLID  # Esto es un borde solido
)
marco.pack(side=TOP, anchor=CENTER)
# Cuando metamos el formulario se va a deformar entonces tenemos que utlizar pack_propagate con valor de False para que no se deforme.
# Entonce para meter el formulario en el Frame toca es en vez de ejecutar los label y los button en la ventana toca es meterlos al frame (marco).
marco.pack_propagate(False)

Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=num1, justify='center').pack()

Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=num2, justify='center').pack()

label1 = Label(marco, text="").pack()  # Este la label nos da un espacio.

Button(marco, text='Suma', command=sumar).pack(side='left', fill=X, expand=YES)
Button(marco, text='Restar', command=restar).pack(
    side='left', fill=X, expand=YES)
Button(marco, text='Multiplicar', command=multiplicar).pack(
    side='left', fill=X, expand=YES)
Button(marco, text='Dividir', command=division).pack(
    side='left', fill=X, expand=YES)

ventana.mainloop()