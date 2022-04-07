"""
Variables locales: Se definen dentro de la funcion y no 
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.
"""
#Variable Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."

print(frase)

def holamundo():
    frase = "Hola mundo"
    print("-Dentro de la funcion-")
    print(frase)

    year = 2022
    print(year)

    global website #Aqui la variable website se convierte en global
    website = "@_ds.va_"
    print("DENTRO: " + website)

    return "Dato devuelto "+str(year)


print(holamundo())
print(f"FUERA: {website}")