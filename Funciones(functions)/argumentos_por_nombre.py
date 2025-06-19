print('*** Función con argumentos por nombre ***')

def imprimir_persona(nombre:str, apellido:str = '', edad:int= 0):
    print(f'''
        -----Persona-----
        Nombre: {nombre}
        Apellido: {apellido}
        Edad: {edad}
          ''')

imprimir_persona('Ricardo', 'Pérez', 35)

# Lamar a la función usando argumentos por nombre
imprimir_persona(nombre='Juan', apellido='Rojas', edad=22)

# Llamar a la función usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad= 22, apellido='Mendoza', nombre='Maria')

# Argumentos con valores con default
imprimir_persona(nombre='Carlos', apellido='')