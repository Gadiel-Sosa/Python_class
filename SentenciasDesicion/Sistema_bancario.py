print('*** Bie4nvenido al sistema bancario ***')
salir_sistema_txt = input('Deseas salir del sistema? (si/no)')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos destro del sistema')
else:
    print('Saliendo del sistema...')