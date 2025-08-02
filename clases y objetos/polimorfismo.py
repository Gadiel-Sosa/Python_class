class Animal:
    def hacer_sonido(self):
        print('Hago un sonido')
        
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')
        
print('*** Ejemplo polimorfismo ***')

print('Clase padre Animal')
animal1 = Animal()
animal1.hacer_sonido()

print('\nClase Perro')
perro1 = Perro()
perro1.hacer_sonido()

print('\nClase Gato')
gato1 = Gato()
gato1.hacer_sonido()