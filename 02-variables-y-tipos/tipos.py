nada = None
cadena = "Hola vamos dani no te desconcentres"
cadena = "Desarrollador web"
entero = 99
flotante = 34.2
booleano = True
lista =[10, 42, 34, 43]
listaString = [232, "floa", 23, "fgrw"]
tuplaNocambia = ("mastes Daniel", "en python", "vamos que vamos") #Basicamente es una lista que no puede cambiar
diccionario = {
    "nombre": "Daniel ",
    "apellido": "Vera",
    "curso": "Master en python" 
}#hace un array tipo json que me permite tener clave y valor
rango = range(9)
dato_byte = b"probando"


# imprimir variable
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))

#Como combertir un dato a otro
texto = "hola soy un texto"
numerito = str(324)#Podemos combertir un dato a otro colocando le el tipo de dato y luego metemos dentro de un parentesis el valor 
# 324
# "324"
#print(texto + " "+ numerito) 
print(f"{texto} {numerito}")
numerito = int(324)
print(type(numerito))
numerito = float(324)
print(type(numerito))
numerito = bool(324)
print(type(numerito))
