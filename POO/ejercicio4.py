import math

class Circle:
    def __init__(self, radii):
        self.radii = radii

    def calculate_areas(self):
        return [math.pi * r**2 for r in self.radii]

    def calculate_perimeters(self):
        return [2 * math.pi * r for r in self.radii]


radii = input("Ingrese los radios de los círculos separados por comas: ")

radii = [float(r) for r in radii.split(',')]

circle = Circle(radii)

areas = circle.calculate_areas()
perimeters = circle.calculate_perimeters()

print("Áreas de los círculos:", areas)
print("Perímetros de los círculos:", perimeters)
