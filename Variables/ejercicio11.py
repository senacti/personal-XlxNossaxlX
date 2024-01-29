num = int(input("Ingrese un número: "))

raiz = num

#diferencia entre la raíz y la raíz al cuadrado sea menor que un umbral (0.0001 en este caso)
while abs(raiz - num / raiz) > 0.0001:
    raiz = (raiz + num / raiz) / 2

print("La raíz cuadrada de", num, "es", raiz)
