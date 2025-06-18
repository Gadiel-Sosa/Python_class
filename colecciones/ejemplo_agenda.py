# Diccionarios de diccionarios
print('*** Agenda de contactos ***')

agenda = {
    'Juan': {
        'Phone': '123456789',
        'Email': 'prueba@hotmail.com',
        'Address': 'False street 123',
    },
    'Maria': {
        'Phone': '987654321',
        'Email': 'maria@gmail.com',
        'Address': 'central avenue 456',
    },
    'Pedro': {
        'Phone': '559210487',
        'Email': 'pedro@hotmail.com',
        'Address': 'unknown street 789',
    }
   
}

print(agenda)

# Acceder a un contacto
print(f"Contacto de Juan: {agenda['Juan']['Phone']}")
print(f'Email de Juan: {agenda.get('Juan').get('Email')}')

# Añadir un nuevo contacto
agenda['Ana'] = {
    'Phone': '555123456',
    'Email': 'hola@gmail.com',
    'Address': 'new street 101'
    }
print(agenda)

# ERliminar un contacto
agenda.pop('Pedro')
del agenda['Maria']
print(agenda)

# Mostrar los contactos de la agenda
for contacto, detalle in agenda.items():
    print(f'''
          Nombre: {contacto}
          Teléfono: {detalle.get('Phone')}
          Email: {detalle.get('Email')}
          Dirección: {detalle.get('Address')}
          ''')