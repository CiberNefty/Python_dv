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
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title('NOMINA en Tkinter')
#ventana.geometry("600x400")
ventana.minsize(600,320)
ventana.resizable(TRUE, FALSE)

def liquidar():
    label_liquidar.config(font=("Consola", 20),foreground='blue', background='white', pady=12, padx=175)
    label_liquidar.grid(row=0, column=0, columnspan=3)
    
    frame_liquidar.grid(row=1,pady=2, padx=100)

    btn_Cacular_liquid.grid(row=13, column=0, pady=8,padx=8)
    btn_Cacular_liquid.config(font=("Arial", 10, 'bold'),fg='white', bg='green')
    btn_Guardar_liquid.grid(row=13, column=1, pady=3, padx=8, sticky=W)
    btn_Guardar_liquid.config(font=("Arial", 10, 'bold'), fg='black', bg='lavender')

    label_nomina.grid_remove()
    info_nomina_box.grid_remove()

    return True

def reporte():
    label_nomina.config(font=("Arial", 20), fg='blue', bg='white', pady=12, padx=650)
    label_nomina.grid(row=0, column=0, columnspan=11, sticky=W)
    Label(ventana, text='').grid(row=1)
    info_nomina_box.grid(row=2, column=0)

    # Listar Productos
    """for datos in datos_nomina:
        if len(datos) == 11:
            Label(info_nomina_box, text= datos[0]).grid()
            Label(info_nomina_box, text=datos[1]).grid()
            Label(info_nomina_box, text=datos[2]).grid()
            datos.append('addedd')
            Label(info_nomina_box, text='---------------------').grid()"""
    
    for datos in datos_nomina:
        if len(datos) == 11:
            datos.append('addedd')
            tree_box.insert('', tk.END, values=datos)

    label_liquidar.grid_remove()
    frame_liquidar.grid_remove()

    return True

def add_info():
    datos_nomina.append([
        cedula.get(),
        apellidos.get(),
        nombres.get(),
        cargo.get(),
        htrabajadas.get(),
        valorhoraT.get(),
        totalDevengado.get(),
        descuentoSalud.get(),
        descuentoPension.get(),
        totalDeducidos.get(),
        totalApagar.get()
    ])

    cedula.set('')
    apellidos.set('')
    nombres.set('')
    cargo.set('')
    htrabajadas.set('')
    valorhoraT.set('')
    totalDevengado.set('')
    descuentoSalud.set('')
    descuentoPension.set('')
    totalDeducidos.set('')
    totalApagar.set('')

    label_liquidar.grid_remove()
    frame_liquidar.grid_remove()

    reporte()

def calcular():
    totalDevengado.set(int(htrabajadas.get()) * int(valorhoraT.get()))
    descuentoSalud.set(totalDevengado.get() * 0.04)
    descuentoPension.set(totalDevengado.get() * 0.04)
    totalDeducidos.set(descuentoSalud.get() + descuentoPension.get())
    totalApagar.set(totalDevengado.get() - totalDeducidos.get())

    return True
# Variables Importantes
datos_nomina = [] # Esta variable es para guardar los datos
cedula = StringVar()
apellidos = StringVar()
nombres = StringVar()
cargo = StringVar()
htrabajadas = StringVar()
valorhoraT = StringVar()
totalDevengado = IntVar()
descuentoSalud = IntVar()
descuentoPension = IntVar()
totalDeducidos = IntVar()
totalApagar = IntVar()


# Campos para la pestaña (LIQUIDAR)
label_liquidar = Label(ventana, text='LIQUIDAR NOMINA')

# Frame para guardar todos estos campos.
frame_liquidar = Frame(ventana)

l_cedula_label =Label(frame_liquidar, text='Cedual :')
l_cedula_entry = Entry(frame_liquidar, textvariable=cedula)
l_apellidos_label = Label(frame_liquidar, text='Apellidos :')
l_apellidos_entry = Entry(frame_liquidar, textvariable=apellidos)
l_nombres_label = Label(frame_liquidar, text='Nombres :')
l_nombres_entry = Entry(frame_liquidar, textvariable=nombres)
l_cargo_label = Label(frame_liquidar, text='Cargo :')
l_cargo_entry = Entry(frame_liquidar, textvariable=cargo)
l_htrabajadas_label = Label(frame_liquidar, text='No. Horas trabajadas :')
l_htrabajadas_entry = Entry(frame_liquidar, textvariable=htrabajadas)
l_valorHora_label = Label(frame_liquidar, text='Valor de la Hora :')
l_valorHora_entry = Entry(frame_liquidar, textvariable=valorhoraT)
l_tDevengado_label = Label(frame_liquidar, text='Total Devengado :')
l_tDevengado_entry = Entry(frame_liquidar, textvariable=totalDevengado)
l_descuentoSalud_label = Label(frame_liquidar, text='Descuento Salud :')
l_descuentoSalud_entry = Label(frame_liquidar, textvariable=descuentoSalud)
l_descuentoPension_label = Label(frame_liquidar, text='Descuento Pensión :')
l_descuentoPension_entry = Label(frame_liquidar, textvariable=descuentoPension)
l_totalDeducidos_label = Label(frame_liquidar, text='Total Deducidos :')
l_totalDeducidos_entry = Label(frame_liquidar, textvariable=totalDeducidos)
l_totalApagar_label = Label(frame_liquidar, text='Total apagar :')
l_totalApagar_entry = Entry(frame_liquidar, textvariable=totalApagar)

