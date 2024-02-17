class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def calcular_area(self):
        return self.longitud * self.anchura


longitud = int(input("Ingrese la longitud del rectángulo: "))
anchura = int(input("Ingrese la anchura del rectángulo: "))

rectangulo = Rectangle(longitud, anchura)


print("El área del rectángulo es:", rectangulo.calcular_area())
