tamano = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))

ingredientes = int(input("Ingrese el número de ingredientes adicionales: "))

if tamano == 1:
    precio = 15000
elif tamano == 2:
    precio = 24000
elif tamano == 3:
    precio = 36000
else:
    print("Tamaño inválido. Por favor, seleccione un tamaño de 1, 2 o 3.")

precio_total = precio + ingredientes * 4000

print("El precio total es: ", precio_total)