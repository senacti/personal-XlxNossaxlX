def es_palindromo(cadena):
    cadena = cadena.lower().replace(' ', '')
    return cadena == cadena[::-1]

# Ejemplo de uso:
cadena_muestra = "Ana"
print(es_palindromo(cadena_muestra))  # Imprime: True
