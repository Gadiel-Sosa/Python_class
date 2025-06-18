
print('*** Sistema de envios ***')

destino = input('Cuál es el destino del paquete (nacional/Internacional): ').strip().lower()
peso = float(input('Ingresa el peso del paquete en kg: '))
tarifa_nacional = 10
tarifa_internacional = 20

if destino == 'nacional':
    costo_peso = tarifa_nacional * peso
elif destino == 'internacional':
    costo_peso = tarifa_internacional * peso
else:
    print('Destino no válido')
print()
print(f'Destino: {destino}')
print(f'Peso paquete: {peso} kg')
print(f'Costo paquete: ${costo_peso}')



