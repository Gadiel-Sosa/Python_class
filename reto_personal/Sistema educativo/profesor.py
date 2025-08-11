from persona import Persona
class Profesor(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__cursos_impartidos = []
    def asignar_curso(self, curso):
        self.__cursos_impartidos.append(curso)
    def __str__(self):
        return f'{super().__str__()}\nTotalCursos: {len(self.__cursos_impartidos)}\nCursos: {self.cursos_impartidos}'
    @property
    def cursos_impartidos(self):
        return self.__cursos_impartidos