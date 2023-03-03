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

# Label para el campo de texto (nombre)
label = Label(ventana, text="Nombres:")
label.grid(row=1,column=0, padx=5, pady=5)

# Campo de texto (Objeto Entry) (nombre)
campo_texto = Entry(ventana) #vamos a cargar nuestro objeto entry(campo_texto) en ventana.
#campo_texto.pack(side=LEFT, anchor=W) # Ahora empaquetamos el texto.
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5) # COn esto posicionamos lo que seria el campo de texto con el objeto grid que recibe estos parametros.
campo_texto.config(justify="left", state='normal')

# Label para el campo de texto (apellidos)
label = Label(ventana, text="Apellidos:")
label.grid(row=2,column=0, padx=5, pady=5)

# Campo de texto (Objeto Entry) (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state='disabled') # Esto es para decir desde donde comience el texto y que el campo de texto este bloqueado

# Label para el campo de texto (apellidos)
label = Label(ventana, text="Descripcion:")
label.grid(row=3,column=0, padx=5, pady=5, sticky=NW)

campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height=5,
    font=('Arial', 12),
    padx=15, pady=15
)

ventana.mainloop()