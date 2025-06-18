print('*** Dibujar un rectangulo simetrico ***')
numero_filas = int(input('Proporciona el numero de filas: '))
for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    ateriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{ateriscos}')