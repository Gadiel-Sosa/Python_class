from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
# No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)
