from random import randint
nombre_usuario = input('Introduce uno de tus nombres: ')
apellido_usuario = input('Introduce uno de tus apellidos: ')

año_nacimineto = str(input('Introduce tu año de nacimiento: '))

letras_nombre = nombre_usuario[0:2].upper().strip()
letras_apellido = apellido_usuario[0:2].upper().strip()
numeros_año_nacimiento = año_nacimineto[2:4].strip()

numeros_random = randint(1000,9999)

id_unico = f'{letras_nombre}{letras_apellido}{numeros_año_nacimiento}{numeros_random}'
print(id_unico)

