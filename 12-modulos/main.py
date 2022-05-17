"""
Modulos: son funcionalidades ya hechas para reutilizar.
en python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/tutorial/modules.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""
"""
Para crear un modulo tenemos que crear un archivo dentro de la
 carpeta de nuestro proyecto y le ponemos el nombre que queramos.
  <file.py> 

Dentro del archivo vamos a crear las funciones las clases o lo que queramos.

Esos modulos son para crear funciones o programas que utilizare mas adelante.

Puedo utilizar mis modulos llengo al programa principal y escribo 
la palabra import mi modulo
"""

# Importar modulo propio
#import mimodulo
# Imaginemos que solo queremos importar solo una funcion de nuestro modulo
# No queremos usar todas solo una.
#from mimodulo import holamundo

# Ahora imaginemos que no quiero importar todas las funciones y no tener que llamarla con nuestro modulo.
from mimodulo import *

# Invocar modulo
#print(mimodulo.holamundo('Daniel Vera'))
#print(mimodulo.calculadora(1,4,True))

# para llamar a mi funcion solamente sin llamar al archivo (ó Modulo)
print(holamundo('Juan fe')) # Aqui solo llamamos a nuestra funcion que se encuentra en nuestro modulo.
print(calculadora(1,4,True))

# Modulo Fechas
import datetime

print(datetime.date.today()) # Nos saca la fecha de ese mismo dia que estemos utilizandola

fecha_completa = datetime.datetime.now()

print(fecha_completa) # Nos saca lo que seria la instruccion de la fecha completa con horas y todo.
print(fecha_completa.year) # Nos saca solamente el año.
print(fecha_completa.month) # Nos saca el mes.
print(fecha_completa.day) # Nos saca el dia.

# Podemos personalizar mi fecha
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y,") # Esto se describe como: el porcentaje como lo que seria el indicador de que queremos mostrar, en este caso se muestra primero el dia el mes y luego el año con Y mayuscula.
print("Mi fecha perzonalizada ",fecha_personalizada)

print(datetime.datetime.now().time())

# Modulo de matematicas

import math

# Raiz cuadrada de un numero.
print("Raiz cuadrada de 10:", math.sqrt(10))
#print("Numero pi: ", math.pi)
print("Numero pi: ", float(math.pi)) # Podemos convertirlo a un dato float

print("Redondenar: ",math.ceil(543.2535)) # Redondeo hacia arriba
print("Redondenar: ",math.floor(543.2535)) # Redondeo hacia abajo

# Modulo randoom
import random
print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))