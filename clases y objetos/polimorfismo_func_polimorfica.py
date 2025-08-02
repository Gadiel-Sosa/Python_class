class Animal:
    def hacer_sonido(self):
        print('Hago un sonido')
        
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')
        
# Función polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()
        
print('*** Ejemplo polimorfismo ***')

print('Clase padre Animal')
animal1 = Animal()
hacer_sonido_animal(animal1)

print('\nClase Perro')
perro1 = Perro()
hacer_sonido_animal(perro1)

print('\nClase Gato')
gato1 = Gato()
hacer_sonido_animal(gato1)