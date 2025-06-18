print('*** Sistema de Validación ***')

password = input('Ingresa tu password (Mínimo 6 caracteres): ')

while len(password) < 6:
    print('El password no tiene 6 caracteres, ingrese un password válido')
    password = input('Ingresa tu password (Mínimo 6 caracteres): ')
else:
    print('Password válido ')

