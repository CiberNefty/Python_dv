# Funciones Predefinidas para

nombre = 'Daniel VERA'

print(type(nombre))

#formas de detectar el tipado que tiene una variable

# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar: 
    print("Esa varible es un string")
else:
    print("No es una cadena.")

if not isinstance(nombre,float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = '   mi contenido    '
print(frase)
print(frase.strip())

# Eliminar variables
year = 2022
print(year)
del year
#print(year)

# Comprobar variables vacia
texto = "  ff "

if len(texto) <= 0:
    print("La variables esta vacia")
else:
    print("La variable tienes contenido: ",len(texto))

# Econtrar caracteres 
frase = "La vida es bella"
print(frase.find("vida"))

# Remplazar palabras en un string
nueva_frase = frase.replace("vida","moto") # La funcion replace tiene como objetivo cambiar un caracter , el primer parametro es lo que queremos cambiar y el segundo parametro es lo que vamos a colocar.
print(nueva_frase)

# Mayusculas y minisculas
print(nombre)
print(nombre.lower() + " funcion lower") # Con la funcion lower convertimos esa variable a minisculas
print(nombre.upper() + " funcion upper") # Con la funcion upper convertimos esa variable a mayusculas