print('*** Sistema de descuentos de la tienda online ***')
compra = int(input('Cúal fue el monto de su compra? '))
es_miembro = input('Es miebro de la tienda? (si/no) ').lower().strip()
MONTO_MINIMO = 1000
if compra >= MONTO_MINIMO and es_miembro == 'si':
    print('---Obtuvo un descuento del 10%---')
    print(f'Monto de compra: {compra}')
    descuento = compra * 0.10
    print(f'Descuento equivalente al 10%: {descuento}')
    total_final = compra - descuento
    print(f'Total despues del desceunto: {total_final}')
elif es_miembro == 'si':
    print('Felicidades, obtuviste el 5% de descuento')
    descuento = compra * 0.05
    total_final = compra - descuento
    print(f'Monto de compra: {compra}')
    print(f'Descuento equivalente al 5%: {descuento}')
    print(f'Total final: {total_final}')
else:
    print('''
    No obtuviste ningun descuento
    te invitamos a hacerte miembro de la tienda
    ''')
    print(f'Monto final de la compra: {compra}')
