# Conversión de datos

# De cadena a entero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Numero en formato cadena: {numero_cadena}')
print(f'Número entero: {numero_entero}')

# De cadena a flotante
numero_cadena = '10.9'
numero_flotante = float(numero_cadena)
print(f'\nNumero en formato cadena: {numero_cadena}')
print(f'Número flotante: {numero_flotante}')

# De número a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'\nNumero en formato entero: {numero_entero}')
print(f'Número cadena: {numero_cadena}')

# convertit a booleano
# Tipo bool es falso en los siguientes casos:
# si el valor es 0, cadena vacía o None, entonces regresa Falso
# Regresa verdadero, si el valor es distinto de 0. si es distinto de cadena vacía
# y si es distinto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f'\nValor booleano de 0: {booleano}')

numero_entero = 5
booleano = bool(numero_entero)
print(f'\nValor booleano de 5: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'\nValor booleano de una cadena vacía: {booleano}')

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'\nValor booleano de una cadena no vacía: {booleano}')

variable = None
booleano = bool(variable)
print(f'\nValor booleano de un tipo None: {booleano}')



