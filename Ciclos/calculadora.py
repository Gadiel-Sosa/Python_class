print('*** Calculadora ***')
resultado = 0.0
salir = False

while not salir:
    print('''Opciones de la calculadora
    1. Sumar dos números
    2. Restar dos números
    3. Multiplicar dos números
    4. Dividir dos números
    5. Salir''')
    numero1 = float(input('Ingresa el primer número: '))
    numero2 = float(input('Ingresa el segundo número: '))

    opcion = int(input('Ingresa una opción: '))


    if opcion == 1:

        resultado = numero1 + numero2
        print(f'El resultado de sumar {numero1:.2f} + {numero2:.2f} es: {resultado:.2f}')
    elif opcion == 2:

        resultado = numero1 - numero2
        print(f'El resultado de restar {numero1:.2f} - {numero2:.2f} es: {resultado:.2f}')
    elif opcion == 3:

        resultado = numero1 * numero2
        print(f'El resultado de multiplicar {numero1:.2f} * {numero2:.2f} es: {resultado:.2f}')
    elif opcion == 4:

        if numero2 == 0:
            print('¡No se puede dividir entre 0!')
        else:
            resultado = numero1 / numero2
            print(f'El resultado de dividir {numero1:.2f} / {numero2:.2f} es: {resultado:.2f}')
    elif opcion == 5:
        print('Saliendo de la calculadora...')
        salir = True

