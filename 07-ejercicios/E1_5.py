#EL SEÑOR RAFAEL, SALIÓ DE COMPRAS. COMPRÓ EN EL ALMACÉN COSTA AZUL HABÍA
#DESCUENTO DEL 14% SOBRE EL VALOR DE SU COMPRA. AHÍ COMPRÓ UNA CAMISA
#$35.000 Y UN PANTALÓN $75.000 Y EN TIGO COMPRÓ UN CELULAR POR $900.000
#ELABORE UN ALGORITMO QUE MUESTRE EL SUBTOTAL DE LA COMPRA DEL PANTALÓN
#Y LA CAMISA, EL DESCUENTO Y EL TOTAL DE LA COMPRA EN EL ALMACÉN COSTA AZUL.
#ADEMÁS DEBE MOSTRAR CUÁNTO SE GASTÓ EL SEÑOR RAFAEL EN SU DÍA DE COMPRAS.
def Sena():
    print("SOMOS SENA ;)")
def ProductoscostaAzul():
    descuento = 0.14
    listProdcutos = {'Camisa' : 65000,
                     'Pantalon': 150000,
                     'Zapatos': 350000}
    print(listProdcutos)
def ProductosTigo():
    pass


print("COMPRAS DEL SEÑOR RAFAEL")
dineroDeRafael = float(1600000)
print("""
      #-----------------------#
      |       ALMACENES       |
      |  1. Costa Azul        |
      |  2. Tigo              | 
      |  3. Sena              |
      #-----------------------#""")
opc=int(input("Ingrese el numero del almacen al cual desea ingresar: "))
if opc == 1:
    ProductoscostaAzul()
elif opc == 2:
    ProductosTigo()
elif opc == 3:
    Sena()
else:
    print("Escoja una opcion correcta, intentelo de nuevo")