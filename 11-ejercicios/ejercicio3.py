"""
Ejercicio 3. Programa que compruebe si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y 
mostrarlo en mayusculos.
"""
variable = input("Ingrese valor: ")

if len(variable) <= 0:
    variable = "Valor minusculas a mayusculas"
    print(variable.upper())
else:
    print("No esta vacia la variable: " + variable)

# -------------------------------
# Ejercicio por CIV
texto = ""

if len(texto.strip()) <= 0:
    texto = "Hola soy un texto en minusculas"
    print(texto.upper())
else:
    print("La la variable tiene contenido: " + texto)
