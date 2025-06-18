print('*** Aplicacion de salud y fitnes ***')
META_PASOS_DIARIO = 10000
CALORIA_POR_PASO = 0.04

nombre = input('Cúal es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos caminaste hoy? '))

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO

meta_alcanzada_txt = 'si' if meta_alcanzada else 'no'

calorias_quemadas = pasos_diarios * CALORIA_POR_PASO

print()
print(f'\nUsuario: {nombre}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorías quemadas: {calorias_quemadas}')
print(f'Meta de pasos alcanzada: {meta_alcanzada_txt}')