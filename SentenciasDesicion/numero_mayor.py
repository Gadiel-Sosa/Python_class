print('*** Número Mayor ***')
numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))

if numero1 > numero2:
    print(f'El número 1 ({numero1}) es mayor que  el número 2 ({numero2})')
elif numero2 > numero1:
    print(f'El número 2 ({numero2}) es mayor que el número 1 ({numero1})')
else:
    print(f'Los números {numero1} y {numero2 } son iguales')

