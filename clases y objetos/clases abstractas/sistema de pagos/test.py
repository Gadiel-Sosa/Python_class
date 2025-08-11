from TarjetaCredito import TarjetaCredito
from Efectivo import Efectivo
from MetodoPago import MetodoPago
def procesar_pago(metodo: MetodoPago, monto):
    metodo.pagar(monto)

if __name__ == "__main__":
    pago1 = TarjetaCredito("1234-5678-9876-5432", "Ana")
    pago2 = Efectivo()

    procesar_pago(pago1, 100)
    procesar_pago(pago2, 50)