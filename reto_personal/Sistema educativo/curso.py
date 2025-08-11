class Curso:
    def __init__(self, nombre_curso, descripcion):
        self._nombre_curso = nombre_curso
        self._descripcion = descripcion
    def __str__(self):
        return f'Nombre del Curso: {self.nombre_curso}\nDescipción: {self.descripcion}'
    
    @property
    def nombre_curso(self):
        return self._nombre_curso
    @property
    def descripcion(self):
        return self._descripcion
    @nombre_curso.setter
    def nombre_curso(self, nuevo_nombre):
        self._nombre_curso = nuevo_nombre
    @descripcion.setter
    def descripcion(self, nueva_descr):
        self._descripcion = nueva_descr