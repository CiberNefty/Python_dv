# 6. Programa que permita calcular el 30%, el 60% y el 90% de un número cualquiera 

porcentaje1 = 30
porcentaje2 = 60
porcentaje3 = 90
numero = int(input("Ingresa el numero al cual sacaras un porcentaje: "))
print("""OPCION DE PORCENTAJES:
      a. Sacar el 30%
      b. Sacar el 60%
      c. Sacar el 90%\n""")
opcion= str(input("ingrese la opcion a la cual quiere sacarle porcentaje: "))
if opcion == "a":
    print(f""""---------------\nEl resultado de la opcion {opcion} del {porcentaje1}% es del {numero *(porcentaje1/100)}""")
elif opcion == "b":
    print(f""""---------------\nEl resultado de la opcion {opcion} del {porcentaje2}% es del {numero *(porcentaje2/100)}""")
elif opcion== "c":
    print(f""""---------------\nEl resultado de la opcion {opcion} del {porcentaje3}% es del {numero *(porcentaje3/100)}""")
else:
    print("reinicia el programa, escoje una opcion valida")
