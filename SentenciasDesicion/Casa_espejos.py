print('*** Bienvenido a la casa de los espejos ***')
edad = int(input('Captura tu edad: '))
tienes_miedo_txt = input('Tienes miedo a la oscuridad (si/no)? ').strip().lower()
tienes_miedo = tienes_miedo_txt == 'si'

if not tienes_miedo and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('No puedes entrar a la casa de los espejos')
