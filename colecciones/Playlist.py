
print('*** Playlist de Canciones ***')
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar a la playlist: '))

for indice in range(numero_canciones):
    cancion = input(f'proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

# ordenar alfabeticamente con sort
# lista_reproduccion.sort(reverse=True) # Descendente
lista_reproduccion.sort()
print(f'\nLista de reproducción en orden alfabético:')
print(lista_reproduccion)

for cancion in lista_reproduccion:
    print(cancion)