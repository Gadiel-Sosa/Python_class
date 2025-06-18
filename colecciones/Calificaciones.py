print('*** Sistema de Calificaciones ***')

numero_calificaciones = int(input('Ingresa el # de calificaciones: '))
calificacion_total = 0
lista_calificaciones = []

for i in range(numero_calificaciones):
    calificacion = float(input(f'Ingresa la calificación {i+1}: '))
    lista_calificaciones.append(calificacion)
    calificacion_total += calificacion
total = calificacion_total / numero_calificaciones
print(f'Las calificaciones proporcionadas son: {lista_calificaciones}')
print(f'El prodedio de las calificaciones es: {total:.2f}')