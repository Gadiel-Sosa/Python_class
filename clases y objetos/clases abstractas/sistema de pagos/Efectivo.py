from MetodoPago import MetodoPago
class Efectivo(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} en efectivo")