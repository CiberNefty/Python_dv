" VAMOS A TRABAJAR CON IMAGENES "
from tkinter import *
from PIL import Image, ImageTk # Vamos a importar dos librerias una seria (Image) para cargar la imagen y la otra (ImageTK) que es el que me va a permitir cargar la imagen dentro de un Tkinter

ventana = Tk()
ventana.geometry('700x500')

# para utilizar imagenes puedo utilizar metodos que trae Tkinter que sirven pero tienen varias limitaciones Ó 
# podemos utilizar un modulo que se llama (PILLOW PIL)
'Documentacion: https://pillow.readthedocs.io/en/stable/'
# Instalar el modulo
'https://pypi.org/project/Pillow/'
 
Label(ventana, text="#Hola, Soy daniel#").pack(anchor=W)

# Cargar Imagen
imagen = Image.open('./21-tkinter/imagenes/Lobo1.jpg')

# Ya que tengo la imagen recogida tenemos que renderizarla
render = ImageTk.PhotoImage(imagen)

# Ahora tenemos que cargar la imagen dentro de la ventana y luego en un Label.
Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()