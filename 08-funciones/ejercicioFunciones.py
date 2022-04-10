#       EJERCICIOS # 1
# Crear una funcion sin paramtreo que imprima el nombre 
# de todos los stakeholders de un equipo de trabajo.
"""
def stakeholders():
    print("Lider del proyecto\n")
    print("Analista/Ingeniero de Requisitos")
    print("Arquitecto/Ingeniero de Sistemas")
    print('Ingeniero de Software/Programador')
    print('Asegurador de Calidad/QA')
    print("Administrador de Bases de datos\n")

def stakeholders_fueraDelProyecto():
    print("Cliente")
    print("Usuario")

stakeholders()
stakeholders_fueraDelProyecto() """

#       EJERCICIO # 2
""" Una emprea de TI requiere saber el nombre y el cargo de cada empleado 
que pertenezca al proyect X, mostrar por pantalla nombre y cargo, realizar
ejercicio por medio de una funcion donde evalue cada cargo, si no pertenece 
proyect X decir que no pertenece.

Este ejercicio debe evaluar los roles principales de un proyecto de TI
"""

def stakeholders_fueraDelProyecto():
    #if rol == 'cliente':
        print("ClientE")
    #else:
        print("Usuario")

def stakeholders(nombre,rol):
    print("ROL de proyecto")
    if rol == "Lider de proyecto":
        print(f"{nombre}, eres {rol}.")
    elif rol == "Ingeniero de requisitos":
         print(f"{nombre}, eres {rol}.")
    elif rol == "Ingeniero de sistemas":
         print(f"{nombre}, eres {rol}.")
    elif rol == "Programador":
         print(f"{nombre}, eres {rol}.")
    elif rol == "QA":
         print(f"{nombre}, eres {rol}.")
    elif rol == "Administrador de bases de datos":
         print(f"{nombre}, eres {rol}.")
    else:
        print(f"{nombre}, no perteneces al departamento de TI encargado de realiza el proyect X.")
    
    if rol == "usuario" or  rol == "cliente":
        print("\nPero es parte del pryecto y eres un:")
        stakeholders_fueraDelProyecto()

# stakeholders("Kate", "QA") 
# nombre= input("\nIngresa tu nombre: ")
# rol= input("Que rol tienes en la empresa: ")
#stakeholders(nombre,rol)
# --------------------------------
