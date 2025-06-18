print('*** Operadores de asignación ***')
numero = 5
print(f'valor de número: {numero}')
numero = 10
print(f'valor de número: {numero}')
cadena = 'Saludos desde Python'
print(f'Cadena: {cadena}')

print('\nb*** Asignación Múltiple ***')
x, y, z = 5, 'hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

print('\n*** Asignación Encadenada ***')
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')
print()
# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f'Invertir valores x = {x}, y = {y}')
print()
# Resibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')
