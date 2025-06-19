print('*** Argumentos variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} = {args}')
    # Iteramos los superpoderes 
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
    
# Llamar la función
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Telaraña')