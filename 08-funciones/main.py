"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la funcion 
tantas veces como sea posible.

def nameMyfuncion(parametros):
    # Bloque / conjunto de instrucciones

nameMyfuncion(mi_parametro)
nameMyfuncion(mi_parametro)
"""
# Ejemplo 1
print("####### EJEMPLO 1 ########")

# Definir funcion
def muestraNombres():
    print("Daniel")
    print("Paco")
    print("elsa")
    print("Thor")
    print("Nestro")
    print("Pipe")
    print("Felipe")
    print("\n")

# Invocar funcion
muestraNombres()
muestraNombres()
muestraNombres()
#--------------------
# EJjemplo 2: Parametros
# Un dato que le paso desde afuera hacia la funcion, para poder parametrizar 
print("####### EJEMPLO 2 ########")

def mostrarTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
#mostrarTuNombre("Jose Peres")
#mostrarTuNombre("PAquito")
#mostrarTuNombre("Juanfran")
#mostrarTuNombre(nombre,9) # esta es un dato fijo
mostrarTuNombre(nombre,edad) 

