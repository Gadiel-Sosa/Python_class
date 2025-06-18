print('*** Listas y Diccionarios ***')
#* Creamos la lista de diccionarios
personas = [
    {
        'Nombre':'Regina',
        'Apellido': 'Mensoza',
        'Edad': 25
     },
    {
        'Nombre': 'Alejandro',
        'Apellido': 'Reyes',
        'Edad': 30
    }
]

#! Imprimir la lista de diccionarios
print(personas)
print()
#* Acceder a un diccionario desde una lista (en este caso a regina que está en la posición 0 de la lista)

#* .get se usa para recuperar los valores de las llaves del diccionario
print('Accediendo a un diccionario desde una lista:')
print(f'''
      Nombre: {personas[0].get('Nombre')}
      Apellido: {personas[0].get('Apellido')}
      Edad: {personas[0].get('Edad')}
      ''')

#! Recorrer los elementos de la lista
print() # Salto de línea
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    
#* Imprimir los valores de cada diccionario
#print(f'Detalle: Nombre: {persona.get('Nombre')}, Apellido: {persona.get('Apellido')}, Edad: {persona.get('Edad')}')
# Nota: enumerate devuelve el índice y el valor del elemento en la lista al mismo tiempo.