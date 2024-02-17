from functools import reduce

def multiplicar_lista(lista_numeros):
    return reduce((lambda x, y: x * y), lista_numeros)

# Ejemplo de uso:
lista_muestras = [8,  2,  3, -1,  7]
resultado = multiplicar_lista(lista_muestras)
print(resultado)  # Imprime: -336
