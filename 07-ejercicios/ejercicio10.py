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
