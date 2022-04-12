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
    #numMin = int(input("Ingresa valor para la tabla: "))
    #numLimit = int(input("Cuantas veces quiere que recorra la tabla?: "))

    #if numMin != numLimit:
        #getTablas(numMin,numLimit)
    
    #evaluar = input("Quiere seguir viendo tablas?\n escriba Si o No: ")
    #if evaluar == "No":
        # break  
        getInput = "N" #De esta manera puedo interrumpir un programa 
# --------------------------------
#       EJERCICIO 5
# Ejercicio donde le pida el nombre y por medio de una funcion le retorne una historia dependiendo 
# de si el primer caracter sea una letra en especifico.
print("\n\t\tEJERCICIO # 5")
def historia(nombre):
    his1 = f"""    El dia que {nombre} entro a la universidad se percato,
    que su vida cambiaria de la noche a la mañana, transcurrido el
    el primer semestre noto que muchos de los estudiantes desertaron. """
    his2 = f"""    Luego {nombre} de haber curzado tanto tiempo solo en la u sintio
    que le hacia falta estar con una mujer, con lo cual tuvo que pagar por una 
    rato de intimidad."""
    his3 = f"""    Los primeros y utlimos semestres son los mejores, por que te das
    cuenta que solo es cuestion de atencion en lo que haces y te propones, dentro
    de poco Dios cambiara mi vida, empezare a trabajar para una empresa de TI y
    estare disfrutando mi puesto, por que se que me lo merezco."""
    """
    if nombre == 'Daniel':
        return his1
    elif nombre == 'Juan':
        return his2
    elif nombre = 'Felipe':
        return his3
    else:
        print(f"{nombre} no cuenta para una historia.") """

print(historia("Daniel"))
#-------------------------------
"""     EJERCICIO 6
Crear funcion que evalue de que continente eson si son de sur america 
imprimir 5 paises de igual mododo si es de Europa
"""
print("\n\t\tEJERCICIO # 6")
def continentes(continente):
    eur1 = "Alemania" 
    eur2 = "España"
    eur3 = "Belgica"
    eur4 = "Francia"
    eur5 = "Suecia"
    amer1= "Colombia"
    amer2= "Panama"
    amer3= "Peru"
    amer4= "Argentina"
    amer5= "Chile"
    
    europa = end=eur1,eur2,eur3,eur4,eur5
    america = end= amer1,amer2,amer3,amer4,amer5
    """
    if continentes != "Europa":
        return america
    else: 
        return europa """
print(continentes("America"))
"""print("esto es un",end=" *sd+/")
print("Ejemplo")
print("1","2","3","4","5", sep="-") """
# -------------------------------
