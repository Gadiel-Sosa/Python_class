from abc import ABC, abstractclassmethod
class MetodoPago(ABC):
    @abstractclassmethod
    def pagar(self, monto):
        pass