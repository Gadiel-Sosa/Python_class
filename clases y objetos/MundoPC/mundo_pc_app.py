from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from orden import Orden

print('*** Mundo PC ***')

# Computadora 1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

# Computadora 2
teclado2 = Teclado('HP', 'USBC')
raton2 = Raton('HP', 'USBC')
monitor2 = Monitor('HP', 33)
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

# Orden
orden1 = Orden()
orden1.agregar_computadora(computadora1)
orden1.agregar_computadora(computadora2)
print(orden1)
 