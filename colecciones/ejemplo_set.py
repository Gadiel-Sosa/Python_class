print('Sets en Python')
my_set = {1, 2, 3, 4, 5, 5}  # Los sets no permiten duplicados
# No se manejan índices
print(f'set: {my_set}')

my_set.add(10)
print(f'set: {my_set}')

set2 = {'Juan', 'Pedro', 'Maria'}
set2.add('Juan')
print(f'set2: {set2}')

set2.remove('Maria')
print(f'set2: {set2}')

set2.pop()
print(f'set2: {set2}')
set1 = set2.copy()
print(f'set1: {set1}')

print()
print()
# Operaciones con sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'unión: {union}')

interseccion = a & b
print(f'intersección: {interseccion}')

diferencia = a - b
print(f'diferencia: {diferencia}')