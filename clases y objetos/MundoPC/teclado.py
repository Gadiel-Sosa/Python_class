from dispositivos_entrada import DispositivosEntrada
class Teclado(DispositivosEntrada):
    contador_teclados = 0
    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self.marca}, Entrada: {self.tipo_entrada}'
    @property
    def id_teclado(self):
        return self._id_teclado