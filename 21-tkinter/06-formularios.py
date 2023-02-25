from tkinter import *

ventana = Tk()
ventana.geometry('700x400')
ventana.title('FORMULARIOS')

# Texto encabezado
encabezado = Label(ventana, text='Formularios con Tkinter - Daniel Vera')
encabezado.config(
    fg='white',
    bg='darkgray',
    font=('Open Sans', 18),
    padx=10,
    pady=10
)
"Como estamos utilizando pack() para empaquetar objetos, al utilizar grid no vamos a poder por utilizar pack entonces toca remplazar el pack por grid"
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=True)
encabezado.grid(row=0, column=0, columnspan=12,sticky=W) # El parametro sticky es para pegar y podemos utilizar los mismos paramtros de sticky

# Label para el campo de texto
label = Label(ventana, text="Nombre:")
label.grid(row=1,column=0, sticky=W, padx=5, pady=5)

# Campo de texto (Objeto Entry)
campo_texto = Entry(ventana) #vamos a cargar nuestro objeto entry(campo_texto) en ventana.
#campo_texto.pack(side=LEFT, anchor=W) # Ahora empaquetamos el texto.
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5) # COn esto posicionamos lo que seria el campo de texto con el objeto grid que recibe estos parametros.


ventana.mainloop()