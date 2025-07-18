# Definición de una clase
class Persona:
    def inicializar_persona(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'''Persona:
            Nombre: {self.nombre}
            Apellido_ {self.apellido}''')

# Creación de objetos 
if __name__ == '__main__':
    
    persona1 = Persona()
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()
    
    persona2 = Persona()
    persona2.inicializar_persona('Ian', 'Pérez')
    persona2.mostrar_persona()