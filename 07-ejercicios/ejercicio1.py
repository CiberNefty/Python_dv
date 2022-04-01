"""
EJERCICIO 1.
    - Crear dos varibalbes una pais y otra "continente"
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""

pais = input("Ingrese el pais: ")
continente = input("Ingrese el continete: ")

print(f"el pais es {pais} y su coninente es: {continente}")
#EL tipo de dato es string

print(type(pais))
print(type(continente))

print("-------------------------------")

pais = "España"         #String
continente = "Europa"   #string
year = 2022             #integer
print(f"{pais} - {continente} - {str(year)}")