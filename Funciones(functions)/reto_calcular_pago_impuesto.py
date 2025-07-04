print('*** Pago con impuesto ***')

def pago_final():
    pago = float(input('Ingresa el monto del pago: '))
    impuesto = float(input('Ingresa el porcentaje de impuesto: '))
    total = pago + pago * (impuesto/100)
    return f'Pago con impuestos: {total}'

print(pago_final())