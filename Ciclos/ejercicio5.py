numero = int(input("Introduce un número entero: "))

print("Tabla de multiplicar del {}:".format(numero))

for i in range(1,  11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
