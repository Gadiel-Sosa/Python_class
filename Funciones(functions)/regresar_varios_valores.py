print('*** Regresar una tupla desde una función ***')

def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

nombre, apellido, edad = persona_mayusculas('Juan', 'Pérez', 22)
print(f'Resultado de la persona: nombre: {nombre}, apellido: {apellido}, edad: {edad}')
