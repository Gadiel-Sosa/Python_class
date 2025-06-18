'''
La compresión de listas (list comprehension en inglés) 
es una forma rápida y concisa de crear listas en Python 
a partir de otras listas, rangos u objetos iterables, 
usando una sintaxis compacta.
'''
print('*** Compresión de Listas ***')
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

print('*** Lista de Números Pares ***')
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)

print('*** Saludando a Cada Nombre ***')
nombres = ['Ana', 'Miguel', 'Juan']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)