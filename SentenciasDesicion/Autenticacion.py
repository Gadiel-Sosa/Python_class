print('*** Sistema de Autenticación ***')
USUARIO = 'admin'
PASSWORD = '157'

usuario = input('Usuario: ')
password = input('Password: ')

if usuario == USUARIO and password == PASSWORD:
    print(f'Bienvenido al sistema usuario {USUARIO}')
elif usuario == USUARIO:
    print(f'El password es incorrecto, intente de nuevo')
elif password == PASSWORD:
    print('El usuario es incorrecto, intente de nuevo')
else:
    print('Usuario y password incorrectos, intente de nuevo')


