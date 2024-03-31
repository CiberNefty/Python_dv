# 10. Programa que permita determinar el salario a pagar a un empleado teniendo como entradas 
#     el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe 
#     descontar el 10% por concepto de pensión y 15% por concepto de salud.

diastrabajados= int(input("¿Cuantos dias trabajaste?: "))
horasAlDiadetrabajo = int(input("Cuantas horas trabajas en un dia?: "))
htrabajadas = int(diastrabajados*horasAlDiadetrabajo)

valorhoraT = int(input("Ingresa el valor de la hora: "))

totalDevengado=(int(htrabajadas) * int(valorhoraT))
descuentoSalud=(totalDevengado * 0.15)
descuentoPension=(totalDevengado * 0.1)
totalDeducidos=(descuentoSalud + descuentoPension)
totalApagar=(totalDevengado-totalDeducidos)
print("El salario mensual a pagar al empleado es: $",totalApagar)

print("------------------")
print("HAY DOS FORMAS DE OBTENER EL MISMO RESULTADO")
print("------------------")


def calcular_salario(salario_diario):
    # Suponemos que el mes tiene 30 días
    dias_trabajados = 30
    salario_mensual = (salario_diario * dias_trabajados)
    descuentoPension1= salario_mensual * 0.1 
    descuentosalud1= salario_mensual * 0.15
    totalDeducidos1= descuentoPension1 + descuentosalud1
    salario_mensual = salario_mensual - totalDeducidos1
    return salario_mensual
# Solicitar al usuario el salario diario
try:
    salario_diario = float(input("Ingrese el salario diario del empleado: "))
    salario_total = calcular_salario(salario_diario)
    print(f"El salario mensual a pagar al empleado es: ${salario_total:.2f}")
except ValueError:
    print("Error: Ingrese un valor numérico válido para el salario diario.")

