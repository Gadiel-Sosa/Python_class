print('*** Función par ***')
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    numero = int(input('Proporciona un número: '))
    print(f'Es par? {es_par(numero)}')