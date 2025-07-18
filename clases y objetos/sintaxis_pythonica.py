class Coche():
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color
    def conducir(self):
        print(f'''Conduciendo el coche
            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}''')
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    # Creación primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Rojo')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean públicos 
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Rojo 2'
    # Intentar añadir un atributo nuevo
    setattr(coche1,'Nuevo_atributo', 'Valor atributo')
    print(coche1.Nuevo_atributo)
    coche1.conducir()
    coche1.marca = 'Toyota 3'
    print(f'Atributo marca coche1: {coche1.marca}')
    # Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo}')
    print(f'Atributos del cohe1: {coche2.__dict__}')
    
