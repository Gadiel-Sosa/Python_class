from figura2 import FiguraGeometrica
from color2 import Color
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    def calcular_area(self):
        return self.alto * self.ancho
    def __str__(self):
        return f'''Área de un rectángulo
        {super().__str__()}
        Resultado: {self.calcular_area()}
        Color: {self.color}'''
    