class Animal:
    def comer(self):
        print('Como varias veces al día')
    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
        
print('*** Herencia en Python ***')
print('Clase padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nSoy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() 
perro1.hacer_sonido()   