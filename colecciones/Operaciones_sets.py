print('*** Operaciones con Sets ***')
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union de a | b: {union}') # se usa para unir dos conjuntos

interseccion = a & b
print(f'Intersección de a & b: {interseccion}') # valores que coinciden en ambos conjuntos

diferencia = a - b
print(f'Doferencia de los conjuntos a - b: {diferencia}') # Resta de dos conjuntos 