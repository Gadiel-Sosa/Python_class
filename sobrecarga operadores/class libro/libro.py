class Libro:
    def __init__(self, nombre, autor, paginas):
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas
    def __add__(self, otro):
        return Libro(f'Serie: {self.nombre} & {otro.nombre}',f'{self.autor} & {otro.autor}', self.paginas + otro.paginas)
    def __gt__(self, otro):
        return self.paginas > otro.paginas
    def __lt__(self, otro):
        return self.paginas < otro.paginas
    def __str__(self):
        return f'{self.nombre} por {self.autor} ({self.paginas} páginas)'
libro1 = Libro("1984", "George Orwell", 328)
libro2 = Libro("Un mundo feliz", "Aldous Huxley", 268)
libro3 = libro1 + libro2
print(libro3)
print(libro1 > libro2)  # True
print(libro1 < libro2)  # False
print(libro1)