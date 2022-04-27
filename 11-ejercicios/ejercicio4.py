"""
Ejercicio 4. 
Crear un script que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje 
segun el tipo de dato de cada varibale.
"""
def traducirTipo(tipo): # cuando le pasemos un tipo de dato, me devuelva segun el tipo de dato que sea.
    result = None
    if tipo  == list:
        result= 'LISTA'
    elif tipo == str:
        result = 'CADENA DE TEXTO'
    elif tipo == int:
        result = 'NUMERO ENTERO'
    elif tipo == bool:
        result = 'BOOLEANO' 
    
    return result

def comprobar_tipado(dato, tipo): # Aqui ya estaria realizado el ejercicio  pero necesitamos que cuando imprima deje de imprimir <class 'tipo'>, necesitamos algo mas realisa nos crearemos una nueva funcion.
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result= f"Este dato es del tipo de {traducirTipo(tipo)}"
    else: 
        result= "El tipo de dato no es correcto"

    return result

mi_lista = []
string = "q"
entero = 0
booleano = True

print(comprobar_tipado(mi_lista, list))
print(comprobar_tipado(string, str))
print(comprobar_tipado(entero, int))
print(comprobar_tipado(booleano, bool))

print(type(mi_lista),"\n",
type(string),"\n",
type(entero),"\n",
type(booleano),"\n")