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
encabezado.pack(anchor=N, side=TOP,fill=X, expand=YES)

# Botones Checkboxe

# Radio buttons

# Option Menu

ventana.mainloop()