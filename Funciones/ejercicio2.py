import math

def area_circulo(radio):
    return math.pi * (radio **  2)

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) /  2

# Ejemplo de uso:
radio_circulo =  5
base_rectangulo =  7
altura_rectangulo =  4
base_triangulo =  6
altura_triangulo =  3

print("Área del círculo:", area_circulo(radio_circulo))
print("Área del rectángulo:", area_rectangulo(base_rectangulo, altura_rectangulo))
print("Área del triángulo:", area_triangulo(base_triangulo, altura_triangulo))
