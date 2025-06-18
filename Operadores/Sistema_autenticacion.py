print('*** Sistema de Auetnticación ***')
usuario_input = input('Introduce el usuario: ')
password_input = int(input('Introduce la contraseña: '))

usuario = 'admin'
password = 100105
hay_acceso = (usuario_input.strip() == usuario
              and password_input.strip() == password)

print(f'Acceso al sistema? {hay_acceso}')

