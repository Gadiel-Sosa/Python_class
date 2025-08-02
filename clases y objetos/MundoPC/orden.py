class Orden:
    contador_ordenes = 0
    def __init__(self):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = []
    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)
    def __str__(self):
        compu = [str(comp) for comp in self._computadoras]
        return f'Id: {self.id_orden}, Computadoras: {compu}'
    @property
    def id_orden(self):
        return self._id_orden
    @property
    def computadoras(self):
        return self._computadoras