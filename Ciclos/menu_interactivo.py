print('*** Sistema de Administración de Cuentas ***')
salir = False
while not salir:
    print(f'''Menú:
    1. Crear cuenta
    2. Eliminar cuenta
    3. salir''')
    opcion = int(input('Elige una opción: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema...\n')
        salir = True
    else:
        print('Opción inválida\n')
