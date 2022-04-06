"""
Ejercicio 10.
El programa tiene que pedir la nota a 15 alumnos y 
sacar por pantalla cuantos han aprobado y cuantos suspendido.
"""
aprobar = 0
reprobar = 0
for i in range(1,4):
    if i == i:
        print(f"###########\n Alumno {i}\n###########")
        cont = 1
        nota = 0
        while cont > 0 and cont <4:
            nota = nota + float(input(f"ingresa nota {cont}: "))
            oper1 = nota / 3
            cont += 1
        #--------------------
        if oper1 >= 3.0 and oper1 <=5.0:
            #print(f"Alumno {i} aprobo con {oper1}")
            aprobar = aprobar + 1
        else:
            if oper1 <= 2.9:
                #print(f"Alumno {i} reprobo con {oper1}")
                reprobar = reprobar + 1    

print(f"Estudiantes aprobados: {aprobar}")
print(f"Estudiantes Reprobados: {reprobar}")
#---------------------------------------------------------------
#Ejercicio por Vic
contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota1 = int(input(f"Que nota quieres ponerle al \"alumno {contador}\"?: "))
    
    if nota1 >= 5:
        aprobados+= 1
    else:
        suspendidos +=1
    contador += 1

print(f"\nAlumnos aprobado: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")