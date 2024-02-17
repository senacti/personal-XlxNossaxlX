from datetime import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def tiene_restriccion_pico_placa(self):

        fecha_hora = datetime.now()
        dia_semana = fecha_hora.weekday()
        hora = fecha_hora.hour

        if dia_semana <   5 and (hora >=   7 and hora <   9) or (hora >=   16 and hora <   19):
            return True
        else:
            return False

placa = input("Ingrese la placa del vehículo: ")

vehiculo = Vehiculo(placa)
if vehiculo.tiene_restriccion_pico_placa():
    print(f"El vehículo con placa {vehiculo.placa} tiene restricción de pico y placa.")
else:
    print(f"El vehículo con placa {vehiculo.placa} no tiene restricción de pico y placa.")
