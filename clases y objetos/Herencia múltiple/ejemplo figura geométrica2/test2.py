from cuadrado2 import Cuadrado
from rectangulo import Rectangulo

# Creamos los objetos para el cuadrado
cuadrado1 = Cuadrado(10, 'Rojo')
cuadrado1.calcular_area()
print(cuadrado1)
cuadrado1.alto = 20
print(cuadrado1)

# Creamos los objetos para el rectángulo
regtangulo1 = Rectangulo(10,20,'Verde')
regtangulo1.calcular_area()
print(regtangulo1)
regtangulo1.ancho = 10
print(regtangulo1)
