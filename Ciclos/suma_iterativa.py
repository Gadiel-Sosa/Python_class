print('*** Suma Acumulativa ***')
MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1
    print(f'Suma parcial acumulada: {acumulador_suma}')
    print()
print(f'\nResultado de la suma acumulada: {acumulador_suma}')


