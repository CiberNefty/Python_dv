"""17. Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, 
       Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el 
       programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no 
       la materia 
       (Definitiva mayor a 4.0). Debe imprimir coma salidas el nombre, el código, la materia y si aprobó o no."""


codigo=int(input("Ingresa el codifo del estudiante: "))
nombreEst=input("Ingresa el nombre del estudiante: ")
nombreMat=input("Ingresa el nombre de la materia: ")
nota1=float(input(f"Ingresa la nota 1: "))
nota2=float(input(f"Ingresa la nota 2: "))
nota3=float(input(f"Ingresa la nota 3: "))
oper1 = (nota1+nota2+nota3) / 3
#--------------------
if oper1 >= 4.0 and oper1 <=5.0:
    print(f"<----------------->\nEl estudiante: {nombreEst}\nCodigo: {codigo}\nMateria: {nombreMat}\nAprobo con: {oper1:.2f}")
elif oper1 < 4.0:
    print(f"El estudiante: {nombreEst}\nCodigo: {codigo}\nMateria: {nombreMat}\nReprobo con: {oper1:.2f}")
else:
    print("Escriba las notas correspondientes.")