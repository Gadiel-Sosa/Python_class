# Crear un reloj que actualice la hora actual cada segundo
import time
def reloj():
    while True:
        hora_actual = time.strftime('%H:%M:%S')
        print(hora_actual)
        time.sleep(1)
reloj()