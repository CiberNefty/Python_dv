# ELABORA UN ALGORITMO QUE DADA UNA TEMPERATURA EN GRADOS CELSIUS LA
# CONVIERTA A GRADOS FAHRENHEIT

print('#### CALCULADORA DE TEMPERATURA ####')

c = int(input("Ingresa la temperatura que quieres convertir (°C): "))
gradosFahrenheit = (1.8 * c) +32

print(f'La covnversion °{c} de grados centigrados en grados Fahrenheit es: °{gradosFahrenheit}')