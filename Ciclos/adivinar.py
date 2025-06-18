
from random import randint

print('*** Adivina el número secreto ***')

numero_secreto = randint(1, 50)

contador = 0
intentos = 10
numero_usuario = None
while numero_usuario != numero_secreto and contador < intentos:
    if contador < intentos:
        numero_usuario = int(input('Ingresa un número entre 1 y 50: '))

    if numero_usuario < numero_secreto:
        print(f'El número secreto es mayor que {numero_usuario}')
    else:
        print(f'El número secreto es menor que {numero_usuario}')

    contador += 1

if numero_usuario == numero_secreto:
    print('¡Felicidades! Adivinaste el número secreto.')
else:
    print(f'Se acabaron tus intentos. El número secreto era {numero_secreto}.')
