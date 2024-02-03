nombre = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 100:
    print("Por favor, ingrese una edad válida.")
elif edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
