print('*** Suma con argumentos variables ***')
def sumar(*args):
    total = 0
    for numero in args:
        total +=numero
    return total
print(f'Resultado de la suma: {sumar(1,3,6,2,1,9)}')
        
    