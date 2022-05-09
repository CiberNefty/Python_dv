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
from mimodulo import holamundo


# Invocar modulo
#print(mimodulo.holamundo('Daniel Vera'))
#print(mimodulo.calculadora(1,4,True))

# para llamar a mi funcion solamente sin llamar al archivo (ó Modulo)
print(holamundo('Juan fe')) # Aqui solo llamamos a nuestra funcion que se encuentra en nuestro modulo.


