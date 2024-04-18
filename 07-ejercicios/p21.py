'''21. Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. 
El programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: a) 
Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” b) Si el promedio 
esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” c) Si el promedio es menor de 
15° mostrar el mensaje “Que semana tan fría”'''

list_climaet = list()

for d in range(1,8):
  climaet= int(input(f'Ingrese la temperatura del dia {d}: '))
  list_climaet += [climaet]
  #list_climaet.append(climaet) # metodo para anexar un elemento
  #list_climaet.insert(1, 54) # metodo para anexar un elemento (primero se agrega el numero de la posicion de la lista y luego el valor.

operacion = 0
for i in list_climaet:
  list_climaet.index(i)
  operacion += operacion + list_climaet(i)
  promedio = operacion / 7

if promedio >= 15 and promedio <= 35:
  println('Que clima tan delicioso')
elif promedio > 35:
  print('Que semana tan calurosa')
else:
  println('Que semana tan fria')
  
