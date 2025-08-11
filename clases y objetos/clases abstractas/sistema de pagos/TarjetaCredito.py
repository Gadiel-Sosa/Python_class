from MetodoPago import MetodoPago
class TarjetaCredito(MetodoPago):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} con tarjeta de crédito de {self.titular}")