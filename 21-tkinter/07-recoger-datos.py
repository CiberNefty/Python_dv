from tkinter import *

ventana = Tk() 
ventana.geometry('700x700')
ventana.config(
    bd=50, # Esto tendra un borde transparente de 50 pixeles
)

def getDato():
    resultado.set(dato.get()) # Aquí le metemos el dato que esta dentro de dato

    if len(resultado.get()) >= 1:
        texto_recogido.config(
        bg = 'green',
        fg ='white'
        )

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW) # Vamos a utilizar el objeto ENtry para meter un campo de texto, y textvariable es para recoger textos.

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)

texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)

ventana.mainloop()