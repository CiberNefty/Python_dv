"""EL ÍNDICE DE MASA CORPORAL ES EL PESO EN KILOGRAMOS DIVIDIDO POR LA
ESTATURA EN METROS CUADRADOS. ELABORA UN ALGORITMO QUE CALCULE EL IMC
DE UNA PERSONA."""

print("""### CALCULADORA DE IMC ###""")
peso = float(input('Ingresa tu peso (kg): '))
estatura = float(input('Ingresa tu estatura (m^2): '))

#imc = peso / estatura^2
imc = peso / estatura*estatura

print(f'Tu indice de masa corporal es: {imc} IMC')