# Definir o crear excepciones personalizadas
class NumerosIgualesException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje