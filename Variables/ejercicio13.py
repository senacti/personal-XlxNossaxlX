tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))

minutos = tiempo_segundos // 60
horas = minutos // 60

segundos = tiempo_segundos % 60
minutos = minutos % 60

print("El tiempo en horas y minutos es: ", horas, ":", minutos, ":", segundos)
