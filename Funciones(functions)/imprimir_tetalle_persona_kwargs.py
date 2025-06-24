print('*** Detalle persona usando kwargs ***')
# Función que acepta argumentos variables en forma key-value
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamar a la función
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')