class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
        return f'Id: {self.id_computadora}, Nombre: {self.nombre}, Monitor: {self.monitor}, Teclado: {self.teclado}, Ratón: {self.raton}'
    @property
    def nombre(self):
        return self._nombre
    @property
    def monitor(self):
        return self._monitor
    @property
    def teclado(self):
        return self._teclado
    @property
    def raton(self):
        return self._raton
    @property
    def id_computadora(self):
        return self._id_computadora