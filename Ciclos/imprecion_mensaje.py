print('*** Imprecion de un mensaje ***')
mensaje = input('proporciona un mensaje a repetir: ')
n = int(input('Proporciona el numero de repeticiones: '))

for i in range(n):
    print(f'{i} - {mensaje}')