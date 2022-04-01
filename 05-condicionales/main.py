#Es una estructura de control que permite controlar el flujo del programa,
# si un dato cumple un tipo de condicion se introduciran un tipo de 
# instrucciones y si no se cumple la condicion se iniciara otras 
# instrucciones.

"""
# Condicional IF

SI se_cumple_esta_Instruccion:
|   Ejecutar grupo de instrucciones
SI NO:
|   Se ejecutaran otro grupo de instrucciones

If condicion:
|   instrucciones
else:
|   otras instrucciones

# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# OPERADORES LOGICOS
and Y
or  O
!   negacion
not no

"""
# Ejemplo 1
print("############  EJEMPLO 1 ################")
color = 'rojo'
#color = input("Adivina mi color favorito: ")
if color == 'rojo':
    print("En horabuena")
    print("el color el rojo")
else:
    print("Color incorrecto.")
# Ejemplo 2
print("\n############  EJEMPLO 2 ################")
year= 2020
#year= int(input("En que año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("es un año anterior a 2021")

# EJEMPLO 3
print("########### EJEMPLO 3 #################")

nombre = "Daniel Vera"
ciudad ="Girardot"
continente ="Sur america"
edad= 18
mayoria_edad = 18
if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")
    if continente != "Sur america":
        print(f"{nombre} No es sur americano, tu eres de {continente}")
    else:
        print(f"Es sur americano y la ciudad de {ciudad}")
else:
    print(f"{nombre} No es mayorde edad ")


# EJEMPLO 4
print("########### EJEMPLO 4 #################")
dia=2
#dia = int(input("introduce el numero de la semana: "))
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else: 
            if (dia == 4):
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print('Es sabado')
                    else:
                        if dia == 7:
                            print("Es domingo")
                    
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("Es fin de semana")

# EJEMPLO 5
print("\n########### EJEMPLO 5 #################") 
#Ejemplo de si una persona esta en condicion de trabajar o no!
# con un rango de edad de 18 a 65 años
edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("tienes eedad de trabajar?, introduce tu edad: "))
edad_oficial=18
if edad_oficial >= 18 and edad_oficial <=65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

# EJEMPLO 6
print("\n########### EJEMPLO 6 #################") 
#ejercicio de comprobar si en ese pais se habla algun idioma, haciendo
#una comparacion entre paises
pais = "España"

if pais == "Mexico" or pais =="España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

# EJEMPLO 7
print("\n########### EJEMPLO 7 #################") 
#ejercicio de comprobar si en ese pais se habla algun idioma, haciendo
#una comparacion entre paises (OPERADOR DE NEGACION )
pais = "Alemania"

if not(pais == "Mexico" or pais =="España" or pais == "Colombia"):
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana")

# EJEMPLO 8
print("\n########### EJEMPLO 8 #################") 
#ejercicio de comprobar si en ese pais se habla algun idioma, haciendo
#una comparacion entre paises (OPERADOR DE comparacion DIFERENTE )
pais = "Colombia"

if pais != "Mexico" and pais !="España" and pais != "Colombia":
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana :)")


