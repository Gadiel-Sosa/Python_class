resultado = None
try:
    a = int(input('Ingresa un número: '))
    b = int(input('Ingresa otro número: '))
    resultado = a / b
except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}')
except TypeError as e:
    print(f'Ocurrió un error: {e}')
except ValueError as e:
    print(f'Ocurrió un error: {e}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(resultado)