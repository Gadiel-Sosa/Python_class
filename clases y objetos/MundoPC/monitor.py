class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        self._marca = marca
        self._tamanio = tamanio
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
    def __str__(self):
        return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'
    
    @property
    def marca(self):
        return self._marca
    @property
    def tamanio(self):
        return self._tamanio
    @property
    def id_monitor(self):
        return self._id_monitor
        