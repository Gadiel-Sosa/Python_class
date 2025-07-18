class Persona:
    contador_persona = 0
    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')
        
    @staticmethod
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_persona
    @classmethod
    def get_contador_personas(cls):
        print('Método classmethod')
        return cls.contador_persona
        
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Pérez')
    persona1.mostrar_persona()
    
    persona2 = Persona('Daniel', 'Rios')
    persona2.mostrar_persona()
    
    print(f'Contador obejetos persona (static): {Persona.get_contador_personas_estatico()}')
    
    print(f'Contador objetos persona (classmethod): {Persona.get_contador_personas()}')
    
    