# Definimos un diccionario
persona ={
    'Nombre': 'Juan',
    'Edad': 30,
    'Ciudad': 'Madrid',
    'Estado Civil': 'Soltero',
}

# Acceder a un dato
print(f'Nombre: {persona['Nombre']}')

# Modificar un dato
persona['Edad'] = 21
print(f'Edad: {persona["Edad"]}')

# Aañadir un nuevo elemento
persona['Profesión'] = 'Ingeniero'
print(persona)

# Eliminar un elemento
del persona['Ciudad']
print(persona)

persona.pop('Estado Civil')
print(persona)

print()
#! Iterar sobre un diccionario
for llave, valor in persona.items():
    print(f'{llave}: {valor}')
print()
#TODO Obtener los valores
for valor in persona.values():
    print(f'Valor: {valor}')
#TODO Obtener las llaves
print()
for key in persona.keys():
    print(f'Key: {key}')