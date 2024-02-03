monto = float(input("Ingrese el monto de la cuenta: "))


if monto < 150000:
    print("Pago en efectivo.")
elif 150000 <= monto < 300000:
    print("Pago con el celular (dinero electrónico).")
elif 300000 <= monto < 600000:
    print("Pago con la tarjeta de débito.")
else:
    print("Pago con la tarjeta de crédito.")
