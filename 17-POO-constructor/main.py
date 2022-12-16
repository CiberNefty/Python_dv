"""
Vamos a aprender a trabajar con el constructor y vamos hacer un ejemplo guardando
una clase dentro de un modulo, una clase seria un fichero unico que nosotros vamos
a poder importar y esa seria la manera correcta de trabajar, tener diferentes 
ficheros separados por cada clase que yo quiera crear he importarlo en el programa
del archivo principal donde nosotros queramos usar esa clase y queramos usar esas 
funcionalidades en concreto.
"""
from coche import Coche # Aqui estamos diciendo que, de nuestro fichero (modulo) coche.py importe la clase Coche

carro = Coche('Amarillo','Ranault','Clio',110, 200, 4) #Aqui creamos nuestro primero obejto y le asignamos nuevos paramotros a nuestro objeto.
carro1 = Coche('Morado','Pegaut','X3r',160, 215, 4) 
carro2 = Coche('Verde Militar','Ford','Ranger',280, 200, 4) 
carro3 = Coche('Blanco','Bmw','x10',350, 400, 4) 

# Para sacar un dato en especifico.
#print(carro.getColor())

""" Es muy trabajoso sacar dato a dato, vamos a crear metodos getter y setter para
cada propiedad y luego vamos haer un metodo que nos saque de golpe de cada 
coche que vallamos creando"""

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Como detectar el tipado de un objeto.
# DETECTAR TIPADO

carro3 = 'Daniel'
if type(carro3) == Coche:
    print('Es un objeto correcto !!')
else:
    print('No es un objeto !!')