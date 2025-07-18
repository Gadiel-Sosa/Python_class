class Aritmetica():
    def __init__(self):
        self.operando1 = int(input('Ingresa un número: '))
        self.operando2 = int(input('Ingresa otro número: '))
    
    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'El resultado de la suma es: {resultado}')
    
    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'El resultado de la resta es: {resultado}')
        
    def multiplicacion(self):
        resultado = self.operando1 * self.operando2
        print(f'El resultado de la multiplicación es: {resultado}')
    
    def division(self):
        if self.operando2 == 0:
            print('No es posible dividrie entre cero')
        else:
            resultado = self.operando1 / self.operando2
            print(f'El resultado de la división es: {resultado}')
            
aritmetica1 = Aritmetica()
aritmetica1.sumar()
aritmetica1.resta()
aritmetica1.multiplicacion()
aritmetica1.division()
        
        