from estudiante import Estudiante
from profesor import Profesor
class Asistente(Estudiante, Profesor):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__cursos_impartidos = []
    def __str__(self):
        return super().__str__()
    
if __name__ == '__main__':
    asis = Asistente('Juan', 25)
    asis.inscribir_curso('Python')
    asis.asignar_curso('Poo')
    print(asis)