# Formato de cadenas
nombre = 'Juan'
edad = 30
mensaje = f'Hola me llamo {nombre} y tengo {edad} años'
print(mensaje)

# Metodo format
mensaje = 'Hola me llamo {} y tengo {} años'.format(nombre, edad)
print(mensaje)
def suma(a,b):
    return a + b
def imp(resultado, mensaje2):
    print(mensaje2)
a = float(input('Captura un número: '))
b = float(input('Captura otro número: '))

resultado = suma(a,b)
mensaje2 = f'El resultado de sumar {a} y {b} es {resultado}'
imp(resultado,mensaje2)
