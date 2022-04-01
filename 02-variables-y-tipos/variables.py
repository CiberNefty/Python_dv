"""
 Una variables es un contenedor de informacion
 que dentro guardara un dato, se pueden crear
 muchas variables y que cada una tenga un dato distinto.
 """
#Crear Variables y asignarles un valor
texto = "Mastes en perder tiempo"
texto2 = "Con Daniel Vera"
numero=45
decimal = 6.4
#mostrar rel valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("_-----------------------------------_")
# Sustituir el valor de algunas variables / Reasignar valores
numero =32
decimal=4.5
print(numero)
print(decimal)

print("_-----------------------------------_")
# Concatenación

nombre = "Daniel "
apellidos = "Vera"
web = "ChicoAutentico.com"

print(nombre +" "+ apellidos+ " "+ web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))
