class Veterinaria:
    def __init__(self, nombrev):
        self._nombrev = nombrev
        self._mascotas = []
    def agregar_mascota(self, mascota):
        self._mascotas.append(mascota)
    def buscar_por_especie(self, especie):
        for mascota in self._mascotas:
            if mascota.especie.lower() == especie.lower():
                self.mostrar_mascota(mascota)
    def buscar_por_dueño(self, dueño):
        for mascota in self._mascotas:
            if mascota.dueño.lower() == dueño.lower():
                self.mostrar_mascota(mascota)
    def buscar_por_nombre(self, nombre):
        for mascota in self._mascotas:
            if mascota.nombre.lower() == nombre.lower():
                self.mostrar_mascota(mascota)
    def mostrar_mascota(self, mascota):
        print(f'Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad}, Dueño: {mascota.dueño}')
    def mostrar_todas_mascotas(self):
        for mascota in self._mascotas:
            self.mostrar_mascota(mascota)
    @property
    def nombre(self):
        return self._nombrev
    @property
    def mascotas(self):
        return self._mascotas
    
        
    