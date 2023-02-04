import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        database="proyectonotas_python"
    )
    #Verificamos si funciona la coneccion 
    #print(database)

    cursor = database.cursor(buffered=True) # Este buffered me va a permitir hacer muchas consultas usanndo el mismo cursor

    return [database, cursor] # Aqui tendremos la posibilidad de devolver lo que seria la conexion a la DB y al cursor