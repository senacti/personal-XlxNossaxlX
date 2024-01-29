salario_diario = int(input("Ingrese el salario diario del empleado: "))

dias_trabajados = int(input("Ingrese el número de días trabajados: "))

# Calcula el salario 
salario_bruto = salario_diario * dias_trabajados

# Descontar el 10% y el 15% 
pension = salario_bruto * 0.10
salud = salario_bruto * 0.15

salario_neto = salario_bruto - pension - salud

print("El salario neto a pagar al empleado es: ", salario_neto)
