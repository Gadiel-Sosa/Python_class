from empleado import Empleado
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        
    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)
    def obtener_num_empleados_dep(self, departamento):
        contador_empleado_dep = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleado_dep += 1
                
        return contador_empleado_dep
    def obtener_total_empleados(self):
        print(f'\nTotal de empleados para la empresa {self.nombre}')
        for empleado in self.empleados:
            print(f'''Empleado {empleado.id}
                  Nombre: {empleado.nombre}
                  Dep: {empleado.departamento}
                  ''')