"""Liquidar Nomina y Reporte de Nomina sin conexciona DB

User: Cybernefty
by: Daniel Santiago Vera Arias

Este proyecto contrendra:
- calculos
- ingreso de datos
- Guardado de dato
- Mensaje de dialogos
- Valores de las operaciones
"""
"""import os
import sys
import time
import datetime
import logging"""
from tkinter import *

ventana = Tk()
ventana.title('NOMINA en Tkinter')
ventana.geometry("600x400")


# Creamos un Menu y luego lo metemos dentro de ventana.
menu_nomina = Menu(ventana)
ventana.config(menu=menu_nomina)

# |SubMenu|
subliquidar_nomina = Menu(menu_nomina, tearoff=0)
subliquidar_nomina.add_command(label='Hola mundo')
subliquidar_nomina.add_command(label='Salir', command= quit)

menu_nomina.add_cascade(label='Liquidar Nomina', menu= subliquidar_nomina)
menu_nomina.add_command(label='Reporte Nomina')
menu_nomina.add_command(label='Exit', command=ventana.quit)

ventana.mainloop()