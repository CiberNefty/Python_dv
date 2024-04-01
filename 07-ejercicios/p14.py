# 14. Programa para saber si un estudiante del Enrique Olaya Herrera requiere refrigerio.  
#     Por disposición de la secretaria de Educación requieren refrigerio los estudiantes de grado sexto hacia abajo.

cursodelAlumno = (input("Ingrese el curso en que se encuentra el estudiante: "))
listadegrados = ['primero', 'segundo','tercero','cuarto','quinto','sexto','septimo','octavo','noveno','decimo','once']

if cursodelAlumno in listadegrados[0:5+1] :
    print("El estudiante esta en el grado {}".format(cursodelAlumno), "y puede recibir refigerio")
else:
    print("El estudiante no recibe refigierio porque esta en un grado superior.")