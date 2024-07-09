# Elabora un algoritmo que muestre al usuario las siguientes opciones: IMC (índice de
# masa corporal), porcentaje de grasa corporal y tasa metabólica basal. El algoritmo
# debe permitir que el usuario escoja la opción y de acuerdo a la opción, realice los
# cálculos correspondientes y muestre al usuario el resultado:
print("### CALCUDORA DE MEDIDAS CORPORALES ###")
dineroDeRafael = float(1600000)
print("""
      #----------------------------------#
      |             CALCULADORA          |
      |  1. IMC                          |
      |  2. Porcentaje de grasa corporal | 
      |  3. Tasa Metabolica              |
      #----------------------------------#""")
opc=int(input("Ingrese el numero de la lista que quiere calcular: "))
if opc == 1:
    print("""### CALCULADORA DE IMC ###""")
    peso = float(input('Ingresa tu peso (kg): '))
    estatura = float(input('Ingresa tu estatura (m^2): '))
    #imc = peso / estatura^2
    imc = peso / estatura*estatura
    print(f'Tu indice de masa corporal es: {imc} IMC')
elif opc == 2:
    print("""FORMULA DEURENBERG
      #------------------#
      |      SEXO        |
      |  1. MUJER        |
      |  2. Hombre       | 
      #------------------#""")
    sexo = input(input('Ingrese el numero de su sexo: '))
    peso = float(input('Ingresa tu peso (kg): '))
    estatura = float(input('Ingresa tu estatura (m^2): '))
    imc = peso / estatura*estatura
    edad= int(input("Ingrese su edad: "))
    if sexo == 2:
        porcentajeGrasaCorporal= (1.2 * (imc)) + (0.23 * edad) - (10.8 * 1) # 1 equivale al tipo de sexo hombre
        print(f"Tu porcentaje de grasa corporal es de {porcentajeGrasaCorporal}%")
    else:
        porcentajeGrasaCorporal= (1.2 * (imc)) + (0.23 * edad) - (10.8 * 0) # 1 equivale al tipo de sexo femenino
    
    
elif opc == 3:
    Sena()
else:
    print("Escoja una opcion correcta, intentelo de nuevo")