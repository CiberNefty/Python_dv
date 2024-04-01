# 19. Programa que permita determinar el total a pagar por una compra de la cual se sabe el valor
#     unitario y la cantidad. Se debe tener en cuenta que se realiza un descuento del 15% por compra
#     inferiores a $20000 y del 35% por compras mayores o iguales a $20000.

valorproductos = []
productos_a_comprar = int(input("Cuantos productos desea adquirir?: "))
iva = 0.16

for i in range(1, productos_a_comprar+1):
    precio = float(input(f"ingrese el precio del producto {i}: "))
    valorproductos.append(precio)

print("\nLos productos son: ")
for producto in valorproductos:
    print(f"{valorproductos.index(producto)+1}. {producto:.2f}")

print("<------------------------------->")
print("Cantidad de productos: ", len(valorproductos))  # cantidad de productos
productosConIVA = sum(valorproductos)*iva
valorApagar = sum(valorproductos)+productosConIVA

if valorApagar < 20000:
    descuento = valorApagar*15/100
    valorApagar = valorApagar - descuento
    print("Total productos: $", sum(valorproductos))
    print("IVA: 16%\nTotal IVA: $", productosConIVA)
    print("Tienes un descuento del 15%: $", descuento)
    print("Valor a pagar: ${}".format(valorApagar))
elif valorApagar >= 20000:
    descuento = valorApagar*35/100
    valorApagar = valorApagar - descuento
    print("Total productos: $", sum(valorproductos))
    print("IVA: 16%\nTotal IVA: $", productosConIVA)
    print("Tienes un descuento del 35%: $", descuento)
    print("Valor a pagar: ${}".format(valorApagar))
else:
    print("No alcanza el valor de venta para descuento.")
    print("Total productos: $", sum(valorproductos))
    print("Total IVA: $", productosConIVA)
    print("Valor a cancelar: $", valorApagar)
