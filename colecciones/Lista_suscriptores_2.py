
print('*** Lista de Suscriptores ***')
suscriptores = set()
numero_ssucriptores = int(input('Ingresa el # de suscriptores a registrar: '))

for i in range(numero_ssucriptores):
    suscriptor = input(f'Ingresa el correo del suscriptor {i+1}: ')
    if suscriptor in suscriptores:
        print(f'El suscriptor {suscriptor} ya está en la lista')
    else:
        suscriptores.add(suscriptor)
eliminar_suscriptor = input('Ingresa el suscriptor a eliminar: ')
suscriptores.remove(eliminar_suscriptor)

for suscriptor in suscriptores:
    print('-', suscriptor)

