# Programacion orientada a objetos (POO ó OOP)

# Basicamente una clase es un molde para crear mas objetos
"""de ese tipo con caracteristicas parecidas y entendiendo una clase como un molde podriamos
definir una clase como un coche esta clase sera la plantilla para crear diferentes objetos
de nuevos coches tambien, tendra atributos ó propiedades lo que antes se conocia como 
variables que, serian las piezas o caracteristicas del coche por ejemplo el color, modelo, etc.

Tambien esta clase tendra metodos lo que antes se conocia como funciones y estos metodos
seran las acciones que puede hacer un coche y, con los metodos vamos a interactuar con los
atributos y si es necesaio cambiaremos los valores que tienen."""

# DEFINIR UNA CALSE (Molde para crear mas obetos de ese tipo
# (Coche) con caracteristicas similares)

class Coche:
    # Atributos ó Propiedades (varibles)
    # Caracteristicas del coche.
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2 # Asientos

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

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self): # Sacame la velocidad
        return self.velocidad # Voy a sacar la velocidad

# Fin deficion clase.

# Crear objetos / Instanciar la clase
coche = Coche() # De esta manera creamos un objeto, creando una variable donde guardaremos nuestra clase que contiene metodos.

print(coche) # Invocamos obejto.

#Cambiamos el color, el modelo del coche.
coche.setColor('Amarillo')
coche.setModelo('F40')

# Si queremos sacar el valor de una propiedad, al ser propiedades publicas
#print(coche.marca)
print(coche.marca, coche.getModelo(), coche.getColor())
#print('Velocidad actual: ', coche.velocidad) # En lugar de sacar la velocidad de esta manera la podemos sacar con la funcion que creamos que retorna la velocidad, como a continuacion.
print('Velocidad actual: ',coche.getVelocidad())
# Llamar metodos
# Estos metodos serian metodos setter por que le asignar un valor a la propiedad
coche.acelerar()
coche.acelerar()
coche.acelerar() 
coche.acelerar() # Aqui estamos llamando al metodo acelerar varias veces y aumentara en 1 cada vez que se llame el metodo.
coche.frenar() # Aquí el metodo frenar disminuira la velocidad en 1.

#print('Velocidad nueva: ', coche.velocidad)
print('Velocidad nueva: ', coche.getVelocidad())

# ---------------------------
# Para llamar a una propiedad de una manera correcta es mejor utilizar 
# los  metodos de getter  y setter
# El metodo getter es para sacar un valor.
# EL metodo setter es para asignarle un valor.
