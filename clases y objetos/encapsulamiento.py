class Coche():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self._modelo = modelo
        self.__color = color
        
    def conducir(self):
        print(f'''Conduciendo el coche
              Marca: {self.marca}
              Modelo: {self._modelo}
              Color: {self.__color}''')
if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2' # Esto no es una buena práctica
    coche1.__color = 'Azul 2'
    coche1._Coche__color = 'Azul 3'
    coche1.conducir() # Ignoró la modificación