class Mascota:
    def __init__(self, nombre, especie, edad, dueño):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._dueño = dueño
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def especie(self):
        return self._especie
    @property
    def edad(self):
        return self._edad
    @property
    def dueño(self):
        return self._dueño
