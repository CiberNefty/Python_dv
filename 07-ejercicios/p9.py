# 9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios 
#    elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de 
#    productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA. 
valorproductos = []
productos_a_comprar = int(input("Cuantos productos desea adquirir?: "))
iva=0.16

for i in range(1, productos_a_comprar+1):
    precio = int(input(f"ingrese el precio del producto {i}: "))
    valorproductos.append(precio)

print("\nEl valor de los productos son: ")
for producto in valorproductos:    
    print(f"{valorproductos.index(producto)+1}. {producto}")


print("Cantidad de productos: ",len(valorproductos), '\nIVA: 16%') # cantidad de productos
valorConIVA=sum(valorproductos)*iva
valorApagar=sum(valorproductos)+valorConIVA
print("Total del IVA: ",valorConIVA)
print("Valor a pagar: {}".format(valorApagar))

