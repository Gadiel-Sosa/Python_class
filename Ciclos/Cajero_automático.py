print('*** Cajero Automático ***')
saldo_inicial = 0.0
salir = False
while not salir:
    print('''Menú:
    1. Consulta de saldo
    2. Depositar
    3. Retirar
    4. Salir''')
    opcion = int(input('Ingresa una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es de: ${saldo_inicial:.2f}\n')
    elif opcion == 2:
        deposito = float(input('Ingresa la cantidad a depositar: '))
        saldo_inicial += deposito
        print(f'Se ha depositado ${deposito} a tu cuenta bancaria')
        print(f'Tu nuevo saldo es: ${saldo_inicial}')
    elif opcion == 3:
        retiro = float(input('Ingresa la cantidad a retirar: '))
        if retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print(f'Se ha retirado ${retiro} de la cuenta')
            print(f'Saldo actual: ${saldo_inicial}')
        else:
            print('Saldo insuficiente, favor de realizar un deposito')
    elif opcion == 4:
        print('Saliendo del sistema...')
        salir = True
