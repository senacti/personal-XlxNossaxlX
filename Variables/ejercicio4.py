from datetime import date #Colocar la fecha actual 

def calcular_edad(nacimiento):
    hoy = date.today()
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

fecha_nacimiento = date(anio_nacimiento, 1, 1) # Se establece el dia y el mes

edad = calcular_edad(fecha_nacimiento)

print("Tu edad es: ", edad)
