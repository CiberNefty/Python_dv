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
def historia(nombre=''):
    global his1
    his1 = f"""H-1    El dia que {nombre} entro a la universidad se percato,
    que su vida cambiaria de la noche a la mañana, transcurrido el
    el primer semestre noto que muchos de los estudiantes desertaron. """
    his2 = f"""H-2    Luego {nombre} de haber curzado tanto tiempo solo en la u sintio
    que le hacia falta estar con una mujer, con lo cual tuvo que pagar por una 
    rato de intimidad."""
    his3 = f"""H-3    Los primeros y utlimos semestres son los mejores, por que te das
    cuenta que solo es cuestion de atencion en lo que haces y te propones, dentro
    de poco Dios cambiara mi vida, empezare a trabajar para una empresa de TI y
    estare disfrutando mi puesto, por que se que me lo merezco."""
    
    if not nombre.find('D'):
        his1.upper()
        return his1
    elif not nombre.find('J'):
        return his2
    elif not nombre.find('F'):
        return his3
    else:
        print(f"{nombre} no cuenta para una historia.")

#nombre = input('Ingrese nombre: ')
#print(historia(nombre))
#-------------------------------
"""     EJERCICIO 6
Crear funcion que evalue de que continente es o si son de sur america 
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
#print(continentes("America"))
"""print("esto es un",end=" *sd+/")
print("Ejemplo")
print("1","2","3","4","5", sep="-") """
# -------------------------------
"""frase = '   mi contenido    '
print(frase)
print(frase.strip() and frase.find('m'))
#------------------------- """
"""     EJERCICIO 7
Crear un menu donde el usuario escoja que quiere realizar,
asu vez realizar variras funciones que cada una contenga:
- Detectar el tipado 
- Limpiar espacios
- Eliminar variables
- Comprobar variables vacias # por ahora no pude realizarlo
- Encontrar caracteres 
- Mayusculas y Minisculas
* Tener por lo menos una funcion lambda
"""
def DetectarType(nombre, edad,peso,year):
    comprobar = int(input("1. Nombre.\n2. Edad.\n3. Peso\n4. Año\n5. Todas las anteriores\n\nCual dato quieres saber su tipo?:"))
    if comprobar == 1: 
        texto = f"{nombre} es de tipo: {type(nombre)}"
        return texto
    elif comprobar == 2:
        texto = f"{edad} es de tipo: {type(edad)}"
        return texto
    elif comprobar == 3:
        texto = f"{peso} es de tipo: {type(peso)}"
        return texto
    elif comprobar == 4:
        texto = f"{year} es de tipo: {type(year)}"
        return texto
    elif comprobar == 5:
        texto = f"{nombre} es de tipo: {type(nombre)}"
        texto += f"\n{edad} es de tipo: {type(edad)}"
        texto += f"\n{peso} es de tipo: {type(peso)}"
        texto += f"\n{year} es de tipo: {type(year)}"
        return texto
    else:
        print("Opcion no resgistrada:")

def LimpiarEspacios():
    print("Esta funcion de limpiar espacios funciona cuando una variable\n contiene espacios al principio o al final.\n",
    "\nEjemplo: variable = ___Hola Mundo___\n\nEsta funcion elimina los espacios que se refleja.")
    limpiar = input("Escribe alguna ejemplo: ")
    return limpiar.strip()

def EliminarVariable(nombre,edad,peso,year):
    comprobar =int(input("1. Nombre.\n2. Edad.\n3. Peso.\n4. Año.\n5.Todas.\nQue variable quiere que no se muestre:"))
    if comprobar == 1:
        del nombre
        return edad,peso,year
    elif comprobar == 2:
        del edad
        return nombre,peso,year
    elif comprobar == 3:
        del peso
        return nombre,edad,year
    elif comprobar == 4:
        del year
        return nombre,edad,peso
    elif comprobar == 5:
        del nombre,edad,peso,year
        return f"Eliminaste todas las variables."
""" Esta funcion me esta mamando huevo, que rabia.

def ComprobarVaciedad(nombre='',edad='',peso=1.5,year=0):
    if len(nombre) <= 0: 
        texto = f"La variable nombre esta vacia"    
        

    if len(edad) <= 0: 
        texto = f"La variable peso esta vacia"
        return texto

    if len(peso) <= 0.0: 
        texto = f"La variable peso esta vacia"
        return texto
    if len(year) <= 0: 
        texto = f"La variable año esta vacia"
        return texto
    else: 
        return f"La variable nombre tiene contenido de {len(nombre)} caracteres.\n", f"La variable nombre tiene contenido de {len(edad)} caracteres.\n","La variable nombre tiene contenido de {len(peso)} caracteres.\n", f"La variable nombre tiene contenido de {len(year)} caracteres."
 
nombre = input('Ingresa el nombre: ')
edad = int(input('Ingresa la edad: ')) 
peso = float(input('Ingresa tu  peso: ')) 
year = int(input('Ingresa el año: '))
"""
#---------------------------------------
def EncontrarCaracter(frase,encontrar = ''):
    encontrar = input('Desde que posicion empieza: ')
    texto = frase.find(encontrar)
    return texto

def MayusMinis():
    minisMayur = input("Ingresa una frase a convertir: \n")
    evaluar = int(input("\n1. Mayusculas.\n2. Minusculas\nIngresa la opcion a convertir tu frase: "))
    
    if evaluar == 1:
        return minisMayur.upper()
    elif evaluar == 2: #otra opcion para mostrar como convertir.
        minisMayur = minisMayur.lower()
        return minisMayur 
    else:
        return "Opcion no registrada"

#------------------------------------
print("Ingresa unos valore primero para que se te despliegue un menu.")
nombre = input("Ingresa Nombre: ")
edad = int(input("Ingresa Edad: "))
peso = float(input("Ingresa Peso: ")) # Aqui debi colocar estatura XD
year = int(input("Ingresa Año: "))

cont_final = 0

while cont_final != 1:
    if not len(nombre) <= 0 and not len(str(edad)) <= 0 and not len(str(peso)) <= 0 and not len(str(year)) <= 0:
        print("\n\t*************************")
        print("\t********  MENU **********")
        print("\t*************************")
        print("\t1. Detectar tipado de variables.\n",
        "\t2. Limpiar espacios.\n",
        "\t3. Eliminar variables.\n",
        "\t5. Encontrar caracteres.\n",
        "\t6. Mayusculas y minisculas.\n",
        "\t7. Salir.\n", 
        "\t\t\1 \2 \3 \4 \5 \6")

        menuopciones= int(input("Digita numero Opcion: \n"))

        if menuopciones == 1:
            print("DECTECTAR TIPO DE VARIABLE\n")
            print(DetectarType(nombre,edad,peso,year))
        elif menuopciones == 2:
            print("LIMPIAR ESPACIOS\n")
            print(LimpiarEspacios())
        elif menuopciones == 3:
            print("ELIMINAR VARIABLES\n")
            print(EliminarVariable(nombre,edad,peso,year))
        elif menuopciones == 5:
            print("ENCONTRAR CARACTERES\n")        
            frase =input('Ingresa un frase o un texto para que más adelante puedas encontrar la posicion de alguna frase o caracter: ')
            print(EncontrarCaracter(frase))
        elif menuopciones == 6:
            print("MAYUSCULAS Y MAYUSCULAS\n")
            print(MayusMinis())
        elif menuopciones == 7:
            cont_final = 1

