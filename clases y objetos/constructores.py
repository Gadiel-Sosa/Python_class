class Persona():
    def __init__(self):
        self.nombre = input('Ingresa tu nombre: ')
        self.apellido = input('Ingresa tu apellido: ')
        
    def mostrar_persona(self):
        print(f'''Persona:
            Nombre: {self.nombre}
            Apellido: {self.apellido}''')

if __name__ == '__main__':
    persona1 = Persona()
    persona1.mostrar_persona()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem Hex persona1: {hex(id(persona1))}')
