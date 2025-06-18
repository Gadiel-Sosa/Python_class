print('*** Manejo de Listas ***')
mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista {len(mi_lista)}')

# Acceder a los elementos de la lisrta por índice
print(f'Accedemos a los elementos de la lista en índice 4: {mi_lista[4]}')
print(f'Accedemos al último valor: {mi_lista[-1]}')

# Modificar los elementos de la lista
mi_lista[1] = 10
print(f'Modificamos el valor del índice 1: {mi_lista[1]}')

# Agregar un nuevo eleemnto al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> se agregó eol elemento 6')

# Añadir un nuevo elemento en un índice específico
mi_lista.insert(2, 15)
print(f'{mi_lista} -> se añadió el valor de 15 en el indice 2')

# Eliminar elementos de una lista
mi_lista.remove(5) # se remueve por valor del eleemnto no por índice
print(f'{mi_lista} -> se removió el valor 5')
# Removemos por índice
mi_lista.pop(1)
print(f'{mi_lista} -> se eliminó el índice 1')
# usando del
del mi_lista[2]
print(f'{mi_lista} -> se eliminó el índice 2')

# obtener sublistas
sub_lista = mi_lista[1:3] # genera una sublista del indice 1 al 2
print(f'{sub_lista} -> sublista genrada a aprtir de los índices 1:3')
