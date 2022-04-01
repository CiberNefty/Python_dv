"""
Regalas generales de las funciones:
1- No se ejecuta la funcion a menos que la llames
2- La puedo llamar la cantidad de veces que quiere 
3- Primero hay que definir la funcion, y despues llamarla
4- Primero van los parametros requeridos y al final los opcionales
5- para cambiar el scope una variable, utilizar return
"""

# FUNCIONES SIN PARAMETROS
"""
def miFuncion():
    #conjunto de instrucciones  
"""
#Ejemplo: QUiero que me devuelva los derechos humanos

def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualda ante la ley")
    print("Derecho a la libertad")

derechos_humanos()

def derechos_mayordeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")

# FUNCIONES CON PARAMETROS
"""
def miFuncion2(parametro1, parametro2):
    #conjunto de instrucciones
"""
def mayoria_de_edad(nombre,edad):
    print(f"Segun la edad de {nombre}, sus derechos son:")
    if edad >= 18:
        derechos_humanos()
        derechos_mayordeEdad()
    else: 
        derechos_humanos()

mayoria_de_edad('Pepito', 19)
mayoria_de_edad('Rosa', 60)
mayoria_de_edad('Juan', 10)
mayoria_de_edad(edad = 5, nombre="MArgarit")

# FUNCIONES CON PARAMETROS OPCIONALES
"""
def miFuncion3(parametro1,parametro2=valorpordefecto):
    #Conjunto de instrucciones
"""
def mayoria_de_edad2(edad,nombre='X'):
    print(f"Segun la edad de {nombre}, sus derechos son:")
    if edad >= 18:
        derechos_humanos()
        derechos_mayordeEdad()
    else: 
        derechos_humanos()

mayoria_de_edad2(15,'dds')
 
 