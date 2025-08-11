class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
# Encapsulamiento getter y setter
    # Getter ancho
    @property
    def ancho(self):
        return self._ancho
    #Getter alto
    @property
    def alto(self):
        return self._alto
    #Setter ancho
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
    #Setter alto
    @alto.setter
    def alto(self, valor):
        self._alto = valor
        
        