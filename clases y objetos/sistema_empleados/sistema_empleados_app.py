from empresa import Empresa
from empleado import Empleado
print('Sistema de empleados')

#Creamos las instancias de la empresa
empresa1 = Empresa('Google')

#Contratar empleados

empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')

# Obtener total de objetos de tipo empleado

print(f'Total de empleados: {Empleado.obtener_total_empleados()} ')

# Obtener empleados en Ventas
print(f'Empleados en departamento de ventas: {empresa1.obtener_num_empleados_dep("Ventas")}')

#Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()