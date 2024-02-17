def esta_en_rango(numero, limite_inferior, limite_superior):
    return limite_inferior <= numero <= limite_superior

# Ejemplo de uso:
numero_muestra =  15
limite_inferior =  10
limite_superior =  20

print(esta_en_rango(numero_muestra, limite_inferior, limite_superior))  # Imprime: True
