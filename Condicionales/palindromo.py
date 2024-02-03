frase = input("Ingrese la frase: ")

frase_transformada = frase.lower()
frase_sin_espacios = frase_transformada.replace(" ", "")
frase_invertida = frase_sin_espacios[::-1]

print("Frase original:", frase_transformada)
print("Frase sin espacios:", frase_sin_espacios)
print("Frase invertida:", frase_invertida)

if frase_sin_espacios == frase_invertida:
    print("La frase o palabra es un palíndromo")
else:
    print("La frase o palabra no es un palíndromo")
