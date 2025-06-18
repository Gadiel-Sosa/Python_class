print('*** Sistema de Calificaicones ***')

calificacion = float(input('Ingrsa la calificacion entre o y 10: '))
calificacion_letra = None

if 9 <= calificacion <= 10:
    calificacion_letra = 'A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Valor desconocido'

print(f'La calificacion {calificacion} es equivalente a la letra {calificacion_letra}')

