from tkinter import *

ventana = Tk()
ventana.title("Menus")
ventana.geometry("500x500")

# creamos una variable y guardamos el objeto Menu
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Esto seria un submenu
archivo = Menu(mi_menu, tearoff=0) # El parametro tearoff sirve para aleminar la linea que genera por defecto.
archivo.add_command(label='New File')
archivo.add_command(label='New Window')
archivo.add_separator() # Aqui le agregamos un separador que parece una linea
archivo.add_command(label='Open File')
archivo.add_command(label='Open Folder')
archivo.add_separator()
archivo.add_command(labe='Salir', command= ventana.quit) # Aqui agregamos la funcion de comando que llame a la ventana princiipal y luego genere la funcion de quit quees para salir.

# Agregamos a nuestro objeto Menu un comando.
mi_menu.add_cascade(label='Archivo', menu=archivo)
mi_menu.add_command(label='Editar')
mi_menu.add_command(label='Seleccion')


ventana.mainloop()