"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operacion
- Mostrar el resultado
"""
from tkinter import *
from tkinter import messagebox

class Calculadora:
    
    # Tenemos que agregaar un contructor para asisgnar un valor a nuestras propiedades.
    def __init__(self, alertas):
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas    
    # Para que no tenga que capturar los errores en cada funcion puedo hacer lo siguiente:
    def convertirFloat(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror('Error', 'Introduce bien los datos')

        return result

    def sumar(self):
        # try:
        # Como es un stringvar tengo que usar el metodo set y de hay paso la operacion que vaya hacer.
        # Con esto sacamos los numeros que hay en num1 y num2 con get luego como de texto String los convertimos en algun nuemero.
        self.resultado.set(self.convertirFloat(self.num1.get()) + self.convertirFloat(self.num2.get()))
        self.mostrarResultado()
    #    except:
    #        MessageBox.showerror('Error','Introduce bien los datos')
    #        num1.set("")
    #        num2.set("")

    def restar(self):
        self.resultado.set(self.convertirFloat(self.num1.get()) - self.convertirFloat(self.num2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.convertirFloat(self.num1.get()) * self.convertirFloat(self.num2.get()))
        self.mostrarResultado()

    def division(self):
        self.resultado.set(self.convertirFloat(self.num1.get()) / self.convertirFloat(self.num2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        messagebox.showinfo('Resultado', f'EL resultado es: {self.resultado.get()}')
        # Cuando se ejecute este metodo al utilizar el set le estamos danto un valor de nada, entonces nos da el mensaje y cambia los valores a nada.
        self.num1.set("")
        self.num2.set("")

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | DV")
ventana.geometry('280x250')
ventana.config(bd=15)

#Creamos nuestro objeto para acceceder a las propiedades de nuestra clase calculadora y le agregamos nuestro messagebox.
calculadora = Calculadora(messagebox)

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

# ya la variable vinculada a los campos no es una variable, sino que es la propiedad de un objeto (objeto.num1)
Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=calculadora.num1, justify=CENTER).pack()

# ya la variable vinculada a los campos no es una variable, sino que es la propiedad de un objeto (objeto.num2)
Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=calculadora.num2, justify=CENTER).pack()

Label(marco, text="").pack()  # Este la label nos da un espacio.

# Lo mismo con los metodos, ya no son metodos, ahora pertenecen a un objeto de una clase (Objeto.metodos)
Button(marco, text='Suma', command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Restar', command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Multiplicar', command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Dividir', command=calculadora.division).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()