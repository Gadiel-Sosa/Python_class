class Persona:
    def __init__(self, nombre, apellido):
        self.apellido = apellido
        self.nombre = nombre 
    
    # sobreescribir el método str, imprime el valor de los atributos de la clase
    
    def __str__(self):
        return f'''Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. memoria: {super.__str__(self)}'''
persona1 = Persona('Mariana', 'Pérez')
print(persona1)
    