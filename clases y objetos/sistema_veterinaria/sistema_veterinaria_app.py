from mascotas import Mascota
from veterinaria import Veterinaria

# Crear la veterinaria
dogtor = Veterinaria('Dog Tor')
print(f'*** Bienvenidos a la veterinaria {dogtor.nombre} ***')

# Crear mascotas
mascota1 = Mascota('Felix', 'Gato', 4, 'Miguel')
mascota2 = Mascota('Zeus', 'Perro', 3, 'Juan')

# Agregar mascotas a la veterinaria
dogtor.agregar_mascota(mascota1)
dogtor.agregar_mascota(mascota2)

# Realizar búsquedas
print("\nBuscar por especie 'Gato':")
dogtor.buscar_por_especie('Gato')

print("\nBuscar por dueño 'Juan':")
dogtor.buscar_por_dueño('Juan')

print("\nBuscar por nombre 'Felix':")
dogtor.buscar_por_nombre('Felix')

# Mostrar todas las mascotas
print("\nTodas las mascotas registradas:")
dogtor.mostrar_todas_mascotas()
