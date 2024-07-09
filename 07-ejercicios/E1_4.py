# ELABORA UN ALGORITMO QUE MUESTRE EL PROMEDIO DE LAS 5 NOTAS DE INGLÉS.
print("## PROMEDIO DE NOTAS ##")
nota = 0
for i in range(1,6):
    nota += float(input(f"Ingrese la nota #{i}: "))
resul = nota/5
if resul >= 3.5:
    print(f"El estudiante aprobo con una nota de {resul}")
else:
    print(f"El estudiante reprobo con una nota de {resul}")