# Tkinter
# Es un modulo para crear interfaces graficas de usuario.

# Importamos todo de tkinter
from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = 'Master en Pytho con Tkinter'
        self.icon = './imagenes/python_icon.ico'  # Esto sera la ruta de mi logotipo
        # Esto sera la ruta alternativa de mi logotipo
        self.icon_alt = './21-tkinter/imagenes/python_icon.ico'
        self.size = '770x470'  # Este va hacer el tamaño de la ventana
        self.resizable = False  # Este va hacer por si quiero el bloqueo de tamaño de pantalla

    # Vamos a tener un metodo que se llamara cargar.
    def cargar(self):
            
        # Crear la ventana raiz
        ventana = Tk() # Podemos hacer que ventana sea una propiedad para compartirla
        self.ventana = ventana
        # Titulo de la ventana.
        #ventana.title("Interfaz Grafica con Python y Tkinter")
        ventana.title(self.title)
        # Comprobar si existe un archivo
        #ruta_icono = os.path.abspath('./imagenes/python_icon.ico')
        ruta_icono = os.path.abspath(self.icon)
        # Comprobar si existe un archivo no desde if
        # si no encuentra esta ruta quiero que me cargue una ruta alternativa...
        if not os.path.isfile(ruta_icono):
            #ruta_icono = os.path.abspath('./21-tkinter/imagenes/python_icon.ico')
            ruta_icono = os.path.abspath(self.icon_alt)
        # Icono de la Ventana.
        # ventana.iconbitmap('./21-tkinter/imagenes/python_icon.ico')
        ventana.iconbitmap(ruta_icono)
        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()  # Esto es para empaquetar el texto en la ventana de la ruta de la imagen}
        # Cambio en el tamaño de la venta
        "ventana.geometry('750x450')"
        ventana.geometry(self.size)
        # Bloquear el tamaño de la venta.
        if self.resizable: # Si esto es True me permitira redimencionar la ventana.
            ventana.resizable(1, 1)
        else: # Y si no es verdadero llamamos al mismo metodo para que este en (0,0) para que este bloqueado.
            ventana.resizable(0,0)
        # Arrancar y mostrar la ventana hasta que se cierre (es impotante que este metodo sea el ultimo)
        #ventana.mainloop()

    # Podemos crear un metodo dentro de esta clase para añadir texto
    #def addTexto(self):
    def addTexto(self,dato):
        # Podemos crear un texto utilizando el metodo o el objeto LABEL
        #texto = Label(self.ventana, text="Hola desde un metodo [addTexto()]")
        texto = Label(self.ventana, text=dato)
        texto.pack()

    # Como el metodo mainloop() ya se ha ejecutado en otro metodo, lo recomendable seria crear otro metodo para mostrar.
    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre (es impotante que este metodo sea el ultimo)
        self.ventana.mainloop()


"""------------------------"""
""" SI ejecutamos el programa desde consola y no! desde visual studio codo nos arrojara un erro, informandonos que no encontrara algunos
 archivos, en este ejemplo desde consola no reconoce y no carga las imagenes de iconos, entonces lo que toca hacer es devolverse desede
 una carpeta antes y ejecutarla comun icorriente ejemplo"""
# No ejecuta de esta manera desde consola
# /Desktop/Proyectos/Master-python/21-tkinter/py 01-ventana.py

# EJecutra desde consola
# Desktop/Proyectos/Master-python/py 21-tkinter/01-ventana.py

""" PAra que nos funciones desde las dos formar hay que utilizar una libreria que ya utilizamos anteriormente en la carpeta 14-sistemas-archivos
 para eso tenemos que utilizar la libreria os.path"""

# AHORA SI toca crear nuestro objeto para que nos muestre por pantalla.

# INSTACIAR MI PROGRAMA
programa = Programa()
programa.cargar()
programa.addTexto("Hola que hace mi pez.")
programa.addTexto("Vamos muy bien sigue adelante")
programa.addTexto("Poco a mucho vas aprendiendo")
programa.addTexto("SOy un texto\n SOy Daniel Vera")
# Luego llamamos a nuestro metodo que mostrara todo
programa.mostrar()