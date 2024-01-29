suma = 0     # Inicializa la suma de la variable 

for _ in range(5): # Ejecuta el bucle 5 veces
    num = int(input("Ingresa un número: ")) 
    suma += num 

promedio = suma / 5 

print("El promedio de los números ingresados es: ", promedio)
