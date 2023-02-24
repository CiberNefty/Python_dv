from tkinter import *

ventana = Tk()
ventana.title('Marcos | Master en python')
ventana.geometry('700x700')

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor= N, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250) #El objeto Frame indicamos donde vamos a cargar nuestro marco
marco.config( # Tenemos que agregarle unos estilos para poder observar
    bg='red',
    bd=5, # Borde
    relief=SOLID #(Podemos colocarlo o con la constante relief='solid') Podemos agregarle otros tipos de relieve como (flat, groove, raised, ridge, solid, suken)
    ) 
marco.pack(side=LEFT, anchor='sw')

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='green',
    bd=5,
    relief=SOLID 
    ) 
marco.pack(side=RIGHT, anchor='se')

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='blue',
    bd=5,
    relief=SOLID
    ) 
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='orange',
    bd=5,
     relief=SOLID 
    ) 
marco.pack(side=RIGHT)






ventana.mainloop()