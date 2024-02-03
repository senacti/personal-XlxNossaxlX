edad = int(input("Ingrese su edad: "))

genero = input("Ingrese su género (masculino o femenino): ")

if genero.lower() == 'femenino':
    pulsaciones = (220 - edad) / 10
elif genero.lower() == 'masculino':
    pulsaciones = (210 - edad) / 10
else:
    print("Género no reconocido. Por favor, ingrese 'masculino' o 'femenino'.")
    exit()

print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: ", pulsaciones)
