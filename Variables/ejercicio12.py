import math

cateto1 = int(input("Ingrese la longitud del primer cateto: "))
cateto2 = int(input("Ingrese la longitud del segundo cateto: "))

# Calcula la hipotenusa, math.sqrt para calcular la raiz cuadrada 
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa del triángulo rectángulo es: ", hipotenusa)
