# 11. Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento 
añoActual = 1945
añoNacimiento = 2025

if (añoNacimiento-añoActual) >= 18:
    print("La persona es mayor de edad, tiene {} años segun su fecha de nacimiento y el año actual".format((añoNacimiento-añoActual)))
else:
    print(f"La persona no es mayor de edad, tiene{(añoNacimiento-añoActual)} años.")