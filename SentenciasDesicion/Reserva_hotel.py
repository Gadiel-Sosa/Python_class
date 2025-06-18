
print('*** Sistema de Reserva de Hotel')
nombre = input('Ingresa tu nombre: ')
dias_estancia = int(input('Días de estancia: '))
cuarto_con_vista_mar = input('Desea un cuarto con vista al mar? (si/no) ').strip().lower()

vista_mar = 'si' if cuarto_con_vista_mar == 'si' else 'no'

CON_VISTA_MAR = 150.50
SIN_VISTA_MAR = 190.50

if vista_mar == 'si':
    costo_total = dias_estancia * CON_VISTA_MAR
    print('----------Detalles de la reserva----------')
    print(f'Cliente: {nombre}')
    print(f'Días estancia: {dias_estancia}')
    print(f'Costo total: {costo_total}')
    print(f'Habitación con vista al mar: {vista_mar}')
else:
    costo_total = dias_estancia * SIN_VISTA_MAR
    print('----------Detalles de la reserva----------')
    print(f'Cliente: {nombre}')
    print(f'Días estancia: {dias_estancia}')
    print(f'Costo total: {costo_total}')
    print(f'Habitación con vista al mar: {vista_mar}')



