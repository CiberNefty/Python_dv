"""CONSTRUCTOR:
EL constructor es un metodo especial dentro de una clase y se suele utilizar para 
para darle un valor a los atributos de un objeto al crearlo.

Digamos que es el primero metodo que se ejecuta al crear el objeto y se llama
automaticamente al crearlo es decir este metodo puede recibir parametros como cualquier
otro metodo y para pasarselo simplemente tenemos que pasarle parametro a lo que es el
objeto cuando lo invocamos.
"""

class Coche:
    # Atributos ó Propiedades (varibles)
    # Caracteristicas del coche.
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2 # Asientos
    
    # CONSTRUCTOR
    def __init__(self,color,marcar,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Metodos, son acciones que hace el objeto (coche) (Funciones)
    # Podemos modificar el color del coche con setter.
    def setColor(self, color):# Para poder modificar el valor de una propiedad, tenemos que agregarle un par de argumentos, el primero seria el parametro self y luego la propiedad que queremos cambiar.
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca


    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self): # Sacame la velocidad
        return self.velocidad # Voy a sacar la velocidad

    # Vamos a crear un metodo generar que nos saque toda la informacion del coche.
    def getInfo(self):
        informacion = '---- INFORMACION COCHE ----'
        informacion += '\n Color: '+ self.getColor()
        informacion += '\n Marca: '+ self.getMarca()
        informacion += '\n Modelo: '+ self.getModelo()
        informacion += '\n Velocidad: '+ str(self.getVelocidad()) # Aqui convertimos lo que hay en este metodo que es int a! str.

        return informacion
# Fin deficion clase.