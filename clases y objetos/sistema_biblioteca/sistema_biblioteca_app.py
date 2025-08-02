from biblioteca import Biblioteca
from libro import Libro

biblioteca_nacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {biblioteca_nacional.nombre} ***')

# Definir libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Clásico')
libro3 = Libro('El Principito', 'Antoine de Saint-Exupéry', 'Fantasía')
libro4 = Libro('La Sombra del Viento', 'Carlos Ruiz Zafón', 'Misterio')
libro5 = Libro('1984', 'George Orwell', 'Ficción')

biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)
biblioteca_nacional.agregar_libro(libro5)

autor = 'George Orwell'
print(f'\nLibros de {autor}')
biblioteca_nacional.buscar_libro_autor(autor)

genero = 'Ficción'
print(f'\nLibros de {genero}')
biblioteca_nacional.buscar_libro_genero(genero)

biblioteca_nacional.mostrar_todos_libros()


