from persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__cursos_inscritos = []
    def inscribir_curso(self, curso):
        self.__cursos_inscritos.append(curso)
    def __str__(self):
        return f'{super().__str__()}\nCursos inscritos: {len(self.__cursos_inscritos)}\nDetalle cursos: {self.cursos_inscritos}'
    @property
    def cursos_inscritos(self):
        return self.__cursos_inscritos
    
if __name__ == '__main__':
    estudiante1 = Estudiante('Miguel', 23)
    estudiante1.inscribir_curso('Matemáticas')
    print(estudiante1)
    