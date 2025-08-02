class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print(f'{self.nombre} está comiendo')
class Perro(Animal):
    def comer(self):
        print(f'{self.nombre} está comiendo croquetas')
class Vaca(Animal):
    def comer(self):
        print(f'{self.nombre} está comiendo pasto')
        
def alimentar_animales(animal):
    animal.comer()

max = Perro('Max')
alimentar_animales(max)

lola = Vaca('Lola')
alimentar_animales(lola)
