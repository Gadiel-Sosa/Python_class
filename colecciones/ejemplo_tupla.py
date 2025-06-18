print('*** Manejo de tuplas ***')
my_tupla = (1, 2, 3, 4, 5)
print('Tupla:', my_tupla)
# No se puede modificar una tupla  
# my_tupla[0] = 10  # Esto causaría un error
for elemento in my_tupla:
    print('elemento: ',elemento, end=' ')
print('\n') 
# Tupla anidada
tupla_anidada = (1, (2, 3), (4, 5))
for elemento in tupla_anidada:
    print('elemento anidado: ', elemento, end=' ')