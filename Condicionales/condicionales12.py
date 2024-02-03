cantidad = int(input("Ingrese la cantidad de artículos: "))

precio_unitario = float(input("Ingrese el precio unitario: "))

if cantidad < 5:
    precio_final = cantidad * precio_unitario
elif 5 <= cantidad < 10:
    precio_final = cantidad * precio_unitario * 0.95
else:
    precio_final = cantidad * precio_unitario * 0.92

print("El valor total a pagar es: ", precio_final)
