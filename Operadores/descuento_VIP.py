print('*** Sistema de descuento VIP ***')

compras_totales = int(input('Cuantos productos compraste hoy? '))
es_miembro = input('Eres miembro? (Si/No) ').lower().strip()

tiene_descuento = compras_totales >= 10 and es_miembro == 'si'

print(f'Tienes acceso al descuento VIP? {tiene_descuento}')

