# HERENCIA
"""
- La herencia es la capacidad de compartir atributos y, metodos entre clases
de forma que yo pueda tener una clase padre que sea un objeto estandar y luego
puedo tener diferentes clases hijas que hereden los metodos y atributos de la 
clase padre y, que sean objetos similares pero con ciertas diferencias.
- Es la posibilidad de compartir atributos y metodos entre clases.
  diferentes clases hereden de otras.
"""
# Vamos a tener una clase persona que va a tener diferentes caracteristicas que van hacer
# las propiedades o atributos, ejemplo: nombre,altura,edad y vamos a tener diferentes metodos
# getter  y setter que nos permitira agregar y sacar su valor a esas propiedades.
# Pero luego tendremos otras clases que hereden de la clase Persona, que son personas tambien
# osea personas diferentes pero con cualidades diferentes unas de ellas.
# Por ejemplo un conductor un, cocinero un, maquinista. Ese tipo de personas son personas original
# a la clase generica esas personas que heredan de la clase padre van a tener las mismas cualidades
# pero con algunos añadidos
class Persona:
    """
    Atributos de nuestra clase:

    nombre
    apellidos
    altura
    edad"""

    #Metodo que me van a ayudar a sacar las diferentes propiedades cuando llame a mi objeto.
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    # Metodos que ayuden a asignarle valores a las propiedades.

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setAltura(self,altura):
        self.altura = altura
    
    def setEdad(self,edad):
        self.edad = edad

# Sabemos que una persona puede hacer diferentes metodos: Hablar, Caminar, escribir puede hacer un monton de acciones.
    def hablar(self):
        return 'Estoy hablando'
    
    def caminar(self):
        return 'Estoy caminando'
    
    def dormir(self):
        return 'Estoy durmiendo'

# De aqui para arriba es nuestra clase persona crear diferentes personas.
class Informatico(Persona): # Dentro de nuestra clase y los parentesis elegimos la clase que queremos heredar
    """ Propiedades:
    lenguajes
    experiencia
    """
    # Creamos un metodo constructor.
    def __init__(self):
        self.lenguajes = 'HTML, CSS, JavaScript, PHP'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return 'Estoy programando'

    def repararPC(self):
        return 'He reparado tu ordenador'

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() # Aqui estamos hereando el constructor de la clase padre, de esta manera entendemos que aqui tambien se guardara el constructor de la clase padre.
        self.auditarRedes = 'Experto'
        self.experienciaRedes = 15

    def auditoria(self):
        return 'Estoy auditando red'