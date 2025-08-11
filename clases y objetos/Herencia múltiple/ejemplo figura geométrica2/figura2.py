class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho 
    @property
    def alto(self):
        return self._alto
    @property
    def ancho(self):
        return self._ancho
    @alto.setter
    def alto(self, valor):
        self._alto = valor
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
    def __str__(self):
        return f'''Detalle de la figura
        Alto: {self.alto}
        Ancho: {self.ancho}'''
