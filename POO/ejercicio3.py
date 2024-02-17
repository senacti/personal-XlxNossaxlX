import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius **  2)

    def calculate_perimeter(self):
        return  2 * math.pi * self.radius

radius = float(input("Ingrese el radio del círculo: "))

circle = Circle(radius)

print("Área del círculo:", circle.calculate_area())
print("Perímetro del círculo:", circle.calculate_perimeter())
