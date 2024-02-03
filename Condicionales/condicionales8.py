numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numeros = [numero1, numero2, numero3]

numeros.sort() #sort()  ordenar los números en orden ascendente y descendente.
print("Orden ascendente: ", numeros)

numeros.sort(reverse=True)
print("Orden descendente: ", numeros)
