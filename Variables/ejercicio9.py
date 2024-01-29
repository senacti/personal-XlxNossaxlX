valor_unitario = float(input("Ingrese el valor unitario del producto: "))

cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))

#Subtotal de la compra
subtotal = valor_unitario * cantidad

# Calcular el iva sobre el subtotal
iva = subtotal * 0.16

precio_final = subtotal + iva

print("El precio final de la compra es: ", precio_final)
