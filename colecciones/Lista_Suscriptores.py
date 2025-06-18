print('*** Sistema de Suscriptores ***')
suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de ssucriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = 'karla@mail.com'
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor ya se ha agregado a la sista de suscriptores {nuevo_suscriptor}')

print(f'Lista de ssucriptores actualizada: {suscriptores}')

suscriptor_eliminar = 'elena@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de ssucriptores actualizada: {suscriptores}')
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

print('------Lista de Suscriptores------')
for suscriptor in suscriptores:
    print('-',suscriptor)