btn_Cacular_liquid = Button(frame_liquidar, text='Calcular Nomina', command=calcular)
btn_Guardar_liquid = Button(frame_liquidar, text='Guardar Liquidación', command=add_info)

l_cedula_label.grid(row=2, column=0, padx=1, sticky=W)
l_cedula_entry.grid(row=2, column=1), l_cedula_entry.config(width=40)
l_apellidos_label.grid(row=3, column=0, padx=3, sticky=W)
l_apellidos_entry.grid(row=3, column=1), l_apellidos_entry.config(width=40)
l_nombres_label.grid(row=4, column=0, padx=3, sticky=W)
l_nombres_entry.grid(row=4, column=1), l_nombres_entry.config(width=40)
l_cargo_label.grid(row=5, column=0, padx=3, sticky=W)
l_cargo_entry.grid(row=5, column=1), l_cargo_entry.config(width=40)
l_htrabajadas_label.grid(row=6, column=0, padx=3, sticky=W)
l_htrabajadas_entry.grid(row=6, column=1), l_htrabajadas_entry.config(width=40)
l_valorHora_label.grid(row=7, column=0, padx=3, sticky=W)
l_valorHora_entry.grid(row=7, column=1), l_valorHora_entry.config(width=40)
l_tDevengado_label.grid(row=8, column=0, padx=3, sticky=W)
l_tDevengado_entry.grid(row=8, column=1), l_tDevengado_entry.config(width=40, background='#CCCCCC', state='disabled')
l_descuentoSalud_label.grid(row= 9, column=0, padx=3, sticky=W)
l_descuentoSalud_entry.grid(row=9, column= 1), l_descuentoSalud_entry.config(width=34, background='#DEDEDE', state='disabled', anchor=W) # El anchor no sirve con ENTRY
l_descuentoPension_label.grid(row=10, column= 0, padx=3, sticky=W)
l_descuentoPension_entry.grid(row=10, column=1, sticky=N), l_descuentoPension_entry.config(width=34, background='#CCCCCC', anchor=W) # este es un LABEL que era antes ENTRY
l_totalDeducidos_label.grid(row=11, column=0, padx=3, sticky=W)
l_totalDeducidos_entry.grid(row=11, column=1, sticky=N), l_totalDeducidos_entry.config(width=34, background='#DEDEDE', anchor=W) # este es un LABEL que era antes ENTRY
l_totalApagar_label.grid(row=12, column=0, padx=3, sticky=W)
l_totalApagar_entry.grid(row=12, column=1), l_totalApagar_entry.config(width=40, background='#CCCCCC', state='disabled') # El STATE sirve para desabilitar campos ENTRY


# Campos para la pestaña (REPORTE)
label_nomina = Label(ventana, text='REPORTE NOMINA')
info_nomina_box = Frame(ventana, width= 250)

columns_reporte = ('Cedula','Apellido','Nombre','Cargo','Hora','Valor Hora','Devengado','Salud','Pension','Deducidos','Neto a Pagar')

tree_box = ttk.Treeview(info_nomina_box, columns=columns_reporte, show='headings')
tree_box.grid(row=1, column=0, columnspan=10, sticky= N)
tree_box.heading("#1", text='Cedula', anchor=W)
tree_box.heading("#2", text='Apellido', anchor=W)
tree_box.heading("#3", text='Nombre', anchor=W)
tree_box.heading("#4", text='Cargo', anchor=W)
tree_box.heading("#5", text='Hora', anchor=W)
tree_box.heading("#6", text='Valor Hora', anchor=W)
tree_box.heading("#7", text='Devengado', anchor=W)
tree_box.heading("#8", text='Salud', anchor=W)
tree_box.heading("#9", text='Pension', anchor=W) # No comprendo porque el tree view no me permite agregar estas tres columnas
tree_box.heading("#10", text='Deducidos', anchor=W)
tree_box.heading("#11", text='Total a Pagar', anchor=W)

# Vamos a unir Un Scrollvar
scrollbar = ttk.Scrollbar(info_nomina_box, orient=tk.VERTICAL, command= tree_box.yview)
tree_box.config(yscroll= scrollbar.set)
scrollbar.grid(row=1, column=1)

btn_devolver_liquidacion = Button(info_nomina_box, text='DEVOLVER', command= liquidar)
btn_devolver_liquidacion.config( bg='lavender', fg='darkblue', padx=5, pady=5, font=('Consolas', 15, 'bold'), border=3)
btn_devolver_liquidacion.grid(row=3, sticky=E)

# Creamos un Menu y luego lo metemos dentro de ventana.
menu_nomina = Menu(ventana)
ventana.config(menu=menu_nomina)

liquidar()

menu_nomina.add_command(label='Liquidar Nomina', command=liquidar)
menu_nomina.add_command(label='Reporte Nomina', command= reporte)
menu_nomina.add_command(label='Exit', command=ventana.quit)

ventana.mainloop()