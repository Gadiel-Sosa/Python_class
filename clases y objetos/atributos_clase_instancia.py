class Persona:
    # Se asocia a la clase
    atributo_clase = 0
    def __init__(self, atributo_instancia):
        # Se asocia con los objetos en sí
        self.atributo_instancia = atributo_instancia
        
if __name__ == '__main__':
    print('*** Atributo de Clae ***')
    print(f'Atributo de clase: {Persona.atributo_clase}')
    # modificar el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atrinuto de clase: {Persona.atributo_clase}')
    
    persona1 = Persona(16)
    # No es una buena práctica acceder a un atributo de clase con un objeto
    print(f'Atributo de clase: {persona1.atributo_clase}')
    
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')
    
    persona2 = Persona(11)
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')
    
    
    