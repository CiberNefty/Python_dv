from tkinter import *

ventana = Tk()
ventana.geometry('800x300')
encabezado = Label(ventana, text='Formularios 2')#.pack()
encabezado.config(
    padx=15,
    pady=15,
    fg='white',
    background='green',
    font=('Consolas', 20)
)#.pack()
#encabezado.pack(anchor=N, side=TOP,fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones Checkboxe
def mostrarProfesion():
    texto = ''
    if web.get(): # si esta variable da true osea si es selecionada
        texto += 'Desarrollo WEB'

    if movil.get(): # si esta variable da true osea si es selecion
        if web.get():
            texto += ' y Desarrollo Movil'
        else:
            texto += ' Desarrollo Movil'

    mostrar.config(
        text=texto,
        background='green',
        fg="white"
    )

web = IntVar() # Va a aser un dato entero.
movil = IntVar()

Label(ventana, text='¿Ha que te dedicas?').grid(row=1, column=0)
Checkbutton(
    ventana,
    text='Desarrollo Web',
    variable=web,
    onvalue=1, # Significa cuando este marcado
    offvalue=0,  # Cuando no este marcado
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text='Desarrollo Movil',
    variable=movil,
    onvalue=1,
    offvalue=0,
    command= mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons

# Option Menu

ventana.mainloop()