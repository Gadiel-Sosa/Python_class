print('*** Calculadora con funciones ***')

def suma(num1, num2):
    return f'El resultado de la suma es: {num1 + num2}'

def resta(num1, num2):
    return f'El resultado de la resta es: {num1 - num2}'

def multiplicacion(num1, num2):
    return f'El resultado de la multiplicación es: {num1 * num2}'

def division(num1, num2):
    if num2 == 0:
        print('No es posible dividir entre cero')
        return
    else:
        return f'El resultado de la división es: {num1 / num2}'

def menu():
    while True:
        print('\n----Menú----')
        print('1.- Sumar')
        print('2.- Restar')
        print('3.- Multiplicar')
        print('4.- Dividir')
        print('5.- Salir')
        
        opcion = input('Elige una opción: ')
        
        if opcion == '1':
            num1 = float(input('Ingresa el primer valor (puede ser decimal): '))
            num2 = float(input('Ingresa el segundo valor (puede ser decimal): '))
            print(suma(num1, num2))
        elif opcion == '2':
            num1 = float(input('Ingresa el primer valor (puede ser decimal): '))
            num2 = float(input('Ingresa el segundo valor (puede ser decimal): '))
            print(resta(num1, num2))
        elif opcion == '3':
            num1 = float(input('Ingresa el primer valor (puede ser decimal): '))
            num2 = float(input('Ingresa el segundo valor (puede ser decimal): '))
            print(multiplicacion(num1, num2))
        elif opcion == '4':
            num1 = float(input('Ingresa el primer valor (puede ser decimal): '))
            num2 = float(input('Ingresa el segundo valor (puede ser decimal): '))
            resultado = division(num1, num2)
            if resultado:
                print(resultado)
        elif opcion == '5':
            print('Saliendo de la calculadora ...')
            break
        else:
            print('Introduce una opción válida')

menu()


    