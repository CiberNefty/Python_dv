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
#
print("\n\t\tEJERCICIO # 3")
def tabla_multiplicar(numero):
    print(f"table del {numero}")
    
    for i in range(11):
        operacion = str(numero) + " X "+ str(i)+" = "+ str(numero * i)
        #print(operacion)
        oper = numero * i
        print(f"{numero} x {i} = {oper}") # Esta es mas lejible de leer

def tabla_multiplicarWhile(numero):
    contador = 1
    while contador != 0 and contador <= numero:
        oper = numero * contador
        print(f"{numero} x {contador} = {oper}")
        contador = contador + 1


# tabla_multiplicar(2)
#numero = int(input("Ingresa numero a multiplicar: "))
#tabla_multiplicarWhile(numero)
#for ntabla in range(1,11):
    #tabla_multiplicar(ntabla)
    print("\n")
# --------------------------------  
#       EJERCICIO 4
# Crear un funcion que imprima las tablas de multiplicar 
# que el usuario escoja.
print("\n\t\tEJERCICIO # 4")

def getTablas(numMin = False, numLimit= False):
    for i in range (numMin, numLimit):
        oper = numMin * i
        print(f"{numMin} X {i} = {oper}")

getInput = "d"
while getInput != "N":
    numMin = int(input("Ingresa valor para la tabla: "))
    numLimit = int(input("Cuantas veces quiere que recorra la tabla?: "))

    if numMin != numLimit:
        getTablas(numMin,numLimit)
    
    evaluar = input("Quiere seguir viendo tablas?\n escriba Si o No: ")
    if evaluar == "No":
        # break  
        getInput = "N" #De esta manera puedo interrumpir un programa 
