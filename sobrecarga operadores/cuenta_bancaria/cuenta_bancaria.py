class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __add__(self, otro):
        return CuentaBancaria(f'{self.titular} & {otro.titular}', self.saldo + otro.saldo)

    def __sub__(self, monto):
        return CuentaBancaria(self.titular, self.saldo - monto)

    def __str__(self):
        return f'Titulares: {self.titular} | Saldo: {self.saldo}'

cuenta1 = CuentaBancaria('Juan', 1000)
cuenta2 = CuentaBancaria('Alicia', 500)

cuenta3 = cuenta1 + cuenta2
print(cuenta3)  # Titulares: Juan & Alicia | Saldo: 1500

cuenta4 = cuenta1 - 200
print(cuenta4)  # Titulares: Juan | Saldo: 800
