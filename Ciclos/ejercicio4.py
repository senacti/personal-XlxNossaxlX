suma =  0
contador =  0

print("Por favor, introduce  10 números:\n")

for i in range(1,  11):
    num = int(input("Número {}: ".format(i)))
    suma += num
    contador +=  1

promedio = suma / contador

print("La suma de los  10 números es: ", suma)
print("El promedio de los  10 números es: ", promedio)
