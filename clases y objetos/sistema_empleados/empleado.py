class Empleado:
    contador_empleado = 0
    def __init__(self, nombre:str, departamento:str):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleado += 1
        self.id = Empleado.contador_empleado
    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleado