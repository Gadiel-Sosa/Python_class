class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def __str__(self):
        return f"Detalle persona\nNombre: {self.nombre}\nEdad: {self.edad}"
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
        