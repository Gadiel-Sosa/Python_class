from dispositivos_entrada import DispositivosEntrada
class Raton(DispositivosEntrada):
    contador_ratones = 0
    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        
    def __str__(self):
        return f'Id: {self.id_raton}, Marca: {self.marca}, Entrada: {self.tipo_entrada}'
    @property
    def id_raton(self):
        return self._id_raton