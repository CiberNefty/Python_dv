# 15.  Programa para determinar la mitad de un número ingresado por el usuario es mayor o menor de 100. 
num= float(input("Ingrese un numero: "))
numero_inferior= 0.1
numero_superior= 100
operacion= num/2.0

if numero_inferior <= operacion <= float(numero_superior) :
    print("El numero {} esta entre 1 y 100".format(operacion))
else:
    print("El numero no se encuentra dentro del rango permitido.")

