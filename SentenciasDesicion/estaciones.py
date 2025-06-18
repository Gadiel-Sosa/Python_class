print('*** Estaciones del año ***')
entrada_mes = int(input('Ingrsa el número de mes: '))
estacion = None

if entrada_mes == 1 or entrada_mes == 2 or entrada_mes == 12:
    estacion = 'Invierno'

elif entrada_mes == 3 or entrada_mes == 4 or entrada_mes == 5:
    estacion ='Primavera'

elif entrada_mes == 6 or entrada_mes == 7 or entrada_mes == 8:
    estacion = 'Verano'

elif entrada_mes == 9 or entrada_mes == 10 or entrada_mes == 11:
    estacion = 'Otoño'

else:
    estacion = 'Estación desconocida'

print(f'La estación para el mes {entrada_mes} es {estacion}')

