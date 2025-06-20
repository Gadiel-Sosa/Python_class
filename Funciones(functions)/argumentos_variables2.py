# *args --> arguments (argumentos) --> tupla
# **kwargs --> keyword arguments --> diccionario
print('*** Argumentos Variables con **kwargs ***')
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Más info {kwargs}')
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Dinero','Tecnología', edad=55)
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')




