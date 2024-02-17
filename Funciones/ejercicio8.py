def contar_letras(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas

# Ejemplo de uso:
cadena_muestra = "EjemploDeCadena"
mayusculas, minusculas = contar_letras(cadena_muestra)
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
    