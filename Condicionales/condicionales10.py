cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 6:
    precio_unitario = 240000
elif 6 <= cantidad <= 7:
    precio_unitario = 221000
else:
    precio_unitario = 180000

valor_total = cantidad * precio_unitario

print("El valor total a pagar es: ", valor_total)
