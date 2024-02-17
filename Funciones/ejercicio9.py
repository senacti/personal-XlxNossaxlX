def lista_unica(lista):
    return list(set(lista))

# Ejemplo de uso:
lista_duplicados = [1,  2,  3,  1,  2,  3,  4,  5,  4]
lista_unicos = lista_unica(lista_duplicados)
print(lista_unicos)  # Imprime: [1,  2,  3,  4,  5]
