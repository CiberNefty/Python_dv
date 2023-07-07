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
#ventana.geometry("600x400")
ventana.minsize(600,500)
ventana.resizable(FALSE, FALSE)

def liquidar():
    label_liquidar.config(
        font=("Consola", 20),
        foreground='blue', background='white',
        pady=12, padx=175
    )
    label_liquidar.grid(row=0, column=0, columnspan=12)
    l_cedula_label.grid(row=1, column=0)
    l_cedula_entry.grid(row=1, column=1)
    l_apellidos_label.grid(row=2, column=0)
    l_apellidos_entry.grid(row=2, column=1)
    l_nombres_label.grid(row=3, column=0)
    l_nombres_entry.grid(row=3, column=1)
    l_cargo_label.grid(row=4, column=0)
    l_cargo_entry.grid(row=4, column=1)
    l_htrabajadas_label.grid(row=5, column=0)
    l_htrabajadas_entry.grid(row=5, column=1)
    l_valorHora_label.grid(row=6, column=0)
    l_valorHora_entry.grid(row=6, column=1)

    label_nomina.grid_remove()

    return True

def reporte():
    label_nomina.config(
        font=("Arial", 20),
        fg='blue', bg='white',
        pady=12, padx=175
    )
    label_nomina.grid(row=0, column=0, columnspan=12)

    label_liquidar.grid_remove()

    return True

# Variables Importantes
cedula = StringVar()
apellidos = StringVar()
nombres = StringVar()
cargo = StringVar()
htrabajadas = StringVar()
valorhoraT = StringVar()


# Campos para la pestaña (LIQUIDAR)
label_liquidar = Label(ventana, text='LIQUIDAR NOMINA')
l_cedula_label =Label(ventana, text='Cedual :')
l_cedula_entry = Entry(ventana, textvariable=cedula)
l_apellidos_label = Label(ventana, text='Apellidos :')
l_apellidos_entry = Entry(ventana, textvariable=apellidos)
l_nombres_label = Label(ventana, text='Nombres :')
l_nombres_entry = Entry(ventana, textvariable=nombres)
l_cargo_label = Label(ventana, text='Cargo :')
l_cargo_entry = Entry(ventana, textvariable=cargo)
l_htrabajadas_label = Label(ventana, text='No. Horas trabajadas:')
l_htrabajadas_entry = Entry(ventana, textvariable=htrabajadas)
l_valorHora_label = Label(ventana, text='Valor de la Hora:')
l_valorHora_entry = Entry(ventana, textvariable=valorhoraT)


# Campos para la pestaña (REPORTE)
label_nomina = Label(ventana, text='REPORTE NOMINA')



# Creamos un Menu y luego lo metemos dentro de ventana.
menu_nomina = Menu(ventana)
ventana.config(menu=menu_nomina)

liquidar()

menu_nomina.add_command(label='Liquidar Nomina', command=liquidar)
menu_nomina.add_command(label='Reporte Nomina', command= reporte)
menu_nomina.add_command(label='Exit', command=ventana.quit)

ventana.mainloop()