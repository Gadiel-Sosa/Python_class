class Aritmetica():
    def __init__(self):
        self._operando1 = int(input('Ingresa un número: '))
        self._operando2 = int(input('Ingresa otro número: '))
    @property
    def operando1(self):
        return self._operando1
    @operando1.setter
    def operando1(self, valor):
        self._operando1 = int(valor)
    @property
    def operando2(self):
        return self._operando2
    @operando2.setter
    def operando2(self, valor):
        self._operando2 = int(valor)
    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'El resultado de la suma es: {resultado}')
    
    def resta(self):
        resultado = self._operando1 - self._operando2
        print(f'El resultado de la resta es: {resultado}')
        
    def multiplicacion(self):
        resultado = self._operando1 * self._operando2
        print(f'El resultado de la multiplicación es: {resultado}')
    
    def division(self):
        if self._operando2 == 0:
            print('No es posible dividrie entre cero')
        else:
            resultado = self._operando1 / self._operando2
            print(f'El resultado de la división es: {resultado}')
            
aritmetica1 = Aritmetica()
aritmetica1.sumar()
aritmetica1.resta()
aritmetica1.multiplicacion()
aritmetica1.division()

aritmetica1.operando1 = input('Ingresa el nuevo valor del primer número: ')
aritmetica1.sumar()

aritmetica1.operando2 = input('Ingresa el nuevo valor del segundo número: ')
aritmetica1.division()
        
        