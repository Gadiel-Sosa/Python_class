print('*** Manejo de Tuplas ***')
mi_tupla = (1, 2, 3, 4, 5, 6)
print(mi_tupla)

# mi_tupla[0] = 10  -> error
# mi_tupla.append(10) -> error

for elemento in mi_tupla:
    print(elemento, end=' ')

'''
Crear una tupla para una coordenada x, y
'''
coordenadas = (3, 5)
print(f'\nCoordenada en el eje x {coordenadas[0]}')
print(f'\nCoordenada en el eje y: {coordenadas[1]}')

tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

tupla_anidada = (1, (2, 3), (4, 5))
print(f'Segundo elemento de la tupla anidada: {tupla_anidada[1]}')