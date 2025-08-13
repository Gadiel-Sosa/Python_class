resultado = None
a = 10
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}') # Excepción más específica
except TypeError as e:
    print(f'Ocurrió un error: {e}') # Excepción más específica
except Exception as e:
    print(f'Ocurrió un error: {e}') # Excepción más general
    
print(resultado)
print('continuamos...')