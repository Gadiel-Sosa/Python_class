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
        
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Pérez')
    persona1.mostrar_persona()
    
    persona2 = Persona('Daniel', 'Rios')
    persona2.mostrar_persona()
    
    