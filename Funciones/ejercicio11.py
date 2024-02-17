def imprimir_pares(lista_numeros):
    for num in lista_numeros:
        if num %  2 ==  0:
            print(num, end=" ")

# Ejemplo de uso:
lista_muestras = [10,  21,  4,  45,  66,  93]
imprimir_pares(lista_muestras)
# Salida:  10  4  66
