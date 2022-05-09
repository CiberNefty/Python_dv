def holamundo(nombre):
    return f'Hola que tal estas {nombre}'

def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""
    if basicas != False:
        cadena += "Suma: "+str(suma)
        cadena += "\n"
        cadena += "Resta: "+str(resta)
    else:
        cadena += "\n"
        cadena += "Multiplicacion: "+str(multi)
        cadena += "\n"
        cadena += "Division: "+str(division)    

    return cadena