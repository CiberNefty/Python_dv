def suma(a,b):
    result = a+b
    print (result)
    return result

def operaciones(a,b):
    suma = a+b
    multiplacion = a*b
    resta = a-b
    return suma, multiplacion, resta



s,m,r = operaciones(5,6)
print(s,m,r)